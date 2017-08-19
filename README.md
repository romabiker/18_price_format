# Price Formatter

The script takes a string representing positive float number and formats to a string representing positive integer divided with spaces to thousands. It can be run from  a console or used in web applications. On a console it validates input values and gives help messages to the console in case  of incorrect input values.  It outputs a result also to the console.When using in web apps it returns the result or None in case of invalid input data. 
The script has a testcase.

## Quickstart

Example of script launch on Linux, Python 3.5:

```
$ python3 format_price.py -p 172617.892734

Formatted price:  172 618

```
Example in other applications:

```
$ python3

>>>from format_price import format_price_for_site
>>>price = format_price_for_site('172617.892734')
>>>print(price)
172 618
```
Example of test run:
```
$ python3 tests.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
