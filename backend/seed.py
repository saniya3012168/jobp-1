from backend.app import create_app
from backend.extensions import db
from backend.models.job import Job  # adjust if your path differs

app = create_app()

with app.app_context():
    # Clear old jobs
    Job.query.delete()

    job1 = Job(
        title="Frontend Developer",
        company="TechNova",
        location="Mumbai",
        description="Looking for React developer with 2+ years experience."
    )

    job2 = Job(
        title="Backend Developer",
        company="CodeCraft",
        location="Pune",
        description="Flask/Django developer required."
    )

    job3 = Job(
        title="Full Stack Developer",
        company="InnovateX",
        location="Bangalore",
        description="MERN stack developer needed urgently."
    )

    db.session.add_all([job1, job2, job3])
    db.session.commit()

    print("Sample jobs added successfully!")
