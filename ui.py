import ipywidgets as widgets
from IPython.display import display, clear_output
from config import NUTRITION_DATA_PATH
from debug import debug_print
import shutil

upload_widget = widgets.FileUpload(accept=".txt", multiple=True, description="Upload nutrition data files")
question_input = widgets.Text(placeholder="Ask your nutrition-related question", description="Question:")
send_button = widgets.Button(description="Send", icon="paper-plane")
cleanup_button = widgets.Button(description="Clear Database", button_style="danger", icon="trash")
output = widgets.Output()

def setup_ui(on_send_clicked, on_cleanup_clicked):
    upload_widget.observe(on_send_clicked, names="value")
    send_button.on_click(on_send_clicked)
    cleanup_button.on_click(on_cleanup_clicked)

    print("🥗 Welcome to the Nutrition Assistant Chatbot!")
    print("⬆️ Upload nutrition data files first:")
    display(upload_widget)
    print("\n💬 Ask your nutrition questions below:")
    display(question_input, send_button, cleanup_button)
    display(output)
