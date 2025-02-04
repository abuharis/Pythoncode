from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

#app.config['SESSION_COOKIE_NAME'] = 'abuharis'
app.secret_key = 'supersecretkey' #Replace with a strong hash to encrypt the session ID.

# Sample user database
users = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "full_name": "Admin User",
        "account_number": "0000000000",
        "balance": 100000,
        "email": "admin@azricsbank.com",
        "phone": "1234567890",
        "account_type": "Current",
        "transactions": []  # Track deposits/withdrawals
    },
    "user1": {
        "password": "user123",
        "role": "standard",
        "full_name": "John Doe",
        "account_number": "1234567890",
        "balance": 5000,
        "email": "john.doe@example.com",
        "phone": "9876543210",
        "account_type": "Savings",
        "transactions": []  # Track deposits/withdrawals
    }
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome {session['username']}, Role: {session['role']}"
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('dashboard'))
        else:
            return f"Invalid credentials, please try again. {users[username]['password'] == password}"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))

from datetime import datetime

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('deposit.html', error="Enter a valid deposit amount.")

            # Update user balance
            users[username]['balance'] += amount

            # Log transaction with formatted timestamp
            users[username]['transactions'].append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Deposit",
                "amount": amount
            })

            return redirect(url_for('balance'))

        except ValueError:
            return render_template('deposit.html', error="Invalid amount. Please enter a valid number.")

    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('withdraw.html', error="Enter a valid withdrawal amount.")

            if users[username]['balance'] < amount:
                return render_template('withdraw.html', error="Insufficient funds!")

            # Deduct from balance
            users[username]['balance'] -= amount

            # Log transaction
            users[username]['transactions'].append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "Withdrawal",
                "amount": -amount
            })

            return redirect(url_for('dashboard'))

        except ValueError:
            return render_template('withdraw.html', error="Invalid amount. Please enter a valid number.")

    return render_template('withdraw.html')

@app.route('/profile')
def profile():
    username = session.get('username')
    if username:
        user_info = users.get(username)             #To get the session data from the server.
        response  = render_template('profile.html', user=user_info)
       # session.pop('username', None)
        return response
    else:
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user_info = users.get(username)
    return render_template('dashboard.html', user=user_info)

@app.route('/balance')
def balance():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user_balance = users[username]['balance']
    return render_template('balance.html', balance=user_balance)

@app.route('/statement')
def statement():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_transactions = users.get(username, {}).get('transactions', [])

    return render_template('statement.html', transactions=user_transactions)


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)