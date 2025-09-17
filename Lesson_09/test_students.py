import pytest
from sqlalchemy.exc import IntegrityError
from models import Student
from datetime import datetime


def test_create_student(db_session):
    """Тест на добавление студента"""
    # Arrange
    student_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }

    # Act
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Assert
    assert student.id is not None
    assert student.name == "Иван Иванов"
    assert student.email == "ivan@example.com"
    assert student.is_active == True
    assert student.deleted_at is None

    # Проверяем, что студент действительно сохранен в БД
    saved_student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert saved_student is not None
    assert saved_student.name == "Иван Иванов"


def test_update_student(db_session):
    """Тест на изменение данных студента"""
    # Arrange - создаем студента
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Act - обновляем данные
    student.name = "Петр Сидоров"
    student.email = "petr.sidorov@example.com"
    db_session.commit()
    db_session.refresh(student)

    # Assert
    updated_student = db_session.query(Student).filter_by(id=student.id).first()
    assert updated_student.name == "Петр Сидоров"
    assert updated_student.email == "petr.sidorov@example.com"


def test_soft_delete_student(db_session):
    """Тест на мягкое удаление студента"""
    # Arrange - создаем студента
    student = Student(name="Мария Иванова", email="maria@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Act - выполняем мягкое удаление
    student.deleted_at = datetime.now()
    db_session.commit()

    # Assert - проверяем, что студент помечен как удаленный
    deleted_student = db_session.query(Student).filter_by(id=student.id).first()
    assert deleted_student.deleted_at is not None

    # Проверяем, что студент не возвращается в обычных запросах
    active_students = db_session.query(Student).filter_by(deleted_at=None).all()
    assert student not in active_students


def test_unique_email_constraint(db_session):
    """Тест на уникальность email"""
    # Arrange - создаем первого студента
    student1 = Student(name="Анна", email="anna@example.com")
    db_session.add(student1)
    db_session.commit()

    # Act & Assert - пытаемся создать второго студента с тем же email
    student2 = Student(name="Другая Анна", email="anna@example.com")
    db_session.add(student2)

    with pytest.raises(IntegrityError):
        db_session.commit()

    # Откатываем неудачную транзакцию
    db_session.rollback()


def test_get_all_active_students(db_session):
    """Тест на получение только активных студентов"""
    # Arrange - создаем активных и удаленных студентов
    active_student1 = Student(name="Активный 1", email="active1@example.com")
    active_student2 = Student(name="Активный 2", email="active2@example.com")
    deleted_student = Student(name="Удаленный", email="deleted@example.com")
    deleted_student.deleted_at = datetime.now()

    db_session.add_all([active_student1, active_student2, deleted_student])
    db_session.commit()

    # Act - получаем только активных студентов
    active_students = db_session.query(Student).filter_by(deleted_at=None).all()

    # Assert
    assert len(active_students) == 2
    assert deleted_student not in active_students
    assert active_student1 in active_students
    assert active_student2 in active_students