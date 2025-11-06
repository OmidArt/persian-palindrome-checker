def is_persian_palindrome():
    num = input("عدد رو وارد کن (مثل ۱۲۱): ")
    # تبدیل اعداد فارسی به انگلیسی
    persian_to_english = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
    num_en = num.translate(persian_to_english)
    
    if not num_en.isdigit():
        return "عدد معتبر نیست!"
    
    x = int(num_en)
    if x < 0:
        return "عدد منفی پالین‌دروم نیست!"
    
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    return "پالین‌درومه!" if original == reversed_num else "پالین‌دروم نیست!"

# اجرا
print(is_persian_palindrome())