from bs4 import BeautifulSoup

class SeleniumSEO:
    def __init__(self, driver):
        """Initialize the SeleniumSEO class with a Selenium Driver."""
        self.driver = driver
        self.ignore_words = {
            "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", 
            "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", 
            "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", 
            "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", 
            "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", 
            "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", 
            "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", 
            "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", 
            "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", 
            "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", 
            "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", 
            "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", 
            "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", 
            "you're", "you've", "your", "yours", "yourself", "yourselves"
        }
        self.tags = ['p', 'h1', 'h2', 'h3', 'li']
        self.cleaned_keywords = {}

    def get_tags(self):
        """Return the tags used to extract keywords."""
        return self.tags

    def set_tags(self, tags):
        """Set the tags used to extract keywords."""
        self.tags = tags

    def get_ignore_words(self):
        """Return the ignored words used to remove from keywords."""
        return self.ignore_words

    def set_ignore_words(self, ignore_words):
        """Set the ignored words used to remove from keywords."""
        self.ignore_words = ignore_words

    def process_keywords(self):
        """Return keywords by pulling text from tags, removing ignored words, and cleaning non-alphabetic characters."""

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        words = []
        for tag in self.tags:
            elements = soup.find_all(tag)
            for element in elements:
                words.extend(element.get_text().split())

        keywords = {}
        for word in words:
            lower_word = word.lower()
            if lower_word in keywords:
                keywords[lower_word] += 1
            else:
                keywords[lower_word] = 1

        # Remove ignored words and clean non-alphabetic characters
        self.cleaned_keywords = {
            ''.join(char for char in word if char.isalpha()): count
            for word, count in keywords.items()
            if word.lower() not in self.ignore_words
        }

        return sorted(self.cleaned_keywords.items(), key=lambda item: item[1], reverse=True)
