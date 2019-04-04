from tkinter import *
import sys
import queue
import numpy as np
from Card_Game.Card_Game import card_game as c

class CardGame:
    def __init__(self,master):

        self.master = master
        self.p_red = 0.5
        self.p_black = 0.5
        self.black_card = 4
        self.red_card = 4

        self.total_payoff = 0
        frame = Frame(self.master)
        frame.pack()

        self.payoff_matrix = c.card_game(self.red_card,self.black_card)
        self.expected_value = self.payoff_matrix[self.red_card, self.black_card]


        #
        # self.ticker = ""
        # self.ticker_count = 0
        self.origx = 10   #this the original output label for the x_entry
        self.ticker_queue = queue.Queue()
        self.ticker_list = []  #this is just to store all the tickers currently available
        self.heading = Label(frame,text="Card Game -- Choose Wisely",\
                             font=("arial",25,"bold"),fg ='black').pack()

        self.expected_val_label = Label(master, text="Net expected payoff", \
                                      font=("arial", 10, "bold"), fg='black').place(x=200, y=100)
        self.expected_value_label = Label(master, bg='green', width=10, fg='black')
        self.expected_value_label.place(x=225, y=125)  # this for the current value of the ticker
        self.expected_value_label.config(text=str(int(self.expected_value*100)/100))  #Init a value for expected payoff


        #this is just a user input test, this will go in another function
        self.pick_card_button = Button(master,text = 'Pick a Card',bg= "green",command=self.update_card_count).place(x=10,y=100)
        self.dont_pick_card_button = Button(master,text = 'Quit Game', bg = "blue",command=self.quit).place(x=10,y=150)



        self.red_card_color_label = Label(master, bg='red', width=2, fg='black')
        self.red_card_color_label.place(x=10, y=200)  # this for the current value of the ticker

        self.red_card_label = Label(master, bg='white', width=5, fg='black')
        self.red_card_label.place(x=50, y=200)  # this for the current value of the ticker
        self.red_card_label.config(text=str(self.red_card))  # Init a value for expected payoff

        self.black_card_color_label = Label(master, bg='black', width=2, fg='black')
        self.black_card_color_label.place(x=10, y=225)  # this for the current value of the ticker

        self.black_card_label = Label(master, bg='white', width=5, fg='black')
        self.black_card_label.place(x=50, y=225)  # this for the current value of the ticker
        self.black_card_label.config(text=str(self.black_card))  # Init a value for number of black cards

        self.black_card_label.place(x=50, y=225)  # this for the current value of the ticker
        self.black_card_label.config(text=str(self.black_card))  # Init a value for number of black cards

        self.payoff_label = Label(master, text="Net current Payoff", \
                                        font=("arial", 10, "bold"), fg='black').place(x=205, y=150)
        self.payoff_val_label = Label(master, bg='green', width=10, fg='black')
        self.payoff_val_label.place(x=225, y=175)  # this for the current value of the ticker
        self.payoff_val_label.config(text=str(0))  # Init a value for expected payoff

        self.info_label = Label(master, bg='yellow', width=20, fg='black')
        self.info_label.place(x=100, y=300)  # this for the current value of the ticker
        self.info_label.config(text=str(0))  # Init a value for expected payoff

        # self.ironcondor_button = Button(master,text = 'Iron Condor (Delta Neutral)',command=self.iron_condor_init).place(x=10,y =200)
        # self.trading_statistics_button = Button(master,text = 'Get Trade Statistics',command=self.trade_stats_init).place(x=10,y =250)
        #
        #
        #

    def gen_probability(self):
        self.number = np.random.choice(np.arange(0,2), p=[self.p_red,self.p_black])
        #represent 1 as black card and 0 as red card, as the number of cards changes so does the probability of choosing each of the cards

    def update_card_count(self):

        self.gen_probability()
        if self.number:
            if self.black_card >= 1:
                self.total_payoff += 1
                self.black_card -= 1
            else:
                self.info_label.config(text=str("You are out of black cards"))
        else:
            if self.red_card >= 1:
                self.total_payoff -= 1

                self.red_card -= 1
            else:
                self.info_label.config(text="You are out of red cards")

        if self.black_card == 0 and self.red_card == 0:
            self.quit()
        self.expected_value_update()
        self.p_red = self.red_card/(self.red_card + self.black_card)
        self.p_black = 1 - self.p_red

        self.expected_value = self.payoff_matrix[self.red_card, self.black_card]
        self.expected_value_update()
        self.cards_left()
        self.update_payoff()
    def quit(self):


        self.expected_value_update()
        self.cards_left()
        self.update_payoff()
        self.info_label.config(text="Game Over")

        sys.exit()


    def expected_value_update(self):
        self.expected_value_label.config(text=str(int(self.expected_value*100)/100))

    def cards_left(self):
        self.red_card_label.config(text=str(self.red_card))
        self.black_card_label.config(text=str(self.black_card))
    def update_payoff(self):
        self.payoff_val_label.config(text=str(self.total_payoff))






        #
        #
        #
        # ##############################  label is on top of entry   #####################################################
        # self.ticker = StringVar()  #get the ticker you would like to get prce  alerts off....what the latest price is
        # self.position_open = StringVar()   # the opening price of the ticker..the price you bought it at
        #
        # self.ticker_label = Label(master, text="Ticker", \
        #                      font=("arial", 10, "bold"), fg='black').place(x=150, y=280)
        # self.price_label = Label(master, text="Position_Price", \
        #                      font=("arial", 10, "bold"), fg='black').place(x=280, y=280)
        #
        #
        # self.live_update_entry = Entry(master, width=10, textvariable=self.ticker,
        #                                         bg='lightgreen',
        #                                         fg='black').place(x=150, y=300)
        # self.price_entry = Entry(master, width=10, textvariable=self.position_open,
        #                                         bg='lightgreen',
        #                                         fg='black').place(x=280, y=300)  #optional argument what value you entered the market
        #
        # self.live_update_button = Button(master, text='Get Quote',command = lambda: process(target=self.livealert).start())
        # self.live_update_button.place(x=10, y=300)  # this just places the button
        #
        # #################################  beta hedging ######################################
        # self.ticker_a = StringVar()
        # self.ticker_b = StringVar ()
        #
        # # self.beta_hedge_label = Label(master, text="Beta Hedging", \
        # #                      font=("arial", 10, "bold"), fg='black').place(x=280, y=350)
        # self.beta_hedge_entry_a = Entry(master, width=10, textvariable=self.ticker_a,
        #                          bg='lightgreen',
        #                          fg='black').place(x=150, y=350)  # optional argument what value you entered the market, THIS IS THE BASE TICKER
        # self.beta_hedge_entry_b = Entry(master, width=10, textvariable=self.ticker_b,
        #                          bg='lightgreen',
        #                          fg='black').place(x=280, y=350)  # optional argument what value you entered the market, THIS IS THE Y TICKER
        # self.beta_hedge_button = Button(master, text='Beta Hedge  (X,Y)',
        #                                  command=self.get_beta_hedge_parameters)
        # self.beta_hedge_button.place(x=10, y=350)  # this just places the button
        #             # self.beta_hedge =
        # self.plot = IntVar()
        # Checkbutton(master, text="Plot", variable=self.plot).grid(row=0, sticky=W)

        # self.ironcondor_button.pack(side=LEFT)
        # self.put_credit_spread_button.pack(side=LEFT)
        # self.call_debit_spread_button.pack(side=LEFT)

    # def get_beta_hedge_parameters(self):
    #
    #
    #     print("In here")
    #     self.alpha, self.beta, self.summary = bh.beta_hedging(self.ticker_a.get(),self.ticker_b.get()).getstatistics()
    #     print(self.alpha)
    #     print(self.beta)
    #     print(self.summary)
    #
    #
    # def livealert(self) :
    #     self.plot = self.plot.get()
    #     if self.ticker.get() is not "" and self.ticker not in self.ticker_list:
    #         self.ticker_list.append(self.ticker.get())
    #         self.ticker_queue.put(self.ticker.get())
    #         self.ticker_count += 1
    #         self.newx = self.origx + (self.ticker_count - 1) * 100
    #         self.launch_label = create_and_update_price_label(self.master,self.ticker_list,self.newx,self.ticker_count-1,self.position_open.get())





    # def iron_condor_init(self):
    #     self.root_ic = Toplevel(self.master)
    #     self.ic = ots.iron_condor(self.root_ic)
    #     self.root_ic.mainloop()
    #
    # def trade_stats_init(self):
    #     self.root_trading = Toplevel(self.master)
    #     self.trading = ots.trading_stats(self.root_trading)
    #     self.root_trading.mainloop()

