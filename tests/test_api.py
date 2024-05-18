from api_client import get_post


def test_get_post_status_code(post_id):
    response = get_post(post_id)
    assert response.status_code == 200, "Status code is not 200"


def test_get_post_content_type(post_id):
    response = get_post(post_id)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_get_post_response_body(post_id):
    response = get_post(post_id)
    json_response = response.json()
    assert "userId" in json_response, "Response JSON does not have 'userId'"
    assert json_response["id"] == post_id, f"ID is not {post_id}"
    assert "title" in json_response, "Response JSON does not have 'title'"
    assert "body" in json_response, "Response JSON does not have 'body'"
