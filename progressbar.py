import sys
import time


class ProgressBar(object):

    def __init__(self, max_value, fill_character="#", rem_character="-", update_time=0.04, width=80):
        self.cur_value = 0
        self.max_value = max_value
        self.fill_char = fill_character
        self.rem_char = rem_character
        self.width = width

        self.update_time = update_time
        self.effective_width = self.width - 2
        self.start_time = time.time()

        self.print_bar(cur_value=0)

    def update(self, cur_value, extra_text=""):
        if cur_value > self.max_value + 1:
            raise ValueError("Update value is too big.")

        if cur_value == self.max_value:
            self.print_bar(cur_value=self.max_value, extra_text=extra_text)

        self.cur_time = time.time()
        self.cur_value = cur_value
        self.delt_t = self.cur_time - self.start_time
        if self.delt_t >= self.update_time:
            self.print_bar(self.cur_value, extra_text=extra_text)
            self.start_time = self.cur_time
            self.cur_time = time.time()

    def print_bar(self, cur_value, extra_text=""):
        ratio = cur_value / self.max_value
        current_progress = int(ratio * 100)
        num_of_hashes = int(ratio * self.effective_width)
        num_of_minuses = self.effective_width - num_of_hashes
        sys.stdout.write('\r[{hashes}{minuses}] {percentage}% {info}'.format(hashes=self.fill_char * num_of_hashes,
                                                                             minuses='-' * num_of_minuses,
                                                                             percentage=current_progress,
                                                                             info=extra_text))
        sys.stdout.flush()

if __name__ == "__main__":
    pb = ProgressBar(max_value=1000)
    for i in range(1000 + 1):
        time.sleep(0.01)
        pb.update(i, extra_text=i)
