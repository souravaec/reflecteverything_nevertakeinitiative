import requests
import pytest
import logging
# pytest-html is installed in the Python 3 virtual environment,
# but that module is not required to be imported in code

LOGGER = logging.getLogger(__name__)

@pytest.fixture
def supply_required_data():
    data_dict = {

        'base_url' : 'https://jsonplaceholder.typicode.com/',
        'get_posts_path' : 'posts'
    }
    return data_dict

# I have made this function deliberately long with lots of
# informative messages, comments etc.
# In Real Life, I will NOT make it this long
# Also if 1 function exceeds the size of screen,
# I will consider breaking them into multiple parts
def test_get_posts(supply_required_data, caplog):
    caplog.set_level(logging.INFO)
    LOGGER.info("Testing get posts now!")
    # Initially expected_val_count is set to 2 for status_code and
    # type of json
    # Later depending on the length of the json returned,
    # This expected value would be updated
    expected_val_count = 2
    actual_val_count = 0
    url = supply_required_data['base_url'] + supply_required_data['get_posts_path']
    print("The URL is    ", url)
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    r = requests.get(url, headers = headers)
    # Verify that status code is 200
    if r.status_code == 200:
        LOGGER.info("Status code is fine")
        actual_val_count = actual_val_count + 1
    else:
        LOGGER.error('Status code is not as per expectation' + str(r.status_code))
    # Verify that GET call returns at least 100 records
    r_json = r.json()
    LOGGER.info("Please have your complete response for debugging ")
    LOGGER.info(str(r_json))
    if type(r_json) == type([]):
        LOGGER.info("Type of returned json is fine")
        actual_val_count = actual_val_count + 1
    else:
        print("Type of returned json is NOT fine")
    # Since I am going to check only for 2 iterations, expected value count
    # is considered for only 2 iterations
    # assuming length of json is only 2!
    # expected_val_count = expected_val_count + 1 + len(r_json)*6
    # Have put 5 instead of 6 to make the test fail and
    # Display plenty of informative messages
    expected_val_count = expected_val_count + 1 + 2 * 6
    if len(r_json) >= 100:
        LOGGER.info("Number of records is fine")
        actual_val_count = actual_val_count + 1
        # Check 1
        expected_key_list = ({'id': 1, 'userId': 1, 'title': 'Hello W', 'body': 'mind'}).keys()
        LOGGER.info("Expected key list is    " + str(expected_key_list))
        # Verify if the elements in the list are of type dictionary
        # Don't want to check for 100 elements during test development,
        # So, checking only the 1st 2 elements in the list
        # I am NOT sure if checking all elements inside the list is necessary or NOT
        # I don't see any harm in checking all elements
        # And if execution time is a concern, in the era of big data,
        # Maybe clusters for execution can be explored?
        # And i have no intention of stopping at the first failure,
        # So, test code will proceed even if there is any failure
        # AND final pass /fail status will be decided after all
        # checkpoints are verified
        # for i in range(len(r_json))
        for i in range(2):
            # Check 1 inside for loop
            if type(r_json[i]) == type({1:2}):
                LOGGER.info("The type of element in list is fine")
                actual_val_count = actual_val_count + 1
                # Check the keys in the dictionary
                actual_key_list = r_json[i].keys()
                LOGGER.info("Actual key list is    " + str(actual_key_list))
                # Check 2 inside for loop
                if actual_key_list == expected_key_list:
                    LOGGER.info("The keys in the dict are fine")
                    actual_val_count = actual_val_count + 1
                    # Validate the type of values
                    # Check 3 inside for loop
                    if type(r_json[i]['id']) == type(10):
                        LOGGER.info("The val for key id is of correct type")
                        actual_val_count = actual_val_count + 1
                    else:
                        LOGGER.error("The val for key id is NOT of correct type")
                    # Check 4 inside for loop
                    if type(r_json[i]['userId']) == type(10):
                        LOGGER.info("The val for key userId is of correct type")
                        actual_val_count = actual_val_count + 1
                    else:
                        LOGGER.error("The val for key userId is NOT of correct type")
                    # Check 5 inside for loop
                    if type(r_json[i]['title']) == type("Hello World"):
                        LOGGER.info("The val for key title is of correct type")
                        actual_val_count = actual_val_count + 1
                    else:
                        LOGGER.error("The val for key title is NOT of correct type")
                    # Check 6 inside for loop
                    if type(r_json[i]['body']) == type("Hello World"):
                        LOGGER.info("The val for key body is of correct type")
                        actual_val_count = actual_val_count + 1
                    else:
                        LOGGER.error("The val for key body is NOT of correct type")
                else:
                    LOGGER.error("The keys in the list are NOT fine")
            else:
                LOGGER.error("The type of element in list is NOT fine")
                break
    else:
        LOGGER.error("Num of records is not as per expectation" + str(len(r_json)))
    LOGGER.info("Expected value count " + str(expected_val_count))
    LOGGER.info("Actual value count " + str(actual_val_count))
    assert actual_val_count == expected_val_count, "Test failed"

def test_postcall_post(supply_required_data, caplog):
    caplog.set_level(logging.INFO)
    LOGGER.info("Testing post posts now!")
    expected_val_count = 4
    actual_val_count = 0
    url = supply_required_data['base_url'] + supply_required_data['get_posts_path']
    print("The URL is    ", url)
    body = {
        "title": "abc",
        "body": "xyz",
        "userId": 1
    }

    #headers = {'Content-Type': 'application/json; charset=utf-8'}
    r = requests.post(url, data=body)

    if r.status_code == 201:
        LOGGER.info("Status code is fine")
        actual_val_count = actual_val_count + 1
    else:
        LOGGER.error('Status code is not as per expectation' + str(r.status_code))
    r_json = r.json()
    LOGGER.info("Please have your complete response for debugging ")
    LOGGER.info(str(r_json))
    if type(r_json) == type({1: 2}):
        LOGGER.info("The type of post response is fine")
        actual_val_count = actual_val_count + 1
    # Check the schema of the returned dict
    expected_key_list = ({'id': 1}).keys()
    actual_key_list = r_json.keys()

    if actual_key_list == expected_key_list:
        LOGGER.info("The keys in the dict are fine")
        actual_val_count = actual_val_count + 1
    else:
        LOGGER.info("The expected keys in the dict are   " + str(expected_key_list))
        LOGGER.error("The keys in the dict are NOT fine" + str(actual_key_list))

    if r_json["id"] == 101:
        LOGGER.info("The id returned in post response is fine")
        actual_val_count = actual_val_count + 1
    else:
        LOGGER.error("The id returned in post response is NOT fine" + str(r_json["id"]))
    LOGGER.info("Expected value count " + str(expected_val_count))
    LOGGER.info("Actual value count " + str(actual_val_count))
    assert actual_val_count == expected_val_count, "Test failed"




