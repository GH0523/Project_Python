class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 50만원")

if __name__ == "__main__":
    print("Thailand 모듈 직접 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 모듈 외부 실행")