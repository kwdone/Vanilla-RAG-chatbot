from chain import init_conversation_chain
from config import TEMP_DIR, NUTRITION_DATA_PATH
from text_utils import clean_answer
from ui import upload_widget, question_input, send_button, cleanup_button, output, setup_ui
from data_utils import handle_upload
import shutil
from IPython.display import clear_output
import atexit

conversation = None
chat_history = []

def on_send_clicked(_):
    global conversation
    with output:
        clear_output()
        question = question_input.value.strip()
        if not question:
            print("Please enter a question.")
            return

        if conversation is None:
            print("Initializing nutrition assistant...")
            try:
                conversation = init_conversation_chain()
            except Exception as e:
                print(f"Initialization failed: {e}")
                return

        response = conversation({"question": question, "chat_history": chat_history})
        answer = clean_answer(response["answer"])

        print("Answer:", answer)
        print("\n--- Retrieved Docs ---\n")
        for doc in response["source_documents"]:
            print(doc.page_content[:500])
            print("-----------")

        chat_history.append((question, answer))
        for q, a in chat_history:
            print(f"Q: {q}\nA: {a}\n---")
        question_input.value = ""

def on_cleanup_clicked(_):
    global conversation, chat_history
    with output:
        clear_output()
        conversation = None
        chat_history.clear()
        shutil.rmtree(TEMP_DIR)
        os.makedirs(NUTRITION_DATA_PATH, exist_ok=True)
        print("Database cleared. You may upload new nutrition files now.")

setup_ui(on_send_clicked, on_cleanup_clicked)
atexit.register(lambda: shutil.rmtree(TEMP_DIR))