# def rand_func(self, a, b, c):
#     print "self:", self, "a:", a, "b:", b, "c:", c
#     pr   int (a+b+c)

#
# class create_and_update_price_label:
#     def __init__(self,master,ticker_list,newx,ticker_count,position_price=""):
#         self.position_price = position_price
#         self.newx = newx
#         self.ticker_list = ticker_list
#
#         self.ticker_count = ticker_count
#         self.master = master
#
#         self.label = Label(self.master, bg='blue',width=10,fg='black')
#
#         self.label.place(x=self.newx, y=400)
#
#
#         self.label2 = Label(self.master, bg='green', width=10,
#                        fg='black')
#         self.label2.place(x=self.newx, y=425)  # this for the current value of the ticker
#         self.latest_price = ""
#         self.price_update()
#
#     def price_update(self):
#         # print(self.ticker.get())
#         self.ticker = self.ticker_list[self.ticker_count]
#         self.label['text'] = self.ticker # this is for the ticker symbol
#         try:
#             response = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(self.ticker, api_key))
#             json_data = json.loads(response.text)
#             # print(self.json_data)
#             latest_price = json_data['Global Quote']['05. price']
#         except:
#             latest_price = random.randint(1,100)
#         # self.label2['text'] = str(latest_price)
#         self.latest_price = str(latest_price)
#         if self.position_price is not "":
#             if float(self.latest_price) < float(self.position_price) and float(self.position_price) is not "":
#                 self.label2['bg'] = "red"
#             else:
#                 self.label2['bg'] = "green"
#         self.label2.config(text=self.latest_price)
#         self.master.after(1000, self.price_update)  #call recursively in a loop


if __name__ == '__main__':
    root = Tk()
    root.title("Options Trading Strategies")
    root.geometry('640x640+0+0')
    app = CardGame(root)
    app.gen_probability()
    root.mainloop()