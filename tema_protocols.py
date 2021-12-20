from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __setitem__(self, key, value):
        self._crayons[key] = value
        return self._crayons

    def __delitem__(self, value):
        del self._crayons[value]
        return self._crayons

    def insert(self, value):
        self._crayons.append(value)
        return self._crayons

crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

print(crayons_box)

print(crayons_box.__len__())
print(crayons_box.__getitem__(5))
print(crayons_box.__setitem__(3, 'Pink'))
print(crayons_box.__delitem__(0))
print(crayons_box.insert('Violet'))