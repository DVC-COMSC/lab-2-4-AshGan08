def main():
    original_str = "Python Programming"
    sub1 = original_str[0:6]
    sub2 = original_str[7:18]+original_str[6]
    merge_str = sub2 + sub1
    return sub1, sub2, merge_str


if __name__ == '__main__':
    sub1, sub2, merge_str = main()
    print(sub2)
    print(sub1)
    print(merge_str)