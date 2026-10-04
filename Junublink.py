import streamlit as st

# This file is kept as a simple entry point for local runs.
# The deployed app lives in app.py.

from app import *  # noqa: F401,F403

if __name__ == "__main__":
    # Streamlit app is launched from app.py;
    # this file serves as a compatibility wrapper.
    pass
