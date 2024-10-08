import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QComboBox

class FFmpegConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FFmpeg Video Converter with Compression')

        layout = QVBoxLayout()

        # Input file
        self.input_label = QLabel('Input File:')
        layout.addWidget(self.input_label)

        self.input_line = QLineEdit(self)
        layout.addWidget(self.input_line)

        self.input_button = QPushButton('Browse', self)
        self.input_button.clicked.connect(self.select_input_file)
        layout.addWidget(self.input_button)

        # Output file
        self.output_label = QLabel('Output File:')
        layout.addWidget(self.output_label)

        self.output_line = QLineEdit(self)
        layout.addWidget(self.output_line)

        self.output_button = QPushButton('Browse', self)
        self.output_button.clicked.connect(self.select_output_file)
        layout.addWidget(self.output_button)

        # Compression settings
        self.codec_label = QLabel('Select Codec:')
        layout.addWidget(self.codec_label)

        self.codec_combo = QComboBox(self)
        self.codec_combo.addItems(['libx264 (H.264)', 'libx265 (H.265)'])
        layout.addWidget(self.codec_combo)

        self.bitrate_label = QLabel('Bitrate (in kbps, e.g., 1000):')
        layout.addWidget(self.bitrate_label)

        self.bitrate_line = QLineEdit(self)
        layout.addWidget(self.bitrate_line)

        self.resolution_label = QLabel('Resolution (e.g., 1280x720 or leave blank):')
        layout.addWidget(self.resolution_label)

        self.resolution_line = QLineEdit(self)
        layout.addWidget(self.resolution_line)

        # Convert button
        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_video)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select Input File')
        if file_path:
            self.input_line.setText(file_path)

    def select_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Select Output File', '', 'Video Files (*.mp4 *.avi *.mkv)')
        if file_path:
            self.output_line.setText(file_path)

    def convert_video(self):
        input_file = self.input_line.text()
        output_file = self.output_line.text()
        selected_codec = self.codec_combo.currentText().split(' ')[0]  # Get codec (libx264 or libx265)
        bitrate = self.bitrate_line.text()
        resolution = self.resolution_line.text()

        if not input_file or not output_file:
            QMessageBox.critical(self, 'Error', 'Please provide both input and output file paths.')
            return

        command = ['ffmpeg', '-i', input_file, '-vcodec', selected_codec]

        if bitrate:
            command.extend(['-b:v', f'{bitrate}k'])  # Set video bitrate

        if resolution:
            command.extend(['-vf', f'scale={resolution}'])  # Resize video

        command.append(output_file)

        try:
            subprocess.run(command, check=True)
            QMessageBox.information(self, 'Success', 'Conversion and Compression successful!')
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, 'Error', f'Conversion failed: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = FFmpegConverter()
    converter.show()
    sys.exit(app.exec_())
