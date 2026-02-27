def test_get_single_post(post_api):
    response = post_api.get_post(1)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_create_new_post(post_api):
    response = post_api.create_post(
        title="Tanulom a fixture-öket",
        body="A pytest és a niquests szuper páros!",
        user_id=11
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Tanulom a fixture-öket"
    assert data["id"] == 101

def test_edit_post(post_api):
    response = post_api.edit_post(
        post_id=1,
        title="Megtanultam a fixture-öket",
        body="Így igaz",
        user_id=20
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Megtanultam a fixture-öket"
