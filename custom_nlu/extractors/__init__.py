from custom_nlu.common import NotInstalled

try:
    from custom_nlu.extractors.SimpleEntityExtractor import SimpleEntityExtractor
except ImportError:
    SimpleEntityExtractor = NotInstalled("SimpleEntityExtractor", "spacy")


__all__ = ["SimpleEntityExtractor"]
