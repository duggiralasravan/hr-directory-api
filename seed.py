
from app.models import Base, Employee, OrganizationColumnConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

employees = [
    Employee(id=1, name="Alice", status="Active", location="New York", company="TechCorp", department="Engineering", position="Developer", organization_id=1),
    Employee(id=2, name="Bob", status="Terminated", location="San Francisco", company="HealthInc", department="Sales", position="Sales Manager", organization_id=1),
    Employee(id=3, name="Carol", status="Not Started", location="Boston", company="TechCorp", department="HR", position="Recruiter", organization_id=2),
    Employee(id=4, name="John", status="Active", location="New Jersey", company="TechCorp", department="Engineering",
             position="Developer", organization_id=1),
    Employee(id=5, name="Mark", status="Terminated", location="San Francisco", company="HealthInc", department="Sales",
             position="Sales Manager", organization_id=1),
    Employee(id=6, name="Carl Case", status="Not Started", location="Boston", company="TechCorp", department="HR",
             position="Recruiter", organization_id=2)
    ,
]

session.add_all(employees)

column_configs = [
    OrganizationColumnConfig(organization_id=1, column_name="department"),
    OrganizationColumnConfig(organization_id=1, column_name="location"),
    OrganizationColumnConfig(organization_id=1, column_name="position"),
    OrganizationColumnConfig(organization_id=2, column_name="location"),
]

session.add_all(column_configs)
session.commit()
session.close()
print("Seeded successfully!")
