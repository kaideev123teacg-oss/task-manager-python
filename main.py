tasks=[]

while True:
  print("\n1: タスク追加")
  print("2:タスク一覧表示")
  print("3:終了")

choice = input("選択してください:")

if choice == "1":
  task = input("タスク内容：")
  tasks.append(task)
  print("追加しました。")

elif choice == "2":
    print("\n--- タスク一覧 ---")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

elif choice == "3":
    print("終了します。")
    break

else:
    print("無効な入力です。")
