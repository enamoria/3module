# -*- coding: utf-8 -*-

""" Created on 4:26 PM 7/16/18
    @author: ngunhuconchocon
    @brief:
"""

from __future__ import print_function
import time

import pickle
import logging
import os

from features.features import sent2features
from regex_tokenize import tokenize


def word_seg(text, word_seg_crf_model):
    """
    Perform word segmentation
    :param text: input, raw
    :param word_seg_crf_model: notunderthesea :D
    :return: list[segmentated words]
    """
    return _word_seg(text, word_seg_crf_model)


def _word_seg(text, word_seg_crf_model):
    sentence = tokenize(text).split()
    X_test = [sent2features(sentence, 'raw')]

    start = time.time()
    IOBtag = word_seg_crf_model.predict(X_test)
    print("Executed time for segmentating: " + str(time.time() - start))

    output = []
    for tag, token in zip(IOBtag[0], sentence):
        if tag == "I_W":
            output[-1] = output[-1] + u" " + token
        else:
            output.append(token)

    return output


if __name__ == "__main__":
    ws_model = "bigram_dict.pkl"
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    print(curr_dir)
    models_dir = os.path.join(curr_dir, "models/")
    print(models_dir)
    ws_model = pickle.load(open(models_dir + ws_model, 'rb'))

    # st = "đây là cầu nối giữa các nhà nghiên cứu của Việt Nam . Qua đây các nhà nghiên cứu có thể triển khai các ý tưởng , tích hợp các bộ dữ liệu , kết quả nghiên cứu mới nhất của mình cho cộng đồng".lower()
    # st = "Để bảo đảm quá trình chuẩn bị, triển khai đúng quy định, chặt chẽ, hiệu quả, Thủ tướng Chính phủ giao Ban Cán sự Đảng Bộ Văn hóa, Thể thao và Du lịch có tờ trình, báo cáo Bộ Chính trị trong tháng 7 để xin ý kiến về chủ trương đăng cai tổ chức Sea Games 31 và Para Games 11 năm 2021 tại thành phố Hà Nội, trên cơ sở đó thông báo chính thức tới Liên đoàn Thể thao Đông Nam Á. Sau khi Bộ Chính trị đồng ý về chủ trương, UBND thành phố Hà Nội chủ trì, phối hợp chặt chẽ với Bộ Văn hóa, Thể thao và Du lịch và các bộ, cơ quan, địa phương liên quan xây dựng Đề án tổ chức Sea Games 31 và Para Games 11 trên tinh thần tiết kiệm, an toàn, hiệu quả, thành công; chủ động rà soát, hoàn thiện phương án chi tiết về cơ sở vật chất theo hướng tận dụng tối đa cơ sở vật chất sẵn có, hạn chế xây dựng và mua sắm mới, tăng cường mạnh mẽ xã hội hóa nguồn lực."
    st = "Tuy nhiên , tối hôm đó trời mưa nên ba em đã chui vào cây ATM trên đường Lê Duẩn đoạn từ phố Khâm Thiên rẽ sang ga Hà Nội lấy mì tôm sống ra ăn và được người dân phát hiện báo công an phường Khâm Thiên ."

    x = word_seg(st, ws_model)

    print(" ".join([xxx.replace(" ", "_") for xxx in x]))
    print("tuy_nhiên , tối hôm_đó trời mưa nên ba em đã chui vào cây ây ti_em trên đường lê_duẩn đoạn từ phố_khâm thiên_rẽ sang_ga hà nội lấy mì tôm sống ra ăn và được người dân phát_hiện báo công_an phường khâm_thiên .")
    print("Để bảo_đảm quá trình chuẩn bị , triển_khai đúng quy_định , chặt_chẽ , hiệu_quả , thủ_tướng chính_phủ giao_ban cán_sự_Đảng bộ văn_hóa , thể_thao và du_lịch có tờ_trình , báo_cáo bộ chính_trị trong tháng 7 để xin ý kiến về chủ trương_đăng_cai tổ chức sea_games 31 và para_games 11 năm 2021 tại thành_phố hà_nội , trên cơ sở_đó thông_báo chính thức tới liên_đoàn thể_thao Đông_nam Á . sau khi bộ chính_trị đồng_ý về chủ_trương , ubnd thành phố_hà nội chủ_trì , phối_hợp chặt_chẽ với bộ văn_hóa , thể_thao và du_lịch và các bộ , cơ_quan , địa_phương liên_quan xây dựng_Đề án tổ_chức sea_games 31 và para_games 11 trên tinh thần tiết_kiệm , an_toàn , hiệu_quả , thành công ; chủ_động rà soát , hoàn_thiện phương_án chi tiết về cơ_sở vật_chất theo hướng tận dụng tối_đa cơ_sở vật_chất sẵn có , hạn_chế xây dựng và mua sắm mới , tăng cường mạnh_mẽ xã hội hóa_nguồn lực .")
    print("Để bảo_đảm quá trình chuẩn bị , triển_khai đúng quy_định , chặt_chẽ , hiệu_quả , thủ_tướng chính_phủ giao_ban cán_sự Đảng_bộ văn_hóa , thể_thao và du_lịch có tờ_trình , báo_cáo bộ chính_trị trong tháng 7 để xin ý kiến về chủ trương_đăng_cai tổ chức sea_games 31 và para_games 11 năm 2021 tại thành_phố hà_nội , trên cơ sở_đó thông_báo chính thức tới liên_đoàn thể_thao Đông_nam_Á . sau khi bộ chính_trị đồng_ý về chủ_trương , ubnd thành phố_hà nội chủ_trì , phối_hợp chặt_chẽ với bộ văn_hóa , thể_thao và du_lịch và các bộ , cơ_quan , địa_phương liên_quan xây dựng_Đề án tổ_chức sea_games 31 và para_games 11 trên tinh thần tiết_kiệm , an_toàn , hiệu_quả , thành công ; chủ_động rà_soát , hoàn_thiện phương_án chi tiết về cơ_sở vật_chất theo hướng tận dụng tối_đa cơ_sở vật_chất sẵn có , hạn_chế xây_dựng và mua sắm mới , tăng cường mạnh_mẽ xã hội hóa_nguồn lực .")