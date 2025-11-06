"""구글맵스 API 연동 모듈"""
import os
from typing import List, Dict
import json

class GoogleMapsIntegration:
    """구글맵스 연동 서비스"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('GOOGLE_MAPS_API_KEY')
        if not self.api_key:
            print("⚠️  경고: 구글 맵스 API 키가 설정되지 않았습니다.")
            print("    .env 파일에 GOOGLE_MAPS_API_KEY를 설정해주세요.")

    def create_map_url(self, locations: List[Dict]) -> str:
        """구글맵스 URL 생성"""
        if not locations:
            return ""

        # 구글맵스 URL 형식
        base_url = "https://www.google.com/maps/dir/"

        # 각 위치의 좌표를 URL에 추가
        coords = []
        for loc in locations:
            if 'coordinates' in loc:
                lat = loc['coordinates']['lat']
                lng = loc['coordinates']['lng']
                coords.append(f"{lat},{lng}")

        # URL 생성
        map_url = base_url + "/".join(coords)
        return map_url

    def generate_map_html(self, locations: List[Dict], filename: str = "yeosu_trip_map.html"):
        """HTML 지도 파일 생성 (구글맵스 embedded)"""

        if not locations:
            print("위치 정보가 없습니다.")
            return

        # 지도 중심 좌표 (여수 시청)
        center_lat = 34.7604
        center_lng = 127.6622

        # HTML 템플릿
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>여수 2박 3일 여행 경로</title>
    <style>
        body {{
            font-family: 'Malgun Gothic', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        #map {{
            width: 100%;
            height: 600px;
            margin: 20px 0;
            border: 2px solid #ddd;
            border-radius: 8px;
        }}
        .info {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .location-list {{
            margin-top: 20px;
        }}
        .location-item {{
            padding: 15px;
            margin: 10px 0;
            background: #f9f9f9;
            border-left: 4px solid #4285f4;
            border-radius: 4px;
        }}
        .day-header {{
            background: #4285f4;
            color: white;
            padding: 10px 15px;
            margin: 20px 0 10px 0;
            border-radius: 4px;
            font-weight: bold;
        }}
        .location-name {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        .location-time {{
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }}
        .location-address {{
            color: #888;
            font-size: 13px;
            margin-top: 5px;
        }}
        .type-badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 5px;
        }}
        .type-attraction {{ background: #e3f2fd; color: #1976d2; }}
        .type-meal {{ background: #fff3e0; color: #f57c00; }}
        .type-accommodation {{ background: #f3e5f5; color: #7b1fa2; }}
        .type-arrival {{ background: #e8f5e9; color: #388e3c; }}
        .type-departure {{ background: #ffebee; color: #d32f2f; }}
    </style>
</head>
<body>
    <div class="info">
        <h1>🗺️ 서울-여수 2박 3일 여행 경로</h1>

        <div id="map"></div>

        <div class="location-list">
            <h2>📍 방문 장소 목록</h2>
"""

        # 일정별로 그룹화
        current_day = 0
        for loc in locations:
            if loc['day'] != current_day:
                current_day = loc['day']
                html_content += f'            <div class="day-header">Day {current_day}</div>\n'

            # 타입별 배지 색상
            type_class = f"type-{loc['type']}"

            html_content += f"""            <div class="location-item">
                <div class="location-name">
                    <span class="type-badge {type_class}">{loc['type']}</span>
                    {loc['name']}
                </div>
                <div class="location-time">⏰ {loc['time']}</div>
                <div class="location-address">📍 {loc.get('address', '')}</div>
            </div>
"""

        # 구글맵스 스크립트 (API 키 필요)
        html_content += f"""        </div>
    </div>

    <script>
        // 구글맵스 초기화
        function initMap() {{
            // 지도 생성
            const map = new google.maps.Map(document.getElementById('map'), {{
                zoom: 12,
                center: {{ lat: {center_lat}, lng: {center_lng} }},
                mapTypeId: 'roadmap'
            }});

            // 마커 위치 데이터
            const locations = {json.dumps(locations, ensure_ascii=False)};

            // 경로 좌표 배열
            const path = [];

            // 마커 추가
            locations.forEach((loc, index) => {{
                if (loc.coordinates) {{
                    const position = {{
                        lat: loc.coordinates.lat,
                        lng: loc.coordinates.lng
                    }};

                    // 마커 아이콘 색상 (타입별)
                    let icon = {{
                        url: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
                    }};

                    if (loc.type === 'attraction') {{
                        icon.url = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png';
                    }} else if (loc.type === 'meal') {{
                        icon.url = 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png';
                    }} else if (loc.type === 'accommodation') {{
                        icon.url = 'http://maps.google.com/mapfiles/ms/icons/purple-dot.png';
                    }} else if (loc.type === 'arrival' || loc.type === 'departure') {{
                        icon.url = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png';
                    }}

                    // 마커 생성
                    const marker = new google.maps.Marker({{
                        position: position,
                        map: map,
                        title: loc.name,
                        icon: icon,
                        label: {{
                            text: String(index + 1),
                            color: 'white',
                            fontWeight: 'bold'
                        }}
                    }});

                    // 정보 창
                    const infoWindow = new google.maps.InfoWindow({{
                        content: `
                            <div style="padding: 10px; font-family: 'Malgun Gothic';">
                                <h3 style="margin: 0 0 10px 0;">${{loc.name}}</h3>
                                <p style="margin: 5px 0;"><strong>시간:</strong> ${{loc.time}}</p>
                                <p style="margin: 5px 0;"><strong>Day ${{loc.day}}</strong></p>
                                <p style="margin: 5px 0;">${{loc.address || ''}}</p>
                            </div>
                        `
                    }});

                    // 마커 클릭 이벤트
                    marker.addListener('click', () => {{
                        infoWindow.open(map, marker);
                    }});

                    // 경로에 추가
                    path.push(position);
                }}
            }});

            // 경로 선 그리기
            const routePath = new google.maps.Polyline({{
                path: path,
                geodesic: true,
                strokeColor: '#4285f4',
                strokeOpacity: 0.8,
                strokeWeight: 3
            }});

            routePath.setMap(map);
        }}
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key={self.api_key or 'YOUR_API_KEY'}&callback=initMap">
    </script>
</body>
</html>
"""

        # 파일 저장
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"\n✅ 구글맵스 HTML 파일이 생성되었습니다: {filename}")
        print(f"   파일을 브라우저에서 열어 여행 경로를 확인하세요!")

        return filename

    def generate_google_maps_link(self, locations: List[Dict]):
        """구글맵스 링크 생성 및 출력"""
        print(f"\n{'='*80}")
        print("🗺️  구글맵스 여행 경로")
        print(f"{'='*80}\n")

        # Day별로 그룹화
        days = {}
        for loc in locations:
            day = loc['day']
            if day not in days:
                days[day] = []
            days[day].append(loc)

        # Day별 링크 생성
        for day_num in sorted(days.keys()):
            day_locations = days[day_num]
            url = self.create_map_url(day_locations)

            print(f"📅 Day {day_num} 경로:")
            print(f"   {url}\n")

        # 전체 경로 링크
        full_url = self.create_map_url(locations)
        print(f"📍 전체 여행 경로 (3일):")
        print(f"   {full_url}\n")

        print("💡 위 링크를 클릭하거나 복사하여 브라우저에서 열어보세요!")
        print("   구글맵스에서 전체 여행 경로를 확인할 수 있습니다.")
        print(f"{'='*80}\n")

    def export_to_json(self, locations: List[Dict], filename: str = "yeosu_trip.json"):
        """여행 정보를 JSON 파일로 저장"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(locations, f, ensure_ascii=False, indent=2)

        print(f"✅ 여행 정보가 JSON 파일로 저장되었습니다: {filename}")
