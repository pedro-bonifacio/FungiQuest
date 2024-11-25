import gradio as gr
from placeholders import get_random_mushroom
from app_utils import init_section, init_accordions
from functions.events import check_answer, increment_question, decrement_question, update_quiz_state


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(f"# Fungi Quest! 🍄")
            gr.Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKs2uyTN_MPnilf6B2YHHqBIFbrvA-SA1fA&s", label="Guess me!")

        with gr.Column(scale=2):
            # ------------- App State ----------------
            current_q = gr.State(0)  # Track current question index
            mushroom = gr.State(get_random_mushroom())

            # ------------- App Structure -------------
            # Generate initial question section
            question, radio, submit_btn, feedback = init_section()

            with gr.Row():
                back_btn = gr.Button("← Back", visible=False)
                next_btn = gr.Button("Next →")

            gr.Markdown("### Mushroom Details")
            accordions = init_accordions(10)

            # ------------- Event Handlers -------------
            current_q.change(fn=update_quiz_state,
                             inputs=[current_q],
                             outputs=[question, radio, submit_btn, feedback, back_btn, next_btn] + accordions)

            submit_btn.click(
                fn=check_answer,
                inputs=[mushroom, radio, current_q],
                outputs=[feedback, submit_btn]
            )

            next_btn.click(
                fn=increment_question,
                inputs=[current_q],
                outputs=[current_q]
            )

            back_btn.click(
                fn=decrement_question,
                inputs=[current_q],
                outputs=[current_q]
            )


# Launch the app
if __name__ == "__main__":
    demo.launch()