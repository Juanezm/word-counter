from typing import Tuple

import click
from wordcounter.domain.operations import get_repeated_words, \
    get_top_five_frequent_words, get_unique_words


def convert_input_to_list(input_list: str) -> list:
    return list(input_list.replace(' ', '').split(','))


def obtain_operations(words) -> Tuple[list, list, list]:
    repeated_words = get_repeated_words(words)
    unique_words = get_unique_words(words)
    top_five_freq_words = get_top_five_frequent_words(words)
    return repeated_words, unique_words, top_five_freq_words


def print_results(repeated_words: list, unique_words: list,
                  top_five_freq_words: list
                  ):
    click.echo("Repeated words:")
    print_list(repeated_words)
    click.echo("\nUnique words:")
    print_list(unique_words)
    click.echo("\nTop five frequent words:")
    print_list(top_five_freq_words)


def print_list(list_to_print: list):
    for element in list_to_print:
        click.echo(f"- {element}")
