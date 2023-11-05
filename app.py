from flask import Flask, render_template

app = Flask(__name__)

job_details_list = [
    {
        "id": 1,
        "contactEmail": "darshanjyotitalukdar@gmail.com",
        "title": "Software Developer",
        "location": "San Francisco, USA",
        "salary": "$80,000 - $100,000",
        "job_details":
        "Design, implement, and maintain software applications. Collaborate with cross-functional teams to define, design, and ship new features.",
        "key_skills": ["Python", "JavaScript", "Database Management"],
        "company_details": {
            "name": "Tech Solutions Inc.",
            "industry": "Information Technology",
            "size": "5000+ employees",
            "website": "https://techsolutions.com",
        },
    },
    {
        "id": 2,
        "contactEmail": "darshanjyotitalukdar@gmail.com",
        "title": "Data Scientist",
        "location": "New York, USA",
        "salary": "$90,000 - $120,000",
        "job_details":
        "Apply statistical and machine learning techniques to analyze and interpret complex data sets. Collaborate with data engineers to develop effective data pipelines.",
        "key_skills": ["Machine Learning", "Data Visualization", "Statistics"],
        "company_details": {
            "name": "Data Insights Co.",
            "industry": "Data Analytics",
            "size": "1000+ employees",
            "website": "https://datainsights.com",
        },
    },
    {
        "id": 3,
        "contactEmail": "darshanjyotitalukdar@gmail.com",
        "title": "UX/UI Designer",
        "location": "London, UK",
        "salary": "£60,000 - £80,000",
        "job_details":
        "Create user-centric designs for web and mobile applications. Conduct user research and gather feedback to enhance user experience.",
        "key_skills": ["UI/UX Design", "Prototyping", "Adobe Creative Suite"],
        "company_details": {
            "name": "Design Innovators Ltd.",
            "industry": "Design",
            "size": "200+ employees",
            "website": "https://designinnovators.com",
        },
    },
    {
        "id": 4,
        "contactEmail": "darshanjyotitalukdar@gmail.com",
        "title": "Marketing Specialist",
        "location": "Paris, France",
        "salary": "€70,000 - €90,000",
        "job_details":
        "Develop and implement marketing strategies. Analyze market trends and competitor activities to identify opportunities.",
        "key_skills": ["Digital Marketing", "SEO", "Social Media Management"],
        "company_details": {
            "name": "Marketing Pros Co.",
            "industry": "Marketing",
            "size": "300+ employees",
            "website": "https://marketingpros.com",
        },
    },
    {
        "id": 5,
        "contactEmail": "darshanjyotitalukdar@gmail.com",
        "title": "Backend Developer",
        "location": "Paris, France",
        "salary": "€70,000 - €90,000",
        "job_details":
        "Build and maintain scalable and efficient server-side applications. Collaborate with front-end developers to integrate user-facing elements.",
        "key_skills": ["Java", "Spring Boot", "RESTful APIs"],
        "company_details": {
            "name": "Innovative Tech Solutions Ltd.",
            "industry": "Information Technology",
            "size": "1500+ employees",
            "website": "https://innovativetechsolutions.com",
        },
    },
    # Add more job details as needed
]


@app.route("/")
def hello():
  return render_template('home.html', job_details_list=job_details_list)
  
@app.route("/login")
def login():
  # Render the all.html template with all job details
  return render_template('login.html')

@app.route("/all-jobs")
def all_jobs():
  # Render the all.html template with all job details
  return render_template('alljob.html', job_details_list=job_details_list)


@app.route("/job/<int:job_id>")
def job_details(job_id):
  # Find the job details with the specified ID
  job = next((job for job in job_details_list if job['id'] == job_id), None)

  if job:
    # Render the job_details.html template with job details
    return render_template('job_details.html', job=job)
  else:
    # Return a 404 error if job ID is not found
    return render_template('404.html'), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
