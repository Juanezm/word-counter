from wordcounter.entrypoints.cli import main
from click.testing import CliRunner

from tests.random_words import generate_random_string_of_words


def test_main(json_test_file):
    runner = CliRunner()
    word_list = generate_random_string_of_words()
    result = runner.invoke(main, ['--input-list', word_list, json_test_file])
    assert result.exit_code == 0


def test_main_expected_output(json_test_file):
    runner = CliRunner()
    word_list = "a, a, a, a, b, b, b, c, c, d, d, e"
    result = runner.invoke(main, ['--input-list', word_list, json_test_file])
    expected_output = 'Repeated words:\n- a\n- b\n- c\n- d\n\n' \
                      'Unique words:\n- e\n\n' \
                      'Top five frequent words:\n- a\n- b\n- c\n- d\n- None\n'
    assert expected_output == result.output

