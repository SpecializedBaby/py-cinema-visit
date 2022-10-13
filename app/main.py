from cinema import bar, hall
from people import cinema_staff, customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for cs in customers:
        customers_list.append(customer.Customer(cs["name"], cs["food"]))
    for cs in customers_list:
        bar.CinemaBar.sell_product(cs, cs.food)

    cleaner = cinema_staff.Cleaner(cleaner)

    hall.CinemaHall(hall_number).movie_session(movie, customers_list, cleaner)
