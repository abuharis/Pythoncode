from flask import Flask, render_template, request, redirect, url_for, flash, Response, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone, UTC
from fpdf import FPDF
import csv

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_commissions.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Auto logout after 30 minutes
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='agent')  # 'admin' or 'agent'

# Carnival Model
class Carnival(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Assigned Agent
    agent = db.relationship('User', backref=db.backref('carnivals', lazy=True))

# Shop Model
class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    commission_rate = db.Column(db.Float, nullable=False)
    carnival_id = db.Column(db.Integer, db.ForeignKey('carnival.id'), nullable=False)
    carnival = db.relationship('Carnival', backref=db.backref('shops', lazy=True))

# Sale Model
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    carnival_id = db.Column(db.Integer, db.ForeignKey('carnival.id'), nullable=False)  # Track which carnival this belongs to
    agent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Track which agent recorded the sale
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    receipt_number = db.Column(db.String(50), unique=True, nullable=False)  # Unique receipt for tracking
    advance = db.Column(db.Float, default=0.0)  # Any advance taken
    settled = db.Column(db.Boolean, default=False)  # Tracks if the shop settled payments
    shop = db.relationship('Shop', backref=db.backref('sales', lazy=True))
    carnival = db.relationship('Carnival', backref=db.backref('sales', lazy=True))
    agent = db.relationship('User', backref=db.backref('sales', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def session_timeout():
    session.permanent = True
    session.modified = True
    if 'last_activity' in session:
        last_activity = session['last_activity']
        if isinstance(last_activity, str):  # Convert string to datetime
            last_activity = datetime.fromisoformat(last_activity)  

            if last_activity.tzinfo is None:
                last_activity = last_activity.replace(tzinfo=timezone.utc)  # Convert to UTC

        if datetime.now(timezone.utc) - last_activity > app.config['PERMANENT_SESSION_LIFETIME']:
            logout_user()
            flash('Session expired. Please log in again.', 'warning')
            return redirect(url_for('login'))
    session['last_activity'] = datetime.now(UTC).isoformat()  # Store as ISO string

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'agent')  # Default role is agent
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_password, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash('User registered successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            session.permanent = True  # Enable session expiration
            flash('Login successful!', 'success')
            return redirect(url_for('manage_users')) if user.role == 'admin' else redirect(url_for('record_sales'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    shops = Shop.query.all()  # Get all shops
    sales = Sale.query.order_by(Sale.date.desc()).limit(10).all()  # Show last 10 sales

    total_sales = sum(sale.amount for sale in Sale.query.all())
    total_commission = sum(sale.amount * (sale.shop.commission_rate / 100) for sale in Sale.query.all())

    return render_template('dashboard.html', shops=shops, sales=sales, total_sales=total_sales, total_commission=total_commission)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/admin/carnivals', methods=['GET', 'POST'])
@login_required
def manage_carnivals():
    if current_user.role != 'admin':
        flash('Access denied!', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        agent_id = request.form['agent_id']

        new_carnival = Carnival(name=name, start_date=start_date, end_date=end_date, agent_id=agent_id)
        db.session.add(new_carnival)
        db.session.commit()
        flash('Carnival added successfully!', 'success')

    carnivals = Carnival.query.all()
    agents = User.query.filter_by(role='agent').all()
    return render_template('manage_carnivals.html', carnivals=carnivals, agents=agents)

@app.route('/admin/carnivals/delete/<int:carnival_id>', methods=['POST'])
@login_required
def delete_carnival(carnival_id):
    if current_user.role != 'admin':
        flash('Access denied!', 'danger')
        return redirect(url_for('dashboard'))

    carnival = Carnival.query.get_or_404(carnival_id)
    db.session.delete(carnival)
    db.session.commit()
    flash('Carnival deleted successfully!', 'success')
    return redirect(url_for('manage_carnivals'))

@app.route('/admin/users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != 'admin':
        flash('Access denied: Only admins can manage users.', 'danger')
        return redirect(url_for('sales_report'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'agent')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_password, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
    
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        flash("Unauthorized access!", "danger")
        return redirect(url_for('dashboard'))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully!", "success")
    return redirect(url_for('manage_users'))

@app.route('/admin/shops', methods=['GET', 'POST'])
@login_required
def manage_shops():
    if current_user.role != 'admin':
        flash('Access denied!', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        commission_rate = float(request.form['commission_rate'])
        carnival_id = request.form['carnival_id']

        new_shop = Shop(name=name, commission_rate=commission_rate, carnival_id=carnival_id)
        db.session.add(new_shop)
        db.session.commit()
        flash('Shop added successfully!', 'success')

    shops = Shop.query.all()
    carnivals = Carnival.query.all()
    return render_template('manage_shops.html', shops=shops, carnivals=carnivals)

@app.route('/admin/shops/delete/<int:shop_id>', methods=["GET", "POST"])
@login_required
def delete_shop(shop_id):
    if current_user.role != 'admin':
        flash('Access denied: Only admins can delete shops.', 'danger')
        return redirect(url_for('manage_shops'))
    
    shop = Shop.query.get(shop_id)
    if shop:
        db.session.delete(shop)
        db.session.commit()
        flash('Shop deleted successfully!', 'success')
    else:
        flash('Shop not found.', 'danger')
    
    return redirect(url_for('manage_shops'))

@app.route('/admin/shops/edit/<int:shop_id>', methods=['GET', 'POST'])
@login_required
def edit_shop(shop_id):
    if current_user.role != 'admin':  # Only admins can edit shops
        flash("Unauthorized access!", "danger")
        return redirect(url_for('dashboard'))

    shop = Shop.query.get_or_404(shop_id)

    if request.method == 'POST':
        shop.name = request.form['name']
        shop.commission_rate = float(request.form['commission_rate'])
        db.session.commit()
        flash("Shop updated successfully!", "success")
        return redirect(url_for('manage_shops'))

    return render_template('edit_shop.html', shop=shop)

@app.route('/admin/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied: Only admins can edit users.', 'danger')
        return redirect(url_for('manage_users'))
    
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.role = request.form.get('role')
        db.session.commit()
        flash('User role updated successfully!', 'success')
        return redirect(url_for('manage_users'))
    
    return render_template('edit_user.html', user=user)

@app.route('/admin/dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('index'))

    from datetime import datetime, timedelta

    # Get filters from request
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    shop_id = request.form.get('shop_id')
    settled_filter = request.form.get('settled_filter')
    carnival_id = request.form.get('carnival_id')

    query = Sale.query

    if start_date and end_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(Sale.date.between(start_date, end_date))
    else:
        three_days_ago = datetime.now(UTC) - timedelta(days=3)
        query = query.filter(Sale.date >= three_days_ago)

    if shop_id and shop_id != 'all':
        query = query.filter(Sale.shop_id == shop_id)

    if settled_filter == 'settled':
        query = query.filter(Sale.settled == True)
    elif settled_filter == 'unsettled':
        query = query.filter(Sale.settled == False)
    
    if carnival_id and carnival_id != 'all':
        query = query.filter(Sale.carnival_id == carnival_id)

    sales = query.all()

    summary_data = {}
    carnival_summary = {"total_sales": 0.0, "commission": 0.0, "advance": 0.0, "balance": 0.0}

    for sale in sales:
        shop_name = sale.shop.name if sale.shop else "Unknown Shop"
        
        if shop_name not in summary_data:
            summary_data[shop_name] = {
                "total_sales": 0.0,
                "commission": 0.0,
                "advance": 0.0,
                "balance": 0.0,
                "shop_id": sale.shop_id,
                "settled": sale.settled
            }

        summary_data[shop_name]["total_sales"] += sale.amount
        summary_data[shop_name]["commission"] += sale.amount * 0.2  # Example: 20% commission
        summary_data[shop_name]["advance"] += sale.advance
        summary_data[shop_name]["balance"] = (
            summary_data[shop_name]["total_sales"]
            - summary_data[shop_name]["commission"]
            - summary_data[shop_name]["advance"]
        )

        carnival_summary["total_sales"] += sale.amount
        carnival_summary["commission"] += sale.amount * 0.2
        carnival_summary["advance"] += sale.advance
        carnival_summary["balance"] = (
            carnival_summary["total_sales"] - carnival_summary["commission"] - carnival_summary["advance"]
        )

    sales_data = [
        {
            "shop": shop,
            "total_sales": data["total_sales"],
            "commission": data["commission"],
            "advance": data["advance"],
            "balance": data["balance"],
            "shop_id": data["shop_id"],
            "settled": data["settled"]
        }
        for shop, data in summary_data.items()
    ]

    return render_template(
        "admin_dashboard.html", 
        sales_data=sales_data, 
        carnival_summary=carnival_summary,
        shops=Shop.query.all(),
        carnivals=Carnival.query.all()
    )

@app.route('/admin/settle', methods=['POST'])
@login_required
def settle_sales():
    if current_user.role != 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('index'))

    shop_id = request.form.get("shop_id")
    if not shop_id:
        flash("Invalid shop.", "danger")
        return redirect(url_for("admin_dashboard"))

    # Settle all sales of this shop in the last 3 days
    three_days_ago = datetime.utcnow() - timedelta(days=3)
    sales = Sale.query.filter(Sale.shop_id == shop_id, Sale.date >= three_days_ago, Sale.settled == False).all()

    if not sales:
        flash("Sale not found or already settled.", "warning")
        return redirect(url_for("admin_dashboard"))

    for sale in sales:
        sale.settled = True  # Mark as settled

    db.session.commit()
    flash("Sales settled successfully!", "success")
    return redirect(url_for("admin_dashboard"))

# @app.route('/sales', methods=['GET', 'POST'])
# @login_required
# def record_sales():
#     if request.method == 'POST':
#         shop_id = int(request.form.get('shop_id'))
#         amount = float(request.form.get('amount'))
#         advance = float(request.form.get('advance', 0))
        
#         new_sale = Sale(shop_id=shop_id, amount=amount, advance=advance)
#         db.session.add(new_sale)
#         db.session.commit()
#         flash('Sale recorded successfully!', 'success')
    
#     shops = Shop.query.all()
#     return render_template('record_sales.html', shops=shops)

@app.route('/sales/report', methods=['GET'])
@login_required
def sales_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    shop_id = request.args.get('shop_id')

    query = Sale.query

    # Filter by date range
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        query = query.filter(Sale.date.between(start_date, end_date))

    # Filter by shop
    if shop_id:
        query = query.filter_by(shop_id=int(shop_id))

    # Ensure agents see only their own shops' sales
    if current_user.role == 'agent':
        agent_shop_ids = [shop.id for shop in Shop.query.filter_by(agent_id=current_user.id).all()]
        query = query.filter(Sale.shop_id.in_(agent_shop_ids))

    sales = query.order_by(Sale.date.desc()).all()
    
    report = []
    for sale in sales:
        commission = sale.amount * (sale.shop.commission_rate / 100)
        net_total = sale.amount - commission - sale.advance
        report.append({
            'shop': sale.shop.name,
            'date': sale.date.strftime('%Y-%m-%d'),
            'amount': sale.amount,
            'commission': commission,
            'advance': sale.advance,
            'net_total': net_total
        })

    shops = Shop.query.all() if current_user.role == 'admin' else Shop.query.filter_by(agent_id=current_user.id).all()
    
    return render_template('sales_report.html', report=report, shops=shops, start_date=start_date, end_date=end_date, selected_shop=shop_id)

@app.route('/agent/record_sales', methods=['GET', 'POST'])
@login_required
def record_sales():
    if current_user.role != 'agent':
        flash("Access denied. Only agents can record sales.", "danger")
        return redirect(url_for('dasboard'))

    # Get shops assigned to the agent's carnival
    agent_carnival = Carnival.query.filter_by(agent_id=current_user.id).first()
    
    if not agent_carnival:
        flash("No carnival assigned to you.", "warning")
        print(f"{agent_carnival}")
        return redirect(url_for('dashboard'))

    shops = Shop.query.filter_by(carnival_id=agent_carnival.id).all()

    if request.method == 'POST':
        shop_id = request.form.get('shop_id')
        amount = request.form.get('amount')
        advance = request.form.get('advance', 0.0)

        try:
            amount = float(amount)
            advance = float(advance)
        except ValueError:
            flash("Invalid input!", "danger")

        if not shop_id:
            flash("Please Select a Shop", "danger")
        else:

            receipt_number = f"REC-{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}-{shop_id}"

            sale = Sale(
                shop_id=int(shop_id),
                carnival_id=agent_carnival.id,  # Assign the carnival ID
                agent_id=current_user.id,  # Assign the agent ID
                amount=float(amount),
                advance=float(advance),
                receipt_number=receipt_number
            )
            db.session.add(sale)
            db.session.commit()
            flash("Sale recorded successfully!", "success")

    return render_template('record_sales.html', shops=shops)

@app.route('/admin/export', methods=['GET'])
@login_required
def export_sales():
    if current_user.role != 'admin':
        flash("Access denied.", "danger")
        return redirect(url_for('index'))

    export_format = request.args.get('format', 'csv')  # Default to CSV
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    shop_id = request.args.get('shop_id')
    settled = request.args.get('settled')
    carnival_id = request.args.get('carnival_id')

    query = Sale.query
    
    if start_date:
        query = query.filter(Sale.date >= start_date)
    if end_date:
        query = query.filter(Sale.date <= end_date)
    if shop_id:
        query = query.filter(Sale.shop_id == shop_id)
    if settled is not None:
        query = query.filter(Sale.settled == (settled.lower() == 'true'))
    if carnival_id:
        query = query.filter(Sale.carnival_id == carnival_id)

    sales = query.all()

    if export_format == 'csv':
        return export_csv(sales)
    elif export_format == 'pdf':
        return export_pdf(sales)
    else:
        flash("Invalid export format.", "danger")
        return redirect(url_for('admin_dashboard'))

def export_csv(sales):
    def generate():
        yield 'Shop,Date,Amount,Commission,Advance,Net Balance,Settled\n'
        for sale in sales:
            yield f'{sale.shop.name},{sale.date},{sale.amount},{sale.amount * 0.2},{sale.advance},{sale.amount - (sale.amount * 0.2) - sale.advance},{"Yes" if sale.settled else "No"}\n'
    
    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=sales_report.csv"})

def export_pdf(sales):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
    
    pdf.set_font("Arial", size=10)
    pdf.cell(30, 10, "Shop", 1)
    pdf.cell(30, 10, "Date", 1)
    pdf.cell(30, 10, "Amount", 1)
    pdf.cell(30, 10, "Commission", 1)
    pdf.cell(30, 10, "Advance", 1)
    pdf.cell(30, 10, "Net Balance", 1)
    pdf.cell(20, 10, "Settled", 1)
    pdf.ln()
    
    for sale in sales:
        pdf.cell(30, 10, sale.shop.name, 1)
        pdf.cell(30, 10, str(sale.date.date()), 1)
        pdf.cell(30, 10, str(sale.amount), 1)
        pdf.cell(30, 10, str(sale.amount * 0.2), 1)
        pdf.cell(30, 10, str(sale.advance), 1)
        pdf.cell(30, 10, str(sale.amount - (sale.amount * 0.2) - sale.advance), 1)
        pdf.cell(20, 10, "Yes" if sale.settled else "No", 1)
        pdf.ln()
    
    response = Response(pdf.output(dest='S').encode('latin1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=sales_report.pdf'
    return response

@app.route('/export_report', methods=['GET'])
@login_required
def export_report():
    sales = Sale.query.all()
    
    def generate():
        yield 'Shop,Amount Collected,Commission,Advance Taken,Net Amount,Date\n'
        for sale in sales:
            commission = sale.amount_collected * (sale.shop.commission_rate / 100)
            net_amount = sale.amount_collected - commission - sale.advance_taken
            yield f'{sale.shop.name},{sale.amount_collected},{commission},{sale.advance_taken},{net_amount},{sale.date}\n'
    
    response = Response(generate(), mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="sales_report.csv")
    return response

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():  # This ensures the app context is active
        db.create_all()  # Initialize database tables
    app.run(debug=True)

