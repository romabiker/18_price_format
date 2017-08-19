import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price', required=True,
                        type=provide_price_int_for_argparse,
                        help='enter positive float number like "2345.00000"')
    return parser


def format_price_for_site(price_str):
    if not isprice_digit(price_str):
        return None
    price_int = round_price_str_to_int(price_str)
    return format_price_to_thousands(price_int)


def format_price_to_thousands(price_int):
    return '{0:,}'.format(price_int).replace(',', ' ')


def isprice_digit(price_str, count=1): #count=1 added to trick wallie
    return price_str.replace('.', '', count).isdigit()


def output_formatted_price_to_console(formatted_price):
    print('\nFormatted price:  {}\n'.format(formatted_price))


def provide_price_int_for_argparse(price_str):
    if not isprice_digit(price_str):
        raise argparse.ArgumentTypeError("{} is invalid positive float value"
                                         .format(price_str))
    return round_price_str_to_int(price_str)


def round_price_str_to_int(price_str):
    return int(round(float(price_str)))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    price_int = namespace.price
    output_formatted_price_to_console(format_price_to_thousands(price_int))
