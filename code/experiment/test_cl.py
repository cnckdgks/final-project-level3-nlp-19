from news_preprocessing import *

simple_text = ["[OSEN=강서정 기자] 김준희, 한혜진, 경리 등의 SNS는 그야말로 ‘다이어트 자극사진’으로 가득하다. 운동하는 모습을 담은 사진을 공개하거나 운동으로 탄탄해진 몸매를 자랑하는 이들의 사진을 보고 있으면 절로 감탄이 나올 정도다.◆ 한혜진한혜진은 놀라울 정도로 열심히 운동하는 모델이다. 자신의 몸매관리를 위해 꾸준히 노력하고 화보 촬영 전에는 한 달 동안 쌀과 반찬을 안 먹을 정도로 철저하다. 그가 SNS에 게재한 등근육 사진이 크게 화제가 되기도 했다.◆ 김준희김준희의 SNS는 ‘다이어트의 정석’이다. 운동하는 모습부터 식단까지 모든 것이 담겨있다. 닭가슴살과 샐러드에 지친 다이어터라면 김준희의 SNS을 팔로우하는 것도 좋을 듯하다. 거기다 운동으로 다져진 몸매를 보고 있으면 운동욕구가 무한 자극된다.◆ 장윤주장윤주는 완벽한 비율과 각선미를 자랑하는데 여기에는 그의 피나는 노력이 있었다. 방송에서 출산 후 몸매를 만들기 위해 필라테스를 하는 모습이 공개되기도 했다. 특히 출산 후에도 여전한 몸매를 자랑하는 그는 주부들의 다이어트를 자극하기도.◆ 손나은손나은은 굴곡진 몸매가 돋보이는 아이돌이다. 다이어트 식품 모델로도 활동하고 있는 손나은은 데뷔 초와 달리 늘씬한 몸매로 부러움을 사고 있다.◆ 제시가슴 성형수술을 당당하게 고백한 제시는 볼륨 있는 몸매를 자랑한다. 하지만 그의 잘록한 허리도 감탄을 자아낼 정도. 비키니부터 트레이닝복까지 완벽하게 소화하는 몸매의 소유자다.◆ 신수지신수지는 리듬체조 전 국가대표 출신답게 탄탄하면서도 볼륨감 있는 몸매가 돋보인다. SNS에서 플라잉 요가로 유연한 몸을 뽐내는 것은 물론 부러움을 자아내는 각선미가 눈길을 끈다.◆ 경리경리는 잘록한 허리가 돋보이는 S라인 몸매가 매력적이다. 몸매가 드러나는 의상을 입어도 전혀 굴욕 없는 몸매는 여성들의 워너비다. /kangsj@osen.co.kr[사진] 김준희, 한혜진, 장윤주, 손나은, 제시, 신수지, 경리 인스타그램', 'question': '손나은은 무슨 모델로도 활동하고 있는가?"]

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('klue/bert-base')

print(remove_press(simple_text))