import pytest

from items.item_utils import load_df_from__csv_file_by_path


def test_exception_when_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_df_from__csv_file_by_path("wrong_place.csv")
