class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        from collections import deque, defaultdict
        if endWord not in wordList:
            return 0
        intermidiateWords = defaultdict(list)
        wordLen = len(beginWord)
        for word in wordList:
            for i in range(wordLen):
                intermidiateWords[word[:i] + '*' + word[i+1:]].append(word)
        queue = deque()
        memo = set()
        queue.append(beginWord)
        memo.add(beginWord)
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curWord = queue.popleft()
                for i in range(wordLen):
                    intermidiateCurWord = curWord[:i] + '*' + curWord[i+1:]
                    for word in intermidiateWords[intermidiateCurWord]:
                        if word == endWord:
                            return step + 1
                        if word not in memo:
                            queue.append(word)
                            memo.add(word)
            step += 1
        else:
            return 0