def test_get_single_post(comments_api):
    response = comments_api.get_comments(1)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
