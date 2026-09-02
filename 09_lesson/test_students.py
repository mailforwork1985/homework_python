from database import Student


def test_add_student(db_session):
    """Тест на добавление сущности."""
    # 1. Создаем объект
    new_student = Student(name="Иван Иванов", age=20)
    db_session.add(new_student)
    db_session.commit()

    # 2. Проверяем, что он появился в БД
    student_in_db = db_session.query(Student).filter_by(name="Иван Иванов").first()
    assert student_in_db is not None
    assert student_in_db.age == 20
    assert student_in_db.id is not None


def test_update_student(db_session):
    """Тест на изменение сущности."""
    # 1. Создаем начальные данные
    student = Student(name="Петр Петров", age=21)
    db_session.add(student)
    db_session.commit()

    # 2. Изменяем данные
    student.age = 22
    db_session.commit()

    # 3. Проверяем изменения
    updated_student = db_session.query(Student).filter_by(name="Петр Петров").first()
    assert updated_student.age == 22


def test_delete_student(db_session):
    """Тест на удаление сущности."""
    # 1. Создаем начальные данные
    student = Student(name="Сергей Сергеев", age=23)
    db_session.add(student)
    db_session.commit()

    # 2. Удаляем созданного студента
    db_session.delete(student)
    db_session.commit()

    # 3. Проверяем, что сущности больше нет в БД
    deleted_student = db_session.query(Student).filter_by(name="Сергей Сергеев").first()
    assert deleted_student is None
