"""
This program implements a fitness tracker system that collects, stores, and displays user activity data, focusing on the Observer pattern and adhering to SOLID principles.

SOLID Principles:

1. Single Responsibility Principle (SRP):
   - Each class has a single responsibility:
     - User: Represents a user profile.
     - Activity: Represents an activity type.
     - ActivityMonitor: Manages activity data collection and notification.
     - DataStorage: Handles data storage.
     - Display: Manages data display.

2. Open/Closed Principle (OCP):
   - The system allows for easy addition of new activity types without modifying existing classes. 
   - This is achieved through the Observer pattern, where new activity types can be added as subclasses of Activity without changing ActivityMonitor or Display.

3. Liskov Substitution Principle (LSP):
   - Subclasses of Activity adhere to the observer pattern's contract by providing an activity_type attribute, ensuring compatibility with ActivityMonitor's notification mechanism.

4. Interface Segregation Principle (ISP):
   - Separate interfaces (DataStorage and Display) are defined for data storage and display concerns, respectively.
   - Clients can use only the methods they need without depending on unnecessary functionality.

5. Dependency Inversion Principle (DIP):
   - Dependencies like DataStorage and Display are injected into the ActivityMonitor constructor.
   - This promotes loose coupling and makes it easier to test and maintain the code.
"""

from abc import ABC, abstractmethod


# Interface for data storage
class DataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass


# Interface for display
class Display(ABC):
    @abstractmethod
    def update(self, data):
        pass


# Subject class
class ActivityMonitor:
    def __init__(self, storage: DataStorage, display: Display):
        self.storage = storage
        self.display = display
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def collect_activity_data(self, user, activity_type, data):
        activity_data = {"user": user, "type": activity_type, "data": data}
        self.storage.save_data(activity_data)
        self.notify_observers(activity_data)


#Subject subclass user
class User:
    def __init__(self, name):
        self.name = name


#Subject subclass actuvuty
class Activity:
    def __init__(self, activity_type):
        self.activity_type = activity_type


#Observer
class ActivityDisplay(Display):
    def update(self, data):
        print("New activity data received:", data)


#Observer
class FileStorage(DataStorage):
    def save_data(self, data):
        with open("activity_data.txt", "a") as file:
            file.write(str(data) + "\n")


if __name__ == "__main__":
    #Dummy Data
    user = User("John")
    running_activity = Activity("Running")
    
    #Dependencies
    file_storage = FileStorage()
    display = ActivityDisplay()
    activity_monitor = ActivityMonitor(file_storage, display)

    # Adding observer
    activity_monitor.add_observer(display)

    #Dummy Data
    activity_monitor.collect_activity_data(user, running_activity.activity_type, {"steps": 5000, "distance": 4.5, "calories": 300})
