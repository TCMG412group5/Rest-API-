# REST API Project :computer:
> :exclamation::exclamation::exclamation: **NOTICE: In order for /slack-alert to work, the web_hook.txt must be updated with the webhook URL. We should have included it in the Canvas comments for the submission (if we didn't please message us in the group-5 chat). We didn't include it in the repo for security reasons (and because Slack actively scans for webhooks URLs and revokes them)**. :exclamation::exclamation::exclamation:

This repo will be used for the rest of the semester.

## Instructions
To access the endpoints, run the Flask.py program using `python3 Flask.py`.  Then, using a browser or a program like [Postman](https://www.postman.com/ "Postman"), type this URL http://localhost:4000/[Endpoint]/[Argument].

## Endpoints:
- **/md5/[string]** - returns the MD5 hash of the string that is passed as the input
- **/factorial/[int]** - returns the factorial (product of the integer and all integers below it) for the integer that is passed as input
- **/fibonacci/[int]** - returns an array of integers with all the Fibonacci numbers (in order) that are less than or equal to the input number
- **/is-prime/[int]** - returns a boolean value depending on whether the input is a prime number
- **/slack-alert/[string]** - posts the string value to the group-5 private channel in the TCMG 412 Slack
*NOTE: Requires web_hook.txt to be updated. The webhook URL was included in the submission comments.*

## Dependencies:
- **Flask** - `pip install Flask`
