import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import math
import pandas as pd
import matplotlib.pyplot as mt
Rf = []
RW = []
FR = []
RB = []
RTR = []
ve = []
RA = []
RApp = []
RT = []
EP = []
SM = []
PD = []
GB = []
SP = []
BP = []

class connectpage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Density(ρ)(kg/m^3)"))
        self.f = TextInput(multiline=False)
        self.add_widget(self.f)

        self.add_widget(Label(text="Gravity(m/sec^2)"))
        self.g = TextInput(multiline=False)
        self.add_widget(self.g)

        self.add_widget(Label(text="Length overall(LOA)(m)"))
        self.LOA = TextInput(multiline=False)
        self.add_widget(self.LOA)

        self.add_widget(Label(text="Length of the waterline(LWL)(m)"))
        self.LWL = TextInput(multiline=False)
        self.add_widget(self.LWL)

        self.add_widget(Label(text="Length between perpendiculars(LBP)(m)"))
        self.LBP = TextInput(multiline=False)
        self.add_widget(self.LBP)

        self.add_widget(Label(text="LCB in percentage(%)"))
        self.LCB = TextInput(multiline=False)
        self.add_widget(self.LCB)

        self.add_widget(Label(text="Breadth(B)(m)"))
        self.B = TextInput(multiline=False)
        self.add_widget(self.B)

        self.add_widget(Label(text="Draft(T)(m)"))
        self.T = TextInput(multiline=False)
        self.add_widget(self.T)

        self.add_widget(Label(text="Block coefficient(Cb)"))
        self.CB = TextInput(multiline=False)
        self.add_widget(self.CB)

        self.add_widget(Label(text="Prismatic coefficient(Cp)"))
        self.CP = TextInput(multiline=False)
        self.add_widget(self.CP)

        self.add_widget(Label(text="Midship coefficient(Cm)"))
        self.CM = TextInput(multiline=False)
        self.add_widget(self.CM)

        self.add_widget(Label(text="Waterline coefficient(Cwl)"))
        self.CWL = TextInput(multiline=False)
        self.add_widget(self.CWL)

        self.add_widget(Label(text="Wetted Surface Area(S)(m^2)"))
        self.S = TextInput(multiline=False)
        self.add_widget(self.S)

        self.add_widget(Label(text="Viscosity(Ns/m^2)"))
        self.M = TextInput(multiline=False)
        self.add_widget(self.M)

        self.add_widget(Label(text="ABT(m^2)"))
        self.ABT = TextInput(multiline=False)
        self.add_widget(self.ABT)

        self.add_widget(Label(text="hB(m)"))
        self.hB = TextInput(multiline=False)
        self.add_widget(self.hB)

        self.add_widget(Label(text="ATR(m^2)"))
        self.ATR = TextInput(multiline=False)
        self.add_widget(self.ATR)

        self.add_widget(Label(text="Number of Speed"))
        self.n = TextInput(multiline=False)
        self.add_widget(self.n)

        self.add_widget(Label(text="Underwater volume(V)(m^3)"))
        self.V = TextInput(multiline=False)
        self.add_widget(self.V)

        self.add_widget(Label(text="Csternchoice"))
        self.Csternchoice = TextInput(multiline=False)
        self.add_widget(self.Csternchoice)

        self.add_widget(Label(text="Bulbchoice"))
        self.Bulbchoice = TextInput(multiline=False)
        self.add_widget(self.Bulbchoice)

        self.add_widget(Label(text="Sapp(m^2)"))
        self.Sapp = TextInput(multiline=False)
        self.add_widget(self.Sapp)

        self.add_widget(Label(text="Appendage"))
        self.Appendage = TextInput(multiline=False)
        self.add_widget(self.Appendage)

        self.join = Button(text="Calculate")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        global Cstern
        f = float(self.f.text)
        g = float(self.g.text)
        LOA = float(self.LOA.text)
        LWL = float(self.LWL.text)
        LBP = float(self.LBP.text)
        LCB = float(self.LCB.text)
        B = float(self.B.text)
        T = float(self.T.text)
        CB = float(self.CB.text)
        CP = float(self.CP.text)
        CM = float(self.CM.text)
        CWL = float(self.CWL.text)
        S = float(self.S.text)
        M = float(self.M.text)
        ABT = float(self.ABT.text)
        hB = float(self.hB.text)
        ATR = float(self.ATR.text)
        n = int(self.n.text)
        V = float(self.V.text)
        Csternchoice = float(self.Csternchoice.text)
        Bulbchoice = float(self.Bulbchoice.text)
        Sapp = float(self.Sapp.text)
        Appendage = float(self.Appendage.text)

        """FRICTIONAL RESISTANCE"""
        for vkn in range(1, n):
            if Csternchoice == 1:
                Cstern = -25
            elif Csternchoice == 2:
                Cstern = -10
            elif Csternchoice == 3:
                Cstern = 0
            elif Csternchoice == 4:
                Cstern = 10
            else:
                print("Invalid choice")
            Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
            k = 0.93 + ((0.487118 * (1 + 0.011 * Cstern)) * ((B / LOA) ** 1.06806) * ((T / LOA) ** 0.46106) * ((LWL / Lr) ** 0.121563) * (((LWL ** 3) / V) ** 0.36486) * ((1 - CP) ** -0.604247))
            v = vkn * 0.5144
            Re = (v * LBP) / M
            CF = (0.075 / (((math.log10(Re)) - 2) ** 2))
            ACF = 0.00051
            R = (CF + ACF) * (0.5 * f * S * (v ** 2))
            RF = k * R
            Rf.append(RF)
            continue

        """WAVE MAKING RESISTANCE"""
        for vkn in range(1, n):
            v = vkn * 0.5144
            Fr = v / (math.sqrt(g * LBP))
            if Fr < 0.40:
                Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
                ie = 1 + (89 * (math.exp(
                    (-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367) * (
                                (Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
                if B / LBP < 0.11:
                    c7 = 0.229577 * ((B / LBP) ** 0.3333)
                elif 0.11 <= B / LBP <= 0.25:
                    c7 = B / LBP
                else:
                    c7 = 0.5 - (0.0625 * (LBP / B))
                c1 = 2223105 * (c7 ** 3.78613) * ((T / B) ** 1.07961) * ((90 - ie) ** (-1.37565))
                c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
                c2 = math.exp(-1.89 * (math.sqrt(c3)))
                c5 = 1 - (0.8 * (ATR / (B * T * CM)))
                if CP < 0.8:
                    c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
                else:
                    c16 = 1.73014 - (0.7067 * CP)
                m1 = (0.014047 * (LBP / T)) - ((1.75254 * (V ** (1 / 3))) / LBP) - (4.79323 * (B / LBP)) - c16
                if LBP / B < 12:
                    l = (1.446 * CP) - (0.03 * (LBP / B))
                else:
                    l = (1.446 * CP) - 0.36
                if ((LBP ** 3) / V) < 512:
                    c15 = -1.69385
                elif 512 < ((LBP ** 3) / V) < 1726.91:
                    c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
                else:
                    c15 = 0
                m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
                d_ = -0.9
                Rw = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (Fr ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
                RW.append(Rw)
                FR.append(Fr)
                continue
            elif 0.40 < Fr < 0.55:
                Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
                ie = 1 + (89 * (math.exp(
                    (-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367) * (
                                (Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
                if B / LBP < 0.11:
                    c7 = 0.229577 * ((B / LBP) ** 0.3333)
                elif 0.11 <= B / LBP <= 0.25:
                    c7 = B / LBP
                else:
                    c7 = 0.5 - (0.0625 * (LBP / B))
                c1 = 2223105 * (c7 ** 3.78613) * ((T / B) ** 1.07961) * ((90 - ie) ** (-1.37565))
                c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
                c2 = math.exp(-1.89 * (math.sqrt(c3)))
                c5 = 1 - (0.8 * (ATR / (B * T * CM)))
                if CP < 0.8:
                    c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
                else:
                    c16 = 1.73014 - (0.7067 * CP)
                m1 = (0.014047 * (LBP / T)) - ((1.75254 * (V ** (1 / 3))) / LBP) - (4.79323 * (B / LBP)) - c16
                if LBP / B < 12:
                    l = (1.446 * CP) - (0.03 * (LBP / B))
                else:
                    l = (1.446 * CP) - 0.36
                if ((LBP ** 3) / V) < 512:
                    c15 = -1.69385
                elif 512 < ((LBP ** 3) / V) < 1726.91:
                    c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
                else:
                    c15 = 0
                m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
                d_ = -0.9
                rwo_ = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (0.44 ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
                rwo__ = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (0.55 ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
                Rw = rwo_ + (((10 * Fr) - 4) * ((rwo__ - rwo_) / 1.5))
                RW.append(Rw)
                FR.append(Fr)
                continue
            else:
                Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
                ie = 1 + (89 * (math.exp(
                    (-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367) * (
                                (Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
                c17 = (6919.3 * (CM ** (-1.3346))) * ((V / (LBP ** 3)) ** 2.00977) * (((LBP / B) - 2) ** 1.40692)
                m3 = (-7.2035 * ((B / LBP) ** 0.326869)) * ((T / B) ** 0.605375)
                c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
                c2 = math.exp(-1.89 * (math.sqrt(c3)))
                c5 = 1 - (0.8 * (ATR / (B * T * CM)))
                if CP < 0.8:
                    c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
                else:
                    c16 = 1.73014 - (0.7067 * CP)
                m1 = (0.014047 * (LBP / T)) - ((1.75254 * (V ** (1 / 3))) / LBP) - (4.79323 * (B / LBP)) - c16
                if LBP / B < 12:
                    l = (1.446 * CP) - (0.03 * (LBP / B))
                else:
                    l = (1.446 * CP) - 0.36
                if ((LBP ** 3) / V) < 512:
                    c15 = -1.69385
                elif 512 < ((LBP ** 3) / V) < 1726.91:
                    c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
                else:
                    c15 = 0
                m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
                d_ = -0.9
                Rw = c17 * c2 * c5 * V * f * g * (math.exp((m3 * (Fr ** d_) + (m4 * (math.cos(l * (Fr ** -2)))))))
                RW.append(Rw)
                FR.append(Fr)
                continue

        """BULB RESISTANCE"""
        for vkn in range(1, n):
            v = vkn * 0.5144
            if Bulbchoice == 1:
                Fri = v / (math.sqrt((g * (T - hB - (0.25 * (math.sqrt(ABT))))) + (0.15 * (v ** 2))))
                pb = (0.56 * (math.sqrt(ABT))) / (T - (1.5 * hB))
                Rb = 0.11 * (math.exp(((-3) * (pb ** (-2)))) * (Fri ** 3) * (ABT ** 1.5) * f * g) / (1 + (Fri ** 2))
                RB.append(Rb)
                continue
            elif Bulbchoice == 0:
                Rb = 0
                RB.append(Rb)
                continue
            else:
                print("Error")

        """TRANSOM RESISTANCE"""
        for vkn in range(1, n):
            v = vkn * 0.5144
            ve.append(v)
            FRT = v / (math.sqrt((2 * g * ATR) / (B + (B * CWL))))
            if FRT < 5:
                c6 = 0.2 * (1 - (0.2 * FRT))
            else:
                c6 = 0
            Rtr = 0.5 * f * (v ** 2) * ATR * c6
            RTR.append(Rtr)
            continue

        """MODEL-SHIP CORRELATION RESISTANCE RA"""
        for vkn in range(1, n):
            v = vkn * 0.5144
            if T / LBP <= 0.04:
                c4 = T / LBP
            else:
                c4 = 0.04
            c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
            c2 = math.exp(-1.89 * (math.sqrt(c3)))
            try:
                CA = (0.006 * ((LBP + 100) ** -0.16)) - 0.00205 + (
                            0.003 * (math.sqrt(LBP / (7.5 * (CB ** 4) * c2 * (0.04 - c4)))))
            except ZeroDivisionError:
                CA = (0.006 * ((LBP + 100) ** -0.16)) - 0.00205
            Ra = 0.5 * f * S * (v ** 2) * CA
            RA.append(Ra)
            continue

        """APPENDAGE RESISTANCE"""
        if Appendage == 1:
            k2 = 1.5
        elif Appendage == 2:
            k2 = 1.3
        elif Appendage == 3:
            k2 = 2.8
        elif Appendage == 4:
            k2 = 1.5
        elif Appendage == 5:
            k2 = 2.8
        else:
            k2 = 1.4
        for vkn in range(1, n):
            v = vkn * 0.5144
            Re = (v * LBP) / M
            CF = (0.075 / (((math.log10(Re)) - 2) ** 2))
            Rapp = 0.5 * f * (v ** 2) * Sapp * k2 * CF
            RApp.append(Rapp)
            continue

        for i in range(0, len(Rf)):
            RT.append(Rf[i] + RW[i] + RB[i] + RTR[i] + RA[i] + RApp[i])

        for i in range(0, len(RT)):
            EP.append((RT[i] * ve[i]))
            SM.append((EP[i] * 1.15))
            PD.append((EP[i] / 0.65))
            SP.append((PD[i] / 0.95))
            BP.append((SP[i] / 0.85))

        d = pd.DataFrame(
            {'Velocity': ve,
             'RFrictional': Rf,
             'RwaveMaking':RW,
             'RBulbous': RB,
             'RTransom': RTR,
             'RCorrelation': RA,
             'R Appendage': RApp,
             'Total Resistance(N)': RT,
             'Effective Power': EP,
             'Sea Margin': SM,
             'Delivered Power': PD,
             'Shaft Power': SP,
             'Brake Power(W)': BP}
        )

        d.style.set_properties(**{'text-align': 'right'})
        d.style.set_table_styles([dict(selector='th', props=[('text-align', 'right')])])
        pd.set_option('display.width', 9000)
        pd.set_option('display.max_columns', 50)
        Result = f"{d}"
        Run_app.info_page.update_info(Result)
        Run_app.screen_manager.current = "Result"

        mt.plot(FR, RT)
        mt.xlabel("Froude Number")
        mt.ylabel("Total Resistance")
        mt.show()

        mt.plot(ve, RT)
        mt.xlabel("Velocity(m/sec)")
        mt.ylabel("Total Resistance")
        mt.show()

        mt.plot(ve, BP)
        mt.xlabel("Velocity(m/sec")
        mt.ylabel("Power(W)")
        mt.show()


class Resultpage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.message = Label(halign="center", valign="top", font_size=13)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)


class ResistanceCalculator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.info_page = Resultpage()
        self.connect_page = connectpage()
        self.screen_manager = ScreenManager()

    def build(self):
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Result")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    Run_app = ResistanceCalculator()
    Run_app.run()
