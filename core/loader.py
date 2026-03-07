import os


def load_documents(folder_path):
    documents = []

    # loop through files
    for filename in os.listdir(folder_path):

        # we only want text files
        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            document = {
                "text": text,
                "metadata": {
                    "source": filename
                }
            }

            documents.append(document)

    return documents