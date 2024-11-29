import gradio as gr
from placeholders import get_random_mushroom
from functions.inits import init_section, init_accordions
from functions.events import check_answer, increment_question, decrement_question, update_quiz_state, show_quiz


with gr.Blocks() as demo:
    # ------------- App State ----------------
    current_q = gr.State(-1)  # Track current question index
    mushroom = gr.State(get_random_mushroom())
    user_answers = gr.State({"growth_location": None, "cap_shape": None})
    # ------------ App Components ------------
    with gr.Row():
        with gr.Column(visible=True) as welcome_screen:
            gr.Markdown("# Welcome to Fungi Quest! 🍄")
            gr.Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKs2uyTN_MPnilf6B2YHHqBIFbrvA-SA1fA&s", label="Mushroom Quiz!")
            start_btn = gr.Button("Start Quiz")

        with gr.Column(scale=1, visible=False) as shroom_screen:
            gr.Markdown(f"# Fungi Quest! 🍄")
            gr.Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWKs2uyTN_MPnilf6B2YHHqBIFbrvA-SA1fA&s", label="Guess me!")

        with gr.Column(scale=2, visible=False) as quiz_screen:
            # Generate initial question section
            question, radio, submit_btn, feedback = init_section()

            with gr.Row():
                back_btn = gr.Button("← Back", visible=False)
                next_btn = gr.Button("Next →")

            gr.Markdown("### Mushroom Details")
            accordions = init_accordions(10)

    # ------------- Event Handlers -------------

    current_q.change(fn=update_quiz_state,
                     inputs=[current_q, user_answers],
                     outputs=[radio, submit_btn, feedback, back_btn, next_btn] + accordions)

    submit_btn.click(
        fn=check_answer,
        inputs=[mushroom, radio, current_q, user_answers],
        outputs=[feedback, submit_btn, user_answers]
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

    start_btn.click(show_quiz, [], [current_q, welcome_screen, shroom_screen, quiz_screen])


# Launch the app
if __name__ == "__main__":
    demo.launch()