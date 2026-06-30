"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code or by using the pytest command from the Terminal command line.
"""
import logging

import pytest

from problem_3 import *


class Tests:
    @pytest.fixture(scope="class")
    def logger(self):
        # set up debug logging
        log = logging.getLogger("debug")
        return log

    def mock_input(self, mock_data, call_counter, monkeypatch):
        """
        Mock the builtin input function
        :param mock_data: Dictionary of data to mock.
        :param call_counter: Dictionary of counters for function calls
        :param monkeypatch: pytest's monkeypatch object
        """

        def new_input(message=""):
            call_counter["input"] += 1
            return mock_data["input"].pop(0)

        monkeypatch.setattr(
            "builtins.input",
            lambda *args, **kwargs: new_input(*args, **kwargs),
        )

    def assert_qualification_output(
        self, expected_fragments, not_expected_fragments, capsys, result, test_inputs
    ):
        captured = capsys.readouterr()
        output_text = captured.out.lower().strip()

        if result is not None:
            if isinstance(result, bool):
                if result:
                    output_text = f"{output_text}\nyou qualify".strip()
                else:
                    output_text = f"{output_text}\nsorry, you don't qualify".strip()
            else:
                output_text = f"{output_text}\n{str(result).lower()}".strip()

        for expected in expected_fragments:
            assert (
                expected.lower() in output_text
            ), f'The qualify function did not print or return a message containing "{expected}" as expected when testing the user inputs: {test_inputs}.'

        for not_expected in not_expected_fragments:
            assert (
                not_expected.lower() not in output_text
            ), f'The qualify function unexpectedly printed or returned "{not_expected}" when testing the user inputs: {test_inputs}.'

    def test_valid_homeowner_1(self, capsys, monkeypatch, logger):
        """
        Check whether a homeowner with valid income will qualify.
        """

        mock_data = {"input": ["$30,000", "y", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["you qualify"],
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 2
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_valid_homeowner_2(self, capsys, monkeypatch, logger):
        """
        Check whether a homeowner with valid income will qualify.
        """

        mock_data = {"input": ["$1,000,000", "y", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["you qualify"],
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 2
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_invalid_homeowner_1(self, capsys, monkeypatch, logger):
        """
        Check whether a homeowner with invalid income will qualify.
        """

        mock_data = {"input": ["$20,000", "y", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            ["you qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 2
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_invalid_homeowner_2(self, capsys, monkeypatch, logger):
        """
        Check whether a homeowner with invalid income will qualify.
        """

        mock_data = {"input": ["$29,999", "y", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            ["you qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 2
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_valid_renter_1(self, capsys, monkeypatch, logger):
        """
        Check whether a renter with valid income will qualify.
        """

        mock_data = {"input": ["$100,000", "n", "$5,000", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["you qualify"],
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 3
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_valid_renter_2(self, capsys, monkeypatch, logger):
        """
        Check whether a renter with valid income will qualify.
        """

        mock_data = {"input": ["$50,000", "n", "$2,400", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["you qualify"],
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 3
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_invalid_renter_1(self, capsys, monkeypatch, logger):
        """
        Check whether a renter with invalid income will qualify.
        """

        mock_data = {"input": ["$100,000", "n", "$5,001", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            ["you qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 3
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."

    def test_invalid_renter_2(self, capsys, monkeypatch, logger):
        """
        Check whether a renter with invalid income will qualify.
        """

        mock_data = {"input": ["$50,000", "n", "$2,501", "foo", "bar"]}
        call_counter = {
            "input": 0,
        }
        test_inputs = mock_data["input"].copy()
        self.mock_input(mock_data, call_counter, monkeypatch)

        result = qualify()
        self.assert_qualification_output(
            ["sorry, you don't qualify", "sorry, you do not qualify"],
            ["you qualify"],
            capsys,
            result,
            test_inputs,
        )

        expected = 3
        actual = call_counter["input"]
        assert (
            actual == expected
        ), f"Expected the input function to be called {expected} times when the user inputs the test data: {test_inputs}; instead, it was called {actual} times."
