""""
In Flask, sessions are used to store information about a user across multiple requests, allowing the server to 
remember details like the user's identity, preferences, or authentication status. 
Here's a simplified explanation of how sessions work and how the server identifies the user:

1. User login in:
When a user logs in by providing their username and password, the server verifies these credentials.
Upon successful authentication, the server creates a unique identifier for the user, often referred to as a session ID.

2. Session ID Stored in a Cookie:

The server sends this session ID back to the user's browser as a cookie.
This cookie is stored on the user's device and is automatically included in subsequent requests to the server.

3. Server Identifies the User:

Each time the user makes a request, their browser includes the session cookie.
The server reads this cookie to retrieve the session ID.
Using the session ID, the server can access the stored user information (like username, role, etc.) associated with 
that session.

4. Rendering User Information in Templates (Check AzricsBank project):

With the user's information retrieved from the session, the server can pass this data to templates.
In the template (e.g., profile.html), you can access and display this information using Jinja2 templating syntax.


#More about Sessions in Flask
The SECRET_KEY is used to securely sign session cookies, ensuring that the data within them cannot be tampered with by 
the client. This key is not sent to the browser; rather, it is used server-side to sign the session cookie. 
The session cookie itself contains the session ID, which the server uses to retrieve the corresponding session data.

#Understanding Flask Session Cookies:

Session Cookie Name: By default, Flask names the session cookie 'session'. You can change this name by setting the 
SESSION_COOKIE_NAME configuration variable. 

Session Cookie Content: The session cookie contains a signed value that includes the session ID. 
This value is signed using the SECRET_KEY to prevent tampering. 
The actual session data (like user information) is stored server-side, and only the session ID is stored in the cookie.

#Viewing Session Cookies in the Browser:

In Chrome: Right-click on the page, select "Inspect," then go to the "Application" tab.
In Firefox: Right-click on the page, select "Inspect," then go to the "Storage" tab.
Navigate to Cookies:

In the left sidebar, find and select your website under the "Cookies" section.
Locate the Session Cookie:

Look for a cookie named 'session' (or whatever name you've configured).
Inspect the Cookie Value:

The value will appear as a long string. This is the signed session data. 
While you can view this value, it is not human-readable and is signed to prevent tampering.

#Session Cookie expires when the browser is closed. If you wanted to log out the user after the first visit,
you would need to delete the session cookie.

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        # Render the profile page
        response = render_template('profile.html', username=username)
        # Clear the session data
        session.pop('username', None) #The user session is popped from the session dictionary
        return response
    else:
        return redirect(url_for('login'))
"""