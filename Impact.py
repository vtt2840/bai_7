# Nhập các thư viện cần thiết
from builtins import set, frozenset
from calendar import prcal
from random import sample

import numpy as np
import scipy.stats as stats
from numpy.random import sample


class Impact:
    def __init__(self, n, k, min, max):
        self.n = n
        self.k = k
        self.min = min
        self.max = max
        sample = 0

    def getImpact(self):
        # Sinh ra ngẫu nhiên các giá trị của mẫu tuân theo phân bố chuẩn
        # Bạn có thể thay đổi các tham số trung bình (mean) và độ lệch chuẩn (std) theo ý muốn
        mean = (self.min + self.max) / 2 # Trung bình của phân bố chuẩn
        std = (self.max - mean) / 3 # Độ lệch chuẩn của phân bố chuẩn
        samples = np.random.normal(mean, std, self.n) # Mẫu dữ liệu tuân theo phân bố chuẩn
        samples = np.round(samples, 2)

        # In ra mẫu dữ liệu
        print("Mẫu dữ liệu tuân theo phân bố chuẩn là: ")
        print(samples)

        count = 0
        for num in samples:
            if num < 0:
                count += 1
        print(f"Negative {count}")

        # Tính toán giá trị p_value để kiểm tra xem mẫu dữ liệu có phải là phân bố chuẩn hay không
        # Sử dụng phương pháp Shapiro-Wilk, một trong những phương pháp phổ biến để kiểm định giả thuyết thống kê về phân bố chuẩn
        # Bạn có thể tham khảo thêm về phương pháp này tại đây [^1^]
        stat, p_value = stats.shapiro(samples) # Tính toán giá trị thống kê và giá trị p_value

        # In ra giá trị p_value
        print("Giá trị p_value là: ")
        print(p_value)


        # Đặt mức ý nghĩa thống kê (significance level) là 0.05
        # Nếu giá trị p_value nhỏ hơn mức ý nghĩa thống kê, ta bác bỏ giả thuyết không và kết luận mẫu dữ liệu không tuân theo phân bố chuẩn
        # Nếu giá trị p_value lớn hơn hoặc bằng mức ý nghĩa thống kê, ta không bác bỏ giả thuyết không và kết luận mẫu dữ liệu tuân theo phân bố chuẩn
        alpha = 0.05 # Mức ý nghĩa thống kê
        if p_value < alpha:
            print("Mẫu dữ liệu không tuân theo phân bố chuẩn")
        else:
            print("Mẫu dữ liệu tuân theo phân bố chuẩn")
        # Kiểm tra xem liệu các mẫu này có tuân theo phân phối chuẩn không bằng cách sử dụng kiểm định Kolmogorov-Smirnov
        stat, p_value = stats.kstest(samples, 'norm')
        # In ra giá trị p_value
        print("Giá trị p_value là: ")
        print(p_value)
        if p_value < alpha:  # null hypothesis: x comes from a normal distribution
            print("Theo kiểm định Kolmogorov-Smirnov, các mẫu không tuân theo phân phối chuẩn")
        else:
            print("Theo kiểm định Kolmogorov-Smirnov, các mẫu có thể tuân theo phân phối chuẩn")
        return samples
