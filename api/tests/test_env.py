'''
This file is intended to showcase a basic test setup with py.test.
The setup for Flask testing is not complete and may require some more research.

Everything here is subject to change, including the single-file structure
(most likely).
'''
# TODO: Create conftest.py to make the fixtures for setting up the tests.


class TestTravis:
    "Meta tests for the CI environment, if needed."

    def test_travis_working(self):
        assert True


class TestAPI:
    "Tests for the basic API calls with mock data."

    @classmethod
    def setup_class(cls):
        # TODO: Set up application testing, maybe pytest-flask.
        # May require config refactoring
        pass

    def test_api_route(self):
        # Not implemented
        assert True


class TestCRUD:
    "Tests of the CRUD functionality with a proper DB."

    @classmethod
    def setup_class(cls):
        # TODO: See above.
        pass

    def test_create(self):
        assert True

    @classmethod
    def teardown_class(cls):
        # TODO: Clean all the test data of the database.
        pass
