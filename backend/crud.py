from sqlalchemy.orm import Session

from . import models, schemas


# For Departments
def add_department(db: Session, department: schemas.DepartmentCreate):
    db_dep = models.Department(dname=department.dname, loc=department.loc)
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep


def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Department).offset(skip).limit(limit).all()


def get_department(db: Session, dept_no: int):
    return (
        db.query(models.Department).filter(models.Department.deptno == dept_no).first()
    )


def delete_department(db: Session, dept_no: int):
    db_dept = (
        db.query(models.Department).filter(models.Department.deptno == dept_no).first()
    )
    if db_dept:
        db.delete(db_dept)
        db.commit()
        return db_dept
    return None


# For Employees
def add_employee(db: Session, employee: schemas.EmployeeCreate):
    db_user = models.Employee(
        ename=employee.ename,
        job=employee.job,
        deptno=employee.deptno,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.empno == emp_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def update_employee(db: Session, emp_id: int, employee_update: schemas.EmployeeCreate):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.empno == emp_id).first()
    )
    if db_employee:
        for key, value in employee_update.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.empno == emp_id).first()
    )
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None


def get_detailed_information(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(
            models.Employee.empno,
            models.Employee.ename,
            models.Department.deptno,
            models.Department.dname,
        )
        .join(models.Department, models.Department.deptno == models.Employee.deptno)
        .offset(skip)
        .limit(limit)
        .all()
    )
