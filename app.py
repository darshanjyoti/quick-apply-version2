from flask import Flask, render_template, request, redirect, url_for, session
from database import load_jobs_from_database, add_application_to_database, load_usersinfo_from_database

app = Flask(__name__)
app.secret_key = 'your_secret_key'
error_message = ""

result = load_jobs_from_database()
# Convert each tuple to a dictionary
job_details_list = [
    {
        'id': row[0],
        'title': row[1],
        'location': row[2],
        'salary': row[3],
        'currancy': row[4],
        'jobdetails': row[5],
        'responsibilities': row[6],
        'requirements': row[7],
        'companydetails': row[8],
        'contactemail': row[9],
        # Add other keys as needed
    } for row in result
]
#root route or login
@app.route("/", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the provided username and password match any user in the database
    if authenticate_user(username, password):
      session['logged_in'] = True
      session['username'] = username  # Store the username in the session for later use
      return redirect(url_for('home'))
    else:
      error_message = 'Invalid credentials'
      return render_template('login.html', error=error_message)

  return render_template('login.html')

# Logout route
@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/home")
def home():
  return render_template('home.html', job_details_list=job_details_list)


def authenticate_user(username, password):
  users = load_usersinfo_from_database()
  return any(user[0] == username and user[1] == password for user in users)


def is_user_logged_in():
  return session.get('logged_in', False)



@app.route("/all-jobs")
def all_jobs():
  # Render the all.html template with all job details
  return render_template('alljob.html', job_details_list=job_details_list)


@app.route("/job/<int:job_id>")
def job_details(job_id):
  # Find the job details with the specified ID
  job = next((job for job in job_details_list if job['id'] == int(job_id)),
             None)

  if job:
    # Render the job_details.html template with job details
    return render_template('job_details.html', job=job)
  else:
    # Return a 404 error if job ID is not found
    return render_template('404.html'), 404


@app.route("/application/<int:job_id>")
def applicationformbyjobid(job_id):
  # Find the job details with the specified ID
  job = next((job for job in job_details_list if job['id'] == int(job_id)),
             None)

  if job:
    # Render the job_details.html template with job details
    return render_template('applicationForm.html', job=job)
  else:
    # Return a 404 error if job ID is not found
    return render_template('404.html'), 404


@app.route("/job/<int:job_id>/submit", methods=['post'])
def submitapplicationform(job_id):
  data = request.form
  #store data in db
  job = next((job for job in job_details_list if job['id'] == int(job_id)),
             None)
  add_application_to_database(job_id, data)
  #display submit succesfully
  return render_template('submit_succesfull.html', job=job_id)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
