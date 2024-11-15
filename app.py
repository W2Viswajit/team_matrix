from gradio import Interface
from generate_environment import generate_environment as process_prompt

def make_image(user_input, enrich_choice, extra_data=None):
    # Process the prompt based on the choice
    new_prompt = process_prompt(user_input)

    # Generate the image
    img = pipe(new_prompt, num_inference_steps=50).images[0]

    return img

ui = Interface(
    fn=make_image,
    inputs=["text", "dropdown", "text"],  # Input fields
    outputs="image",  # Output is an image
    title="360° Image Generator",  # Updated title
    description="Enter a prompt, choose an enhancement, and create stunning 360° visuals!",  # Updated description
)

ui.launch()
