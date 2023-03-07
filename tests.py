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
    test_list = [
    ("/md5/",
     "",
     404),
    ("/md5/hello_world",
     '{"input":"hello_world","output":"99b1ff8f11781541f7f89f9bd41c4a17"}',
     200),
     ("/md5/test!",
      '{"input":"test!","output":"c4d354440cb41ee38e162bc1f431e99b"}',
      200),
      ("/md5/5um",
      '{"input":"5um","output":"13db2c82a7b5cbdd32a5b7ead600f503"}',
      200),
      ("/is-prime/5",
       '{"input":5,"output":true}',
       200),
       ("/is-prime/6",
       '{"input":6,"output":false}',
       200),
       ("/is-prime/six",
       '',
       404),
       ("/is-prime/7",
       '{"input":7,"output":true}',
       200),
    ("/factorial/5",
      '{"input":5,"output":120}',
      200),
      ("/factorial/$6",
       "",
       404),
       ("/factorial/3",
        '{"input":3,"output":6}',
        200),
        ("/factorial/7",
        '{"input":7,"output":5040}',
        200),
       ("/fibonacci/8",
        '{"input":8,"output":[0,1,1,2,3,5,8]}',
        200),
        ("/fibonacci/eight",
         "",
         404),
         ("/fibonacci/37",
          '{"input":37,"output":[0,1,1,2,3,5,8,13,21,34]}',
          200),
          ("/fibonacci/41",
          '{"input":41,"output":[0,1,1,2,3,5,8,13,21,34]}',
          200),
          
]
]

tests_failed = False
for test in test_list:
    try:
        test_endpoint(*test)
    except SystemExit as e:
        if e != 0:
            test_failure = True

if tests_failed == True:
    print()
    print("A test case failed - Exit Code 1")
    sys.exit(1)
else:
    print()
    print("All test cases passed - Exit Code 0")
    sys.exit(0)
