#!/usr/bin/python

def main():

    print("\n my country list: \n")
    my_list = [
        ("mexico", "costa rica"),
        ("mexico","peru"),
        ("costa_rica","colombia"),
        ("costa_rica","venezuela"),
        ("colombia","chile"),
        ("venezuela","chile"),
        ("venezuela","peru"),
        ("peru","chile"),
    ]
    print(my_list)

    print("\n my country dictionary: \n")
    my_dict = {
        "mexico": ["costa_rica","peru"],
        "costa_rica": ["colombia","venezuela"],
        "venezuela": ["peru","chile"],
        "peru": ["chile"],
        "colombia": ["chile"],
    }
    print(my_dict)

if __name__ == '__main__':
    main()