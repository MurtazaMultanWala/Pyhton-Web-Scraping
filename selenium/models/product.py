class Product:
    def __init__(self, title: str, author: str, duration: str, release_date: str):
        self.title = title
        self.author = author
        self.duration = duration
        self.release_date = release_date

    def __str__(self):
        return (
            str(self.__class__)
            + "\n"
            + "\n".join(
                ("{} = {}".format(item, self.__dict__[item]) for item in self.__dict__),
            )
        )

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "duration": self.duration,
            "release_date": self.release_date,
        }
