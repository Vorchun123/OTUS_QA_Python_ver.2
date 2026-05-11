import requests
import pytest

URL = 'https://jsonplaceholder.typicode.com'


@pytest.mark.parametrize(('user_id', 'name', 'username', 'email', 'phone'),
                         [pytest.param(2, 'Ervin Howell', 'Antonette', 'Shanna@melissa.tv',
                                       '010-692-6593 x09125', id='id_2_Ervin Howell'),
                          pytest.param(5, 'Chelsey Dietrich', 'Kamren', 'Lucio_Hettinger@annie.ca',
                                       '(254)954-1289', id='id_5_Chelsey Dietrich'),
                          pytest.param(9, 'Glenna Reichert', 'Delphine', 'Chaim_McDermott@dana.io',
                                       '(775)976-6794 x41206', id='id_9_Glenna Reichert')])
def test_check_users(user_id, name, username, email, phone):
    new_url = f'{URL}/users/{user_id}'
    response = requests.get(new_url)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()['name'] == name, 'Name is not correct'
    assert response.json()['username'] == username, 'Username is not correct'
    assert response.json()['email'] == email, 'Email is not correct'
    assert response.json()['phone'] == phone, 'Phone is not correct'


@pytest.mark.parametrize(('user_id', 'count', 'album_index', 'title'),
                         [pytest.param(2, 10, 7, 'nesciunt quia et doloremque', id='user_id_2'),
                          pytest.param(4, 10, 7, 'unde a sequi id', id='user_id_4'),
                          pytest.param(6, 10, 3, 'aut non illo amet perferendis', id='user_id_6')])
def test_check_albums_of_user(user_id, count, album_index, title):
    new_url = f'{URL}/albums?userId={user_id}'
    response = requests.get(new_url)
    albums = response.json()
    assert response.status_code == 200, "Status code is not 200"
    assert len(albums) == count
    assert albums[album_index]['title'] == title, 'Title is not correct'


def test_post_users():
    new_url = f'{URL}/posts'
    body = {'title': 'OTUS', 'body': 'test post api', 'userId': 1}
    response = requests.post(new_url, data=body)
    result_json = response.json()
    assert response.status_code == 201
    assert result_json.get('title') == 'OTUS'
    assert result_json.get('body') == 'test post api'


def test_put_users():
    new_url = f'{URL}/posts/1'
    body = {'id': 1, 'title': 'new_OTUS', 'body': 'test put api', 'userId': 1}
    response = requests.put(new_url, data=body)
    result_json = response.json()
    assert response.status_code == 200
    assert result_json.get('title') == 'new_OTUS'
    assert result_json.get('body') == 'test put api'


def test_delete_users():
    new_url = f'{URL}/posts/1'
    response = requests.delete(new_url)
    result_json = response.json()
    assert response.status_code == 200
    assert result_json.get('title') is None
    assert result_json.get('body') is None
