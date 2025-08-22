#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    # Create some authors and magazines
    author1 = Author("Alice Smith")
    author2 = Author("Bob Johnson")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    magazine3 = Magazine("Travel Guide", "Travel")
    # Add articles
    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Healthy Living Tips")
    article3 = author2.add_article(magazine1, "Blockchain Basics")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
