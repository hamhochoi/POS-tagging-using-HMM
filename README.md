# POS-tagging-using-HMM

## Tập dữ liệu gồm khoảng 50000 từ tiếng Anh trong tập Brown Corpus
- Các câu đều được gán nhãn
- Mỗi câu được viết trên 1 dòng (tính theo ký tự '\n')
- Mỗi từ trong một câu được gán nhãn, các từ phân cách nhau bởi dấu cách; từ ghép được viết theo cú pháp "từ-ghép"; từ và nhãn tương ứng của nó được phân cách nhau bởi dấu '/'.
- Thuật toán sử dụng là triagram HMM.
- Mỗi câu sẽ được chèn thêm 2 fake word "XXXXXX" vào trước và 2 fake word  "XXXXXX" vào sau.

## File read_next_token dùng để đọc một từ trong một dòng 
-  Trong file này chỉ có một hàm: read_next_token(f_read, current_line, current_word)
  - f_read tham số read file truyền vào. vd: f = open(path, 'r'); f_read = f.read()
  - current_line : dòng hiện tại đang xét (vì một file có nhiều dòng)
  - current_word : vị trí hiện tại muốn đọc từ.
  - Mỗi câu được thêm 2 fake word ở trước và 2 fake word ở sau nên current có thể từ -2 --> len(line) + 2.
  
## File find_word_in_dictionary dùng để tìm nhãn một từ trong từ điển
- Thuật toán sử dụng: Duyệt hết từ đầu đến cuối từ điển
- Nếu thuật toán quá chậm, có thể thay thế sử dụng các thuật toán khác để duyệt.

## Lưu ý: Các đường dẫn trong các file là đường dẫn tuyệt đối, phải điều chỉnh khi download về và chạy chương trình.
