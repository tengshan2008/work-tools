class Segment:
    def __init__(self, user_dict) -> None:
        self.user_dict = user_dict
        self.max_length = self.get_max_length()

    def get_max_length(self):
        return max([len(item) for item in self.user_dict])

    def FMM(self, sentence):
        """
        param user_dict: 用户分词词典
        param sentence: 需分词句子
        """
        result = []
        start = 0
        while start != len(sentence):
            index = start + self.max_length
            if index > len(sentence):
                index = len(sentence)
            for i in range(index, start, -1):
                if (sentence[start:i] in self.user_dict) or (len(sentence[start:i]) == 1):
                    result.append(sentence[start:i])
                    break
            start = i
        return result

    def BMM(self, sentence):
        """
        param user_dict: 用户分词词典
        param sentence: 需分词句子
        """
        result = []
        start = len(sentence)
        while start != 0:
            index = start - self.max_length
            if index < 0:
                index = 0
            for i in range(index, start):
                if (sentence[i:start] in self.user_dict) or (len(sentence[i:start]) == 1):
                    result.append(sentence[i:start])
                    break
            start = i
        return result

    def merge_match(self, sentence):
        """
        param user_dict: 用户分词词典
        param sentence: 需分词句子
        """
        FMM_ = self.FMM(sentence)
        BMM_ = self.BMM(sentence)
        if (len(FMM_)) != (len(BMM_)):
            if (len(FMM_)) <= (len(BMM_)):
                return FMM_
            else:
                return BMM_
        else:
            FMM_single = 0
            BMM_single = 0
            for i in range(len(FMM_)):
                if len(FMM_[i]) == 1:
                    FMM_single += 1
            for j in range(len(BMM_)):
                if len(FMM_[i]) == 1:
                    BMM_single += 1
            if FMM_single > BMM_single:
                return BMM_single
            else:
                return FMM_single
