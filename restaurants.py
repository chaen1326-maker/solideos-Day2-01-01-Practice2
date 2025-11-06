"""여수 맛집 정보 모듈"""
from typing import List, Dict

class YeosuRestaurants:
    """여수 맛집 서비스"""

    def __init__(self):
        self.restaurants = self._load_restaurants()

    def _load_restaurants(self) -> List[Dict]:
        """여수 맛집 데이터"""
        return [
            {
                "id": 1,
                "name": "거북식당",
                "category": "돌게장",
                "cuisine": "한식",
                "location": "여수시 중앙동 111-1",
                "coordinates": {"lat": 34.7397, "lng": 127.7389},
                "description": "여수 대표 돌게장 맛집, 신선한 게장과 함께 먹는 백반",
                "menu": ["돌게장정식", "간장게장", "양념게장"],
                "price_range": "15000-25000",
                "opening_hours": "11:00-21:00",
                "rating": 4.6,
                "specialty": "돌게장",
                "recommended_meal": "점심",
                "must_visit": True
            },
            {
                "id": 2,
                "name": "서울식당",
                "category": "돌게장",
                "cuisine": "한식",
                "location": "여수시 돌산읍 돌산로 3600",
                "coordinates": {"lat": 34.7456, "lng": 127.7642},
                "description": "60년 전통의 돌게장 원조 맛집",
                "menu": ["돌게장백반", "게장정식", "된장찌개"],
                "price_range": "18000-30000",
                "opening_hours": "10:00-20:00",
                "rating": 4.7,
                "specialty": "돌게장",
                "recommended_meal": "점심",
                "must_visit": True
            },
            {
                "id": 3,
                "name": "돌산횟집거리",
                "category": "회",
                "cuisine": "한식",
                "location": "여수시 돌산읍 돌산로 일대",
                "coordinates": {"lat": 34.7465, "lng": 127.7653},
                "description": "신선한 활어회를 맛볼 수 있는 횟집 거리",
                "menu": ["모듬회", "광어회", "우럭회", "매운탕"],
                "price_range": "40000-80000",
                "opening_hours": "11:00-22:00",
                "rating": 4.4,
                "specialty": "활어회",
                "recommended_meal": "저녁"
            },
            {
                "id": 4,
                "name": "진남관백반",
                "category": "백반",
                "cuisine": "한식",
                "location": "여수시 군자동 5-10",
                "coordinates": {"lat": 34.7385, "lng": 127.7352},
                "description": "푸짐한 반찬과 함께 나오는 가정식 백반",
                "menu": ["제육볶음정식", "고등어구이정식", "된장찌개정식"],
                "price_range": "8000-12000",
                "opening_hours": "07:00-21:00",
                "rating": 4.3,
                "specialty": "한정식",
                "recommended_meal": "아침"
            },
            {
                "id": 5,
                "name": "낭만포차",
                "category": "포차",
                "cuisine": "한식",
                "location": "여수시 중앙동 포차거리",
                "coordinates": {"lat": 34.7421, "lng": 127.7381},
                "description": "여수 밤바다를 즐기며 먹는 포차 음식",
                "menu": ["오징어무침", "간장게장", "새우튀김", "해물파전"],
                "price_range": "10000-30000",
                "opening_hours": "18:00-02:00",
                "rating": 4.5,
                "specialty": "안주류",
                "recommended_meal": "저녁"
            },
            {
                "id": 6,
                "name": "여수아구찜",
                "category": "찜",
                "cuisine": "한식",
                "location": "여수시 학동 252-1",
                "coordinates": {"lat": 34.7423, "lng": 127.7512},
                "description": "매콤하고 푸짐한 아구찜 전문점",
                "menu": ["아구찜", "아구수육", "물아구"],
                "price_range": "30000-50000",
                "opening_hours": "11:00-22:00",
                "rating": 4.5,
                "specialty": "아구찜",
                "recommended_meal": "저녁"
            },
            {
                "id": 7,
                "name": "여수장어구이",
                "category": "장어",
                "cuisine": "한식",
                "location": "여수시 문수동 1265",
                "coordinates": {"lat": 34.7352, "lng": 127.7289},
                "description": "국내산 장어를 숯불에 구워주는 전문점",
                "menu": ["장어구이", "장어탕", "장어덮밥"],
                "price_range": "35000-60000",
                "opening_hours": "12:00-22:00",
                "rating": 4.4,
                "specialty": "장어구이",
                "recommended_meal": "저녁"
            },
            {
                "id": 8,
                "name": "해양식당",
                "category": "백반",
                "cuisine": "한식",
                "location": "여수시 광무동 1-5",
                "coordinates": {"lat": 34.7392, "lng": 127.7425},
                "description": "갓 잡은 생선으로 만든 생선구이 정식",
                "menu": ["갈치구이정식", "고등어구이정식", "삼치구이정식"],
                "price_range": "10000-15000",
                "opening_hours": "08:00-20:00",
                "rating": 4.3,
                "specialty": "생선구이",
                "recommended_meal": "점심"
            },
            {
                "id": 9,
                "name": "향일암식당",
                "category": "해물탕",
                "cuisine": "한식",
                "location": "여수시 돌산읍 향일암로 55",
                "coordinates": {"lat": 34.6241, "lng": 127.7255},
                "description": "향일암 근처의 해물탕 맛집",
                "menu": ["해물탕", "해물찜", "해물전골"],
                "price_range": "30000-50000",
                "opening_hours": "09:00-20:00",
                "rating": 4.2,
                "specialty": "해물탕",
                "recommended_meal": "점심"
            },
            {
                "id": 10,
                "name": "여수한정식",
                "category": "한정식",
                "cuisine": "한식",
                "location": "여수시 소호동 567-1",
                "coordinates": {"lat": 34.7401, "lng": 127.7445},
                "description": "여수 지역 식재료로 만든 고급 한정식",
                "menu": ["특선한정식", "계절한정식", "전복한정식"],
                "price_range": "40000-80000",
                "opening_hours": "11:30-21:00",
                "rating": 4.6,
                "specialty": "한정식",
                "recommended_meal": "저녁"
            }
        ]

    def get_all_restaurants(self) -> List[Dict]:
        """모든 맛집 반환"""
        return self.restaurants

    def get_by_specialty(self, specialty: str) -> List[Dict]:
        """특정 메뉴 전문 맛집 검색"""
        return [r for r in self.restaurants if r['specialty'] == specialty]

    def get_by_meal_time(self, meal_time: str) -> List[Dict]:
        """식사 시간대별 맛집 추천"""
        return [r for r in self.restaurants if r.get('recommended_meal') == meal_time]

    def get_dolgetjang_restaurants(self) -> List[Dict]:
        """돌게장 맛집만 반환"""
        return [r for r in self.restaurants if r['category'] == '돌게장']

    def print_restaurant(self, restaurant: Dict):
        """맛집 정보 출력"""
        print(f"\n🍽️  {restaurant['name']}")
        print(f"   분류: {restaurant['category']} ({restaurant['cuisine']})")
        print(f"   위치: {restaurant['location']}")
        print(f"   설명: {restaurant['description']}")
        print(f"   대표메뉴: {', '.join(restaurant['menu'][:3])}")
        print(f"   가격대: {restaurant['price_range']}원")
        print(f"   영업시간: {restaurant['opening_hours']}")
        print(f"   평점: {restaurant['rating']}/5.0")
        if restaurant.get('must_visit'):
            print(f"   ⭐ 필수 방문 맛집")
