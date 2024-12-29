from unittest.mock import mock_open, patch

import pandas as pd
import pytest
import streamlit as st
from pandas.testing import assert_frame_equal

from streamlit_gsheets import GSheetsConnection


@pytest.fixture()
def expected_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": ["1/1/1975", "2/1/1975", "3/1/1975", "4/1/1975", "5/1/1975"],
            "births": [265775, 241045, 268849, 247455, 254545],
        }
    )


def test_read_public_sheet(expected_df: pd.DataFrame):
    url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit"

    conn = st.connection("connection_name", type=GSheetsConnection)

    df = conn.read(spreadsheet=url, usecols=[0, 1])

