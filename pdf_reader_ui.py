# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PySide6 import QtCore, QtWidgets
from ui_form import Ui_MainWindow  # Import the generated form UI
import os
from main import main  # Import the main function from your application logic

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

# Worker class to handle the application logic in a separate thread
class Worker(QtCore.QObject):
    finished = QtCore.Signal(str)
    error = QtCore.Signal(str)

    def __init__(self, output_dir, folder_path):
        super().__init__()
        self.output_dir = output_dir
        self.folder_path = folder_path

    def run(self):
        try:
            result_message = main(self.output_dir, self.folder_path)
            self.finished.emit(result_message)

        except Exception as e:
            error_message = str(e)
            self.error.emit(error_message)


# Main window class
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PDF Reader")
        self.ui = Ui_MainWindow()  # Create an instance of the generated UI class
        self.ui.setupUi(self)  # Set up the UI elements

        # Connect signals to slots
        self.ui.input_browse_button.clicked.connect(self.select_input_directory)
        self.ui.output_browse_button.clicked.connect(self.select_output_directory)
        self.ui.run_button.clicked.connect(self.run_script)

        self.worker = None
        self.progress_dialog = None

    def select_input_directory(self):
        # Open a folder dialog and get the selected folder path
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.folder_path.setText(folder_path)

    def select_output_directory(self):
        # Open a folder dialog and get the selected folder path
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.output_dir.setText(folder_path)

    def on_script_finished(self, result_message):
        if self.progress_dialog is not None:
            self.progress_dialog.close()
        output_message = f"All PDFs have been read, {result_message}"
        QtWidgets.QMessageBox.information(self, "PDF Reader", output_message)

        self.worker_thread.quit()
        self.worker_thread.wait()
        self.ui.run_button.setEnabled(True)

    def on_script_error(self, error_message):
        if self.progress_dialog is not None:
            self.progress_dialog.close()
        QtWidgets.QMessageBox.critical(self, "Error", error_message)

        self.worker_thread.quit()
        self.worker_thread.wait()
        self.ui.run_button.setEnabled(True)

    def run_script(self):
        if self.worker is not None and self.worker_thread.isRunning():
            return

        folder_path = self.ui.folder_path.text()
        output_dir = self.ui.output_dir.text()

        if not folder_path or not output_dir:
            QtWidgets.QMessageBox.critical(self, "Error", "Please select both input and output directories.")
            return

        try:
            if os.path.isdir(folder_path) and os.path.isdir(output_dir):
                self.ui.run_button.setEnabled(False)

                # Create worker object and move it to a separate thread
                self.worker = Worker(output_dir, folder_path)
                self.worker_thread = QtCore.QThread()
                self.worker.moveToThread(self.worker_thread)

                # Connect signals to slots
                self.worker.finished.connect(self.on_script_finished)
                self.worker.error.connect(self.on_script_error)
                self.worker_thread.started.connect(self.worker.run)
                self.worker_thread.start()

                # Create and configure the progress dialog
                self.progress_dialog = QtWidgets.QProgressDialog(self)
                self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
                #self.progress_dialog.label().setStyleSheet("color: white;")
                self.progress_dialog.setLabelText("Reading PDFs...")
                self.progress_dialog.setCancelButton(None)
                self.progress_dialog.setRange(0, 0)  # Set range to 0 to make it indeterminate
                self.progress_dialog.setStyleSheet("QProgressBar::chunk { background-color: #00853f; }")
                self.progress_dialog.show()
                self.progress_dialog.setWindowTitle("Progress Bar")

            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Make sure the chosen path leads to a folder")

        except Exception as e:
            # Displays an error message if an exception is raised
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
            self.ui.run_button.setEnabled(True)

            if self.progress_dialog is not None:
                self.progress_dialog.close()

            if self.worker_thread.isRunning():
                self.worker_thread.quit()
                self.worker_thread.wait()

            self.ui.run_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle("PDF Reader")
    widget.show()
    sys.exit(app.exec())

