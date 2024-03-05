class Frame:
    @classmethod
    def repr_throw(cls, val):
        if val == 10:
            return "X"
        if val == 0:
            return "-"
        else:
            return str(val)

    def __init__(self):
        self.score = []

    def _set_score(self, score: list):
        if len(score) > 2:
            raise ValueError("There cannot be more than two throws in a frame.")
        if sum(score) > 10:
            raise ValueError("Total score cannot exceed 10.")
        for throw in score:
            if throw < 0 or throw > 10:
                raise ValueError("Each throw must be within [0..10].")

        self.score = score

    def throw(self, pin_count: int):
        if len(self.score) >= 2:
            raise IndexError("Frame cannot exceed two throws.")
        if pin_count < 0:
            raise ValueError("Pin count cannot be negative.")
        if (sum(self.score) + pin_count) > 10:
            raise ValueError(f"Frame score cannot exceed 10 (current score: {sum(self.score)}).")

        self.score.append(pin_count)

    def get_score(self):
        return self.score

    def can_throw_again(self):
        return len(self.score) < 2 and self.score[0] != 10

    @classmethod
    def _show_score(cls, score):
        if len(score) == 0:
            return "   "
        if score[0] == 10:
            return "X  "

        total = sum(score)
        if total >= 10:  # Spare
            return f"{cls.repr_throw(score[0])} /"
        try:
            return f"{cls.repr_throw(score[0])} {cls.repr_throw(score[1])}"
        except IndexError:
            return f"{cls.repr_throw(score[0])}  "

    def __repr__(self):
        out = ""
        for value in self.score:
            out += f"{value:2d}, "

        return f"{out[:-2]:10s}"

    def __str__(self):
        return self._show_score(self.score)


if __name__ == "__main__":
    test_scores = [
        [],
        [0],
        [6],
        [10],
        [0, 0],
        [1, 7],
        [5, 4],
        [0, 4],
        [6, 0],
        [10, 0],
        [3, 7],
        [0, 10]
    ]
    error_scores = [
        [-1, 10],
        [10, 1],
        [8, 8],
        [1, 2, 3]
    ]

    # Testing score representations
    for score in test_scores:
        frame = Frame()
        for throw in score:
            frame.throw(throw)
        print(f"{score.__str__():8s}: |{frame}|")

    # Testing erroneous scores.
    for score in error_scores:
        try:
            frame = Frame()
            for throw in score:
                frame.throw(throw)
            print(f"{score.__str__():8s}: |{frame}|")
        except Exception as err:
            print(f"{score.__str__():8s}: {err}")
