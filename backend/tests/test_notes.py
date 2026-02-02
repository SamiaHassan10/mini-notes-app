from backend.app import app


def test_post_and_get_notes():
    client = app.test_client()

    # start with empty notes
    res = client.get("/notes")
    assert res.status_code == 200
    assert res.get_json() == {"notes": []}

    # add a new note
    res = client.post("/notes", json={"note": "buy milk"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["message"] == "Note added"
    assert data["total_notes"] >= 1

    # get notes and check the note is present
    res = client.get("/notes")
    assert res.status_code == 200
    assert "buy milk" in res.get_json()["notes"]
