## `WordBox`

A container that stores words. Make `len`, `in`, and `print` work.

- `__init__(self)` → empty list `words`
- `add(word)` → appends word (lowercased)
- `__len__` → number of words
- `__contains__(word)` → case-insensitive check
- `__str__` → `"WordBox(3 words: hello, world, python)"`

```python
box = WordBox()
box.add("Hello")
box.add("World")
box.add("Python")

print(len(box))          # 3
print("hello" in box)    # True
print("WORLD" in box)    # True
print("Java" in box)     # False
print(box)               # WordBox(3 words: hello, world, python)
```
