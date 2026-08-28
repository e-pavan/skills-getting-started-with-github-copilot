def test_unregister_removes_existing_participant(client):
    # Arrange
    email = "john@mergington.edu"
    activity_name = "Gym Class"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants


def test_unregister_rejects_non_participant(client):
    # Arrange
    email = "ghost@mergington.edu"
    activity_name = "Gym Class"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "not signed up" in response.json()["detail"]


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    email = "someone@mergington.edu"
    activity_name = "Unknown Club"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
