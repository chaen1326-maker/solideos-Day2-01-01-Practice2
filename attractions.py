"""여수 관광지 정보 모듈"""
from typing import List, Dict

class YeosuAttractions:
    """여수 관광지 서비스"""

    def __init__(self):
        self.attractions = self._load_attractions()

    def _load_attractions(self) -> List[Dict]:
        """여수 유명 관광지 데이터"""
        return [
            {
                "id": 1,
                "name": "여수 해상케이블카",
                "category": "관광명소",
                "location": "여수시 돌산읍 돌산로 3600-1",
                "coordinates": {"lat": 34.7461, "lng": 127.7656},
                "description": "여수의 바다를 한눈에 볼 수 있는 케이블카",
                "duration": 120,  # 분
                "opening_hours": "09:00-22:00",
                "admission_fee": 15000,
                "rating": 4.5,
                "recommended_time": "오후",
                "must_visit": True
            },
            {
                "id": 2,
                "name": "오동도",
                "category": "자연경관",
                "location": "여수시 오동도로 222",
                "coordinates": {"lat": 34.7469, "lng": 127.7708},
                "description": "동백꽃으로 유명한 아름다운 섬",
                "duration": 90,
                "opening_hours": "05:00-23:00",
                "admission_fee": 0,
                "rating": 4.6,
                "recommended_time": "오전",
                "must_visit": True
            },
            {
                "id": 3,
                "name": "여수 엑스포 해양공원",
                "category": "공원",
                "location": "여수시 박람회길 1",
                "coordinates": {"lat": 34.7506, "lng": 127.7425},
                "description": "2012 여수세계박람회 개최지",
                "duration": 120,
                "opening_hours": "10:00-18:00",
                "admission_fee": 5000,
                "rating": 4.3,
                "recommended_time": "오전",
                "must_visit": False
            },
            {
                "id": 4,
                "name": "향일암",
                "category": "사찰",
                "location": "여수시 돌산읍 향일암로 60",
                "coordinates": {"lat": 34.6236, "lng": 127.7250},
                "description": "해돋이로 유명한 아름다운 사찰",
                "duration": 90,
                "opening_hours": "05:00-19:00",
                "admission_fee": 0,
                "rating": 4.7,
                "recommended_time": "아침",
                "must_visit": True
            },
            {
                "id": 5,
                "name": "돌산대교",
                "category": "랜드마크",
                "location": "여수시 돌산읍",
                "coordinates": {"lat": 34.7372, "lng": 127.7481},
                "description": "여수의 야경 명소",
                "duration": 30,
                "opening_hours": "24시간",
                "admission_fee": 0,
                "rating": 4.4,
                "recommended_time": "저녁",
                "must_visit": True
            },
            {
                "id": 6,
                "name": "만성리 해수욕장",
                "category": "해변",
                "location": "여수시 만성리 산1-22",
                "coordinates": {"lat": 34.7325, "lng": 127.8089},
                "description": "깨끗한 백사장과 맑은 바닷물",
                "duration": 60,
                "opening_hours": "24시간",
                "admission_fee": 0,
                "rating": 4.2,
                "recommended_time": "오후",
                "must_visit": False
            },
            {
                "id": 7,
                "name": "진남관",
                "category": "역사유적",
                "location": "여수시 군자동 5-1",
                "coordinates": {"lat": 34.7381, "lng": 127.7347},
                "description": "전라좌수영의 본영",
                "duration": 60,
                "opening_hours": "09:00-18:00",
                "admission_fee": 2000,
                "rating": 4.1,
                "recommended_time": "오전",
                "must_visit": False
            },
            {
                "id": 8,
                "name": "여수 밤바다 (낭만포차거리)",
                "category": "거리",
                "location": "여수시 중앙동 일대",
                "coordinates": {"lat": 34.7419, "lng": 127.7378},
                "description": "여수 밤바다를 즐기는 포차거리",
                "duration": 90,
                "opening_hours": "18:00-24:00",
                "admission_fee": 0,
                "rating": 4.5,
                "recommended_time": "저녁",
                "must_visit": True
            },
            {
                "id": 9,
                "name": "하멜등대",
                "category": "등대",
                "location": "여수시 오동도로 222",
                "coordinates": {"lat": 34.7461, "lng": 127.7722},
                "description": "오동도의 상징적인 등대",
                "duration": 30,
                "opening_hours": "24시간",
                "admission_fee": 0,
                "rating": 4.0,
                "recommended_time": "오후",
                "must_visit": False
            },
            {
                "id": 10,
                "name": "여수 해양레일바이크",
                "category": "액티비티",
                "location": "여수시 망마로 187",
                "coordinates": {"lat": 34.7486, "lng": 127.7453},
                "description": "바다 위를 달리는 레일바이크",
                "duration": 60,
                "opening_hours": "09:00-18:00",
                "admission_fee": 20000,
                "rating": 4.4,
                "recommended_time": "오전",
                "must_visit": False
            }
        ]

    def get_all_attractions(self) -> List[Dict]:
        """모든 관광지 반환"""
        return self.attractions

    def get_must_visit_attractions(self) -> List[Dict]:
        """필수 방문 관광지만 반환"""
        return [attr for attr in self.attractions if attr.get('must_visit', False)]

    def get_attraction_by_time(self, time_of_day: str) -> List[Dict]:
        """시간대별 추천 관광지"""
        return [attr for attr in self.attractions if attr['recommended_time'] == time_of_day]

    def print_attraction(self, attraction: Dict):
        """관광지 정보 출력"""
        print(f"\n📍 {attraction['name']}")
        print(f"   분류: {attraction['category']}")
        print(f"   위치: {attraction['location']}")
        print(f"   설명: {attraction['description']}")
        print(f"   소요시간: {attraction['duration']}분")
        print(f"   운영시간: {attraction['opening_hours']}")
        print(f"   입장료: {attraction['admission_fee']:,}원")
        print(f"   평점: {attraction['rating']}/5.0")
        if attraction.get('must_visit'):
            print(f"   ⭐ 필수 방문지")
