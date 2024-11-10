from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from user_interface import GUI
from data_acquisition.social_media import get_x_data, get_reddit_data
from data_acquisition.public_datasets import load_public_dataset
from data_acquisition.local_files import load_local_file

class AppDelegate(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def applicationSupportsSecureRestorableState(self):
        return True

class DataFetcher(QObject):
    finished = pyqtSignal(dict)

    def run(self):
        x_data = get_x_data("python programming", 50)
        reddit_data = get_reddit_data("python", 50)
        public_data = load_public_dataset("example_dataset")

        results = {
            'x_data': x_data,
            'reddit_data': reddit_data,
            'public_data': public_data
        }
        self.finished.emit(results)
def main():
    app = QApplication([])
    delegate = AppDelegate()
    app.setProperty("NSApplicationDelegate", delegate)

    window = GUI()
    window.show()

    # Create a thread for data fetching
    thread = QThread()
    fetcher = DataFetcher()
    fetcher.moveToThread(thread)
    thread.started.connect(fetcher.run)
    fetcher.finished.connect(thread.quit)
    fetcher.finished.connect(fetcher.deleteLater)
    thread.finished.connect(thread.deleteLater)
    fetcher.finished.connect(lambda results: print_results(results))

    # Start the thread
    thread.start()

    return app.exec_()

def print_results(results):
    print(f"Fetched {len(results['x_data'])} posts from X")
    print(f"Fetched {len(results['reddit_data'])} Reddit posts")
    print(f"Public dataset: {results['public_data']}")
if __name__ == "__main__":
    main()
