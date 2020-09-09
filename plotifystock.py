import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from yahoo_fin import stock_info

stockName = input("Enter The Company : ")
price = stock_info.get_live_price(stockName)
print(price)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []



def animate(i, xs, ys):

    
    price = stock_info.get_live_price(stockName)

    
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(price)

    
    xs = xs[-20:]
    ys = ys[-20:]

    
    ax.clear()
    ax.plot(xs, ys)

    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Stock Price with Realtime Plot')
    plt.ylabel('Stock Price in Rupees')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
