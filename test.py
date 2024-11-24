import gradio as gr
from placeholders import id_questionnaire, get_random_mushroom


def generate_section(question_dict):
    """Generate quiz section components"""
    question = gr.Markdown(f"### {question_dict['question']}")
    radio = gr.Radio(choices=list(question_dict['options'].keys()))
    submit_btn = gr.Button("Submit")
    feedback = gr.Markdown(visible=False)
    return question, radio, submit_btn, feedback


def init_accordions(n):
    accordions = []
    for i in range(n):
        with gr.Accordion("Title", open=False) as accordion:
            gr.Markdown("Description")
        accordions.append(accordion)
    return accordions

def update_accordions(options, accordions):
    for i, (option, (description, image)) in enumerate(options.items()):
        gr.update(accordions[i], title=option, content=[gr.Markdown(description), gr.Image(image)])

    if len(options) < len(accordions):
        for i in range(len(options), len(accordions)):
            gr.update(accordions[i], visible=False)
    return accordions


def increment_q(current_q):
    return current_q + 1

def decrement_q(current_q):
    return max(current_q - 1, 0)


def create_quiz_app():
    mushroom = get_random_mushroom()
    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown(f"# Fungi Quest! 🍄")
                gr.Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKs2uyTN_MPnilf6B2YHHqBIFbrvA-SA1fA&s", label="Guess me!")

            with gr.Column(scale=2):
                current_q = gr.State(0)  # Track current question index

                # Generate initial question section
                question, radio, submit_btn, feedback = generate_section(id_questionnaire[0])
                with gr.Row():
                    back_btn = gr.Button("<- Back", visible=False)
                    next_btn = gr.Button("Next ->")

                def check_answer(answer, q_index):
                    """Check if answer is correct and show feedback"""
                    if answer == id_questionnaire[q_index]["correct"]:
                        return {
                            feedback: gr.update(value="✓ Correct!", visible=True),
                            submit_btn: gr.update(visible=False)
                        }
                    else:
                        return {
                            feedback: gr.update(value="✗ Incorrect. Try again!", visible=True)
                        }

                def load_q_question(q_index):
                    """Load q question"""
                    if q_index == 0:
                        back_update = gr.update(visible=False)
                    else:
                        back_update = gr.update(visible=True)

                    if q_index < len(id_questionnaire):
                        return {
                            current_q: q_index,
                            question: gr.update(value=f"### {id_questionnaire[q_index]['question']}"),
                            radio: gr.update(choices=id_questionnaire[q_index]['options'], value=None),
                            submit_btn: gr.update(visible=True),
                            feedback: gr.update(visible=False),
                            back_btn: back_update
                        }
                    else:
                        return {
                            question: gr.update(value="### Quiz completed! 🎉"),
                            radio: gr.update(visible=False),
                            submit_btn: gr.update(visible=False),
                            feedback: gr.update(visible=False)
                        }

                # Event handlers
                submit_btn.click(
                    fn=check_answer,
                    inputs=[radio, current_q],
                    outputs=[feedback, submit_btn]
                )

                next_btn.click(
                    fn=lambda q: load_q_question(increment_q(q)),
                    inputs=[current_q],
                    outputs=[current_q, question, radio, submit_btn, feedback, back_btn]
                )

                back_btn.click(
                    fn=lambda q: load_q_question(decrement_q(q)),
                    inputs=[current_q],
                    outputs=[current_q, question, radio, submit_btn, feedback, back_btn]
                )

    return app


# Launch the app
if __name__ == "__main__":
    quiz_app = create_quiz_app()
    quiz_app.launch()