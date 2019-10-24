import datetime
import random


class Customer:
    def __init__(self, time_of_arrival, id):
        self.time_of_arrival = time_of_arrival
        self.time_of_departure = None
        self.customer_id = id

    def get_customer_id(self):
        return "Customer-{}".format(self.customer_id)

    def __str__(self):
        return "{} Customer-{}".format(self.time_of_arrival.strftime('%H:%M'), self.customer_id)


class HairStylist:
    def __init__(self, name):
        self.name = name
        self.customer = None
        self.last_customer = None
        self.clocked_in = False


class Event:
    def __init__(self, owner, time, action, type):
        self.type = type
        self.time = time
        self.owner = owner
        self.action = action

    def __eq__(self, other):
        return self.type == other.type \
               and self.time == other.type \
               and self.action == self.action \
               and self.owner == other.owner

    def __str_(self):
        return "{} {} {} {}".format(self.time.strftime('%H:%M'), self.owner, self.action, self.type)


class SalonSimulation:

    def __init__(self, start, end, capacity):
        self.salonQueue = []
        self.capacity = capacity
        self.first_shift_stylist = [HairStylist("Anne"), HairStylist("Ben"), HairStylist("Carol"), HairStylist("Derek")]
        self.second_shift_stylist = [HairStylist("Erin"), HairStylist("Frank"), HairStylist("Gloria"),
                                     HairStylist("Heber")]

        today = datetime.datetime.today()
        self.current_time = start
        self.end_time_simulation = end
        self.change_shift_time = today.replace(hour=13, minute=00)
        self.open_time = today.replace(hour=9, minute=00)
        self.close_time = today.replace(hour=17, minute=00)
        self.next_customer = 1

        self.haircut_time_range = (20, 40)

        self.isOpen = False
        self.isFirst = self.isFirstShift(self.current_time)

        self.events = []

    def setBusinessHours(self, open, close):
        self.open_time = open
        self.close_time = close

    def setShiftChangeTime(self, time):
        self.change_shift_time = time

    def haircutTime(self):
        return random.randint(self.haircut_time_range[0], self.haircut_time_range[1])

    def addMinutes(self, c_time, added_time):
        return (c_time + datetime.timedelta(minutes=added_time))  # .strftime('%H:%M')#.time()

    def takeNextCustomer(self):

        if len(self.salonQueue) == 0:
            return

        hair_stylist_available = self.availableHairStylist()

        if hair_stylist_available:
            customer = self.salonQueue[0]
            customer.time_of_departure = self.addMinutes(customer.time_of_arrival, self.haircutTime())
            hair_stylist_available.customer = customer
            event = Event(hair_stylist_available.name, self.current_time, "started cutting",
                          customer.get_customer_id() + "'s hair")
            self.events.append(event)
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

    def freeUpHairStylistsHelper(self, stylistList):
        for s in stylistList:
            if s.customer and s.customer.time_of_departure.strftime('%H:%M') <= self.current_time.strftime('%H:%M'):
                event1 = Event(s.name, s.customer.time_of_departure, "ended cutting",
                               s.customer.get_customer_id() + "'s hair")
                event2 = Event(s.customer.get_customer_id(), s.customer.time_of_departure, "left", "satisfied")
                self.events.append(event1)
                self.events.append(event2)
                s.last_customer = s.customer
                s.customer = None

                if self.isFirstShiftStylist(s):
                    self.endShift([s])

    def freeUpHairStylists(self):
        self.freeUpHairStylistsHelper(self.first_shift_stylist)
        self.freeUpHairStylistsHelper(self.second_shift_stylist)

    def inBusinessHours(self):
        return self.open_time.strftime('%H:%M') <= self.current_time.strftime('%H:%M') < self.close_time.strftime(
            '%H:%M')

    def startShift(self, stylist, shiftStart):
        for s in stylist:
            s.clocked_in = True
            event = Event(s.name, shiftStart, "started", "shift")
            self.events.append(event)

    def endShift(self, stylist):
        for s in stylist:
            if s.clocked_in and not s.customer:
                tod = self.current_time
                if s.last_customer:
                    tod = s.last_customer.time_of_departure

                s.clocked_in = False
                event = Event(s.name, tod, "ended", "shift")
                self.events.append(event)

    def kickEveryOneOut(self):
        self.endShift(self.second_shift_stylist)

        for c in self.salonQueue:
            self.events.append(Event(c.get_customer_id(), self.current_time, "left", "furious"))

    def toggleOpenStatus(self):
        if (not self.isOpen) and self.inBusinessHours():
            self.isOpen = True
            self.events.append(Event("Hair salon", self.open_time, "opened", ""))
            self.startShift(self.first_shift_stylist, self.open_time)

        elif self.isOpen and not self.inBusinessHours():
            self.isOpen = False
            self.events.append(Event("Hair salon", self.close_time, "closed", ""))
            self.endShift(self.second_shift_stylist)

    def toggleShift(self):
        if self.isFirst and not self.isFirstShift(self.current_time):
            self.isFirst = False
            self.endShift(self.first_shift_stylist)
            self.startShift(self.second_shift_stylist, self.change_shift_time)

        elif not self.isFirst and self.isFirstShift(self.current_time):
            self.isFirst = True

    def isHairStylistAvailable(self, stylistList):
        for s in stylistList:
            if not s.customer:
                return s
        return None

    def availableHairStylist(self):
        if self.open_time.strftime('%H:%M') <= self.current_time.strftime('%H:%M') < self.change_shift_time.strftime(
                '%H:%M'):
            return self.isHairStylistAvailable(self.first_shift_stylist)

        elif self.close_time.strftime('%H:%M') > self.current_time.strftime('%H:%M') >= self.change_shift_time.strftime(
                '%H:%M'):
            return self.isHairStylistAvailable(self.second_shift_stylist)

    def areStylistsStillBusy(self, stylists):
        for s in stylists:
            if s.customer:
                return True
        return False

    def isFirstShiftStylist(self, stylist):
        return stylist in self.first_shift_stylist

    def isFirstShift(self, current_time):
        if self.open_time.strftime('%H:%M') <= current_time.strftime('%H:%M') < self.change_shift_time.strftime(
                '%H:%M'):
            return True
        else:
            return False

    def getEvents(self):
        sorted_events = sorted(self.events, key=lambda ev: ev.time)

        s = ""
        for e in sorted_events:
            s += " ".join([e.time.strftime('%H:%M'), e.owner, e.action, e.type, "\n"])
        return s

    def next(self):
        self.next_customer += 1
        self.current_time = self.addMinutes(self.current_time, 10)

    def runSimulation(self):

        while self.current_time <= self.end_time_simulation:

            customer = Customer(self.current_time, self.next_customer)

            if self.current_time.strftime('%H:%M') < self.close_time.strftime('%H:%M'):

                self.toggleOpenStatus()

                self.events.append(Event(customer.get_customer_id(), self.current_time, "entered", ""))

                if len(self.salonQueue) > self.capacity:
                    e = Event(customer.get_customer_id(), self.current_time, "left", "impatiently")
                    self.events.append(e)
                    continue

                self.salonQueue.append(customer)
                self.removeLongWaitingCustomers()
                self.freeUpHairStylists()
                self.toggleShift()
                self.takeNextCustomer()

                self.next()
            else:
                self.toggleOpenStatus()

                if not self.isOpen:
                    self.kickEveryOneOut()
                    self.toggleOpenStatus()

                self.events.append(Event(customer.get_customer_id(), self.current_time, "left", "cursing themselves"))

                self.next()

