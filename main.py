def main():
    original_str = "python programming  "
    sub1 = original_str[0:6]
    sub2 = original_str[7:19]
    merged_str = sub2 + sub1
    return sub1, sub2, merged_str


if __name__ == '__main__':
    sub1, sub2, merged_str = main()
    print(sub2)
    print(sub1)
    print(merged_str)