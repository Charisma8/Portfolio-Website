from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'  # Change this to something random

# Sample projects data
projects = [
    {
        'title': 'My First Website',
        'description': 'A simple website built with HTML and CSS',
        'technologies': ['HTML', 'CSS', 'JavaScript'],
        'github': 'https://github.com/yourusername/project1',
        'demo': 'https://example.com'
    },
    {
        'title': 'Calculator App',
        'description': 'A calculator built with Python',
        'technologies': ['Python', 'Tkinter'],
        'github': 'https://github.com/yourusername/project2',
        'demo': 'https://example.com'
    },
    {
        'title': 'Weather App',
        'description': 'A weather app using API integration',
        'technologies': ['Python', 'Flask', 'API'],
        'github': 'https://github.com/yourusername/project3',
        'demo': 'https://example.com'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)