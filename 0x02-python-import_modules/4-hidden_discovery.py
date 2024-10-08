#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Load the hidden_4.pyc module
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names from the hidden_4 module
    all_names = dir(hidden_4)

    for name in sorted(all_names):
        if not name.startswith("__"):
            print(name)
