import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.loader import load_documents


def test_loader():

    folder_path = "data/raw"

    documents = load_documents(folder_path)

    print(documents)


if __name__ == "__main__":
    test_loader()