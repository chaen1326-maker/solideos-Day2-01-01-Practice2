"""교통편 조회 모듈"""
from datetime import datetime, timedelta
from typing import List, Dict

class TransportationService:
    """교통편 조회 서비스"""

    def __init__(self):
        self.routes = []

    def search_route_to_yeosu(self, departure_time: str) -> List[Dict]:
        """서울시청에서 여수까지 경로 조회"""
        # 출발 시간: departure_time (예: "09:00")
        routes = []

        # 옵션 1: 지하철 + KTX (일반)
        routes.append({
            "option": 1,
            "description": "지하철 + KTX (일반열차)",
            "segments": [
                {
                    "type": "지하철",
                    "line": "2호선",
                    "from": "서울시청역",
                    "to": "서울역",
                    "departure": "08:30",
                    "arrival": "08:40",
                    "duration": 10,
                    "price": 1400
                },
                {
                    "type": "도보",
                    "from": "서울역 (지하철)",
                    "to": "서울역 (KTX)",
                    "duration": 5,
                    "price": 0
                },
                {
                    "type": "KTX",
                    "train_number": "KTX 401",
                    "from": "서울역",
                    "to": "여수EXPO역",
                    "departure": "09:00",
                    "arrival": "11:50",
                    "duration": 170,
                    "price": 59800
                },
                {
                    "type": "버스",
                    "line": "1번",
                    "from": "여수EXPO역",
                    "to": "여수시청",
                    "departure": "12:00",
                    "arrival": "12:10",
                    "duration": 10,
                    "price": 1400
                }
            ],
            "total_duration": 220,  # 3시간 40분
            "total_price": 62600,
            "arrival_time": "12:10"
        })

        # 옵션 2: 지하철 + KTX (취소표 - 할인)
        routes.append({
            "option": 2,
            "description": "지하철 + KTX (취소표 - 10% 할인)",
            "segments": [
                {
                    "type": "지하철",
                    "line": "2호선",
                    "from": "서울시청역",
                    "to": "서울역",
                    "departure": "08:20",
                    "arrival": "08:30",
                    "duration": 10,
                    "price": 1400
                },
                {
                    "type": "도보",
                    "from": "서울역 (지하철)",
                    "to": "서울역 (KTX)",
                    "duration": 5,
                    "price": 0
                },
                {
                    "type": "KTX",
                    "train_number": "KTX 403 (취소표)",
                    "from": "서울역",
                    "to": "여수EXPO역",
                    "departure": "08:50",
                    "arrival": "11:40",
                    "duration": 170,
                    "price": 53820,  # 10% 할인
                    "note": "취소표 - 선착순 마감"
                },
                {
                    "type": "버스",
                    "line": "1번",
                    "from": "여수EXPO역",
                    "to": "여수시청",
                    "departure": "11:50",
                    "arrival": "12:00",
                    "duration": 10,
                    "price": 1400
                }
            ],
            "total_duration": 220,
            "total_price": 56620,
            "arrival_time": "12:00"
        })

        # 옵션 3: 버스 + KTX
        routes.append({
            "option": 3,
            "description": "버스 + KTX",
            "segments": [
                {
                    "type": "버스",
                    "line": "405번",
                    "from": "서울시청",
                    "to": "서울역",
                    "departure": "08:35",
                    "arrival": "08:45",
                    "duration": 10,
                    "price": 1400
                },
                {
                    "type": "KTX",
                    "train_number": "KTX 405",
                    "from": "서울역",
                    "to": "여수EXPO역",
                    "departure": "09:10",
                    "arrival": "12:00",
                    "duration": 170,
                    "price": 59800
                },
                {
                    "type": "도보",
                    "from": "여수EXPO역",
                    "to": "여수시청",
                    "duration": 5,
                    "price": 0
                }
            ],
            "total_duration": 210,
            "total_price": 61200,
            "arrival_time": "12:05"
        })

        return routes

    def search_return_route(self, departure_time: str) -> List[Dict]:
        """여수에서 서울시청까지 귀가 경로 조회"""
        routes = []

        # 옵션 1: KTX + 지하철 (19:00 서울 도착)
        routes.append({
            "option": 1,
            "description": "KTX + 지하철 (서울 19:00 도착)",
            "segments": [
                {
                    "type": "버스",
                    "line": "1번",
                    "from": "여수시청",
                    "to": "여수EXPO역",
                    "departure": "15:30",
                    "arrival": "15:40",
                    "duration": 10,
                    "price": 1400
                },
                {
                    "type": "KTX",
                    "train_number": "KTX 502",
                    "from": "여수EXPO역",
                    "to": "서울역",
                    "departure": "16:00",
                    "arrival": "18:50",
                    "duration": 170,
                    "price": 59800
                },
                {
                    "type": "지하철",
                    "line": "2호선",
                    "from": "서울역",
                    "to": "서울시청역",
                    "departure": "18:55",
                    "arrival": "19:05",
                    "duration": 10,
                    "price": 1400
                }
            ],
            "total_duration": 215,
            "total_price": 62600,
            "arrival_time": "19:05"
        })

        return routes

    def print_route(self, route: Dict):
        """경로 출력"""
        print(f"\n{'='*60}")
        print(f"옵션 {route['option']}: {route['description']}")
        print(f"총 소요시간: {route['total_duration']}분 ({route['total_duration']//60}시간 {route['total_duration']%60}분)")
        print(f"총 비용: {route['total_price']:,}원")
        print(f"도착 시간: {route['arrival_time']}")
        print(f"{'='*60}")

        for i, segment in enumerate(route['segments'], 1):
            print(f"\n[구간 {i}] {segment['type']}")
            if segment['type'] == '도보':
                print(f"  경로: {segment['from']} → {segment['to']}")
                print(f"  소요시간: {segment['duration']}분")
            else:
                if 'line' in segment:
                    print(f"  노선: {segment['line']}")
                if 'train_number' in segment:
                    print(f"  열차: {segment['train_number']}")
                print(f"  출발: {segment['from']} ({segment.get('departure', '-')})")
                print(f"  도착: {segment['to']} ({segment.get('arrival', '-')})")
                print(f"  소요시간: {segment['duration']}분")
                print(f"  요금: {segment['price']:,}원")
                if 'note' in segment:
                    print(f"  ※ {segment['note']}")
