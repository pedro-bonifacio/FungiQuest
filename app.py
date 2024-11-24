import gradio as gr
from placeholders import sections, get_random_mushroom


def handle_submit(user_answer, correct_answer):
    if user_answer == correct_answer:
        feedback_text = "Correct!"
        return feedback_text, gr.update(visible=False), gr.update(visible=True)
    else:
        feedback_text = "Incorrect. Try again."
        return feedback_text, gr.update(visible=True), gr.update(visible=False)


def generate_section(question):
    user_selection = gr.Radio(
        choices=list(question['options'].keys()),
        label=question['question']
    )

    submit = gr.Button("Submit")
    next_button = gr.Button("Next", visible=False)
    feedback = gr.Markdown("")

    submit.click(handle_submit, inputs=[user_selection], outputs=[feedback, submit, next_button])

    gr.Markdown("### Expand each option to see more details:")
    for option, (description, image) in question['options'].items():
        with gr.Accordion(option, open=False):
            gr.Markdown(description)
            gr.Image(image)


def app_ui():
    mushroom = get_random_mushroom()

    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown(f"# Fungi Quest! 🍄")
                gr.Image(mushroom["image"], label="Guess me!")

            with gr.Column(scale=2):
                gr.Markdown("## Please Answer the Following Question:")
                generate_section(sections["growth_location"])

    return app


app = app_ui()
app.launch()
