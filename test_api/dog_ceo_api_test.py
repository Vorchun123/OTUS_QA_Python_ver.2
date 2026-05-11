import requests
import pytest

URL = "https://dog.ceo/api/breed"


@pytest.mark.parametrize(('breed', 'count', 'sub_breed'),
                         [pytest.param('bulldog', 3, 'french', id='bulldog'),
                          pytest.param('hound', 7, 'walker', id='hound'),
                          pytest.param('mastiff', 4, 'tibetan', id='mastiff'),
                          pytest.param('spitz', 2, 'indian', id='spitz')])
def test_count_of_sub_breed(breed, count, sub_breed):
    new_url = f'{URL}/{breed}/list'
    response = requests.get(new_url)
    data = response.json()
    name_sub_breeds = data['message']
    assert response.status_code == 200, "Status code is not 200"
    assert len(name_sub_breeds) == count, 'Count does not match'
    assert sub_breed in name_sub_breeds


@pytest.mark.parametrize(('breed', 'count'),
                         [pytest.param('boxer', 14, id='boxer'),
                          pytest.param('husky', 20, id='husky'),
                          pytest.param('ovcharka', 8, id='ovcharka')])
def test_breed_collection_image(breed, count):
    new_url = f'{URL}/{breed}/images/random/{count}'
    response = requests.get(new_url)
    data = response.json()
    image = data['message']
    assert response.status_code == 200, "Status code is not 200"
    assert len(image) == count, 'Count does not match'
    for image_url in image:
        assert breed in image_url


def test_all_image_of_breed():
    new_url = f'{URL}/boxer/images'
    response = requests.get(new_url)
    data = response.json()
    image = data['message']
    assert response.status_code == 200, "Status code is not 200"
    assert len(image) == 149, 'Count does not match'


def test_sub_breed_collection_image():
    count = 6
    new_url = f'{URL}/mastiff/tibetan/images/random/{count}'
    response = requests.get(new_url)
    data = response.json()
    image = data['message']
    assert response.status_code == 200, "Status code is not 200"
    assert len(image) == count, 'Count does not match'


def test_limitation_random_image_all_dogs_collection():
    count = 109
    new_url = f'{URL}s/image/random/{count}'
    response = requests.get(new_url)
    data = response.json()
    image = data['message']
    assert response.status_code == 200, "Status code is not 200"
    if count <= 50:
        assert len(image) == count
    else:
        assert len(image) == 50
