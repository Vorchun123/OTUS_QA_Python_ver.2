import requests
import pytest

URL = "https://api.openbrewerydb.org/v1/breweries"


@pytest.mark.parametrize(('id_brewery', 'name', 'brewery_type', 'state'),
                         [pytest.param('002ffa9d-8549-4fe5-a883-8f6fe197d55e', 'Resolution Brewing Company',
                                       'brewpub', 'Alaska', id='Resolution Brewing Company'),
                          pytest.param('01f591c5-3a87-4685-af4f-c4e9fccb3a47', 'Barrio Brewing Co',
                                       'micro', 'Arizona', id='Barrio Brewing Co'),
                          pytest.param('896f26a1-d80e-4790-9287-026a86c1799d', '180 and Tapped',
                                       'micro', 'Pennsylvania', id='180 and Tapped')
                          ])
def test_get_breweries_by_id(id_brewery, name, brewery_type, state):
    new_url = f'{URL}/{id_brewery}'
    response = requests.get(new_url)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()['name'] == f'{name}', "Name of the brewery does not match"
    assert response.json()['brewery_type'] == f'{brewery_type}', "Brewery type does not match"
    assert response.json()['state'] == f'{state}', "Name of state does not match"


@pytest.mark.parametrize(('city', 'count'),
                         [pytest.param('dublin', 12, id="Dublin"),
                          pytest.param('osaka', 7, id="Osaka"),
                          pytest.param('zeeland', 1, id="Zeeland"),
                          pytest.param('wexford', 3, id="Wexford")])
def test_count_breweries_on_city(city, count):
    params = {'by_city': city}
    response = requests.get(URL, params=params)
    breweries = response.json()
    assert response.status_code == 200, "Status code is not 200"
    assert len(breweries) == count, 'Count does not match'
    for brewery in breweries:
        assert brewery['city'].lower() == city, "Name is not correct"


def test_count_breweries_on_type():
    params = {'by_type': "brewpub"}
    new_url = f'{URL}/meta'
    response = requests.get(new_url, params=params)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["total"] == 2666, "Total count does not match"


@pytest.mark.parametrize(('country', 'count'),
                         [pytest.param('south korea', 61, id="South Korea"),
                         pytest.param('sweden', 10, id="Sweden"),
                         pytest.param('canada', 200, id="Canada")])
def test_count_breweries_on_country(country, count):
    params = {'by_country': country,
              'per_page': 200}
    response = requests.get(URL, params=params)
    breweries = response.json()
    assert response.status_code == 200, "Status code is not 200"
    assert len(breweries) == count, 'Count does not match'
    for brewery in breweries:
        assert brewery['country'].lower() == country, "Name is not correct"


def test_name_brewery():
    name = 'Ballast Point Brewing Company - Little Italy'
    new_url = f'{URL}?by_name={name}'
    response = requests.get(new_url)
    breweries = response.json()
    brewery = breweries[0]
    assert response.status_code == 200, "Status code is not 200"
    assert brewery['address_1'] == '2215 India St', "Name of the brewery does not match"
    assert brewery['postal_code'] == "92101-1725", "Postal code does not match"
    assert brewery['phone'] == '6192557213', "Phone does not match"
