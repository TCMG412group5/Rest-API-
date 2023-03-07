import requests
import sys


def test_endpoint(input, expected_response, expected_code):
    url = str('http://localhost:4000' + input)
    response = requests.get(url)
    if (response.status_code != 200):
        if (response.status_code != expected_code):
            print(str(input) + " - \u274C FAIL")
            print("\tExp: Status code: %s" % (str(expected_code)))
            print("\tAct: Status code: %s" % (str(response.status_code)))
            sys.exit(1)
        else:
            print(str(input) + " - \u2705 SUCCESS")
            sys.exit(0)
    elif (response.status_code == 200 and response.text.strip() ==
          expected_response):
        print(str(input) + " - \u2705 SUCCESS")
        sys.exit(0)
    else:
        print(str(input) + " - \u274C FAIL")
        print("\tExp: Status Code: %s | Text: %s" %
              (str(expected_code), expected_response))
        print("\tAct: Status Code: %s | Text: %s" %
              (str(response.status_code), response.text))
        sys.exit(1)


# ADD TEST CASES HERE
# Each test case needs to be in the form of a tuple in this order:
# 1) Endpoint (whatever is after localhost:4000)
# 2) Expected text output
# 3) Expected code
test_list = [
    ("/md5/",
     "",
     404),
    ("/md5/hello_world",
     '{"input":"hello_world","output":"99b1ff8f11781541f7f89f9bd41c4a17"}',
     200)
]

for test in test_list:
    try:
        test_endpoint(*test)
    except SystemExit as e:
        if e != 0:
            pass
