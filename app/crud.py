from .models import Employee, OrganizationColumnConfig
from .schemas import SearchQuery
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def search_employees(params: SearchQuery):
    session = SessionLocal()
    query = session.query(Employee).filter(Employee.organization_id == params.organization_id)

    if params.status:
        query = query.filter(Employee.status == params.status)
    if params.location:
        query = query.filter(Employee.location == params.location)
    if params.company:
        query = query.filter(Employee.company == params.company)
    if params.department:
        query = query.filter(Employee.department == params.department)
    if params.position:
        query = query.filter(Employee.position == params.position)

    query = query.offset(params.offset).limit(params.limit)

    employees = query.all()

    columns = session.query(OrganizationColumnConfig.column_name).filter(
        OrganizationColumnConfig.organization_id == params.organization_id).all()
    columns = [c[0] for c in columns]

    result = []
    for emp in employees:
        emp_dict = {"id": emp.id, "name": emp.name}
        for col in columns:
            emp_dict[col] = getattr(emp, col, None)
        result.append(emp_dict)

    session.close()
    return result