today = datetime.datetime.today()
open_time = today.replace(hour=9, minute=00)
shift_change_time = today.replace(hour=9, minute=30)
end_time = today.replace(hour=10, minute=10)

sim = SalonSimulation(start=open_time, end=end_time, capacity=15)
sim.setBusinessHours(open_time, today.replace(hour=10, minute=0))
sim.setShiftChangeTime(shift_change_time)
sim.runSimulation()
print(sim.getEvents())


########### Tests ##################
def isFirstShift():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=10, minute=00)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
    sim.change_shift_time = today.replace(hour=9, minute=30)

    assert sim.isFirstShift(open_time)
    assert not sim.isFirstShift(today.replace(hour=9, minute=31))


def availableHairStylist():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=10, minute=00)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
    sim.first_shift_stylist = [HairStylist("Anne")]

    assert sim.availableHairStylist().name == "Anne"

    sim.first_shift_stylist[0].customer = Customer(open_time, 1)

    assert not sim.availableHairStylist()


def freeUpHairStylist():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=17, minute=00)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
    sim.first_shift_stylist = [HairStylist("Anne")]

    customer = Customer(today.replace(hour=13, minute=00), 1)
    customer.time_of_departure = today.replace(hour=13, minute=10)

    sim.first_shift_stylist[0].customer = customer

    sim.current_time = today.replace(hour=13, minute=30)  # After shift change

    sim.freeUpHairStylists()

    assert sim.events[0].type == "Customer-1\'s hair"
    assert sim.events[0].owner == "Anne"
    assert sim.events[0].action == "ended cutting"

    assert sim.events[1].type == "satisfied"
    assert sim.events[1].owner == "Customer-1"
    assert sim.events[1].action == "left"


def toggleOpenStatus():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=17, minute=00)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
    sim.toggleOpenStatus()

    assert len(sim.events) == 5

    sim.current_time = today.replace(hour=17, minute=1)
    sim.toggleOpenStatus()

    assert len(sim.events) == 6


def toggleShift():
    today = datetime.datetime.today()
    open_time = today.replace(hour=9, minute=00)
    close_time = today.replace(hour=17, minute=00)

    sim = SalonSimulation(start=open_time, end=close_time, capacity=15)
    sim.current_time = today.replace(hour=13, minute=1)
    sim.toggleShift()

    assert len(sim.events) == 4

isFirstShift()
availableHairStylist()
freeUpHairStylist()
toggleOpenStatus()
toggleShift()
