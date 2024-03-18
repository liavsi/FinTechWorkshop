import cProfile
import struct
import datetime
import pandas as pd
import numpy as np
from Table_Data_Object import Table_Data_Object as tdo
from Message import *
from enum import Enum
import psutil


# Added Enum class for readability
class MessageType(Enum):
    A = 65
    U = 85
    E = 69
    D = 68
    K = 75
    Q = 81
    P = 80
    H = 72
    V = 86
    N = 78
    M = 77
    R = 82
    L = 76
    Y = 121
    G = 71


class MBO_Parser:
    __slots__ = ["file", "date"]

    def __init__(self, MBO_FILE):
        self.file = MBO_FILE
        self.date = datetime.datetime.now()

    def calculateTimestamp(self, timestamp):
        time_in_nanoseconds = sum(timestamp)
        time_in_seconds = time_in_nanoseconds // 1000000000
        date = datetime.datetime.utcfromtimestamp(time_in_seconds)
        self.date = datetime.datetime.utcfromtimestamp(time_in_seconds)
        date_as_string_format = date.strftime('%d-%m-%Y %H:%M:%S')
        date_as_string_format += '.' + str(int(time_in_nanoseconds % 1000000000)).zfill(9)
        return date_as_string_format

    def getTimestampWithFormat(self, chunk):
        Timestamp = chunk
        return self.calculateTimestamp(struct.unpack('Q', Timestamp))

    def getTimestamp(self, chunk):
        Timestamp = chunk
        return sum(struct.unpack('Q', Timestamp))

    def getMessageLength(self):
        return sum(struct.unpack('I', self.file.read(4)))

    def getMessageType(self):
        return sum(struct.unpack('B', self.file.read(1)))

    def read_string(self, length):
        string = ''
        x = range(0, length)
        for i in x:
            temp = struct.unpack('c', self.file.read(1))
            temp = temp[0].decode('UTF-8', 'ignore')
            string = string + str(temp)
        return string

    def parse_A_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Side = sum(struct.unpack('B', self.file.read(1)))

        return MessageA(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side)

    def parse_U_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        New_Order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Side = sum(struct.unpack('B', self.file.read(1)))
        Original_order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Original_Price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Original_Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        return MessageU(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, New_Order_reference_number, Price, Volume,
                        Side,
                        Original_order_reference_number, Original_Price, Original_Volume)

    def parse_D_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Side = sum(struct.unpack('B', self.file.read(1)))

        return MessageA(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side)

    def parse_E_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Side = sum(struct.unpack('B', self.file.read(1)))
        match_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Auction_reference_number = sum(struct.unpack('I', self.file.read(4)))
        Coordinated_trade_flag = sum(struct.unpack('B', self.file.read(1)))
        Match_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Yield = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t

        return MessageE(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side,
                        match_reference_number, Auction_reference_number, Coordinated_trade_flag, Match_price, Yield)

    def parse_Q_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Auction_type = sum(struct.unpack('B', self.file.read(1)))
        Auction_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Yield = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Auction_reference_number = sum(struct.unpack('I', self.file.read(4)))
        Last_buy_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume_last_buy = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Best_buy_order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Best_buy_order_volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Last_sell_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Last_sell_price_volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Best_sell_order_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Best_sell_order_volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        return MessageQ(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Auction_type, Auction_price, Volume, Yield,
                        Auction_reference_number, Last_buy_price, Volume_last_buy, Best_buy_order_reference_number,
                        Best_buy_order_volume,
                        Last_sell_price, Last_sell_price_volume, Best_sell_order_reference_number,
                        Best_sell_order_volume)
        # self.file.seek(110)
        # return

    def parse_P_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Trade_status = sum(struct.unpack('B', self.file.read(1)))
        Trade_type = sum(struct.unpack('B', self.file.read(1)))
        Trade_reference_number = sum(struct.unpack('Q', self.file.read(8)))
        Auction_reference_number = sum(struct.unpack('I', self.file.read(4)))
        Trade_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Yield = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Coordinated_trade_flag = sum(struct.unpack('B', self.file.read(1)))
        Action = sum(struct.unpack('B', self.file.read(1)))
        return MessageP(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Trade_status, Trade_type,
                        Trade_reference_number,
                        Auction_reference_number, Trade_price, Yield, Volume, Coordinated_trade_flag, Action)
        # self.file.seek(57)
        # return

    def parse_H_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Entity_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Entity_Type = sum(struct.unpack('B', self.file.read(1)))
        Phase_ID = sum(struct.unpack('B', self.file.read(1)))
        Status = sum(struct.unpack('B', self.file.read(1)))
        Reason_code = sum(struct.unpack('I', self.file.read(4)))
        Reference_value = sum(struct.unpack('Q', self.file.read(8)))  # Decimal_t
        Boundary_crossed = sum(struct.unpack('Q', self.file.read(8)))  # Decmial_t
        Value_violating_the_boundary = sum(struct.unpack('Q', self.file.read(8)))  # Decimal_t
        Correction_Flag = sum(struct.unpack('B', self.file.read(1)))
        return MessageH(Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type, Phase_ID,
                        Status, Reason_code, Reference_value, Boundary_crossed, Value_violating_the_boundary,
                        Correction_Flag)
        # self.file.seek(49)
        # return

    def parse_V_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Entity_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Entity_Type = sum(struct.unpack('B', self.file.read(1)))
        Value_Type = sum(struct.unpack('B', self.file.read(1)))
        Value_Of_Entity = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Yield_t = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        correction_flag = sum(struct.unpack('B', self.file.read(1)))
        return MessageV(Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type, Value_Type,
                        Value_Of_Entity, Volume, Yield_t, correction_flag)
        # self.file.seek(44)
        # return

    def parse_K_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_3 = sum(struct.unpack('Q', self.file.read(8)))
        Name = self.read_string(15)
        Local_Name = self.read_string(30)
        return MessageK(Market_ID, RESERVED_1, RESERVED_2, RESERVED_3, Name, Local_Name)
        # self.file.read(62)
        # return

    def parse_N_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Asset_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Asset_Original_ID = sum(struct.unpack('I', self.file.read(4)))
        Name = self.read_string(10)
        Local_Name = self.read_string(20)
        Asset_Base_Value = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Asset_Type = sum(struct.unpack('I', self.file.read(4)))
        Asset_Status = sum(struct.unpack('B', self.file.read(1)))
        Reason_Code = sum(struct.unpack('I', self.file.read(4)))
        return MessageN(Market_ID, Asset_ID, RESERVED_1, RESERVED_2, Asset_Original_ID, Name, Local_Name,
                        Asset_Base_Value, Asset_Type, Asset_Status, Reason_Code)
        # self.file.seek(68)
        # return

    def parse_M_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Segment_ID = sum(struct.unpack('I', self.file.read(4)))
        English_Symbol = self.read_string(10)
        Local_Symbol = self.read_string(20)
        English_Name = self.read_string(15)
        Local_Name = self.read_string(30)
        Sector = sum(struct.unpack('I', self.file.read(4)))
        Sub_Sector = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Type = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Sub_Type = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Tik_Group_ID = sum(struct.unpack('I', self.file.read(4)))
        Issued_during_trading_day = sum(struct.unpack('B', self.file.read(1)))
        Underlying_asset_ID = sum(struct.unpack('I', self.file.read(4)))
        Underlying_asset_type = sum(struct.unpack('I', self.file.read(4)))
        Asset_original_entity_ID = sum(struct.unpack('I', self.file.read(4)))
        ISIN_code = self.read_string(12)
        Minimum_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Exceptional_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Floor_price_for_continuous_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Ceiling_price_for_continuous_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Base_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Instrument_status = sum(struct.unpack('B', self.file.read(1)))
        Expiration_date = self.read_string(8)
        Strike_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Volume_multiplication_factor = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Calculate_turnover = sum(struct.unpack('B', self.file.read(1)))
        Initialization_code = sum(struct.unpack('B', self.file.read(1)))
        Adjusted_option = sum(struct.unpack('B', self.file.read(1)))
        Exact_expiration_date = sum(struct.unpack('q', self.file.read(8)))
        return MessageM(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Segment_ID, English_Symbol,
                        Local_Symbol, English_Name, Local_Name, Sector, Sub_Sector, Instrument_Type,
                        Instrument_Sub_Type, Instrument_Tik_Group_ID, Issued_during_trading_day, Underlying_asset_ID,
                        Underlying_asset_type, Asset_original_entity_ID, ISIN_code, Minimum_order_size,
                        Exceptional_order_size, Floor_price_for_continuous_phase, Ceiling_price_for_continuous_phase,
                        Base_price, Instrument_status, Expiration_date, Strike_price, Volume_multiplication_factor,
                        Calculate_turnover, Initialization_code, Adjusted_option, Exact_expiration_date)
        # self.file.seek(217)
        # return

    def parse_R_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Instrument_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Segment_ID = sum(struct.unpack('I', self.file.read(4)))
        English_Symbol = self.read_string(10)
        Local_Symbol = self.read_string(20)
        English_Name = self.read_string(15)
        Local_Name = self.read_string(30)
        Sector = sum(struct.unpack('I', self.file.read(4)))
        Sub_Sector = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Type = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Sub_Type = sum(struct.unpack('I', self.file.read(4)))
        Instrument_Tik_Group_ID = sum(struct.unpack('I', self.file.read(4)))
        Currency_Code = sum(struct.unpack('I', self.file.read(4)))
        Company_id = sum(struct.unpack('I', self.file.read(4)))
        ISIN_code = self.read_string(12)
        Pre_open_Minimum_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Continuous_Minimum_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Pre_close_Minimum_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Exceptional_order_size = sum(struct.unpack('q', self.file.read(8)))  # Vol_t
        Floor_price_for_pre_open_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Ceiling_price_for_pre_open_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Floor_price_for_continuous_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Ceiling_price_for_continuous_phase = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Base_price = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Instrument_status = sum(struct.unpack('b', self.file.read(1)))
        Ex_code = sum(struct.unpack('I', self.file.read(4)))
        Dual_registered_code = sum(struct.unpack('B', self.file.read(1)))
        New_Instrument_Indicator = sum(struct.unpack('B', self.file.read(1)))
        Market_Making_Indicator = sum(struct.unpack('B', self.file.read(1)))
        Maintenance_Or_low_liquidity_Indicator = sum(struct.unpack('B', self.file.read(1)))
        Base_yield = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Maturity_date = self.read_string(8)
        Accrued_interest = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Static_price_monitoring_boundary = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Dynamic_price_monitoring_boundary = sum(struct.unpack('q', self.file.read(8)))  # Decimal_t
        Initialization_code = sum(struct.unpack('B', self.file.read(1)))
        return MessageR(Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Segment_ID, English_Symbol,
                        Local_Symbol, English_Name, Local_Name, Sector, Sub_Sector, Instrument_Type,
                        Instrument_Sub_Type,
                        Instrument_Tik_Group_ID, Currency_Code, Company_id, ISIN_code,
                        Pre_open_Minimum_order_size, Continuous_Minimum_order_size, Pre_close_Minimum_order_size,
                        Exceptional_order_size, Floor_price_for_pre_open_phase, Ceiling_price_for_pre_open_phase,
                        Floor_price_for_continuous_phase, Ceiling_price_for_continuous_phase, Base_price,
                        Instrument_status, Ex_code, Dual_registered_code, New_Instrument_Indicator,
                        Market_Making_Indicator, Maintenance_Or_low_liquidity_Indicator, Base_yield, Maturity_date,
                        Accrued_interest, Static_price_monitoring_boundary, Dynamic_price_monitoring_boundary,
                        Initialization_code)
        # self.file.seek(258)
        # return

    def parse_L_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Tick_group_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Range_Count = sum(struct.unpack('I', self.file.read(4)))
        Range_Position = sum(struct.unpack('I', self.file.read(4)))
        Beginning_of_the_range = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        End_of_the_range = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        Tick_value_inside_range = sum(struct.unpack('q', self.file.read(8)))  # Pri_t
        return MessageL(Market_ID, Tick_group_ID, RESERVED_1, RESERVED_2, Range_Count, Range_Position,
                        Beginning_of_the_range, End_of_the_range, Tick_value_inside_range)
        # self.file.read(49)
        # return

    def parse_Y_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Entity_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Entity_Type = sum(struct.unpack('B', self.file.read(1)))
        return MessageY(Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type)
        # self.file.read(18)
        # return

    def parse_G_message(self):
        Market_ID = sum(struct.unpack('B', self.file.read(1)))
        Entity_ID = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_1 = sum(struct.unpack('I', self.file.read(4)))
        RESERVED_2 = sum(struct.unpack('Q', self.file.read(8)))
        Entity_Type = sum(struct.unpack('B', self.file.read(1)))
        return MessageY(Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type)
        # self.file.read(18)
        # return

    def parseFile(self):
        Table_data_type = np.dtype([
            ('Transaction_ID', int),
            ('Name', 'U20'),
            ('Price', float),
            ('Side', int),
            ('Timestamp', np.longlong),
            ('Volume', int),
            ('Order_Executed', int),
            ('Target', int)
        ])
        Targets_Table = pd.read_csv('Targets.csv')
        CommandBook_Table = {}
        Execute_key = 1
        Execute_Table = {}

        self.file.read(55)  # moving the offset past the file header
        while True:
            chunk = self.file.read(8)  # reading the timestamp 8 BYTES
            if not chunk:
                break
            Timestamp = self.getTimestamp(chunk)
            Message_length = self.getMessageLength()  # reading the Message Length 4 BYTES
            Message_Type = self.getMessageType()  # reading the Message Type 1 BYTE

            if Message_Type == MessageType.A.value:
                newMessage = self.parse_A_message()
                side = newMessage.Side
                if side == 83:
                    side = 1
                else:
                    side = 0

                target = 0
                if newMessage.Instrument_ID in set(Targets_Table['Instrument_ID']):
                    index = Targets_Table[Targets_Table.Instrument_ID == newMessage.Instrument_ID].index.tolist()
                    target = Targets_Table._get_value(index[0], 'Target')
                CommandBook_Table[newMessage.Order_reference_number] = tdo(newMessage.Order_reference_number,
                                                                           newMessage.Instrument_ID, newMessage.Price,
                                                                           side, Timestamp, newMessage.Volume, 0,
                                                                           target)
            elif Message_Type == MessageType.U.value:
                newMessage = self.parse_U_message()
                side = newMessage.Side
                if side == 83:
                    side = 1
                else:
                    side = 0

                CommandBook_Table[newMessage.New_Order_reference_number] = tdo(newMessage.New_Order_reference_number,
                                                                               newMessage.Instrument_ID,
                                                                               newMessage.Price, side, Timestamp,
                                                                               newMessage.Volume,
                                                                               CommandBook_Table[
                                                                                   newMessage.Original_order_reference_number].Order_Executed,
                                                                               CommandBook_Table[
                                                                                   newMessage.Original_order_reference_number].Target)
                del CommandBook_Table[newMessage.Original_order_reference_number]
            elif Message_Type == MessageType.D.value:
                newMessage = self.parse_D_message()
                del CommandBook_Table[newMessage.Order_reference_number]
            elif Message_Type == MessageType.E.value:
                newMessage = self.parse_E_message()
                Original_volume = CommandBook_Table[newMessage.Order_reference_number].Volume
                New_volume = Original_volume - newMessage.Volume
                Execute_Table[Execute_key] = tdo(newMessage.Order_reference_number,
                                                 newMessage.Instrument_ID, newMessage.Price,
                                                 CommandBook_Table[newMessage.Order_reference_number].Side,
                                                 Timestamp, newMessage.Volume, 1,
                                                 CommandBook_Table[
                                                     newMessage.Order_reference_number].Target)
                Execute_key = Execute_key + 1
                if New_volume == 0:
                    del CommandBook_Table[newMessage.Order_reference_number]
                else:
                    CommandBook_Table[newMessage.Order_reference_number].Volume = New_volume
            elif Message_Type == MessageType.Q.value:
                self.file.read(110)
            elif Message_Type == MessageType.P.value:
                self.file.read(57)
            elif Message_Type == MessageType.H.value:
                self.file.read(49)
            elif Message_Type == MessageType.V.value:
                self.file.read(44)
            elif Message_Type == MessageType.K.value:
                self.file.read(62)
            elif Message_Type == MessageType.N.value:
                self.file.read(68)
            elif Message_Type == MessageType.M.value:
                self.file.read(217)
            elif Message_Type == MessageType.R.value:
                self.file.read(258)
            elif Message_Type == MessageType.L.value:
                self.file.read(49)
            elif Message_Type == MessageType.Y.value:
                self.file.read(18)
            elif Message_Type == MessageType.G.value:
                self.file.read(18)

        # Creating the columns from CommandBook_Table and Execute_Table
        transaction_ids = [obj.Transaction_ID for obj in list(CommandBook_Table.values())]
        transaction_ids.extend([obj.Transaction_ID for obj in list(Execute_Table.values())])
        names = [obj.Name for obj in list(CommandBook_Table.values())]
        names.extend([obj.Name for obj in list(Execute_Table.values())])
        prices = [obj.Price for obj in list(CommandBook_Table.values())]
        prices.extend([obj.Price for obj in list(Execute_Table.values())])
        sides = [obj.Side for obj in list(CommandBook_Table.values())]
        sides.extend([obj.Side for obj in list(Execute_Table.values())])
        timestamps = [obj.Timestamp for obj in list(CommandBook_Table.values())]
        timestamps.extend([obj.Timestamp for obj in list(Execute_Table.values())])
        volumes = [obj.Volume for obj in list(CommandBook_Table.values())]
        volumes.extend([obj.Volume for obj in list(Execute_Table.values())])
        orders_executed = [obj.Order_Executed for obj in list(CommandBook_Table.values())]
        orders_executed.extend([obj.Order_Executed for obj in list(Execute_Table.values())])
        targets = [obj.Target for obj in list(CommandBook_Table.values())]
        targets.extend([obj.Target for obj in list(Execute_Table.values())])

        # Creating a structured array
        data_array = np.array(
            list(zip(transaction_ids, names, prices, sides, timestamps, volumes, orders_executed, targets)),
            dtype=Table_data_type
        )

        return data_array
