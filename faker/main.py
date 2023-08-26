from faker import Faker
from faker.providers import address


def example_one():
    fake = Faker(["fa", "en_US"])
    print("Name:", fake.name())
    print("Address:", fake.address())
    print("Text:", fake.text())

    fake_names = [fake.name() for _ in range(5)]
    print("Names:", fake_names)


def example_two():
    fake = Faker()
    fake.add_provider(address)

    print("Country:", fake.country())
    print("Country Code:", fake.country_code())
    print("City", fake.city())

    fake_postcodes = [fake.postcode() for _ in range(5)]
    print("Postcodes:", fake_postcodes)


if __name__ == "__main__":
    example_one()
    example_two()
