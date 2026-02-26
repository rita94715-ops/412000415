import random
import time

# 定義獎勵池與機率 (機率加總應為 1.0)
CHANCE_CONFIG = {
    "UR": 0.01,   # 1%
    "SSR": 0.04,  # 4%
    "SR": 0.15,   # 15%
    "R": 0.30,    # 30%
    "N": 0.50     # 50%
}

def pull_gacha(times=1):
    results = []
    for _ in range(times):
        # 隨機生成 0.0 到 1.0 之間的浮點數
        seed = random.random()
        current_weight = 0
        
        for rarity, chance in CHANCE_CONFIG.items():
            current_weight += chance
            if seed <= current_weight:
                results.append(rarity)
                break
    return results

def main():
    print("================================")
    print("   歡迎使用系統抽卡模擬器 v2.0")
    print("================================")

    while True:
        cmd = input("\n請選擇操作 [1]單抽 [10]十連抽 [q]退出: ").strip().lower()

        if cmd == 'q':
            print("感謝使用，系統關閉中...")
            break
        
        num = 10 if cmd == '10' else (1 if cmd == '1' else 0)
        
        if num == 0:
            print("無效輸入，請輸入 1, 10 或 q。")
            continue

        print(f"\n>> 正在進行 {num} 次抽取...")
        time.sleep(0.5)
        
        draws = pull_gacha(num)
        
        for i, res in enumerate(draws, 1):
            # 加上顏色，讓 VS Code 終端機看起來專業一點
            color = ""
            if res == "UR": color = "\033[91m"  # 紅色
            elif res == "SSR": color = "\033[93m" # 黃色
            elif res == "SR": color = "\033[95m"  # 紫色
            else: color = "\033[0m"              # 預設
            
            print(f"第 {i:02d} 抽：{color}[{res}]\033[0m")
        
        print("\n抽取完成！")

if __name__ == "__main__":
    main()