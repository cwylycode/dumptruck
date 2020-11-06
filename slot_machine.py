import os,random,time,colorama

class SlotMachine:
    """Here is a slot machine class that'll work in your script - you'll have to set it up yourself, though. There's also a built-in slots minigame in this module that can be executed and played in the terminal, in case you missed it.\n
    You can have as many slot machines as you can justify. To use, start by assigning this class to a variable. From there, set up your items and symbols (numbers, characters, etc) for the machine to make use of, and then set up some slot reels and give them items. You'll figure out the rest - luck is on your side, I'm sure."""

    def __init__(self,max_credits):
        self.credits_inserted = 0
        self.credits_max = max_credits
        self._items = {}
        self._reels = [_Reel(self)]
    def __repr__(self):
        return f"SlotMachine: credits_inserted={self.credits_inserted}, credits_max={self.credits_max}, reels={len(self._reels)}, items={list(self._items.keys())}"
    @property
    def items(self):
        """A dictionary of items attached to this machine. Used by the reels and the slots for them."""
        return self._items
    @property
    def reels(self):
        """List of reels on this machine."""
        return self._reels

    def item_add(self,name:str,worth:list,symbol:str,color="",is_wild:bool=False):
        """Add a slot item to the items dict which can then be added to the reels.\n
        Give it a name, a worth based on each max_credits number (e.g. max_credits = 3, worth: [int,int,int]), a text character for the reel, and an optional color. If the item name already exists, it's contents will be overwritten. The slot item will be returned."""
        si = _SlotItem(name,worth,symbol,color,is_wild)
        self._items.update({name:si})
        return si

    def item_delete(self,name:str):
        """Remove a slot item from the items dict and subsequently from all of the reels and return it."""
        try: it = self._items.pop(name)
        except: return
        for i in range(0,len(self._reels)):
            self._reels[i]._slots = [x for x in self._reels[i]._slots if x.name not in name]
        return it

    def reel_setup(self,reel:int,item_name_list:list):
        """Set up a reel (by index) with a list of slot items by name, in the order they are declared and return it. The item will be added to the reel if the name is found in the items dict, else will be ignored. If the reel doesn't exist, it will be created in place and added to the slot machine. If it does exist, it'll be overwritten with the new list."""
        if reel < 0: raise Exception("Reel index must be zero or greater.")
        try: self._reels[reel]._slots.clear()
        except:
            self._reels.extend([_Reel(self) for _ in range(len(self._reels),reel+1)])
            self._reels[reel]._slots.clear()
        for name in item_name_list:
            if name in self._items.keys():
                self._reels[reel]._slots.append(self._items[name])
        return self._reels[reel]

    def reel_delete(self,reel:int):
        """Remove a reel from the machine and return it."""
        try: x = self._reels.pop(reel)
        except: return
        return x

    def reel_reset(self,reel:int):
        """Reset a reel to its initial, unspun state and return it."""
        self.reel_spin(reel,-self._reels[reel]._relative_pos)

    def reel_spin(self,reel:int,spin_amount:int):
        """Spin a provided reel a certain amount by shifting it's slots. Can be forward or reverse (<= -1 | >= 1)."""
        si = self._reels[reel]._slots
        if spin_amount >= 1:
            for i in range(spin_amount):
                si.insert(0,si.pop())
                rel = self._reels[reel]._relative_pos
                self._reels[reel]._relative_pos = (rel+1) % len(si)
        elif spin_amount <= -1:
            for i in range(spin_amount,0):
                si.insert(len(si),si.pop(0))
                rel = self._reels[reel]._relative_pos
                self._reels[reel]._relative_pos = (rel-1) % len(si)
        else: return
    
    def reel_target(self,reel:int,target:str):
        """Spin the provided reel so that it will line up with the first instance of the slot target on it. Target is the name of a slot item on the reel and if valid, will spin the reel until it's first index lines up with the first instance of the slot item."""
        si = self._reels[reel]._slots
        if target in [x.name for x in si]:
            self.reel_reset(reel)
            while self._reels[reel]._slots[0]._name != target:
                self.reel_spin(reel,1)
        else: return

    def results(self,min_seq:int,paylines:list):
        """Read the current slots (by payline) - across all reels to find winning symbols on straight lines. Returns a list containing one of each of the winning slot item objects on each row - Wildcards aren't included unless they make up the entire sequence.\n
        Min seq is the number of items across reels on the row (sequentially) that are needed to trigger a win for those items. Depending on the minimum sequence and the number of reels on the machine, it's possible to get more than one winning sequence on a play.\n
        Paylines determine which slot rows on the machine are capable of having winning patterns and being read at all.\n
        E.g. paylines = [0, 2, 4] means, starting with the first row, only check the first, third and fifth rows for wins.\n
        Note: A winning sequence is only valid if it begins at the first slot for each row."""
        winning_items = []
        for row in paylines:
            temp = []
            hold = None
            for reel in self._reels:
                s = reel._slots[row]
                if not temp:
                    if not s.is_wild: hold = s
                    temp.append(s)
                    continue
                elif (s == hold or s.is_wild) or (not hold):
                    if not hold and not s.is_wild: hold = s
                    temp.append(s)
                else: break
            if len(temp) >= min_seq:
                if all([(i.is_wild) for i in temp]):
                    winning_items.extend(set(filter(lambda x: x.is_wild,temp)))
                else:
                    winning_items.extend(set(filter(lambda x: not x.is_wild,temp)))
        return list(winning_items)

