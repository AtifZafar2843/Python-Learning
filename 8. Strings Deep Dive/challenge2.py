# Challenge:
# Given a URL string, break it into parts using only string methods (no urllib):
# • protocol (before ://)
# • domain (after :// up to the next /)
# • path (after the domain)
# • query parameters as key/value pairs (after the ?)

# Example:
# url = "https://shop.tab47.com/items/list?category=books&sort=price"
# Protocol: https
# Domain: shop.tab47.com
# Path: /items/list
# Query:
#   category = books
#   sort = price

# Hint: split() on "://", "/", "?", "&", and "=" will get you a long way.

# Solution
url = "https://shop.tab47.com/items/list?category=books&sort=price"
print(f"url = {url}")
print(f"Protocol: {url.split("://")[0]}")
print(f"Domain: {url.split("://")[1].split("/")[0]}")
print(f"Path: {url.split("/")[-2]}/{url.split("/")[-2]}/")
print(f"Query: \n {url.split("?")[-1].split("&")[0]} \n {url.split("&")[-1]}")
