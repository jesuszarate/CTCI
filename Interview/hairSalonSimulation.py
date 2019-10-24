import datetime
import random

class Customer:
    def __init__(self, time_of_arrival, id):
        self.time_of_arrival = time_of_arrival
        self.time_of_departure = None
        self.customer_id = id

    def get_customer_id(self):
        return "Cusotmer - {}".format(self.customer_id)

    def __str__(self):
        return "{} Customer-{}".format(self.time_of_arrival.strftime('%H:%M'), self.customer_id)

class HairStylist:
    def __init__(self, name):
        self.name = name
        self.customer = None

class Event:
    def __init__(self, owner, time, action, type):
        self.type = type
        self.time = time
        self.owner = owner
        self.action = action

    def __str_(self):
        return "{} {} {} {}".format(self.time.strftime('%H:%M'), self.owner, self.action, self.type)


class SalonSimulation:

    def __init__(self, start, end, capacity):
        self.salonQueue = []
        self.capacity = capacity
        self.first_shift_stylist = [HairStylist("Anne"), HairStylist("Ben"), HairStylist("Carol"), HairStylist("Derek")]
        self.second_shift_stylist = [HairStylist("Erin"), HairStylist("Frank"), HairStylist("Gloria"), HairStylist("Heber")]

        today = datetime.datetime.today()
        self.current_time = start
        self.end_time_simulation = end
        self.open_time = today.replace(hour=9, minute=00)
        self.change_shift_time = today.replace(hour=13, minute=00)
        self.close_time = today.replace(hour=17, minute=00)
        self.next_customer = 1

        self.haircut_time_range = (20, 40)

        self.events = []

    def haircutTime(self):
        return random.randint(self.haircut_time_range[0], self.haircut_time_range[1])

    def addMinutes(self, c_time, added_time):
        return (c_time + datetime.timedelta(minutes=added_time))#.strftime('%H:%M')#.time()

    def takeNextCustomer(self):

        if len(self.salonQueue) == 0:
            return

        hair_stylist_available = self.AvailableHairStylist()

        if hair_stylist_available:
            customer = self.salonQueue[0]
            customer.time_of_departure = self.addMinutes(customer.time_of_arrival, self.haircutTime())
            hair_stylist_available.customer = customer
            del self.salonQueue[0]


    def removeLongWaitingCustomers(self):
        '''
        Remove Customers that have been waiting too long
        '''
        while len(self.salonQueue) > 0:
            c = self.salonQueue[0]
            if self.current_time >= self.addMinutes(c.time_of_arrival, 30):
                event = Event(c.get_customer_id(), c.time_of_arrival, "left", "unfulfilled")
                self.events.append(event)
                del self.salonQueue[0]
            else:
                return

    def satisfiedCustomerEvent(self, stylistList):
        for s in stylistList:
            if s.customer and s.customer.time_of_departure.strftime('%H:%M') <= self.current_time.strftime('%H:%M'):
                event = Event(s.customer.get_customer_id(), s.customer.time_of_departure, "left", "satisfied")
                self.events.append(event)
                s.customer = None

    def freeUpHairStylists(self):
        if self.isFirstShift(self.current_time, self.open_time, self.change_shift_time):
            self.satisfiedCustomerEvent(self.first_shift_stylist)
        else:
            self.satisfiedCustomerEvent(self.second_shift_stylist)

    def runSimulation(self):

        while self.current_time < self.end_time_simulation:

            while self.current_time.strftime('%H:%M') < self.close_time.strftime('%H:%M'):
                self.current_time = self.addMinutes(self.current_time, 10) # A customer will come in every 10 minutes for first iteration

                self.salonQueue.append(Customer(self.current_time, self.next_customer))

                self.removeLongWaitingCustomers()
                self.freeUpHairStylists()
                self.takeNextCustomer()

                self.next_customer += 1

    def isHairStylistAvailable(self, stylistList):
        for s in stylistList:
            if not s.customer:
                return s
        return None

    def AvailableHairStylist(self):
        if self.open_time.strftime('%H:%M') <= self.current_time.strftime('%H:%M') < self.change_shift_time.strftime('%H:%M'):
            return self.isHairStylistAvailable(self.first_shift_stylist)
        
        elif self.close_time.strftime('%H:%M') > self.current_time.strftime('%H:%M') >= self.change_shift_time.strftime('%H:%M'):
            return self.isHairStylistAvailable(self.second_shift_stylist)

    def isFirstShift(self, current_time):
        if self.open_time.strftime('%H:%M') <= current_time.strftime('%H:%M') < self.change_shift_time.strftime('%H:%M'):
            return True
        else:
            return False


# today = datetime.datetime.today()
# open_time = today.replace(hour=9, minute=00)
# close_time = today.replace(hour=10, minute=00)
#
# sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
#
# sim.runSimulation()

########### Tests ##################
def isFirstShift():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=10, minute=00)
    change_shift_time = today.replace(hour=9, minute=30)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)

    assert sim.isFirstShift(open_time, open_time, change_shift_time)
    assert not sim.isFirstShift(today.replace(hour=9, minute=31), open_time, change_shift_time)

isFirstShift()
