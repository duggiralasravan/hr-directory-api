from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    location = Column(String)
    company = Column(String)
    department = Column(String)
    position = Column(String)
    organization_id = Column(Integer, index=True)

class OrganizationColumnConfig(Base):
    __tablename__ = "org_column_config"
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, index=True)
    column_name = Column(String)
