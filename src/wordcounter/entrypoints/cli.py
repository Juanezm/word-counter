import click

from wordcounter.domain.operations import add_list_to_words

from wordcounter.util import convert_input_to_list, obtain_operations, print_results

from wordcounter.adapters import repository


@click.command()
@click.option('--input-list', prompt='Enter the input list separated by comma',
              help='This is the input list. Example: apple, mango, cherry')
@click.argument('json_file')
def main(input_list: str, json_file: str):

    input_list = convert_input_to_list(input_list)
    repo = repository.JsonFileRepository(json_file)

    words = repo.get_words()
    add_list_to_words(words, input_list)

    rep, uniq, top_five = obtain_operations(words)
    print_results(repeated_words=rep,
                  unique_words=uniq,
                  top_five_freq_words=top_five)

    repo.add_words(words)


if __name__ == '__main__':
    main()

