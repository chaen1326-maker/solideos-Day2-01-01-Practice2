"""여행 개인화 앱 - 메인 실행 파일"""
import os
from dotenv import load_dotenv
from transportation import TransportationService
from attractions import YeosuAttractions
from restaurants import YeosuRestaurants
from itinerary import ItineraryGenerator
from maps_integration import GoogleMapsIntegration

def print_header():
    """헤더 출력"""
    print("\n" + "="*80)
    print(" " * 20 + "🏖️  서울-여수 2박 3일 여행 계획 🏖️")
    print("="*80 + "\n")

def main():
    """메인 실행 함수"""
    # 환경 변수 로드
    load_dotenv()

    print_header()

    # 서비스 초기화
    transport = TransportationService()
    attractions = YeosuAttractions()
    restaurants = YeosuRestaurants()
    itinerary_gen = ItineraryGenerator()
    maps = GoogleMapsIntegration()

    # 1. 교통편 조회
    print("\n" + "#"*80)
    print("  1️⃣  교통편 조회")
    print("#"*80)

    print("\n📍 서울시청 → 여수 (도착 목표: 12시)")
    print("-" * 80)
    to_yeosu_routes = transport.search_route_to_yeosu("09:00")

    for route in to_yeosu_routes:
        transport.print_route(route)

    print("\n📍 여수 → 서울시청 (도착 목표: 19시)")
    print("-" * 80)
    to_seoul_routes = transport.search_return_route("15:30")

    for route in to_seoul_routes:
        transport.print_route(route)

    # 2. 관광지 정보
    print("\n" + "#"*80)
    print("  2️⃣  여수 주요 관광지")
    print("#"*80)

    must_visit = attractions.get_must_visit_attractions()
    print(f"\n⭐ 필수 방문 관광지 ({len(must_visit)}곳)\n")
    for attr in must_visit:
        attractions.print_attraction(attr)

    # 3. 맛집 정보
    print("\n" + "#"*80)
    print("  3️⃣  여수 맛집 정보")
    print("#"*80)

    print("\n🦀 돌게장 맛집\n")
    dolgetjang = restaurants.get_dolgetjang_restaurants()
    for rest in dolgetjang:
        restaurants.print_restaurant(rest)

    print("\n🍴 추천 맛집 (한식)\n")
    korean_restaurants = [r for r in restaurants.restaurants if r['cuisine'] == '한식' and r['category'] != '돌게장'][:5]
    for rest in korean_restaurants:
        restaurants.print_restaurant(rest)

    # 4. 2박 3일 일정 생성
    print("\n" + "#"*80)
    print("  4️⃣  2박 3일 여행 일정")
    print("#"*80)

    itinerary = itinerary_gen.generate_3day_itinerary()
    itinerary_gen.print_full_itinerary(itinerary)

    # 5. 구글맵스 연동
    print("\n" + "#"*80)
    print("  5️⃣  구글맵스 경로 생성")
    print("#"*80)

    locations = itinerary_gen.get_all_locations(itinerary)

    # JSON 저장
    maps.export_to_json(locations)

    # HTML 지도 생성
    html_file = maps.generate_map_html(locations)

    # 구글맵스 링크 생성
    maps.generate_google_maps_link(locations)

    # 마무리
    print("\n" + "="*80)
    print("✅ 여행 계획이 완성되었습니다!")
    print("="*80)
    print("\n📝 생성된 파일:")
    print(f"   - {html_file}: 브라우저에서 열어 지도 확인")
    print(f"   - yeosu_trip.json: 여행 데이터 JSON")
    print("\n💡 팁:")
    print("   - HTML 파일을 브라우저에서 열면 인터랙티브한 지도를 볼 수 있습니다")
    print("   - 구글맵스 링크를 복사하여 모바일에서도 확인하세요")
    print("   - 각 장소의 마커를 클릭하면 상세 정보를 볼 수 있습니다")
    print("\n🎉 즐거운 여수 여행 되세요! 🎉\n")

if __name__ == "__main__":
    main()
