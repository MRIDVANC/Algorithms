def print_board(board):
    for row in board:
        print(" | ".join(row))  # Tahtanın her satırını | karakteri ile birleştirip yazdırır.
        print("-" * 9)  # Her satırın altına 9 tane - karakteri ekleyerek tahtanın satırlarını ayırır.


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):  # Her satırdaki hücreler oyuncunun işaretiyle doldu mu kontrol eder.
            return True

    for col in range(3):
        if all([board[row][col] == player for row in
                range(3)]):  # Her sütundaki hücreler oyuncunun işaretiyle doldu mu kontrol eder.
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        # Köşegenlerdeki hücreler oyuncunun işaretiyle doldu mu kontrol eder.
        return True

    return False


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])  # Tahtanın dolu olup olmadığını kontrol eder.


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3'lük boş bir tahta oluşturur.
    current_player = "X"  # Oyunun başlangıcında X oyuncusu başlar.

    while True:
        print_board(board)  # Tahtayı görüntüler.
        print(f"Player {current_player}'s turn. Enter row and column (e.g., '1 2'): ", end="")

        try:
            row, col = map(int, input().split())
            if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
                # Kullanıcının girdiği hamleyi doğrulayarak geçerli bir hamle mi kontrol eder.
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")  # Sayı dışı bir giriş yapıldığında hata mesajı gösterir.
            continue

        board[row - 1][col - 1] = current_player  # Geçerli hamleyi tahtaya kaydeder.

        if check_winner(board, current_player):  # Kazanan kontrolü yapar.
            print_board(board)  # Son tahtayı görüntüler.
            print(f"Player {current_player} wins!")  # Kazanan oyuncuyu ilan eder.
            break

        if is_board_full(board):  # Tahtanın dolu olup olmadığını kontrol eder.
            print_board(board)  # Son tahtayı görüntüler.
            print("It's a tie!")  # Berabere ilan eder.
            break

        current_player = "X" if current_player == "O" else "O"  # Sıradaki oyuncuyu değiştirir.

    play_again = input("Do you want to play again? (yes/no): ")  # Oyunu tekrar oynamak isteyip istemediğini sorar.
    if play_again.lower() == "yes":
        main()  # Oyunu tekrar başlatır.
    else:
        print("Thanks for playing!")  # Oyun sona erdiğinde teşekkür mesajı gösterir.


if __name__ == "__main__":
    main()
