def create_customer(connection_db, id_gender, firstname, lastname,
                    email, password, birthday):
    with connection_db.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO `ps_customer`
                (`id_gender`, `firstname`, `lastname`, `email`, `passwd`,
                 `birthday`, `active`, `date_add`, `date_upd`)
            VALUES
                (%s, %s, %s, %s, %s, %s, 1, NOW(), NOW())
            """,
            (id_gender, firstname, lastname, email, password, birthday)
        )
        connection_db.commit()
        return cursor.lastrowid


def get_customer_by_id(connection_db, customer_id):
    with connection_db.cursor() as cursor:
        cursor.execute(
            "SELECT `id_customer`, `firstname`, `lastname`, `email` "
            "FROM `ps_customer` WHERE `id_customer` = %s",
            (customer_id,)
        )
        return cursor.fetchone()


def get_customer_by_email(connection_db, email):
    with connection_db.cursor() as cursor:
        cursor.execute(
            "SELECT `id_customer`, `firstname`, `lastname`, `email` "
            "FROM `ps_customer` WHERE `email` = %s LIMIT 1",
            (email,)
        )
        return cursor.fetchone()


def update_customer(connection_db, customer_id, *,
                    firstname=None, lastname=None, email=None):
    fields, params = [], []

    if firstname is not None:
        fields.append("`firstname` = %s")
        params.append(firstname)
    if lastname is not None:
        fields.append("`lastname` = %s")
        params.append(lastname)
    if email is not None:
        fields.append("`email` = %s")
        params.append(email)

    if not fields:
        return 0

    fields.append("`date_upd` = NOW()")
    params.append(customer_id)

    with connection_db.cursor() as cursor:
        cursor.execute(
            f"UPDATE `ps_customer` SET {', '.join(fields)} WHERE `id_customer` = %s",
            params
        )
        connection_db.commit()
        return cursor.rowcount


def delete_customer(connection_db, customer_id):
    """Удаляет клиента по id. Возвращает rowcount."""
    with connection_db.cursor() as cursor:
        cursor.execute(
            "DELETE FROM `ps_customer` WHERE `id_customer` = %s",
            (customer_id,)
        )
        connection_db.commit()
        return cursor.rowcount


def get_max_customer_id(connection_db):
    with connection_db.cursor() as cursor:
        cursor.execute("SELECT MAX(`id_customer`) AS max_id FROM `ps_customer`")
        return cursor.fetchone()['max_id'] or 0