class _SlotItem:
    def __init__(self,name:str="",worth:list=[],symbol:str="",color="",is_wild:bool=False):
        self._name = name
        self._worth = worth
        self._symbol = symbol
        self._color = color
        self._is_wild = is_wild
    def __repr__(self): return f"SlotItem: {self.name}"
    @property
    def name(self): return self._name
    @property
    def worth(self): return self._worth
    @property
    def symbol(self): return self._symbol
    @property
    def color(self): return self._color
    @property
    def is_wild(self): return self._is_wild

class _Reel:
    def __init__(self,machine:SlotMachine):
        self._machine = machine
        self._relative_pos = 0
        self._slots = [_SlotItem()]
    def __repr__(self): return f"Reel: relative_pos={self._relative_pos}"
    @property
    def slots(self): return self._slots

    def slot_add(self,item_name:str):
        """Add a slot item by name to the end of the reel. If the name doesn't already exist in the items dict, this won't do anything."""
        if item_name in self._machine._items.keys(): self._slots.append(self._machine._items[item_name])
    
    def slot_delete(self,pos:int):
        """Delete a slot item in the reel by index position and return it. Won't do anything if index is out of range."""
        return self._slots.pop(pos)
    
    def slot_remove(self, item_name:str):
        """Remove all instances of a specific slot item in the reel without changing reel length. If the name doesn't already exist in the items dict, this won't do anything."""
        for i in range(len(self._slots)):
            if self._slots[i].name == item_name:
                self._slots[i] = []

