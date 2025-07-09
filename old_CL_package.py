import re
import numpy as np
import random
import matplotlib.pyplot as plt

# -----------------------------------------------------------------

# color index and letter:
#
# 0: orange, O
# 1: blue,   B
# 2: white,  W
# 3: green,  G
# 4: black,  K
#    blank,  b

def color_index(color):
    return ['orange','blue','white','green','black'].index(color)

# -----------------------------------------------------------------

def generate_deck(WOB=0, OKB=0, OKG=0, KKK=0,
 	OO=0, OB=0, BB=0, OG=0, BG=0, WG=0, OK=0, BK=0, KG = 0, KK = 0,
    O=0, B=0, W=0, G=0, K=0,
    b=0):
#
# three icons:
    nWOB = np.array([1,1,1,0,0]) + np.zeros((WOB,5))
    nOKB = np.array([1,1,0,0,1]) + np.zeros((OKB,5))
    nOKG = np.array([1,0,0,1,1]) + np.zeros((OKG,5))
    nKKK = np.array([0,0,0,0,3]) + np.zeros((KKK,5))
#
# two icons:
    nOO  = np.array([2,0,0,0,0]) + np.zeros((OO,5))
    nOB  = np.array([1,1,0,0,0]) + np.zeros((OB,5))
    nBB  = np.array([0,2,0,0,0]) + np.zeros((BB,5))    
    nOG  = np.array([1,0,0,1,0]) + np.zeros((OG,5))
    nBG  = np.array([0,1,0,1,0]) + np.zeros((BG,5))
    nWG  = np.array([0,0,1,1,0]) + np.zeros((WG,5))
    nKG  = np.array([0,0,0,1,1]) + np.zeros((KG,5))
    nKK  = np.array([0,0,0,0,2]) + np.zeros((KK,5))
#
    nOK  = np.array([1,0,0,0,1]) + np.zeros((OK,5))
    nBK  = np.array([0,1,0,0,1]) + np.zeros((BK,5))
#
# one icons:
    nO   = np.array([1,0,0,0,0]) + np.zeros((O,5))
    nB   = np.array([0,1,0,0,0]) + np.zeros((B,5))
    nW   = np.array([0,0,1,0,0]) + np.zeros((W,5))
    nG   = np.array([0,0,0,1,0]) + np.zeros((G,5))
    nK   = np.array([0,0,0,0,1]) + np.zeros((K,5))
#
# no icons:
    nb   = np.zeros((b,5))
#
    deck = np.concatenate((nWOB, nOKB, nOKG, nKKK,
                           nOO, nOB, nBB, nOG, nBG, nWG, 
                           nO, nB, nW, nG, nK, nOK, nBK, nKG, nKK,
                           nb), axis=0).astype(int)
    np.random.shuffle(deck)
    return deck

# -----------------------------------------------------------------

def card_on_top (card,deck):
    return np.concatenate((np.array([card]),deck), axis=0)

# -----------------------------------------------------------------

def generate_flipped_icons(deck,bold_tough):
    if sum(deck[:(2+bold_tough)])[2] > 0:
        icons = sum(deck[:(2+bold_tough+2)])
    else:
        icons = sum(deck[:(2+bold_tough)])
    return icons

# -----------------------------------------------------------------

def generate_icon_distributions (deck,bold_tough,simulations):
    orange_dist = np.array([])
    blue_dist   = np.array([])
    white_dist  = np.array([])
    green_dist  = np.array([])
    black_dist  = np.array([])
    for i in range(0,simulations,1):
        np.random.shuffle(deck)
        flips = generate_flipped_icons(deck,bold_tough)
        o = flips[0]
        b = flips[1]
        w = flips[2]
        g = flips[3]
        k = flips[4]
        orange_dist = np.append(orange_dist,o)
        blue_dist   = np.append(blue_dist,b)
        white_dist  = np.append(white_dist,w)
        green_dist  = np.append(green_dist,g)
        black_dist  = np.append(black_dist,k)        
    return np.array([orange_dist, blue_dist, white_dist,green_dist,black_dist])

# -----------------------------------------------------------------

def generate_probability_distributions(deck,bold_tough,color,simulations):
    P = []
    if color == 'orange':
        label = 0
        col = 'orange'
    elif color == 'blue':
        label = 1
        col = 'blue'
    elif color == 'white':
        label = 2
        col = 'lightgray'

    elif color == 'green':
        label = 3
        col = 'green'

    elif color == 'black':
        label = 4
        col = 'black'
        
    else:
        return "'Wrong color. Please choose 'orange', 'blue', 'white, 'green', or 'black'."
    dist = generate_icon_distributions (deck,bold_tough,simulations)
    prob = plt.hist(dist[label],
                    np.arange(0,21,1)-0.5,
                    rwidth=0.8, 
                    color = col,
                    edgecolor='black', 
                    linewidth=1.0,
                    weights=100*np.ones(len(dist[label])) / len(dist[label]))[0]
    plt.xticks(range(21))
    for i in range(0,20,1):
        if prob[i] > 0.01:
            P.append([i,float('{:.{d}f}'.format(prob[i],d=2))])
    return P

# -----------------------------------------------------------------

def probability_exact_n(deck,color,number,bold_tough,simulations):
    success = 0
    if color == 'orange':
        label = 0
    elif color == 'blue':
        label = 1
    elif color == 'white':
        label = 2
    elif color == 'green':
        label = 3
    elif color == 'black':
        label = 4
    else:
        return "'Wrong color. Please choose 'orange', 'blue', 'white', 'green', or 'black'."
    for i in range(0,simulations,1):
        np.random.shuffle(deck)
        flips = generate_flipped_icons(deck,bold_tough)
        if (flips[label]==number):
            success += 1
    return 100*float(success)/simulations

# -----------------------------------------------------------------

def probability_at_least_n(deck,color,number,bold_tough,simulations):
    success = 0
    if color == 'orange':
        label = 0
    elif color == 'blue':
        label = 1
    elif color == 'white':
        label = 2
    elif color == 'green':
        label = 3
    elif color == 'black':
        label = 4
    else:
        return "'Wrong color. Please choose 'orange', 'blue', 'white', 'green', or 'black'."
    for i in range(0,simulations,1):
        np.random.shuffle(deck)
        flips = generate_flipped_icons(deck,bold_tough)
        if (flips[label]>=number):
            success += 1
    return 100*float(success)/simulations

# -----------------------------------------------------------------

def bluestreak_success_rate(deck,bold_tough,simulations):
    success = 0
    for i in range(0,simulations,1):
        np.random.shuffle(deck)
        flips = generate_flipped_icons(deck,bold_tough)
        if (flips[0]>=1 and flips[1]>=1 and flips[2]>=1):
            success += 1
    return 100*float(success)/simulations



def jazz_success_rate(deck,bold_tough,simulations):
    success = 0
    for i in range(0,simulations,1):
        np.random.shuffle(deck)
        flips = generate_flipped_icons(deck,bold_tough)
        if flips[2]>=2:
            success += 1
    return 100*float(success)/simulations

# -----------------------------------------------------------------
# this has nothing to do with the game. But i use it often
# find the ref to this:

def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

# -----------------------------------------------------------------













