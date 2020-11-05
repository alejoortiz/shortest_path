#!/usr/bin/python

def main():

    print("\nmy country list: \n")
    my_list = [
        ("mexico", "costa rica",1),
        ("mexico","peru",2),
        ("costa_rica","colombia",2),
        ("costa_rica","venezuela",1),
        ("colombia","chile",1),
        ("venezuela","chile",1),
        ("venezuela","peru",1),
        ("peru","chile",1),
    ]
    print(my_list)

    print("\nmy country dictionary: \n")
    nodes = {
        'mexico': ['costa_rica', 'peru'],
        'costa_rica': ['mexico', 'colombia', 'venezuela'],
        'peru': ['mexico', 'venezuela', 'chile'], 
        'colombia': ['costa_rica', 'chile'], 
        'venezuela': ['costa_rica', 'chile', 'peru'], 
        'chile': ['colombia', 'venezuela', 'peru']
        }
    print(nodes)

if __name__ == '__main__':
    main()