import datetime
import pytest

def test_time_status(client):
    response = client.get('/today')
    assert response.status_code == 200
