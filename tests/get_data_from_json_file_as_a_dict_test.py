import os

import pytest

from exceptions import MissingFilePathException, IncorrectFileExtension
from get_data_from_json_file_as_a_dict import get_dict_from_json_file


def test_get_dict_from_json_file_no_param():
    with pytest.raises(MissingFilePathException) as exc:
        get_dict_from_json_file()
    assert "filepath is not filled" == str(exc.value)


def test_get_dict_from_json_file_wrong_extension():
    dataload_file = os.path.join(
        os.path.realpath(os.path.curdir),
        'payloads',
        'textfile_dataload.json'
    )

    with pytest.raises(IncorrectFileExtension) as exc:
        get_dict_from_json_file(dataload_file)
    assert "Incorrect file format" in str(exc.value)


def test_get_dict_from_json_file_correct_test():
    dataload_file = os.path.join(
        os.path.realpath(os.path.curdir),
        'payloads',
        'json_dataload.json'
    )

    data = get_dict_from_json_file(dataload_file)

    assert len(data['persons']) == 2
    assert data['persons'][0]['id'] == 1
