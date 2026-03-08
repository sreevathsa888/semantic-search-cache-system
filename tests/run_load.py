import traceback
import sys
import os

# Ensure repo root is on sys.path so imports like `data.load_data` work when
# running this script directly from the `tests/` directory.
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from data.load_data import load_dataset as load_from_data
from test_data import load_dataset as load_from_test


def try_load(func, name):
    try:
        docs = func()
        print(f"{name}: loaded {len(docs)} documents")
    except Exception as e:
        print(f"{name}: ERROR - {type(e).__name__}: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    print("Running dataset loaders to count documents and show errors (if any)...")
    try_load(load_from_test, 'test_data.load_dataset')
    try_load(load_from_data, 'data.load_data.load_dataset')
