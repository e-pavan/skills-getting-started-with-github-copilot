def test_get_activities_returns_seeded_data(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]
    assert isinstance(payload["Chess Club"]["participants"], list)


def test_get_activities_includes_expected_keys(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    activity = payload["Programming Class"]
    assert set(["description", "schedule", "max_participants", "participants"]).issubset(activity)
