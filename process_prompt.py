# Import necessary libraries
import os
from dotenv import load_dotenv

# Import Watsonx.ai libraries
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods

# Load credentials from a .env file (optional)
load_dotenv()
api_key = os.getenv("api_key", None)
watsonx_project_id = os.getenv("project_id", None)

def setup_model(model_choice, max_words, min_words, method, randomness):
    """
    Creates a Watsonx.ai LLM model object with specified parameters.
    """
    settings = {
        GenParams.MAX_NEW_TOKENS: max_words,
        GenParams.MIN_NEW_TOKENS: min_words,
        GenParams.DECODING_METHOD: method,
        GenParams.TEMPERATURE: randomness,
    }

    model = Model(
        model_id=model_choice,
        params=settings,
        credentials={"apikey": api_key, "url": "https://us-south.ml.cloud.ibm.com"},
        project_id=watsonx_project_id,
    )
    return model

def process_prompt(prompt_text):
    """
    Generates a detailed description based on the user-provided prompt.
    """
    model_choice = ModelTypes.MPT_7B_INSTRUCT2  # Adjust model type if needed
    max_words = 250
    min_words = 150
    method = DecodingMethods.SAMPLE
    randomness = 0.7

    model = setup_model(model_choice, max_words, min_words, method, randomness)

    response = model.generate(prompt=prompt_text)
    result = response["results"][0]["generated_text"]
    return result

# Get user input for the desired environment
user_input = input("Enter your idea for the environment (e.g., peaceful mountain view): ")

# Generate and print the description using Watsonx.ai
output_description = process_prompt(user_input)
print(output_description)
