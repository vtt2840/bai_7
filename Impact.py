import numpy as np
import scipy.stats as stats

class Impact:
    def __init__(self, n, k, min, max):
        self.n = n
        self.k = k
        self.min = min
        self.max = max

    def getImpact(self):
        emotions = ["pleasure", "surprise", "anger", "fear", "hate", "sad"]
        samples = np.zeros((len(emotions), self.n))  # Khởi tạo mảng 2 chiều với các giá trị ban đầu là 0

        for i, emotion in enumerate(emotions):
            mean = (self.min + self.max) / 2  # Trung bình của phân bố chuẩn
            std = (self.max - mean) / 3  # Độ lệch chuẩn của phân bố chuẩn
            samples[i] = np.random.normal(mean, std, self.n)  # Sinh mẫu dữ liệu tuân theo phân bố chuẩn cho mỗi cảm xúc

        samples = np.round(samples, 2)  # Làm tròn giá trị đến 2 chữ số thập phân

        # In ra mẫu dữ liệu
        print("Mẫu dữ liệu tuân theo phân bố chuẩn là: ")
        print(samples)

        # Tính số lượng giá trị âm trong mỗi cảm xúc
        counts = np.sum(samples < 0, axis=1)
        for i, emotion in enumerate(emotions):
            print(f"Negative '{emotion}': {counts[i]}")

        # Tính toán giá trị p_value để kiểm tra xem mẫu dữ liệu có phải là phân bố chuẩn hay không
        # Sử dụng phương pháp Shapiro-Wilk
        stat, p_value = stats.shapiro(samples.flatten()) # Tính toán giá trị thống kê và giá trị p_value

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
        stat, p_value = stats.kstest(samples.flatten(), 'norm')
        # In ra giá trị p_value
        print("Giá trị p_value là: ")
        print(p_value)
        if p_value < alpha:  # null hypothesis: x comes from a normal distribution
            print("Theo kiểm định Kolmogorov-Smirnov, các mẫu không tuân theo phân phối chuẩn")
        else:
            print("Theo kiểm định Kolmogorov-Smirnov, các mẫu có thể tuân theo phân phối chuẩn")
        return samples
