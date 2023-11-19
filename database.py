from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://yvyf63zfzwdkzdmi3f07:pscale_pw_bIcLN0uQXFoxN8BIWJEUkd7DJ3m2DwuB1wvdSKXXfaX@aws.connect.psdb.cloud/quick-apply?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_database():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row)
    return jobs


def add_application_to_database(job_id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, phone, education, workexperience, linkedin, resumelink, accomplishment) VALUES (:job_id, :full_name, :email, :phone, :education, :workexperience, :linkedin, :resumelink, :accomplishment)"
    )

    parameters = {
        'job_id': int(job_id),
        'full_name': data.get('name', ''),
        'email': data.get('email', ''),
        'phone': data.get('phone', ''),
        'education': data.get('education', ''),
        'workexperience': data.get('workExperience', ''),
        'linkedin': data.get('linkedin', ''),
        'resumelink': data.get('resumeLink', ''),
        'accomplishment': data.get('accomplishments', '')
    }

    conn.execute(query, parameters)


def load_usersinfo_from_database():
  ## with engine.connect() as conn:
  ## result = conn.execute(text("select * from users"))
  ## userinfo = []
  ## for row in result.all():
  ## userinfo.append(row)
  ## return userinfo
  # Replace this with your actual database query logic
  # For now, I'm just returning a hardcoded list of tuples
  return [('user1', 'password1'), ('user2', 'password2')]
