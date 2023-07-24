# AI detector research tool

## Overview

This tool allows you to test the accuracy of various AI detectors. It is a command line tool designed to make it easy to test a large number of detectors at the same time using the same data.

## Requirements

- Python 3.8 or higher
- API keys for the detectors you want to test

## Installation

1. Clone this repository
2. Install the requirements using `pip install -r requirements.txt`

## Usage

1. Make a note of your API keys for the detectors you want to test
2. Run the tool using `python main.py`
3. Follow the instructions in the tool adding your API keys when prompted
4. The tool will run the detectors and output the results to a CSV file

## Usage notes

- The tool will only run the detectors you have API keys for
- If when the tool is finished you are not prompted to generate a confusion matrix or the generation fails run `python matrix.py` to generate the confusion matrix

## Adding detectors

To add a detector you need to do the following:
1. Find the detectors API documentation
2. Find the endpoint for the detector
3. Find the parameters required for the endpoint
4. Add the detector to the `detectors.py` file in the following format:

```"YOUR_DETECTOR_NAME": {
    "post_parameters": {
        # The endpoint URL for the API.
        "endpoint": "YOUR_API_ENDPOINT_URL",

        # The body of the POST request. This usually contains the text to be analyzed.
        # The actual contents will depend on what the API expects.
        # Add or remove parameters as needed depending on the API requirements.
        "body": {"PARAMETER_NAME": "PARAMETER_VALUE"},

        # The headers for the POST request. This usually includes the API key and content type.
        # Add or remove headers as needed depending on the API requirements.
        "headers": {"HEADER_NAME": "HEADER_VALUE"},

        # Information about where the API key is included in the request.
        "API_KEY_POINTER": {
            # The location that the API key will end up (usually 'headers' or 'body').
            "location": "headers_or_body",

            # The actual API key. This is usually read from an environment variable or input by the user.
            "value": "YOUR_API_KEY",

            # The name of the key or field where the API key is included. e.g 'x-api-key' or 'api_key'.
            "key_name": "API_KEY_HEADER_OR_PARAMETER_NAME",
        },

        # The key in the body of the POST request where the text to be analyzed is included. e.g 'text' or 'content'.
        "text_key": "KEY_NAME_FOR_TEXT",
    },

    "response": {
        # The expected response from the API. The actual structure will depend on what the API returns.
        # This should include mappings for how to interpret the API's response.
        # Add or remove mappings as needed.
        # e.g if the API returns a JSON object with a key called 'result' and the value of 'result' is a list of objects
        # with a key called 'score' then the mapping would be:
        # "result": {
        #     "score": "result.score"
        # }
        "200": {
            "result": {
                "MAPPING_FOR_DESIRED_OUTPUT": "RESPONSE_KEY_PATH",
            }
        }
    },
}
```