#Slot machine mini-game
def play_slot_machine_game():
    """Mini-game that plays in the terminal using a slot machine object. Enjoy!"""

    #Begin
    use_termios = False
    try: import msvcrt
    except ImportError:
        import termios
        use_termios = True
    colorama.init(autoreset=True)
    IND1,IND2 = " "*2," "*5
    RUNTIME = True

    class Game:
        slots = []
        game_over = False
        spinning = False
        input_active = True
        current_prompt = 0
        current_bet = 0
        current_freespins = 0
        current_result = ""
        money_player = 0
        money_house = 0
        debug = False

    class Animations:
        lsv = "|"
        rsv = "|"
        ldv = "$$$"
        rdv = "$$$"
        tv = [""]*9
        l_spin = ['|','\\','—','/']
        r_spin = ['|','/','—','\\']
        l_dollar = ['$$$','   ','  $',' $$']
        r_dollar = ['$$$','   ','$  ','$$ ']
        table = ["",colorama.Back.WHITE]
        
        @classmethod
        def animate(cls,machine:SlotMachine,anim_slots,anim_title,anim_table,anim_money,choices=[],result:_SlotItem=None):
            #Animate all the flashy bits and spin the reels as needed
            def interval(speed,cycle=[0],instant_start=True):
                t = (time.time() + 1 / (speed * len(cycle))) if not instant_start else time.time()
                while True:
                    if t < time.time():
                        t = time.time() + 1 / (speed * len(cycle))
                        yield True
                    else: yield False
            reel_speeds = (1.5,1.0,1.2)
            reel_duration = interval(random.uniform(1.2,2.0),instant_start=False)
            spinny = [interval(10,cls.l_spin),0]
            dollar = [interval(2,cls.l_dollar),0]
            table_blink = [interval(2,cls.table),0]
            table_cell = [i for i,j in enumerate(list(machine.items.keys())) if j == result.name][0] if result else 0
            payout = result.worth[Game.current_bet-1] if result else 0
            orig_pay = Game.money_player if result and result.name != "Free Spins" else Game.current_freespins
            money_factor = interval(payout if payout > 0 else 1)
            reel_stopped = [False,False,False]
            slot_cycles = [interval(reel_speeds[x],machine.reels[x].slots) for x in range(len(machine.reels))]
            cr = 0
            while True:
                draw_game()
                #Reels
                if anim_slots:
                    Game.spinning = True
                    spin_dir = 1
                    if next(reel_duration):
                        machine.reel_target(cr,choices[cr])
                        machine.reel_spin(cr,2)
                        reel_stopped[cr] = True
                        cr += 1
                    for i in range(len(machine.reels)):
                        if next(slot_cycles[i]) and not reel_stopped[i]: machine.reel_spin(i,spin_dir)
                        spin_dir = -spin_dir
                    if all(reel_stopped):
                        Game.spinning = False
                        break
                #Title
                if anim_title:
                    if next(spinny[0]):
                        spinny[1] = (spinny[1]+1) % len(cls.l_spin)
                        cls.lsv = cls.l_spin[spinny[1]]
                        cls.rsv = cls.r_spin[spinny[1]]
                    if next(dollar[0]):
                        dollar[1] = (dollar[1]+1) % len(cls.l_dollar)
                        cls.ldv = cls.l_dollar[dollar[1]]
                        cls.rdv = cls.r_dollar[dollar[1]]
                #Table
                if anim_table:
                    if next(table_blink[0]):
                        table_blink[1] = (table_blink[1]+1) % len(cls.table)
                        cls.tv[table_cell] = cls.table[table_blink[1]]
                #Money
                if anim_money:
                    if next(money_factor):
                        if result.name == "Free Spins":
                            Game.current_freespins += 1
                            if Game.current_freespins >= orig_pay + payout:
                                Game.current_freespins = orig_pay + payout
                                break
                        else:
                            Game.money_house -= 1
                            Game.money_player += 1
                            if Game.money_house <= 0:
                                Game.money_house = 0
                                break
                            if Game.money_player >= orig_pay + payout:
                                Game.money_player = orig_pay + payout
                                break
            #Cleanup
            cls.lsv = cls.l_spin[0]
            cls.rsv = cls.r_spin[0]
            cls.ldv = cls.l_dollar[0]
            cls.rdv = cls.r_dollar[0]
            cls.tv[table_cell] = cls.table[0]
            draw_game()
    
    def flush_input():
        if use_termios:
            termios.tcflush(os.sys.stdin, termios.TCIOFLUSH)
        else:
            while msvcrt.kbhit():
                msvcrt.getch()

    def draw_game():
        #Clear screen of stuff
        if os.name == "nt": os.system("cls")
        else: os.system("clear")
        #Value assignment
        lsv = Animations.lsv
        rsv = Animations.rsv
        ldv = Animations.ldv
        rdv = Animations.rdv
        tv = Animations.tv
        r = lambda x,y: f"{sm.reels[x].slots[y].color}{sm.reels[x].slots[y].symbol}{colorama.Style.RESET_ALL}"
        #Draw slot machine and payout table
        print(f"{IND1+IND2*2}{lsv} Welcome to the {ldv}Lucky Terminal{rdv} slot machine! {rsv}\n")
        print(f"{IND1}-------------------{IND2*4}-----------------------------------")
        print(f"{IND1}|  {r(0,0)}  |  {r(1,0)}  |  {r(2,0)}  |{IND2*4}{tv[0]}{sm.items['Jackpot'].color}| $$$ | 300/600/1000 |    Jackpot |")
        print(f"{IND1}|  {r(0,1)}  |  {r(1,1)}  |  {r(2,1)}  |{IND2*4}{tv[1]}{sm.items['Lucky'].color}| 777 | 100/200/300  |      Lucky |")
        print(f"{IND1}|  {r(0,2)}  |  {r(1,2)}  |  {r(2,2)}  | <-- Payline{IND1*4}{tv[2]}{sm.items['Bell'].color}| &&& | 50/100/150   |       Bell |")
        print(f"{IND1}|  {r(0,3)}  |  {r(1,3)}  |  {r(2,3)}  |{IND2*4}{tv[3]}{sm.items['Cherry'].color}| %%% | 20/40/60     |     Cherry |")
        print(f"{IND1}|  {r(0,4)}  |  {r(1,4)}  |  {r(2,4)}  |{IND2*4}{tv[4]}{sm.items['Bar'].color}| ### | 10/20/30     |        Bar |")
        print(f"{IND1}-------------------{IND2*4}{tv[5]}{sm.items['Jewel'].color}| +++ | 5/10/15      |      Jewel |")
        print(f"{IND1}{IND2*7+IND1*2}{tv[6]}{sm.items['Coin'].color}| @@@ | 2/4/6        |       Coin |")
        print(f"{IND1}{IND2*7+IND1*2}{tv[7]}{sm.items['Wild'].color}| ??? | 1/2/3        |       Wild |")
        print(f"{IND1}{IND2*7+IND1*2}{tv[8]}{sm.items['Free Spins'].color}| !!! | (1)/(2)/(3)  | Free Spins |")
        print(f"{IND1}-------------------{IND2*4}-----------------------------------")
        #Draw money area
        print(f"{IND1}The House: {Game.money_house}")
        print(f"{IND1}You: {Game.money_player}")
        print(f"\n{IND1}Credits: {sm.credits_inserted}")
        print(f"{IND1}Free Spins: {Game.current_freespins}")
        print(f"{IND1}-------------------\n")
        #Spinning and result state
        if Game.spinning: print(f"{IND1}Spinning...\n")
        elif Game.current_result: print(f"{IND1}{Game.current_result}\n")
        #60 fps max refresh rate - prevents console flickering
        time.sleep(1/60)

    #Runtime
    while RUNTIME:
        #Initialize
        Game.money_house = 800
        Game.money_player = 200
        sm = SlotMachine(3)
        Game.slots = []*10
        sm.item_add("Jackpot",[300,600,1000],"$",colorama.Fore.LIGHTWHITE_EX)
        sm.item_add("Lucky",[100,200,300],"7",colorama.Fore.LIGHTCYAN_EX)
        sm.item_add("Bell",[50,100,150],"&",colorama.Fore.LIGHTYELLOW_EX)
        sm.item_add("Cherry",[20,40,60],"%",colorama.Fore.LIGHTRED_EX)
        sm.item_add("Bar",[10,20,30],"#",colorama.Fore.LIGHTWHITE_EX)
        sm.item_add("Jewel",[5,10,15],"+",colorama.Fore.LIGHTBLUE_EX)
        sm.item_add("Coin",[2,4,6],"@",colorama.Fore.LIGHTMAGENTA_EX)
        sm.item_add("Wild",[1,2,3],"?",colorama.Fore.LIGHTGREEN_EX,is_wild=True)
        sm.item_add("Free Spins",[1,2,3],"!",colorama.Fore.LIGHTWHITE_EX)
        sm.item_add(" ",[0,0,0],"-")
        sm.reel_setup(0,["Jackpot"," ","Cherry"," ","Coin"," ","Free Spins"," ","Lucky"," ","Bar"," ","Wild"," ","Bell"," ","Jewel"," "])
        sm.reel_setup(1,["Lucky"," ","Bar"," ","Wild"," ","Jewel"," ","Bell"," ","Coin"," ","Free Spins"," ","Cherry"," ","Jackpot"," "])
        sm.reel_setup(2,["Bell"," ","Jewel"," ","Free Spins"," ","Lucky"," ","Bar"," ","Coin"," ","Jackpot"," ","Wild"," ","Cherry"," "])
        slot_probability = {
            "Jackpot":random.randint(1,10),
            "Lucky":random.randint(2,10),
            "Bell":random.randint(2,10),
            "Cherry":random.randint(3,10),
            "Bar":random.randint(4,10),
            "Jewel":random.randint(4,10),
            "Coin":random.randint(4,10),
            "Wild":random.randint(5,10),
            "Free Spins":random.randint(6,10),
            " ":random.randint(1,5)
        }

        #Game Loop
        while True:
            #Initial draw
            draw_game()

            #Player input
            if Game.input_active:
                prompts = [
                    f"{IND1}Place a bet and press 'Enter' to spin the slots!\n{IND1}(You can also put in 'Q' at any time to quit)\n{IND1}>",
                    f"{IND1}Current bet: {Game.current_bet}\n{IND1}Press 'Enter' to spin again or place a different bet below\n{IND1}>",
                    f"{IND1}You should know, the house always wins...\n{IND1}Game Over - You lose...Play again?(Y/N)\n{IND1}>",
                    f"{IND1}Wow! You beat the house! Now, the house will beat you...in a dark alley.\n{IND1}Game Over - You win...Play again?(Y/N)\n{IND1}>"
                ]
                err_msgs = [
                    f"{IND1}",
                    f"{IND1}Invalid input. Try again.",
                    f"{IND1}Bet must be a number between 1 and {sm.credits_max}. Try again.",
                    f"{IND1}Not enough money left!"
                ]
                err_msg = 0
                while True:
                    flush_input()
                    draw_game()
                    if err_msg != 0:
                        print(err_msgs[err_msg])
                        err_msg = 0
                        time.sleep(2)
                        continue
                    pi = input(prompts[Game.current_prompt])
                    if Game.game_over:
                        if pi in ["y","Y","yes","YES","Yes"]:
                            break
                        elif pi in ["n","N","no","NO","No"]:
                            RUNTIME = False
                            break
                        else:
                            err_msg = 1
                            continue
                    else:
                        if pi.isdigit():
                            if int(pi) > sm.credits_max or int(pi) < 1:
                                err_msg = 2
                                continue
                            elif int(pi) > Game.money_player:
                                err_msg = 3
                                continue
                            else:
                                sm.credits_inserted = Game.current_bet = int(pi)
                                Game.current_prompt = 1
                                break
                        elif pi == "" and Game.current_prompt == 1:
                            if Game.money_player < Game.current_bet:
                                err_msg = 3
                                continue
                            sm.credits_inserted = Game.current_bet
                            break
                        elif pi.lower() == "q":
                            RUNTIME = False
                            break
                        else:
                            err_msg = 1
                            continue

            #Stop game if we aren't playing anymore
            if not RUNTIME or Game.game_over: break

            #Handle money and freebies
            if Game.current_freespins > 0:
                Game.current_freespins -= 1
            else:
                Game.money_house += Game.current_bet
                Game.money_player -= Game.current_bet

            #Animate reels and title flashiness
            if Game.debug: slot_choices = ["Wild","Lucky","Wild"]
            else: slot_choices = random.choices([k for k in slot_probability.keys()],[v for v in slot_probability.values()],k=3)
            Animations.animate(sm,True,True,False,False,slot_choices)

            #Display results, payout and animate
            draw_game()
            spin_results = {
                "-":f"Too bad.",
                "!":f"You got {Game.current_bet} Free Spin{'s' if Game.current_bet>1 else ''}!",
                "?":f"Whoa, that's wild...",
                "@":f"Ka-ching!",
                "+":f"Ooh...Shiny!",
                "#":f"Way to raise the bar!",
                "%":f"Eat, drink and be Cherry!",
                "&":f"You are for whom the bell tolls!",
                "7":f"Killer Seven Wooooo!!!",
                "$":f"HOLY CRAP! JACKPOT!!!"
            }
            result = sm.results(3,[2])
            if result:
                Game.current_result = spin_results[result[0].symbol]
                Animations.animate(sm,False,True,True,True,result=result[0])
            else:
                Game.current_result = spin_results["-"]
                draw_game()

            #Check current money
            if Game.money_player <= 0:
                Game.game_over = True
                Game.current_prompt = 2
            elif Game.money_house <= 0:
                Game.game_over = True
                Game.current_prompt = 3

            #Cleanup
            sm.credits_inserted = 0
            Game.current_result = ""
            time.sleep(1)
            flush_input()
    #End

if __name__ == "__main__":
    play_slot_machine_game()