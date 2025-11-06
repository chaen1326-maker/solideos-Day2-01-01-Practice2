"""여행 일정 생성 모듈"""
from typing import List, Dict
from datetime import datetime, timedelta
from attractions import YeosuAttractions
from restaurants import YeosuRestaurants

class ItineraryGenerator:
    """여행 일정 생성기"""

    def __init__(self):
        self.attractions_service = YeosuAttractions()
        self.restaurants_service = YeosuRestaurants()

    def generate_3day_itinerary(self) -> Dict:
        """2박 3일 여수 여행 일정 생성"""

        # 첫째 날: 여수 도착 12시, 오후/저녁 관광
        day1 = {
            "day": 1,
            "date": "Day 1",
            "title": "여수 도착 및 오후 관광",
            "schedule": [
                {
                    "time": "12:00",
                    "type": "arrival",
                    "title": "여수 도착",
                    "location": "여수시청",
                    "description": "서울시청에서 출발하여 여수 도착"
                },
                {
                    "time": "12:30-14:00",
                    "type": "meal",
                    "title": "점심 식사 - 돌게장 맛집",
                    "location": "서울식당",
                    "restaurant": self.restaurants_service.restaurants[1],  # 서울식당 (돌게장)
                    "description": "60년 전통의 돌게장 맛집에서 점심"
                },
                {
                    "time": "14:30-16:30",
                    "type": "attraction",
                    "title": "오동도 관광",
                    "attraction": self.attractions_service.attractions[1],  # 오동도
                    "description": "동백꽃으로 유명한 아름다운 섬 관광"
                },
                {
                    "time": "17:00-19:00",
                    "type": "attraction",
                    "title": "여수 해상케이블카",
                    "attraction": self.attractions_service.attractions[0],  # 해상케이블카
                    "description": "여수의 바다를 한눈에 보는 케이블카 체험"
                },
                {
                    "time": "19:30-21:00",
                    "type": "meal",
                    "title": "저녁 식사 - 아구찜",
                    "location": "여수아구찜",
                    "restaurant": self.restaurants_service.restaurants[5],  # 여수아구찜
                    "description": "매콤하고 푸짐한 아구찜으로 저녁 식사"
                },
                {
                    "time": "21:00",
                    "type": "accommodation",
                    "title": "숙소 도착",
                    "location": "여수 시내 호텔",
                    "description": "숙소로 이동 및 휴식"
                }
            ]
        }

        # 둘째 날: 하루 종일 관광
        day2 = {
            "day": 2,
            "date": "Day 2",
            "title": "여수 본격 관광",
            "schedule": [
                {
                    "time": "06:00-08:00",
                    "type": "attraction",
                    "title": "향일암 해돋이",
                    "attraction": self.attractions_service.attractions[3],  # 향일암
                    "description": "해돋이로 유명한 아름다운 사찰 방문"
                },
                {
                    "time": "08:30-10:00",
                    "type": "meal",
                    "title": "아침 식사 - 백반",
                    "location": "진남관백반",
                    "restaurant": self.restaurants_service.restaurants[3],  # 진남관백반
                    "description": "푸짐한 반찬과 함께 나오는 가정식 백반"
                },
                {
                    "time": "10:30-12:00",
                    "type": "attraction",
                    "title": "해양레일바이크",
                    "attraction": self.attractions_service.attractions[9],  # 해양레일바이크
                    "description": "바다 위를 달리는 레일바이크 체험"
                },
                {
                    "time": "12:30-14:00",
                    "type": "meal",
                    "title": "점심 식사 - 생선구이",
                    "location": "해양식당",
                    "restaurant": self.restaurants_service.restaurants[7],  # 해양식당
                    "description": "갓 잡은 생선으로 만든 생선구이 정식"
                },
                {
                    "time": "14:30-16:30",
                    "type": "attraction",
                    "title": "여수 엑스포 해양공원",
                    "attraction": self.attractions_service.attractions[2],  # 엑스포 해양공원
                    "description": "2012 여수세계박람회 개최지 관광"
                },
                {
                    "time": "17:00-18:00",
                    "type": "attraction",
                    "title": "진남관",
                    "attraction": self.attractions_service.attractions[6],  # 진남관
                    "description": "전라좌수영의 본영 역사 유적 탐방"
                },
                {
                    "time": "18:30-20:30",
                    "type": "attraction",
                    "title": "돌산대교 야경 & 낭만포차거리",
                    "attraction": self.attractions_service.attractions[4],  # 돌산대교
                    "description": "여수의 대표 야경 명소 및 포차거리 방문"
                },
                {
                    "time": "20:30-21:00",
                    "type": "meal",
                    "title": "저녁 식사 - 낭만포차",
                    "location": "낭만포차거리",
                    "restaurant": self.restaurants_service.restaurants[4],  # 낭만포차
                    "description": "여수 밤바다를 즐기며 포차 음식"
                },
                {
                    "time": "21:00",
                    "type": "accommodation",
                    "title": "숙소 도착",
                    "location": "여수 시내 호텔",
                    "description": "숙소로 이동 및 휴식"
                }
            ]
        }

        # 셋째 날: 오전 관광 후 서울 귀가
        day3 = {
            "day": 3,
            "date": "Day 3",
            "title": "여수 마지막 관광 및 서울 귀가",
            "schedule": [
                {
                    "time": "09:00-10:00",
                    "type": "attraction",
                    "title": "만성리 해수욕장",
                    "attraction": self.attractions_service.attractions[5],  # 만성리 해수욕장
                    "description": "깨끗한 백사장과 맑은 바닷물"
                },
                {
                    "time": "10:30-11:30",
                    "type": "attraction",
                    "title": "하멜등대",
                    "attraction": self.attractions_service.attractions[8],  # 하멜등대
                    "description": "오동도의 상징적인 등대 방문"
                },
                {
                    "time": "12:00-13:30",
                    "type": "meal",
                    "title": "점심 식사 - 장어구이",
                    "location": "여수장어구이",
                    "restaurant": self.restaurants_service.restaurants[6],  # 여수장어구이
                    "description": "국내산 장어를 숯불에 구워주는 전문점"
                },
                {
                    "time": "14:00-15:00",
                    "type": "shopping",
                    "title": "기념품 구매 및 여행 정리",
                    "location": "여수 중앙시장",
                    "description": "여수 특산물 및 기념품 구매"
                },
                {
                    "time": "15:30",
                    "type": "departure",
                    "title": "여수 출발",
                    "location": "여수시청",
                    "description": "서울로 출발"
                },
                {
                    "time": "19:05",
                    "type": "arrival",
                    "title": "서울 도착",
                    "location": "서울시청",
                    "description": "여행 종료 및 귀가"
                }
            ]
        }

        return {
            "trip_title": "서울-여수 2박 3일 여행",
            "duration": "2박 3일",
            "days": [day1, day2, day3]
        }

    def print_daily_schedule(self, day: Dict):
        """일일 일정 출력"""
        print(f"\n{'='*80}")
        print(f"  {day['date']} - {day['title']}")
        print(f"{'='*80}\n")

        for item in day['schedule']:
            print(f"⏰ {item['time']}")
            print(f"   📍 {item['title']}")

            # 위치 정보 처리
            location = item.get('location', '')
            if 'attraction' in item and 'location' in item['attraction']:
                location = item['attraction']['location']
            elif 'restaurant' in item and 'location' in item['restaurant']:
                location = item['restaurant']['location']

            if location:
                print(f"   위치: {location}")
            print(f"   설명: {item['description']}")

            if item['type'] == 'meal' and 'restaurant' in item:
                r = item['restaurant']
                print(f"   음식: {r['specialty']} (가격대: {r['price_range']}원)")
            elif item['type'] == 'attraction' and 'attraction' in item:
                a = item['attraction']
                if a['admission_fee'] > 0:
                    print(f"   입장료: {a['admission_fee']:,}원")
            print()

    def print_full_itinerary(self, itinerary: Dict):
        """전체 일정 출력"""
        print(f"\n{'#'*80}")
        print(f"  {itinerary['trip_title']}")
        print(f"  기간: {itinerary['duration']}")
        print(f"{'#'*80}")

        for day in itinerary['days']:
            self.print_daily_schedule(day)

        # 비용 계산
        self.print_cost_summary(itinerary)

    def print_cost_summary(self, itinerary: Dict):
        """여행 비용 요약"""
        print(f"\n{'='*80}")
        print(f"  💰 여행 비용 예상")
        print(f"{'='*80}\n")

        # 교통비
        print("1. 교통비")
        print("   - 서울 → 여수: 56,620원 (지하철 + KTX 취소표 + 버스)")
        print("   - 여수 → 서울: 62,600원 (버스 + KTX + 지하철)")
        print("   소계: 119,220원\n")

        # 식사비 (대략적인 추정)
        print("2. 식사비 (1인 기준)")
        print("   - Day 1: 점심(25,000) + 저녁(40,000) = 65,000원")
        print("   - Day 2: 아침(10,000) + 점심(12,000) + 저녁(25,000) = 47,000원")
        print("   - Day 3: 점심(50,000) = 50,000원")
        print("   소계: 162,000원\n")

        # 관광지 입장료
        print("3. 관광지 입장료")
        print("   - 해상케이블카: 15,000원")
        print("   - 엑스포 해양공원: 5,000원")
        print("   - 해양레일바이크: 20,000원")
        print("   - 진남관: 2,000원")
        print("   소계: 42,000원\n")

        # 숙박비
        print("4. 숙박비 (2박, 1인 기준)")
        print("   - 호텔/모텔: 약 150,000원 (2박)\n")

        # 총합
        print(f"{'='*80}")
        print("💵 총 예상 비용 (1인 기준): 약 473,220원")
        print(f"{'='*80}\n")

    def get_all_locations(self, itinerary: Dict) -> List[Dict]:
        """일정의 모든 위치 정보 추출 (구글맵스용)"""
        locations = []

        for day in itinerary['days']:
            for item in day['schedule']:
                location_data = {
                    "name": item['title'],
                    "time": item['time'],
                    "day": day['day'],
                    "type": item['type']
                }

                # 좌표 정보 추가
                if 'attraction' in item:
                    location_data['coordinates'] = item['attraction']['coordinates']
                    location_data['address'] = item['attraction']['location']
                elif 'restaurant' in item:
                    location_data['coordinates'] = item['restaurant']['coordinates']
                    location_data['address'] = item['restaurant']['location']
                else:
                    # 기본 위치 (여수시청)
                    location_data['coordinates'] = {"lat": 34.7604, "lng": 127.6622}
                    location_data['address'] = item['location']

                locations.append(location_data)

        return locations
