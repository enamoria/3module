from src.eval import whole_word_position
from underthesea import word_sent, pos_tag, chunk
test = "Đối với các chuyên khoa khác như : Phẩu thuật tổng quát ( nội trú 5 năm ) , sản ( nội trú 5 năm ) , chấn thương chỉnh hình ( nội trú 5 năm ) . Và chuyên sâu mỗi chuyên khoa tầm ( 1 - 3 năm tùy chuyên khoa ) . Nói chung cũng tầm 15 - 16 năm ( cho lầm sàn , chưa kể Ph.D )"
print(word_sent(test))
print(chunk(test))

from underthesea.word_sent.model_crf import CRFModel
