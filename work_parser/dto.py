class Vacansy:
    def __init__(self, vacansy_id: int, title: str, href: str):
        self.vacansy_id = vacansy_id
        self.title = title
        self.href = href

    def to_list(self):
        return [self.vacansy_id, self.title, self.href]
    
    def to_dict(self):
        return {
            "vacancyID": self.vacansy_id,
            "title": self.title,
            "href": self.href
        }
