class Tweet:
    def __init__(self, username, tweet_content):
        self.username = username
        self.tweet_content = tweet_content

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
            "username": self.username,
            "tweet_content": self.tweet_content,
        }
