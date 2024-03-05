from Frame import Frame


class Frame10(Frame):

    def _set_score(self, score: list):
        if len(score) != 3:
            raise ValueError("There cannot be more than three throws in frame 10.")
        for throw in score:
            if throw < 0 or throw > 10:
                raise ValueError("Each throw must be within [0..10].")

        self.score = score

    def throw(self, pin_count: int):
        if len(self.score) >= 3:
            raise IndexError("Frame 10 cannot exceed three throws.")
        if pin_count < 0:
            raise ValueError("Pin count cannot be negative.")
        if len(self.score) < 2 and sum(self.score) != 10 and (sum(self.score) + pin_count) > 10:
            raise ValueError("First two throws cannot exceed 10.")

        self.score.append(pin_count)

    def can_throw_again(self):
        if len(self.score) >= 3:
            return False

        if len(self.score) == 2 and self.score[0] != 10 and sum(self.score) < 10:
            return False

        return True

    def __str__(self):
        if len(self.score) == 0:
            return "     "

        if self.score[0] == 10:
            if len(self.score) == 2 and self.score[1] == 10:
                return "X X  "
            if sum(self.score) == 30:
                return "X X X"
            return "X " + super()._show_score(self.score[1:])

        if len(self.score) == 1:
            return super()._show_score(self.score) + "  "

        if len(self.score) == 2:
            return super()._show_score(self.score) + "  "

        if self.score[2] == 10:
            return super()._show_score(self.score[:2]) + " X"

        return super()._show_score(self.score[:2]) + " " + super().repr_throw(self.score[2])

        # if self.score[0] == 10:
        #     out = "X"
        #     for throw in range(1, 3):
        #         try:
        #             out += " " + super().repr_throw(self.score[throw])
        #         except IndexError:
        #             out += "  "
        #     return out
        #
        # try:
        #     third_throw = " " + super().repr_throw(self.score[2])
        # except IndexError:
        #     third_throw = "  "
        #
        # return super().__str__() + third_throw


if __name__ == "__main__":

    # Testing score representations
    test_scores = [
                  [[], "     "],
                [[ 0], "-    "],
                [[ 5], "5    "],
                [[10], "X    "],
            [[ 0,  0], "- -  "],
            [[ 1,  7], "1 7  "],
            [[ 5,  4], "5 4  "],
            [[ 0,  4], "- 4  "],
            [[ 6,  0], "6 -  "],
            [[10,  0], "X -  "],
            [[ 0, 10], "- /  "],
        [[ 3,  7,  8], "3 / 8"],
        [[ 0, 10, 10], "- / X"],
        [[10,  0,  0], "X - -"],
        [[10,  0,  5], "X - 5"],
        [[ 3,  7,  8], "3 / 8"],
        [[ 0, 10, 10], "- / X"],
        [[ 3,  7, 10], "3 / X"],
        [[10,  3,  6], "X 3 6"],
        [[10,  3,  7], "X 3 /"],
        [[10,  0, 10], "X - /"],
        [[10, 10, 10], "X X X"]
    ]

    for score, goal in test_scores:
        frame = Frame10()
        for throw in score:
            frame.throw(throw)
        # print(f"|{goal}|: |{frame}|")
        assert frame.__str__() == goal

    # Testing erroneous scores.
    # error_scores = [
    #     [-1, 10],
    #     [10, 1],
    #     [8, 8],
    #     [4, 7, 8]
    # ]
    #
    # for score in error_scores:
    #     try:
    #         frame = Frame()
    #         for throw in score:
    #             frame.throw(throw)
    #         print(f"{score.__str__():8s}: |{frame}|")
    #     except Exception as err:
    #         print(f"{score.__str__():8s}: {err}")
