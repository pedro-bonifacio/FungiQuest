import gradio as gr
from placeholders import questionnaire

def init_section(question_dict=questionnaire[0]):
    """Generate quiz section components"""
    question = gr.Markdown("Select the correct answer to narrow down the mushroom species!")
    radio = gr.Radio(label=f"{question_dict['question']}" ,choices=list(question_dict['options'].keys()))
    submit_btn = gr.Button("Submit")
    feedback = gr.Markdown(visible=False)
    return question, radio, submit_btn, feedback


def init_accordions(n):
    accordions = []
    for i in range(n):
        with gr.Accordion(f"Accordion {i+1}", open=False, visible=False) as accordion:
            description = gr.Markdown("Description")
            image = gr.Image(value='https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png')
        accordions += [accordion, description, image]
    return accordions
