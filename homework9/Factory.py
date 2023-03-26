__author__ = 'Костин Георгий'

"""
Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод), решить следующую задачу:
«Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
С использованием указанных паттернов реализовать следующее поведение:
Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
а через фабричный метод или фабрику, например factory.create_tag(name).
"""
# TODO:


class Tag:
    def __init__(self, name):
        self.name = name


class Image(Tag):
    def __init__(self):
        super().__init__('image')


class Input(Tag):
    def __init__(self):
        super().__init__('input')


class Text(Tag):
    def __init__(self):
        super().__init__('<p></p>')


class Link(Tag):
    def __init__(self):
        super().__init__('<a></a>')


class TagFactory:
    def create_tag(self, name):
        pass


class ImageFactory(TagFactory):
    def create_tag(self, name):
        return Image()


class InputFactory(TagFactory):
    def create_tag(self, name):
        return Input()


class TextFactory(TagFactory):
    def create_tag(self, name):
        return Text()


class LinkFactory(TagFactory):
    def create_tag(self, name):
        return Link()


factory = ImageFactory()
img = factory.create_tag("img")

factory2 = InputFactory()
_input = factory.create_tag("input")

factory3 = TextFactory()
text = factory.create_tag("p")

factory4 = LinkFactory()
link = factory.create_tag("a")

print(img)
print(_input)