

# TODO Easings
class Tween:

    FROM = 0    # from value index
    TO = 1      # to value index
    CHANGE = 2  # change-per-time-unit value index

    def __init__(self, target: object = None, time: int = 0):
        self.started = False
        self.finished = False
        self.target = target
        self.ftcs = {}
        self._pingpong = False
        self._time = time

    def set_target(self, target: object):
        if not self.started:
            self.target = target
        return self

    def set_attr(self, name: str, fro: float, to: float):
        if not self.started:
            direction = 1 if fro < to else -1
            change = (to - fro) / self._time * direction
            self.ftcs[name] = (fro, to, change)

    def update(self, delta: int):
        if not self.started or self.finished:
            return

        for name in self.ftcs:
            ftc = self.ftcs[name]
            change = ftc[Tween.CHANGE] * delta
            to = ftc[Tween.TO]
            old_value = getattr(self.target, name)
            new_value = old_value + change

            if (to - new_value) * (to - old_value) <= 0:  # different sides of to-value
                new_value = to
                self.finished = True

            setattr(self.target, name, new_value)

            if self.finished and self._pingpong:
                self._reverse_ftcs()
                self.finished = False

    def _reverse_ftcs(self):
        for name in self.ftcs:
            old_value = self.ftcs[name]
            new_value = (old_value[Tween.TO], old_value[Tween.FROM], -1 * old_value[Tween.CHANGE])
            self.ftcs[name] = new_value
            setattr(self.target, name, new_value[Tween.FROM])

    def set_pingpong(self, pingpong=True):
        self._pingpong = pingpong

    def start(self):
        self.started = True

    def stop(self):
        self.finished = True
