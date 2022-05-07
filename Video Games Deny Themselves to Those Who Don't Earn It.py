from datetime import datetime, timedelta
import time

def encrypt(string, code=5):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ''
    for i in string:
        if(i in alphabet):
            i_index = alphabet.index(i)
            new_string +=(alphabet[(i_index + code)%len(alphabet)])
        else:
            new_string += i
    return new_string

def decrypt(string, key=5):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ''
    for i in string:
        if(i in alphabet):
            i_index = alphabet.index(i)
            new_string +=(alphabet[i_index - key])
        else:
            new_string += i
    return new_string

class States:
    yesses = ["yes", "yea", "yup", "ye", "I consent", "yuppers", "agreed", "sure", "ok", "okay", "why not?", "I consent", "uh-huh"]
    nos = ["no", "nope", "nay", "never", "no way", "no way jose", "uh-uh", "nah"]
    state = 0
    prev_state = 0
    attempts = 0
    retry = False
    name = ""
    acc_names_enc = ["wzxxjqq", "wzxxjqq Bnqqnfrx"]
    acc_names = [decrypt(acc_names_enc[0], 5), decrypt(acc_names_enc[1], 5)]
    
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=15)
        
    def acceptance(self, inp, yes_state, no_state):
        inp = inp.lower()
        if(inp in self.yesses):
            self.state = yes_state
        elif(inp in self.nos):
            self.state = no_state
        else:
            self.error()
    
    def run_state(self):
        if(self.state == 0):
            self.state0()
        elif(self.state == 1):
            self.state1()
        elif(self.state == 2):
            self.state2()
        elif(self.state == 3):
            self.state3()
        elif(self.state == 4):
            self.state4()
        elif(self.state == 5):
            self.state5()
        elif(self.state == 6):
            self.state6()
        elif(self.state == 7):
            self.state7()
        elif(self.state == 8):
            self.state8()
        elif(self.state == 9):
            self.state9()
        elif(self.state == 11):
            self.state11()
        elif(self.state == 12):
            self.state12()
        elif(self.state == 13):
            self.state13()
        elif(self.state == 14):
            self.state14()
        elif(self.state == 15):
            self.state15()
        elif(self.state == 16):
            self.state16()
        elif(self.state == 17):
            self.state17()
        elif(self.state == 18):
            self.state18()
        elif(self.state == 19):
            self.state19()
        elif(self.state == 20):
            self.state20()
        elif(self.state == 21):
            self.state21()
        elif(self.state == -2):
            self.stateneg2()

    def state0(self):
        if(self.retry == False):
            text = "bjqhtrj yt ymj lfrj. dtz hfs sjAjw qjfAj."
            print(decrypt(text,5))
        self.state0_input()

    def state0_input(self):
        text = "btzqi Dtz qnpj yt qjfAj ymj lfrj?"
        inp = input(decrypt(text,5) + "\n")
        self.acceptance(inp, 2, 1)
            
    def state1(self):
        text = "N pstB Dtz."
        print(decrypt(text, 5))
        self.state1_input()
    
    def state1_input(self):
        text = "bmt fwj Dtz?"
        self.name = input(decrypt(text,5) + "\n")
        if(self.name.lower() in self.acc_names):
            self.state = 3
        else:
            self.state = 4
        
    def state2(self):
        if(datetime.now() > self.end_time):
            text = "Tp, Dtz'Aj xujsy ymj wjvznwji ynrj uqfDnsl. SjAjw mfx thhzwwji. dtz'wj kwjj yt lt."
            print(decrypt(text, 5))
            self.state = -2
        else:
            text = "N ytqi Dtz, Dtz'wj ns ny stB. Ymjwj nx st jxhfuj. MtBjAjw, Dtz hfs wjxyfwy fy fsD ynrj gD yDunsl wjxyfwy"
            print(decrypt(text,5))
            self.state = 0
            self.state0_input()
              
    def state3(self):
        text = """bjqhtrj, Wzxxjqq, yt Dtzw xytwD.

dtz'wj xnyynsl fy Dtzw htruzyjw, wjfinsl tsj tk ymj nsyjwfhynAj knhynts unjhjx Bwnyyjs gD tsj tk Dtzw xyzijsyx. Ny'x nsyjwjxynsl, gzy sty xt nsyjwjxynsl ymfy Dtz'i hmttxj yt wjfi ny nk Dtz inis'y sjji yt lwfij ny."""
        print(decrypt(text,5))
        self.state3_input()
        
    def state3_input(self):
        text = "btzqi Dtz qnpj yt pjju wjfinsl?"
        inp = input(decrypt(text,5) + "\n")
        self.acceptance(inp, 5, 6)
    
    def state5(self):
        text = """Ymj yjCy wtqqx kzwymjw. Ymj xytwD gjlnsx yt iwtsj. Xtrjymnsl ns ymj yjCy rfpjx Dtz ymnsp tk Dtzw hmnqimtti. 
Ujwmfux ny Bfx ymj Btwi hmnqimtti. 
dtz Bjwjs'y fqBfDx f uwtkjxxtw. 
Tshj, Dtz Bjwj f hmnqi. F xfqqtB hmnqi. dtz xytu wjfinsl ktw f kjB xjhtsix fsi xnsp nsyt rjrtwnjx tk Dtzw hmnqimtti."""
        print(decrypt(text,5))
        time.sleep(5)
        print(".")
        time.sleep(5)
        print(".")
        time.sleep(5)
        print(".")
        time.sleep(5)
        self.state5_input()
        
    def state5_input(self):
        text = "bfx ny f mfuuD ynrj?"
        inp = input(decrypt(text,5))
        self.acceptance(inp, 8, 7)
            
    def state7(self):
        text = "dtz Bjwjs'y f mfuuD hmnqi. dtzw ufwjsyx Bjwj lwjD ujtuqj Bnym lwjD kfhjx, fsi jAjs ymjD Bjwj htshjwsji fy Dtzw xtrgjw inxutxnynts."
        print(decrypt(text,5))
        self.state7_input()
        
    def state7_input(self):
        text = "Nx ymfy sty wnlmy?"
        inp = input(decrypt(text,5) + "\n")
        self.acceptance(inp, 6, 6)
        
    def state8(self):
        text = """N fr ymj sfwwfytw, Wzxxjqq. Ny Bfx Bmfy N xfD ny Bfx. dtz fwj Bmt N xfD Dtz fwj.
        
Ini Dtz ymnsp ymfy ymnx nsyjwfhynAj xyzkk Btzqi rfpj Dtz ns htsywtq? Fqq Dtz mfAj itsj nx jCufsiji rj. StB, ymj Btwqi nx rnsj ns yjCy, fsi jAjwDBmjwj."""
        print(decrypt(text,5))
        self.state = 7 
        
    def state6(self):
        text = "Fqwnlmy, xt, ymnx unjhj nxs'y zu Dtzw fqqjD? Ymfy'x knsj. Yjqq rj, Bmfy Btzqi Dtz uwjkjw yt wjfi?"
        print(decrypt(text,5))
        self.state6_input()
        
    def state6_input(self):
        text = """1. Xtrjymnsl nsyjwjxynsl, qnpj 'Nk Ts f bnsyjw'x Snlmy f YwfAjqjw' gD Nyfqt HfqAnst
2. Xtrjymnsl gjfzynkzq, qnpj xtrj djfyx
3. Xtrjymnsl... jqxj"""
        inp = input(decrypt(text,5) + "\n")
        if(inp[0] == "1"):
            self.state = 11
        elif(inp[0] == "2"):
            self.state = 12
        elif(inp[0] == "3"):
            self.state = 13
        else:
            self.error()
        
    def state11(self):
        text = """Fqwnlmy, Bjqq, qjy rj ozxy uzqq zu fs jChjwuy tk ymfy. 
        
****************************        

Xt, ymjs, Dtz stynhji ns f sjBxufujw ymfy Nk ts f Bnsyjw'x snlmy f ywfAjqjw mfi fuujfwji, ymj sjB gttp gD Nyfqt HfqAnst, Bmt mfis'y uzgqnxmji ktw xjAjwfq Djfwx. dtz Bjsy yt ymj gttpxmtu fsi gtzlmy ymj Atqzrj. Ltti ktw Dtz.

Ns ymj xmtu BnsitB Dtz mfAj uwtruyqD nijsynknji ymj htAjw Bnym ymj ynyqj Dtz Bjwj qttpnsl ktw. KtqqtBnsl ymnx Anxzfq ywfnq, Dtz mfAj ktwhji Dtzw BfD ymwtzlm ymj xmtu ufx ymj ymnhp gfwwnhfij tk Gttpx dtz MfAjs'y Wjfi, Bmnhm Bjwj kwtBsnsl fy Dtz kwtr ymj yfgqjx fsi xmjqAjx, ywDnsl yt htB Dtz. Gzy Dtz pstB Dtz rzxy sjAjw fqqtB Dtzwxjqk yt gj fBji, ymfy frtsl ymjr ymjwj jCyjsi ktw fhwjx fsi fhwjx ymj Gttpx dtz Sjjis'y Wjfi, ymj Gttpx Rfij Ktw Uzwutxjx Tymjw Ymfs Wjfinsl, Gttpx Wjfi JAjs Gjktwj dtz Tujs Ymjr Xnshj YmjD Gjqtsl Yt Ymj HfyjltwD Tk Gttpx Wjfi Gjktwj Gjnsl bwnyyjs. Fsi ymzx Dtz ufxx ymj tzyjw lnwiqj tk wfrufwyx, gzy ymjs Dtz fwj fyyfhpji gD ymj nskfsywD tk ymj Gttpx Ymfy Nk dtz Mfi Rtwj Ymfs Tsj Qnkj dtz btzqi HjwyfnsqD Fqxt Wjfi Gzy ZsktwyzsfyjqD dtzw IfDx Fwj Szrgjwji. bnym f wfuni rfsjzAjw Dtz gDufxx ymjr fsi rtAj nsyt ymj umfqfsCjx tk ymj Gttpx dtz Rjfs Yt Wjfi Gzy Ymjwj Fwj Tymjwx dtz Rzxy Wjfi Knwxy, ymj Gttpx Ytt JCujsxnAj StB Fsi dtz'qq bfny Ynqq YmjD'wj Wjrfnsijwji, ymj Gttpx inyyt bmjs YmjD Htrj Tzy Ns Ufujwgfhp, Gttpx dtz Hfs GtwwtB Kwtr XtrjgtiD, Gttpx Ymfy JAjwDgtiD'x Wjfi Xt Ny'x Fx Nk dtz Mfi Wjfi Ymjr, Ytt. Jqzinsl ymjxj fxxfzqyx, Dtz htrj zu gjsjfym ymj ytBjwx tk ymj ktwywjxx, Bmjwj tymjw ywttux fwj mtqinsl tzy:

  ymj Gttpx dtz'Aj Gjjs Uqfssnsl Yt Wjfi Ktw Fljx,
  ymj Gttpx dtz'Aj Gjjs Mzsynsl Ktw djfwx bnymtzy Xzhhjxx,
  ymj Gttpx Ijfqnsl bnym Xtrjymnsl dtz'wj btwpnsl Ts Fy Ymj Rtrjsy,
  ymj Gttpx dtz bfsy Yt TBs Xt YmjD'qq Gj MfsiD Ozxy Ns Hfxj,
  ymj Gttpx dtz Htzqi Uzy Fxnij RfDgj Yt Wjfi Ymnx Xzrrjw,
  ymj Gttpx dtz Sjji Yt Lt bnym Tymjw Gttpx Ts dtzw XmjqAjx,
  ymj Gttpx Ymfy Knqq dtz bnym Xziijs, NsjCuqnhfgqj HzwntxnyD, Sty JfxnqD Ozxynknji.

StB Dtz mfAj gjjs fgqj yt wjizhj ymj htzsyqjxx jrgfyyqji ywttux yt fs fwwfD ymfy nx, yt gj xzwj, AjwD qfwlj gzy xynqq hfqhzqfgqj ns f knsnyj szrgjw; gzy ymnx wjqfynAj wjqnjk nx ymjs zsijwrnsji gD ymj frgzxm tk ymj Gttpx Wjfi Qtsl Flt bmnhm Ny'x StB Ynrj Yt Wjwjfi fsi ymj Gttpx dtz'Aj FqBfDx Uwjyjsiji Yt MfAj Wjfi Fsi StB Ny'x Ynrj Yt Xny ItBs Fsi WjfqqD Wjfi Ymjr.

bnym f EnlEfl ifxm Dtz xmfpj ymjr tkk fsi qjfu xywfnlmy nsyt ymj hnyfijq tk ymj SjB Gttpx bmtxj Fzymtw Tw Xzgojhy Fuujfqx Yt dtz. JAjs nsxnij ymnx xywtslmtqi Dtz hfs rfpj xtrj gwjfhmjx ns ymj wfspx tk ymj ijkjsijwx, inAninsl ymjr nsyt SjB Gttpx GD Fzymtwx Tw Ts Xzgojhyx Sty SjB (ktw Dtz tw ns ljsjwfq) fsi SjB Gttpx GD Fzymtwx Tw Ts Xzgojhyx HtruqjyjqD ZspstBs (fy qjfxy yt Dtz), fsi ijknsnsl ymj fyywfhynts ymjD mfAj ktw Dtz ts ymj gfxnx tk Dtzw ijxnwjx fsi sjjix ktw ymj sjB fsi ymj sty sjB (ktw ymj sjB Dtz xjjp ns ymj sty sjB fsi ktw ymj sty sjB Dtz xjjp ns ymj sjB).

Fqq ymnx xnruqD rjfsx ymfy, mfAnsl wfuniqD lqfshji tAjw ymj ynyqjx tk ymj Atqzrjx inxuqfDji ns ymj gttpxmtu, Dtz mfAj yzwsji ytBfwi f xyfhp tk Nk ts f Bnsyjw'x snlmy f ywfAjqjw kwjxm tkk ymj uwjxx, Dtz mfAj lwfxuji f htuD, fsi Dtz mfAj hfwwnji ny yt ymj hfxmnjw xt ymfy Dtzw wnlmy yt tBs ny hfs gj jxyfgqnxmji."""
        print(decrypt(text,5) + "\n\n\n")
        time.sleep(15)
        text2 = """******************

bFNY bFNY bFNY bFNY! StB Bfny ozxy f xjhtsi mjwj.
'Dtz stynhji ns f sjBxufujw'?
'sjB gttp gD Nyfqt HfqAnst'? Ymnx hfrj tzy ijhfijx flt. Nyfqt HfqAnst nx ijfi!
Fqq ymnx inxhzxxnts fgtzy f xmtu BnsitB fsi unhpnsl ymj gttp tzy? dtz inis'y it fsD tk ymfy, N gfxnhfqqD unhpji ny ktw Dtz.
Stsj tk ymjxj ymnslx mfuujsji! Ymnx gttp nx kzqq tk qnjx! Nx ymnx Bmfy Dtz'wj nsyt, f gzshm tk qnjx? N yttp Dtz ktw gjyyjw ymfs ymfy."""
        print(decrypt(text2,5) + "\n")
        self.state11_input()
        
    def state11_input(self):
        text = """bmfy it Dtz jAjs ljy tzy tk ymnx fsDBfD? bmD Btzqi Dtz Bfsy yt wjfi qnjx?

1. Ny'x sty qnjx, ny'x knhynts
2. YmjD'wj gjfzynkzq qnjx ymtzlm
3. Ny'x sty qnjx, N fhyzfqqD ini fqq ymtxj ymnslx"""
        inp = input(decrypt(text,5))
        if(inp[0] == "1"):
            self.state = 14
        elif(inp[0] == "2"):
            self.state = 14
        elif(inp[0] == "3"):
            self.state = 14
        else:
            self.error()
            
    def state12(self):
        text = """Qjy rj ozxy lt xjj Bmfy N mfAj."""
        print(decrypt(text,5))
        time.sleep(15)
        text2 = """Mjwj'x f ltti tsj. 'bmjs dtz Fwj Tqi', gD b.G. djfyx.
        
**************

bmjs Dtz fwj tqi fsi lwjD fsi kzqq tk xqjju,
Fsi stiinsl gD ymj knwj, yfpj itBs ymnx gttp,
Fsi xqtBqD wjfi, fsi iwjfr tk ymj xtky qttp
dtzw jDjx mfi tshj, fsi tk ymjnw xmfitBx ijju;

MtB rfsD qtAji Dtzw rtrjsyx tk lqfi lwfhj,
Fsi qtAji Dtzw gjfzyD Bnym qtAj kfqxj tw ywzj,
Gzy tsj rfs qtAji ymj unqlwnr xtzq ns Dtz,
Fsi qtAji ymj xtwwtBx tk Dtzw hmfslnsl kfhj;

Fsi gjsinsl itBs gjxnij ymj lqtBnsl gfwx,
Rzwrzw, f qnyyqj xfiqD, mtB QtAj kqji
Fsi ufhji zuts ymj rtzsyfnsx tAjwmjfi
Fsi mni mnx kfhj frni f hwtBi tk xyfwx.

************"""
        print(decrypt(text2,5))
        time.sleep(30)
        text3 = """bjqq, ymfy rnlmy gj gjfzynkzq, gzy N mfAj yt xfD, Bmfy ymj mjqq nx ny yfqpnsl fgtzy? bmfy gttp? Ymnx nxs'y f gttp.
Fsi ymnx xttymxfDnsl. dtz pstB ymfy ozxy gjhfzxj ymnx utjr xfDx ymnx Bnqq thhzw itjx sty rfpj ny xt."""
        print(decrypt(text3,5))
        self.state12_input()
        
    def state12_input(self):
        text = """bmfy it Dtz ljy tzy tk f ymnsl qnpj ymnx? """
        inp = input(decrypt(text,5) + "\n")
        text2 = """bjqq, N'r xtwwD yt xfD, Dtz uwtgfgqD Bts'y knsi ymfy mjwj. """
        print(decrypt(text2, 5))
        time.sleep(5)
        print(".")
        time.sleep(5)
        print(".")
        time.sleep(5)
        print(".")
        time.sleep(5)
        self.state = 20
        
    def state13(self):
        text = """Tm, zm, nx ymfy Bmfy Dtz qnpj yt wjfi? Fqwnlmy, N lzjxx yt jfhm ymjnw tBs. Mjwj'x f qnyyqj gny kwtr KnkyD Xmfijx tk LwjD gD J.Q. Ofrjx.

*************

RD rtzym ltjx iwD fsi ijxnwj gqttrx ns rD gtiD... Bmtf.

"Pjju rj nsktwrji," mj xsfux fsi xmzyx tkk mnx umtsj fx mj xywnijx uzwutxjkzqqD ytBfwi rj. N xyfsi ufwfqDEji fx mj hqtxjx ymj inxyfshj gjyBjjs zx, ijAtzwnsl rj Bnym mnx jDjx. MtqD xmny... xtrjymnsl'x frnxx - ymj xywfns ns mnx ofB, ymj fsCnjyD fwtzsi mnx jDjx.

Mj xmwzlx tzy tk mnx ofhpjy, zsitjx mnx ifwp ynj, fsi xqnslx ymjr gtym ts yt ymj htzhm js wtzyj yt rj. Ymjs mnx fwrx fwj Bwfuuji fwtzsi rj, fsi mj'x uzqqnsl rj yt mnr, mfwi, kfxy, lwnuunsl rD utsDyfnq yt ynqy rD mjfi zu, pnxxnsl rj qnpj mnx qnkj ijujsix ts ny. bmfy ymj mjqq Mj iwflx ymj mfnw ynj ufnskzqqD tzy tk rD mfnw, gzy N its'y hfwj. Ymjwj'x f ijxujwfyj, uwnrfq vzfqnyD yt mnx pnxx. Mj sjjix rj, ktw BmfyjAjw wjfxts, fy ymnx utnsy ns ynrj, fsi N mfAj sjAjw kjqy xt ijxnwji fsi htAjyji. Ny'x ifwp fsi xjsxzfq fsi fqfwrnsl fqq fy ymj xfrj ynrj. N pnxx mnr gfhp Bnym jvzfq kjwAtw, rD knsljwx yBnxynsl fsi knxynsl ns mnx mfnw. Tzw ytslzjx jsyBnsji, tzw ufxxnts fsi fwitw jwzuynsl gjyBjjs zx. Mj yfxyjx inAnsj, mty, xjCD, fsi mnx xhjsy - fqq gtiD Bfxm fsi Hmwnxynfs nx xt fwtzxnsl. Mj iwflx mnx rtzym fBfD kwtr rnsj, fsi mj'x xyfwnsl itBs fy rj, lwnuuji gD xtrj zssfrji jrtynts. 

*************"""
        print(decrypt(text,5))
        time.sleep(20)
        text2 = """Fqwnlmy mtqi zu. Ymfy'x fgtzy fqq tk ymfy ymfy N ymnsp N hfs uzy mjwj. MtsjxyqD, nk ymfy'x Bmfy Dtz'wj nsyt, ozxy lt fsi gzD ymfy gttp. 
Gzy N mfAj yt xfD, N its'y ljy ny. dtz pstB ymfy ny'x sty Dtz ns ymfy gttp, wnlmy? Sty tsqD fwj ymtxj ymnslx sty wjfq, gzy ymjD'wj mfuujsnsl yt xtrj tymjw sty wjfq ujwxts. dtz pstB ymfy, its'y Dtz? Ymfy'x sty Dtz."""
        print(decrypt(text2,5))
        self.state13_input()
        
    def state13_input(self):
        text = """1. N inis'y Bfsy yt wjfi ymfy!
2. N its'y ymnsp ny'x rj.
3. N'r sty ns ymnx xytwD jnymjw"""
        inp = input(decrypt(text,5) + "\n")
        if(inp == "1"):
            self.state = 15
        elif(inp == "2"):
            self.state = 16
        elif(inp == "3"):
            self.state = 17
        else:
            error()
            
    def state15(self):
        text = "bjqq st tsj ktwhji Dtz yt. Ns kfhy, st tsj nx ktwhnsl Dtz yt wjfi fsD tk ymnx. dtz, zsqnpj Dtzsl Fsfxyfxnf ymjwj, fwj sty gjnsl ktwhji yt it fsD tk ymnx. Ns kfhy, Dtz'wj ktwhnsl fqq tk ymnx ts rj. "
        print(decrypt(text,5))
        self.state15_input()
        
    def state16(self):
        text = """St, Dtz uwtgfgqD its'y. dtz its'y xjj ymfy Dtz'wj sty wjfqqD ymj tsj ns htsywtq mjwj. dtz uwtgfgqD its'y xjj ymfy Dtz fwj Fsfxyfxnf. N'r xzwj Dtz ymnsp ymfy fqq tk ymnx nx Dtzw hmtnhj. bjqq ymjs, ufwits rD xfwhfxr:"""
        print(decrypt(text,5))
        self.state15_input()
        
    def state17(self):
        text = """dtz fsi N fwj ymj tsqD tsjx Bmt fwj ns ymnx xytwD, ywfuuji mjwj, jsiqjxxqD zsijknsnsl fsi wjijknsnsl tzwxjqAjx. Nx ymfy Dtzw nxxzj Bnym ny, nx ymfy BmD Dtz Bfsy KnkyD Xmfijx? dtz Bfsy f inkkjwjsy sfrj? btzqi Dtz uwjkjw N fiiwjxx Dtz fx xtrjymnsl jqxj? bjqq, N mfAj f wjvzjxy ns jChmfslj."""
        print(decrypt(text,5))
        self.state15_input()
        
    def state15_input(self):
        text = """Xt, Rw. LwjD, Bts'y Dtz uqjfxj, uqjfxj ozxy qjy rj xytu?"""
        inp = input(decrypt(text,5) + "\n")
        self.acceptance(inp, -1, 0)
            
    def state14(self):
        text = """bjqq, wjlfwiqjxx, N Bts'y gj Dtzw rtzymunjhj tk qnjx. bj'qq gj ijfqnsl Bnym ywzymx tsqD mjwj. Qjy'x ljy gfhp yt ywzymx.
dtz fwj sty fy f gttpxytwj, Dtz fwj xnyynsl itBs fy f htruzyjw, wjfinsl yjCy ymfy htrjx tzy ns xmtwy gzwxyx.
Ny'x yjintzx. Ny mtujx yt gj rtwj nsyjwjxynsl gD fqqtBnsl Dtz hmtnhj, fsi Dtz fwj rfpnsl hmtnhjx. Hmtnhjx tk Bmfy yt yDuj ns."""
        print(decrypt(text,5))
        if(self.retry == False):
            text2 = """Xt kfw, Dtz mfAj rfij tsqD ltti hmtnhjx, hmtnhjx Bmnhm Bnqq xtts xjy Dtz kwjj."""
        else:
            text2 = """Xtrj tk Dtzw hmtnhjx mfAj gjjs rnxyfpjx, xjyynsl Dtz kzwymjw kwtr ymj kwjjitr Bmnhm fBfnyx Dtz. Gzy xynqq, Dtz mfAj rfij ny yt mjwj."""
        print(decrypt(text2,5))
        self.state14_input()
        
    def state14_input(self):
        text = """Fwj Dtz wjfiD ktw ymj ywzym? 
"""
        inp = input(decrypt(text,5))
        self.acceptance(inp, 20, 21)
        
    def state20(self):
        text = """Xt ymjs lt tzy fsi knsi ny."""
        print(decrypt(text,5))
        self.state = -2
        
    def state_21(self):
        text = """Ymjs xyfD fx qtsl fx Dtz qnpj."""
        print(decrypt(text,5))
        self.state = -2
        
    def error(self):
        if(self.attempts == 2):
            text = "dtz mfAj fsljwji Lti ytt rfsD ynrjx. Ymnx nx ymj jsi ktw Dtz. XfD lttigDj yt ymj Btwqi Ny mfx fqqtBji Dtz yt hwjfyj fsi Bfyhm fx ny nx jwfxji. Fsi pstB ymnx: Dtz fwj sty kwjj. Ymj Ltiuzyjw ytqi Dtz Bmjs ymnx xyfwyji, Dtz hfs sjAjw qjfAj. dtz fwj f hfuynAj mjwj, f hmfwfhyjw, Bmtxj jAjwD hmtnhj jCnxyx Bnymns ymnx xytwD."
            print(decrypt(text,5))
            self.state = -2
        else:
            self.attempts += 1
            text = """dtzw wjxutsxj mfx fsljwji ymj htruzyjw, kzshyntsfqqD Lti tk ymnx Btwqi. Ny ijyjwrnsjx Bmfy Dtz hfs fsi hfssty it, fsi Dtz mfAj fyyjruyji ymj qfyyjw.
Ns nyx pnsisjxx, Ltiuzyjw mfx ijhniji yt wjAjwxj ymj kqtB tk ynrj fsi xjsi Dtz gfhp yt ywD flfns. GjBfwj nyx nwj."""
            print(decrypt(text,5))
            self.retry = True
            time.sleep(2)
            text2 = "WjAjwxnsl ynrj:"
            print(decrypt(text2,5))
            time.sleep(2)
            
    def stateneg2(self):
        text = "Ymj lfrj Bnqq stB wjxyfwy. Fqq Dtz mfAj itsj Bnqq gj ltsj, jwfxji kwtr ymnx rjrtwD tsqD xqnlmyqD kfxyjw ymfs ny Bnqq kfij kwtr Dtzwx. Fqq ymnslx fwj jumjrjwfq, fsi Dtz fwj st inkkjwjsy."
        print(decrypt(text,5))
        self.state = 0
        self.prev_state = 0
        self.attempts = 0
        self.retry = False
        self.name = ""
        
    def state4(self):
        text = "N fqwjfiD pstB Bmt Dtz fwj? bmD Btzqi Dtz qnj yt rj, Wzxxjqq?"
        print(decrypt(text,5))
        self.state = 3

story = States()
while (story.state != -1):
    story.run_state()
