from models.author import Author


class Entry():
    def __init__(self, id=None, title=None, link=None, updated=None, summary=None, author=Author(), content=None):
        self.id = id
        self.title = title
        self.link = link
        self.updated = updated
        self.summary = summary
        self.author = author
        self.content = content

    def to_array(self):
        return [
            self.id,
            self.title,
            self.link,
            self.updated,
            self.summary,
            self.content,
            self.author.name,
            self.author.uri,
            self.author.email
        ];

    def __str__(self):
        return 'id={0}, title={1}, link={2}, updated={3}, summary={4}, content={5}, author [ name={6}, uri={7}, email={8} ]'.format(
            self.id,
            self.title,
            self.link,
            self.updated,
            self.summary,
            self.content,
            self.author.name,
            self.author.uri,
            self.author.email
        )