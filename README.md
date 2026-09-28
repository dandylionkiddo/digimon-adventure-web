# 디지몬 어드벤처 웹 게임

1999년 TV 시리즈 「디지몬 어드벤처」 스토리를 바탕으로 만든 텍스트 어드벤처 게임입니다.

## 플레이 방법

### 웹 버전 (권장)
브라우저에서 [digimon_adventure.html](digimon_adventure.html) 파일을 엽니다.

GitHub Pages를 켜면 온라인으로도 플레이할 수 있습니다.  
(Settings → Pages → Source: Deploy from a branch → **main**)

### 콘솔 버전
```bash
python3 digimon_adventure_game.py
```
(인터넷 연결 필요)

## 파일 구성

| 파일 | 설명 |
|------|------|
| `digimon_adventure.html` | 웹 게임 진입점 |
| `parts/` | 웹 게임 본문 (압축 데이터) |
| `digimon_adventure_game.py` | 콘솔 버전 런처 |
| `디지몬_어드벤처_스토리.md` | 스토리 원본 |

## 게임 특징

- 파일섬 → 서버 대륙 → 현실 세계 → 다크 마스터즈 → 아포칼립몬
- 턴제 전투, 진화 (아구몬 → 그레이몬 → 메탈그레이몬 → 워그레이몬)
- 문장 수집, Wikimon 디지몬 이미지

즐거운 모험 되세요!
