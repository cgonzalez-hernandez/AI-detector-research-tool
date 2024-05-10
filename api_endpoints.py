from dotenv import load_dotenv
import os

load_dotenv()

# API keys
ORIGINALITY_API_KEY = os.getenv("ORIGINALITY_API_KEY")
ZEROGPT_API_KEY = os.getenv("ZEROGPT_API_KEY")
COPYLEAKS_API_KEY = os.getenv("COPYLEAKS_API_KEY")


# Different endpoints and their corresponding API keys, versions and request parameters
API_ENDPOINTS = {
    "Originality": {
        "post_parameters": {
            "endpoint": "https://api.originality.ai/api/v1/scan/ai",
            "body": {"content": "sample text", "aiModelVersion": "1"},
            "headers": {"X-OAI-API-KEY": "", "Accept": "application/json"},
            "API_KEY_POINTER": {
                "location": "headers",
                "value": ORIGINALITY_API_KEY,
                "key_name": "X-OAI-API-KEY",
            },
            "text_key": "content",
        },
        "response": {
            "200": {
                "score": {
                    "ai": "",
                    "original": "",
                }
            }
        },
    }
#     "ZeroGPT": {
#         "post_parameters": {
#             "endpoint": "https://zerogpt.p.rapidapi.com/api/v1/detectText",
#             "body": {"input_text": "Sample"},
#             "headers": {"X-RapidAPI-Key": "", "Content-Type": "application/json"},
#             "API_KEY_POINTER": {
#                 "location": "headers",
#                 "value": ZEROGPT_API_KEY,
#                 "key_name": "X-RapidAPI-Key",
#             },
#             "text_key": "input_text",
#         },
#         "response": {
#             "200": {
#                 "is_human_written": "",
#                 "is_gpt_generated": "",
#             }
#         },
#     }
 }
