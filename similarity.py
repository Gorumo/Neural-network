# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

word1 = "в том числе для решения проблем в области интеллектуального управления CPS владением широкой общей подготовкой (базовыми знаниями) для решения практических задач в области информационных систем и технологий"
word2 = "владеть широкой общей подготовкой (базовыми знаниями) для решения практических задач в области информационных систем и технологий"


def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()
print("similarity: " + str(similar(word1,word2)))
