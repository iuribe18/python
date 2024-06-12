from art import logo
print(logo)
bids = {}
should_continue = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while should_continue:
    name = input("What's your name: ")
    bid = int(input("What's your bid: "))
    bids[name] = bid
    result = input("Press 'yes' if you go on. Otherwise type 'no' to exit: ")
    if result == "no":
        should_continue = False
        find_highest_bidder(bids)
        print("Goodbye...!!!")