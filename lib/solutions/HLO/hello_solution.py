# noinspection PyUnusedLocal
# friend_name = unicode string
# - {"method":"hello","params":["Craftsman"],"id":"HLO_R1_001"}, expected a value that equals "Hello, World!", got: "Hello, Craftsman!"
# - {"method":"hello","params":["Mr. X"],"id":"HLO_R1_002"}, expected a value that equals "Hello, World!", got: "Hello, Mr. X!"
# def hello(friend_name):
#     return "Hello, World!"

# You are given the name of a friend. Say hello to them!
# Example: if name of friend is "John" than return "Hello, John!".


def hello(friend_name):
    return f"Hello, {friend_name}!"
