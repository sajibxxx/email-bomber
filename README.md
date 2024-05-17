## Multiple POST Requests Sender

### Description
This Python script allows users to send multiple POST requests to a specified URL using the `requests` library. It prompts the user to input an email and the number of requests to send. The script then constructs JSON data with the email input and sends it in the body of each request to the specified URL. The responses from the server are printed for each request, and error handling is included to manage any exceptions that may occur during the process.

### Features
- Simple CLI interface for inputting email and number of requests.
- Utilizes the `requests` library for making HTTP requests.
- Provides error handling for managing exceptions during the request process.

### Usage
1. Clone the repository.
2. Run the script.
3. Enter the email and number of requests as prompted.
4. View the responses from the server for each request.

### Dependencies
- Python 3.x
- `requests` library

**Note**: Be cautious when using this script, as repeatedly sending requests to a server may not be appropriate or allowed by its policies.
