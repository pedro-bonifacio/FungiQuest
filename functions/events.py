import gradio as gr
from placeholders import questionnaire

def update_accordions(options):
    max_accordions = 10
    accordions = []

    for title, (desc_text, img_url) in options.items():
        with gr.Accordion(title, open=False, visible=True) as accordion:
            new_description = gr.Markdown(desc_text)
            new_image = gr.Image(value=img_url ,visible=True)
        accordions += [accordion, new_description, new_image]

    for i in range(len(accordions), max_accordions * 3, 3):
        with gr.Accordion("Placeholder", open=False, visible=False) as accordion:
            new_description = gr.Markdown("Placeholder")
            new_image = gr.Image(value=None, visible=False)
        accordions += [accordion, new_description, new_image]

    return accordions


def update_quiz_state(q_index):
    """Wrapper to update quiz components based on the current question index."""

    accordions = update_accordions(questionnaire[q_index]['options'])

    updates = {
        "question": gr.Markdown(f"### {questionnaire[q_index]['question']}"),
        "radio": gr.Radio(choices=list(questionnaire[q_index]['options'].keys())),
        "submit_btn": gr.Button("Submit", visible=True),
        "feedback": gr.Markdown(visible=False),
        "back_btn": gr.Button("← Back", visible=q_index > 0),
        "next_btn": gr.Button("Next →", visible=q_index < len(questionnaire) - 1),
    }

    return list(updates.values()) + accordions

def increment_question(current_q):
    if current_q == len(questionnaire) - 1:
        return current_q
    return current_q + 1

def decrement_question(current_q):
    if current_q == 0:
        return current_q
    return current_q - 1


def check_answer(mushroom, answer, q_index):
    """Check if answer is correct and show feedback"""
    if answer == mushroom[questionnaire[q_index]['tag']]:
        updates = {
            "feedback": gr.update(value="✓ Correct!", visible=True),
            "submit_btn": gr.update(visible=False)
        }
    else:
        updates = {
            "feedback": gr.update(value="✗ Incorrect. Try again!", visible=True),
            "submit_btn": gr.update(visible=True)
        }
    return list(updates.values())