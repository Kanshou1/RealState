import collections

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'italy'}
lookup = dict(age=42, loc='italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandalf = Wizard("gandalf", 42)
print(gandalf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(lookup['user4@talkpython.fm'])
