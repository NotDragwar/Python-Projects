import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#INPUTS ith candle, starting value of x, default width, and the four critical values: open, close, max\_p, min\_p.  
#RETURN three tuples: (point, width, height, color), topline, bottomline
#topline ((xt0,yt0),(xt1,yt1)) line from max to top middle of box
#bottomline ((xb0,yb0),(xb1,yb1)) line from min to bottom middle of box
def make(i,start,width_default,d):
    a,b,max,min  = d
    if a<= b:
        color = "green"
        point = (start,a)
        yt_1 = b
        yb_1 = a
    else:
        color = "red"
        point = (start,b)
        yt_1 = a
        yb_1 = b
    height_ab = abs(a-b)
    top_line = ((start + (width_default/2),max),(start + (width_default/2),yt_1))
    bottom_line = ((start + (width_default/2),yb_1),(start + (width_default/2),min))
    return (point,width_default,height_ab,color),top_line,bottom_line


# test cases 
if __name__ == "__main__":
    data5 = [[20,15,32,10],[10,14,15,9],[22,23,27,9],[15,16,16,15],[26,12,30,2],[5,30,40,4]]


    fig = plt.figure()
    ax = fig.add_subplot(111)
    start = 0
    default_width = 10
   
    for i in range(len(data5)):
        candle_box,top_line,bottom_line = make(i,start,default_width,data5[i])

        print(candle_box)
        ax.add_patch(matplotlib.patches.Rectangle(*candle_box[0:3],color = candle_box[3]))
        plt.plot([x for x,_ in top_line],[y for _,y in top_line],'black')
        plt.plot([x for x,_ in bottom_line],[y for _,y in bottom_line],'black')
        start += default_width


    plt.xlabel("time (hour)")
    plt.ylabel("Stock X price")
    plt.title("Candlestick for XXX")  
    plt.xlim([0, 60]) #depends on number
    plt.ylim([0, 35]) #depends on price
  
    plt.show()
    

    fig = plt.figure()
    ax = fig.add_subplot(111)
    start = 0
    default_width = 2
   
    # os.chdir("")

    wms = pd.read_csv('walmart_stock.csv', index_col='Date',parse_dates=['Date'])
    # print(wms.head())
    wms_c = wms[['Open','Close','High','Low']]
    print(wms_c.iloc[0].values.flatten().tolist())
    N_stocks = 50
    for i in range(N_stocks):
        candle_box,top_line,bottom_line = make(i,start,default_width,wms_c.iloc[i].values.flatten().tolist())

        # print(candle_box)
        ax.add_patch(matplotlib.patches.Rectangle(*candle_box[0:3],color = candle_box[3]))
        plt.plot([x for x,_ in top_line],[y for _,y in top_line],'black')
        plt.plot([x for x,_ in bottom_line],[y for _,y in bottom_line],'black')
        start += default_width


    plt.xlabel("time day")
    plt.ylabel("Walmart price $")
    plt.title("Candlestick for Walmart")  
    plt.xlim([0, N_stocks*default_width]) #depends on number
    plt.ylim([58, 63]) #depends on price
  
    plt.show()