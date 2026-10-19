import db


def test_create_customer(connection_db):
    customer_id = db.create_customer(
        connection_db,
        id_gender=1,
        firstname="Bart",
        lastname="Simpson",
        email="bart_simpson@example.com",
        password="Mypassword123!",
        birthday="1990-01-01",
    )
    print(f"\nКлиент создан, id={customer_id}")
    assert customer_id > 0

    created = db.get_customer_by_id(connection_db, customer_id)
    assert created is not None, "Клиент не найден в БД!"
    assert created['email'] == "bart_simpson@example.com"


def test_update_customer(connection_db):
    row = db.get_customer_by_email(connection_db, "bart_simpson@example.com")
    assert row is not None, "Клиент bart_simpson@example.com не найден"
    customer_id = row['id_customer']

    new_firstname = "Homer"
    new_lastname = "Simpson"
    new_email = "homer_simpson@example.com"

    affected = db.update_customer(
        connection_db, customer_id,
        firstname=new_firstname,
        lastname=new_lastname,
        email=new_email,
    )

    updated = db.get_customer_by_id(connection_db, customer_id)
    assert updated is not None, "Клиент не найден после обновления!"
    assert updated['firstname'] == new_firstname
    assert updated['lastname'] == new_lastname
    assert updated['email'] == new_email


def test_update_nonexistent_customer(connection_db):
    nonexistent_id = db.get_max_customer_id(connection_db) + 1
    assert db.get_customer_by_id(connection_db, nonexistent_id) is None


def test_delete_customer(connection_db):
    row = db.get_customer_by_email(connection_db, "homer_simpson@example.com")
    assert row is not None, "Клиент homer_simpson@example.com не найден"
    customer_id = row['id_customer']

    deleted = db.delete_customer(connection_db, customer_id)
    assert deleted == 1, f"Ожидалось удаление 1 строки, удалено: {deleted}"

    assert db.get_customer_by_id(connection_db, customer_id) is None, \
        "Клиент не удалён!"


def test_delete_nonexistent_customer(connection_db):
    nonexistent_id = db.get_max_customer_id(connection_db) + 1
    assert db.get_customer_by_id(connection_db, nonexistent_id) is None
