class VacuumCleaner:
    def __init__(self, location='A', status='Clean'):
        self.location = location  # Current location of the vacuum cleaner (either 'A' or 'B')
        self.status = status      # Status of the current location ('Clean' or 'Dirty')

    def print_status(self):
        print(f"Location: {self.location}, Status: {self.status}")

    def clean(self):
        print("Cleaning...")
        self.status = 'Clean'

    def move(self, new_location):
        print(f"Moving from {self.location} to {new_location}")
        self.location = new_location

def vacuum_cleaner_program(env):
    for _ in range(2):  # The vacuum cleaner moves between two locations
        env.print_status()

        if env.status == 'Dirty':
            env.clean()
        else:
            print("clean.")

        env.move('A' if env.location == 'B' else 'B')

if __name__ == "__main__":
    # Initialize the environment with a dirty location
    environment = VacuumCleaner(location='A', status='Dirty')

    print("Initial state of the environment:")
    environment.print_status()

    print("\nVacuum cleaner program:")
    vacuum_cleaner_program(environment)

    print("\nFinal state of the environment:")
    environment.print_status()
