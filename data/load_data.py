import os

def load_dataset():

    dataset_path = "20_newsgroups"

    documents = []

    for category in os.listdir(dataset_path):

        category_path = os.path.join(dataset_path, category)

        if os.path.isdir(category_path):

            for file in os.listdir(category_path):

                file_path = os.path.join(category_path, file)

                try:
                    with open(file_path, "r", encoding="latin1") as f:
                        documents.append(f.read())
                except:
                    pass

    return documents