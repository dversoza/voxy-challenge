import re


class WordCounterService:
    @staticmethod
    def count_words(text: str) -> int:
        """
        Counts the number of words in a given text using regex.
        :param text: The text to count words in.
        :return: The number of words in the text.
        """
        return len(re.findall(r"\w+", text))
