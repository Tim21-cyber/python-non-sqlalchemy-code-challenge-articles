class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title  # ✅ assign to backing variable BEFORE defining property

        # register relationships
        if not hasattr(author, "_articles"):
            author._articles = []
        author._articles.append(self)

        if not hasattr(magazine, "_articles"):
            magazine._articles = []
        magazine._articles.append(self)

        # global list
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"<Article {self.title}>"
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if len(name.strip()) == 0:
            raise Exception("name must be longer than 0 characters")
        
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})

class Magazine:
    _all = []
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise Exception("category must be a string")
        if len(category.strip()) == 0:
            raise Exception("category must be longer than 0 characters")
        
        self._name = name
        self.category = category
        self._articles = []

        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("category must be a string")
        if len(value.strip()) == 0:
            raise Exception("category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        if not self._articles:
            return None
        author_counts = Counter(article.author for article in self._articles)
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not any(mag._articles for mag in cls._all):
            return None
        return max(cls._all, key=lambda mag: len(mag._articles))