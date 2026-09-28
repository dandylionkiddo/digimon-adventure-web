#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
디지몬 어드벤처 - 콘솔 게임
1999년 TV 시리즈 스토리를 기반으로 한 텍스트 어드벤처
"""

import random
import sys

# ========== 디지몬 데이터 ==========
IMG_NOTE = "(이미지: Wikimon Bandai reference book)"

class Digimon:
    def __init__(self, name, stage, hp, atk):
        self.name = name
        self.stage = stage
        self.hp = hp
        self.max_hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)
        return dmg

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def __str__(self):
        return f"{self.name}({self.stage}) HP:{self.hp}/{self.max_hp} ATK:{self.atk}"


EVOLUTIONS = {
    "Agumon": [
        Digimon("Greymon", "성숙기", 180, 45),
        Digimon("MetalGreymon", "완전체", 280, 70),
        Digimon("WarGreymon", "궁극체", 400, 100),
    ],
    "Gabumon": [
        Digimon("Garurumon", "성숙기", 170, 42),
        Digimon("WereGarurumon", "완전체", 270, 68),
        Digimon("MetalGarurumon", "궁극체", 390, 98),
    ],
}

CRESTS = ["용기", "우정", "사랑", "지식", "성실", "희망", "빛", "기적"]


class Game:
    def __init__(self):
        self.partner = Digimon("Agumon", "성장기", 100, 25)
        self.crests = set()
        self.chapter = 0

    def status(self):
        print("\n" + "=" * 40)
        print(f"파트너: {self.partner}")
        owned = ", ".join(sorted(self.crests)) if self.crests else "없음"
        print(f"문장: {owned}")
        print("=" * 40)

    def battle(self, enemy, can_evolve=True):
        print(f"\n>>> 전투 시작! {enemy.name}({enemy.stage})이(가) 나타났다!")
        while self.partner.is_alive() and enemy.is_alive():
            print(f"\n[나] {self.partner}")
            print(f"[적] {enemy}")
            print("1. 공격  2. 진화 시도  3. 문장 사용(회복)")
            choice = input("> ").strip()
            if choice == "1":
                dmg = self.partner.atk + random.randint(0, 9)
                enemy.take_damage(dmg)
                print(f"{self.partner.name}의 공격! {dmg} 데미지")
            elif choice == "2" and can_evolve:
                self.try_evolve()
            elif choice == "3":
                if self.crests:
                    heal = 40 + random.randint(0, 19)
                    self.partner.heal(heal)
                    print(f"문장의 힘으로 HP {heal} 회복!")
                else:
                    print("가진 문장이 없다.")
            else:
                print("잘못된 입력.")
                continue

            if not enemy.is_alive():
                print(f"{enemy.name}을(를) 쓰러뜨렸다!")
                return True

            # 적 턴
            dmg = enemy.atk + random.randint(0, 7)
            self.partner.take_damage(dmg)
            print(f"{enemy.name}의 공격! {dmg} 데미지")

        if not self.partner.is_alive():
            print("파트너가 쓰러졌다... 게임 오버.")
            return False
        return True

    def try_evolve(self):
        evo_list = EVOLUTIONS.get(self.partner.name, EVOLUTIONS["Agumon"])
        stages = ["성장기", "성숙기", "완전체", "궁극체"]
        cur_idx = stages.index(self.partner.stage) if self.partner.stage in stages else 0
        for evo in evo_list:
            next_idx = stages.index(evo.stage)
            if next_idx == cur_idx + 1:
                # 문장 요구 체크 (완전체 이상)
                if evo.stage in ("완전체", "궁극체") and "용기" not in self.crests and "우정" not in self.crests:
                    print("문장이 부족해 진화할 수 없다.")
                    return
                self.partner = Digimon(evo.name, evo.stage, evo.hp, evo.atk)
                print(f"진화! {evo.name}({evo.stage})로 진화했다!")
                return
        print("지금은 진화할 수 없다.")

    def run(self):
        print("=" * 50)
        print("  디지몬 어드벤처 - 콘솔 게임")
        print("  1999년 TV 시리즈 스토리 기반")
        print("=" * 50)

        # Chapter 0: 시작
        print("\n여름 캠프장. 하늘에서 이상한 장치가 떨어진다.")
        print("태일, 아구몬과 함께 디지털 월드로 향한다.")
        print("파일섬에 도착했다.")
        input("\n[Enter] 섬을 탐색한다...")

        # Chapter 1: 쿠와가몬
        print("\n숲을 걷던 중 거대한 곤충 디지몬이 나타난다.")
        if not self.battle(Digimon("Kuwagamon", "성숙기", 90, 20)):
            return
        print("쿠와가몬을 물리쳤다! 아구몬이 성장의 기운을 느낀다.")
        input("[Enter] 계속...")

        # Chapter 2: 쉘몬 & 시드라몬
        print("\n해변에서 쉘몬이 나타난다.")
        if not self.battle(Digimon("Shellmon", "성숙기", 110, 22)):
            return
        print("쉘몬을 쓰러뜨렸다. 바다 쪽으로 나아가자 시드라몬이 나타난다!")
        if not self.battle(Digimon("Seadramon", "성숙기", 120, 25)):
            return
        print("시드라몬도 물리쳤다. 섬 중앙의 산으로 향한다.")
        input("[Enter] 산으로 이동...")

        # Chapter 3: 메라몬 & 안드로몬
        print("\n화산 지대. 메라몬이 길을 막는다.")
        if not self.battle(Digimon("Meramon", "성숙기", 130, 28)):
            return
        print("메라몬을 물리쳤다. 공장 유적에서 안드로몬이 폭주한다.")
        if not self.battle(Digimon("Andromon", "완전체", 160, 32)):
            return
        print("안드로몬을 진정시켰다.")
        print(">>> 용기의 문장을 손에 넣었다!")
        self.crests.add("용기")
        self.status()
        input("[Enter] 다음으로...")

        # Chapter 4: 데비몬
        print("\n파일섬의 어둠. 데비몬이 아이들을 노린다.")
        print("아구몬이 진화할 준비가 되어 있다.")
        self.partner = Digimon("Greymon", "성숙기", 180, 45)
        print("그레이몬으로 진화!")
        self.status()
        if not self.battle(Digimon("Devimon", "성숙기", 200, 40)):
            return
        print("데비몬을 물리쳤다! 파일섬의 어둠이 걷힌다.")
        print("서버 대륙으로 향한다.")
        input("[Enter] 서버 대륙으로...")

        # Chapter 5: 에테몬
        print("\n서버 대륙. 독재자 에테몬이 네트워크를 장악하고 있다.")
        print(">>> 우정의 문장을 찾았다!")
        self.crests.add("우정")
        self.status()
        if not self.battle(Digimon("Etemon", "완전체", 250, 50)):
            return
        print("에테몬을 쓰러뜨렸다!")
        self.partner = Digimon("MetalGreymon", "완전체", 280, 70)
        print("메탈그레이몬으로 진화!")
        self.status()
        input("[Enter] 현실 세계로...")

        # Chapter 6: 묘티스몬
        print("\n현실 세계. 밤의 지배자 묘티스몬이 아이들을 쫓는다.")
        print(">>> 빛의 문장을 얻었다!")
        self.crests.add("빛")
        self.status()
        if not self.battle(Digimon("Myotismon", "완전체", 300, 55)):
            return
        print("묘티스몬이 베놈묘티스몬으로 진화한다!")
        if not self.battle(Digimon("VenomMyotismon", "궁극체", 380, 70)):
            return
        print("베놈묘티스몬을 물리쳤다! 디지털 월드로 다시 돌아간다.")
        input("[Enter] 다크 마스터즈로...")

        # Chapter 7: 다크 마스터즈
        print("\n다크 마스터즈가 디지털 월드를 지배하고 있다.")
        print("메탈시드라몬, 퍼펫몬, 머쉰드라몬, 피에드몬... 하나씩 쓰러뜨려야 한다.")

        bosses = [
            Digimon("MetalSeadramon", "궁극체", 320, 65),
            Digimon("Puppetmon", "궁극체", 300, 60),
            Digimon("Machinedramon", "궁극체", 350, 75),
            Digimon("Piedmon", "궁극체", 360, 80),
        ]
        for boss in bosses:
            print(f"\n>>> {boss.name}과의 전투!")
            if not self.battle(boss):
                return
            print(f"{boss.name}을(를) 물리쳤다!")

        print("\n>>> 용기의 힘으로 워그레이몬으로 진화!")
        self.partner = Digimon("WarGreymon", "궁극체", 400, 100)
        self.status()
        input("[Enter] 최종 보스에게...")

        # Chapter 8: 아포칼립몬
        print("\n모든 악의 집합체. 아포칼립몬이 나타난다.")
        print("아이들의 희망과 우정, 용기가 하나 된다.")
        if not self.battle(Digimon("Apocalymon", "궁극체", 500, 90)):
            return

        print("\n" + "=" * 50)
        print("  아포칼립몬을 물리쳤다!")
        print("  디지털 월드에 평화가 찾아온다.")
        print(f"  태일과 {self.partner.name} ({self.partner.stage})")
        print("  디지몬 어드벤처 - CLEAR!")
        print("=" * 50)
        print("\n원작의 핵심은 아이들이 각자의 약점과 감정을")
        print("마주하며 성장하는 모습입니다.")
        print("플레이해 주셔서 감사합니다!")


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\n\n게임을 종료합니다.")
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")
        print("게임을 종료합니다.")

if __name__ == "__main__":
    main()
