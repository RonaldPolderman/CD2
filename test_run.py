import sys
import main
import io


def test_index():
    # Mock the Flask app
    app = main.app.test_client()

    # Send a GET request to the '/' route
    response = app.get("/")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response data is as expected
    assert response.data.decode("utf-8") == "Hello, world!"


# Run the tests
test_index()
