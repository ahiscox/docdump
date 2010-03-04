from djapian import space
from djapian.indexer import Indexer, CompositeIndexer

from frontend.scans.models import *

class ScanIndexer(Indexer):
    """
        xapian indexing of scan ocr, date, time and tags.
    """

    fields = ['ocr']
    tags = [
        ('datedir', 'datedir'),
        ('timedir', 'timedir'),
        ('filename', 'filename'),
        ('ocr', 'ocr')
    ]

space.add_index(Scan, ScanIndexer, attach_as='search')

class CommentIndexer(Indexer):
    """
        xapian comment indexing.
    """

    fields = ['name', 'content']
    tags = [
        ('name', 'name'),
        ('content', 'content')
    ]

space.add_index(Comment, CommentIndexer, attach_as='search')

class TagIndexer(Indexer):
    """
        Tag indexing
    """

    fields = ['name']
    tags = [('name', 'name')]

space.add_index(Tag, TagIndexer, attach_as='search')

complete_indexer = CompositeIndexer(Scan.search, Comment.search, Tag.search)

