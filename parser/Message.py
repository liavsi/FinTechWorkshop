# Sent when a new volume is released to the visible book. This can happen, for example, when a new
# incoming order was not fully matched, when a new volume of an Iceberg order is released, or when a
# waiting stop-loss order is released.
# Will be sent also as part of the snapshot describing a visible order book.
class MessageA:
    __slots__ = ["_Market_ID", "_Instrument_ID", "_RESERVED_1", "_RESERVED_2", "_Order_reference_number", "_Price", "_Volume", "_Side"]

    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side):
        self._Market_ID = Market_ID
        self._Instrument_ID = Instrument_ID
        self._RESERVED_1 = RESERVED_1
        self._RESERVED_2 = RESERVED_2
        self._Order_reference_number = Order_reference_number
        self._Price = Price
        self._Volume = Volume
        self._Side = Side

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self._Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self._RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self._RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Order_reference_number(self):
        return self._Order_reference_number

    @Order_reference_number.setter
    def Order_reference_number(self, value):
        self._Order_reference_number = value

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Side(self):
        return self._Side

    @Side.setter
    def Side(self, value):
        self._Side = value


# Sent when an order with open volume in the visible book is replaced using an "order cancel/add" request.
# The original order has to be removed from the book and the new order added.
class MessageU:
    __slots__ = ["_Market_ID", "_Instrument_ID", "_RESERVED_1", "_RESERVED_2", "_New_Order_reference_number",
                 "_Price", "_Volume", "_Side", "_Original_order_reference_number",
                 "_Original_Price",
                 "_Original_Volume"]

    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, New_Order_reference_number, Price, Volume,
                 Side, Original_order_reference_number, Original_Price, Original_Volume):
        self._Market_ID = Market_ID
        self._Instrument_ID = Instrument_ID
        self._RESERVED_1 = RESERVED_1
        self._RESERVED_2 = RESERVED_2
        self._New_Order_reference_number = New_Order_reference_number
        self._Price = Price
        self._Volume = Volume
        self._Side = Side
        self._Original_order_reference_number = Original_order_reference_number
        self._Original_Price = Original_Price
        self._Original_Volume = Original_Volume

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self._Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self._RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self._RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def New_Order_reference_number(self):
        return self._New_Order_reference_number

    @New_Order_reference_number.setter
    def New_Order_reference_number(self, value):
        self._New_Order_reference_number = value

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Side(self):
        return self._Side

    @Side.setter
    def Side(self, value):
        self._Side = value

    @property
    def Original_order_reference_number(self):
        return self._Original_order_reference_number

    @Original_order_reference_number.setter
    def Original_order_reference_number(self, value):
        self._Original_order_reference_number = value

    @property
    def Original_Price(self):
        return self._Original_Price

    @Original_Price.setter
    def Original_Price(self, value):
        self._Original_Price = value

    @property
    def Original_Volume(self):
        return self._Original_Volume

    @Original_Volume.setter
    def Original_Volume(self, value):
        self._Original_Volume = value


# Sent when an order is deleted or removed (e.g. due to order suspension) from the visible book
class MessageD:
    __slots__ = ["_Market_ID", "_Instrument_ID", "_RESERVED_1", "_RESERVED_2",
                 "_Order_reference_number",
                 "_Price", "_Volume", "_Side"]

    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side):
        self._Market_ID = Market_ID
        self._Instrument_ID = Instrument_ID
        self._RESERVED_1 = RESERVED_1
        self._RESERVED_2 = RESERVED_2
        self._Order_reference_number = Order_reference_number
        self._Price = Price
        self._Volume = Volume
        self._Side = Side

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self.Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Order_reference_number(self):
        return self.Order_reference_number

    @Order_reference_number.setter
    def Order_reference_number(self, value):
        self._Order_reference_number = value

    @property
    def Price(self):
        return self.Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Volume(self):
        return self.Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Side(self):
        return self.Side

    @Side.setter
    def Side(self, value):
        self._Side = value


# Sent after each execution against a resting order in the visible book. If the execution occurred during an
# auction, the auction ref. number will be filled.
class MessageE:
    __slots__ = ["_Market_ID", "_Instrument_ID", "_RESERVED_1", "_RESERVED_2", "_Order_reference_number",
                 "_Price", "_Volume", "_Side", "_match_reference_number",
                 "_Auction_reference_number",
                 "_Coordinated_trade_flag", "_Match_price", "_Yield"]

    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Order_reference_number, Price, Volume, Side,
                 match_reference_number, Auction_reference_number, Coordinated_trade_flag, Match_price, Yield):
        self._Market_ID = Market_ID
        self._Instrument_ID = Instrument_ID
        self._RESERVED_1 = RESERVED_1
        self._RESERVED_2 = RESERVED_2
        self._Order_reference_number = Order_reference_number
        self._Price = Price
        self._Volume = Volume
        self._Side = Side
        self._match_reference_number = match_reference_number
        self._Auction_reference_number = Auction_reference_number
        self._Coordinated_trade_flag = Coordinated_trade_flag
        self._Match_price = Match_price
        self._Yield = Yield

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self._Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Order_reference_number(self):
        return self._Order_reference_number

    @Order_reference_number.setter
    def Order_reference_number(self, value):
        self._Order_reference_number = value

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Side(self):
        return self._Side

    @Side.setter
    def Side(self, value):
        self._Side = value

    @property
    def match_reference_number(self):
        return self._match_reference_number

    @match_reference_number.setter
    def match_reference_number(self, value):
        self._match_reference_number = value

    @property
    def Auction_reference_number(self):
        return self.Auction_reference_number

    @Auction_reference_number.setter
    def Auction_reference_number(self, value):
        self._Auction_reference_number = value

    @property
    def Coordinated_trade_flag(self):
        return self.Coordinated_trade_flag

    @Coordinated_trade_flag.setter
    def Coordinated_trade_flag(self, value):
        self._Coordinated_trade_flag = value

    @property
    def Match_price(self):
        return self._Match_price

    @Match_price.setter
    def Match_price(self, value):
        self._Match_price = value

    @property
    def Yield(self):
        return self.Yield

    @Yield.setter
    def Yield(self, value):
        self._Yield = value


# Sent after an auction (e.g. opening / closing), after all the other messages describing individual matches
# (i.e. E & P messages).
class MessageQ:
    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Auction_type, Auction_price, Volume, Yield,
                 Auction_reference_number, Last_buy_price, Volume_last_buy, Best_buy_order_reference_number,
                 Best_buy_order_volume,
                 Last_sell_price, Last_sell_price_volume, Best_sell_order_reference_number, Best_sell_order_volume):
        self.Market_ID = Market_ID
        self.Instrument_ID = Instrument_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Auction_type = Auction_type
        self.Auction_price = Auction_price
        self.Volume = Volume
        self.Yield = Yield
        self.Auction_reference_number = Auction_reference_number
        self.Last_buy_price = Last_buy_price
        self.Volume_last_buy = Volume_last_buy
        self.Best_buy_order_reference_number = Best_buy_order_reference_number
        self.Best_buy_order_volume = Best_buy_order_volume
        self.Last_sell_price = Last_sell_price
        self.Last_sell_price_volume = Last_sell_price_volume
        self.Best_sell_order_reference_number = Best_sell_order_reference_number
        self.Best_sell_order_volume = Best_sell_order_volume

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self.Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Auction_type(self):
        return self.Auction_type

    @Auction_type.setter
    def Auction_type(self, value):
        self._Auction_type = value

    @property
    def Auction_price(self):
        return self.Auction_price

    @Auction_price.setter
    def Auction_price(self, value):
        self._Auction_price = value

    @property
    def Volume(self):
        return self.Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Yield(self):
        return self.Yield

    @Yield.setter
    def Yield(self, value):
        self._Yield = value

    @property
    def Auction_reference_number(self):
        return self.Auction_reference_number

    @Auction_reference_number.setter
    def Auction_reference_number(self, value):
        self._Auction_reference_number = value

    @property
    def Last_buy_price(self):
        return self.Last_buy_price

    @Last_buy_price.setter
    def Last_buy_price(self, value):
        self._Last_buy_price = value

    @property
    def Volume_last_buy(self):
        return self.Volume_last_buy

    @Volume_last_buy.setter
    def Volume_last_buy(self, value):
        self._Volume_last_buy = value

    @property
    def Best_buy_order_reference_number(self):
        return self.Best_buy_order_reference_number

    @Best_buy_order_reference_number.setter
    def Best_buy_order_reference_number(self, value):
        self._Best_buy_order_reference_number = value

    @property
    def Best_buy_order_volume(self):
        return self.Best_buy_order_volume

    @Best_buy_order_volume.setter
    def Best_buy_order_volume(self, value):
        self._Best_buy_order_volume = value

    @property
    def Last_sell_price(self):
        return self.Last_sell_price

    @Last_sell_price.setter
    def Last_sell_price(self, value):
        self._Last_sell_price = value

    @property
    def Last_sell_price_volume(self):
        return self.Last_sell_price_volume

    @Last_sell_price_volume.setter
    def Last_sell_price_volume(self, value):
        self._Last_sell_price_volume = value

    @property
    def Best_sell_order_reference_number(self):
        return self.Best_sell_order_reference_number

    @Best_sell_order_reference_number.setter
    def Best_sell_order_reference_number(self, value):
        self._Best_sell_order_reference_number = value

    @property
    def Best_sell_order_volume(self):
        return self.Best_sell_order_volume

    @Best_sell_order_volume.setter
    def Best_sell_order_volume(self, value):
        self._Best_sell_order_volume = value


# Sent during continuous trade if the resting volume was hidden, or during an auction if both sides of the
# trade were hidden volumes.
# Sent also after trade / match cancelation/renewal, as the cancelled/renewed volume does not affect the
# visible book.
class MessageP:
    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Trade_status, Trade_type,
                 Trade_reference_number,
                 Auction_reference_number, Trade_price, Yield, Volume, Coordinated_trade_flag, Action):
        self.Market_ID = Market_ID
        self.Instrument_ID = Instrument_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Trade_status = Trade_status
        self.Trade_type = Trade_type
        self.Trade_reference_number = Trade_reference_number
        self.Auction_reference_number = Auction_reference_number
        self.Trade_price = Trade_price
        self.Yield = Yield
        self.Volume = Volume
        self.Coordinated_trade_flag = Coordinated_trade_flag
        self.Action = Action

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self.Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Trade_status(self):
        return self.Trade_status

    @Trade_status.setter
    def Trade_status(self, value):
        self._Trade_status = value

    @property
    def Trade_type(self):
        return self.Trade_type

    @Trade_type.setter
    def Trade_type(self, value):
        self._Trade_type = value

    @property
    def Trade_reference_number(self):
        return self.Trade_reference_number

    @Trade_reference_number.setter
    def Trade_reference_number(self, value):
        self._Trade_reference_number = value

    @property
    def Auction_reference_number(self):
        return self.Auction_reference_number

    @Auction_reference_number.setter
    def Auction_reference_number(self, value):
        self._Auction_reference_number = value

    @property
    def Trade_price(self):
        return self.Trade_price

    @Trade_price.setter
    def Trade_price(self, value):
        self._Trade_price = value

    @property
    def Yield(self):
        return self.Yield

    @Yield.setter
    def Yield(self, value):
        self._Yield = value

    @property
    def Volume(self):
        return self.Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Coordinated_trade_flag(self):
        return self.Coordinated_trade_flag

    @Coordinated_trade_flag.setter
    def Coordinated_trade_flag(self, value):
        self._Coordinated_trade_flag = value

    @property
    def Action(self):
        return self.Action

    @Action.setter
    def Action(self, value):
        self._Action = value


# An Entity Status message will be sent after every status (e.g. halt, suspension) or trading phase change.
# If market ID is empty – this is for the entire system.
# If entity ID is empty & market ID is not – this is for the market
# If entity ID & market ID are not empty – this is for an instrument or underlying asset (according to entity
# type value).
# For PM halts, ref value is the static/dynamic ref price, boundary value is the crossed limit. The violating
# value is the would-be deal price that caused the halt.
# When an underlying asset is halted, an Entity Status message will be sent for that asset indicating that all
# options and futures of this asset are halted.
class MessageH:
    def __init__(self, Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type, Phase_ID, Status,
                 Reason_code, Reference_value, Boundary_crossed, Value_violating_the_boundary, Correction_Flag):
        self.Market_ID = Market_ID
        self.Entity_ID = Entity_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Entity_Type = Entity_Type
        self.Phase_ID = Phase_ID
        self.Status = Status
        self.Reason_code = Reason_code
        self.Reference_value = Reference_value
        self.Boundary_crossed = Boundary_crossed
        self.Value_violating_the_boundary = Value_violating_the_boundary
        self.Correction_Flag = Correction_Flag

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Entity_ID(self):
        return self.Entity_ID

    @Entity_ID.setter
    def Entity_ID(self, value):
        self._Entity_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Entity_Type(self):
        return self.Entity_Type

    @Entity_Type.setter
    def Entity_Type(self, value):
        self._Entity_Type = value

    @property
    def Phase_ID(self):
        return self.Phase_ID

    @Phase_ID.setter
    def Phase_ID(self, value):
        self._Phase_ID = value

    @property
    def Status(self):
        return self.Status

    @Status.setter
    def Status(self, value):
        self._Status = value

    @property
    def Reason_code(self):
        return self.Reason_code

    @Reason_code.setter
    def Reason_code(self, value):
        self._Reason_code = value

    @property
    def Reference_value(self):
        return self.Reference_value

    @Reference_value.setter
    def Reference_value(self, value):
        self._Reference_value = value

    @property
    def Boundary_crossed(self):
        return self.Boundary_crossed

    @Boundary_crossed.setter
    def Boundary_crossed(self, value):
        self._Boundary_crossed = value

    @property
    def Value_violating_the_boundary(self):
        return self.Value_violating_the_boundary

    @Value_violating_the_boundary.setter
    def Value_violating_the_boundary(self, value):
        self._Value_violating_the_boundary = value

    @property
    def Correction_Flag(self):
        return self.Correction_Flag

    @Correction_Flag.setter
    def Correction_Flag(self, value):
        self._Correction_Flag = value


# Specifies an instrument's price (e.g. Projected Price, Closing Price). In case of an auction price, volume
# will hold the relevant auction volume:
# • Projected Price and Volume
# During the Pre-Opening or Additional Pre-Opening (after a temporary trade suspension) phases, and
# during the Pre-Closing Auction, for every change in theoretical price or volume of an instrument.
# 18
# • Opening Price and Volume
# At the end of the Opening auction, or at the end of an Additional Opening auction after a halt.
# • Closing Auction Price and Volume
# At the end of the Closing auction
# • Closing Price
# After the calculation of the closing price.
# • For Treasury Bills and "Shachar" Government Bonds, yield will be calculated but not for projected
# prices.
# EntityValue messages will also be sent in case prices were changed retroactively, e.g. manually by an
# operator or by cancelling or renewing trades.
# • In case of a retroactive change in Rezef, five consecutive EntityValue messages will be sent, for the
# following five price types: Opening, Halt Resume, Last Sale, Closing Auction and End. In Maof, two
# messages will be sent, for Last Sale and End.
# • Those of them with empty prices (either because the price was not yet set during this trading day, or
# in case the price type is deleted – e.g. all the trades were canceled so the Last Sale price is now
# empty) will appear first, in the above order.
# • Those with existing prices will appear next, in the order they were originally published (e.g., if there
# was a halt resume auction and there were no trades afterwards, then the Last Sale price would
# precede the Halt Resume price).
# • For example, if the security is now in the continuous phase, there was no halt resume auction yet,
# and all trades were canceled, the EntityValue messages that will be sent are: Empty Halt Resume
# price; Empty Last Sale price; Empty Closing Auction price; Empty End price; Filled Opening price.
# • The Correction flag field in the EntityValue messages will contain Y for the all but the last messages
# and L for the last one.
# • If the security is currently in a phase that requires publishing projected price, then after the five
# EntityValue messages there will be another EntityValue with Projected price. In this case the Entity
# value with the Projected price will be the one with the Correction flag field set to L.
# • In case a retroactive change is done in an instrument's base price, it will not be disseminated in an
# EntityValue message, but rather in a Rezef/Maof Instrument Reference Data message. If the security
# is currently in a phase that requires publishing projected price, then an EntityValue with projected
# price will be sent too, with the correction flag field set to L.
class MessageV:
    def __init__(self, Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type, Value_Type, Value_Of_Entity,
                 Volume, Yield_t, correction_flag):
        self.Market_ID = Market_ID
        self.Entity_ID = Entity_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Entity_Type = Entity_Type
        self.Value_Type = Value_Type
        self.Value_Of_Entity = Value_Of_Entity
        self.Volume = Volume
        self.Yield_t = Yield_t
        self.correction_flag = correction_flag

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Entity_ID(self):
        return self.Entity_ID

    @Entity_ID.setter
    def Entity_ID(self, value):
        self._Entity_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Entity_Type(self):
        return self.Entity_Type

    @Entity_Type.setter
    def Entity_Type(self, value):
        self._Entity_Type = value

    @property
    def Value_Type(self):
        return self.Value_Type

    @Value_Type.setter
    def Value_Type(self, value):
        self._Value_Type = value

    @property
    def Value_Of_Entity(self):
        return self.Value_Of_Entity

    @Value_Of_Entity.setter
    def Value_Of_Entity(self, value):
        self._Value_Of_Entity = value

    @property
    def Volume(self):
        return self.Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value

    @property
    def Yield_t(self):
        return self.Yield_t

    @Yield_t.setter
    def Yield_t(self, value):
        self._Yield_t = value

    @property
    def correction_flag(self):
        return self.correction_flag

    @correction_flag.setter
    def correction_flag(self, value):
        self._correction_flag = value


# Reference data for TASE's markets.
# Published every morning before trading,
class MessageK:
    def __init__(self, Market_ID, RESERVED_1, RESERVED_2, RESERVED_3, Name, Local_Name):
        self.Market_ID = Market_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.RESERVED_3 = RESERVED_3
        self.Name = Name
        self.Local_Name = Local_Name

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def RESERVED_3(self):
        return self.RESERVED_3

    @RESERVED_3.setter
    def RESERVED_3(self, value):
        self._RESERVED_3 = value

    @property
    def Name(self):
        return self.Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Local_Name(self):
        return self.Local_Name

    @Local_Name.setter
    def Local_Name(self, value):
        self._Local_Name = value


# Reference data for the underlying assets that are traded in TASE's derivatives' markets.
# Published every morning before trading, but may also be published during the day in case one or more
# parameters have been changed.
class MessageN:
    def __init__(self, Market_ID, Asset_ID, RESERVED_1, RESERVED_2, Asset_Original_ID, Name, Local_Name,
                 Asset_Base_Value, Asset_Type, Asset_Status, Reason_Code):
        self.Market_ID = Market_ID
        self.Asset_ID = Asset_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Asset_Original_ID = Asset_Original_ID
        self.Name = Name
        self.Local_Name = Local_Name
        self.Asset_Base_Value = Asset_Base_Value
        self.Asset_Type = Asset_Type
        self.Asset_Status = Asset_Status
        self.Reason_Code = Reason_Code

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Asset_ID(self):
        return self.Asset_ID

    @Asset_ID.setter
    def Asset_ID(self, value):
        self._Asset_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Asset_Original_ID(self):
        return self.Asset_Original_ID

    @Asset_Original_ID.setter
    def Asset_Original_ID(self, value):
        self._Asset_Original_ID = value

    @property
    def Name(self):
        return self.Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Local_Name(self):
        return self.Local_Name

    @Local_Name.setter
    def Local_Name(self, value):
        self._Local_Name = value

    @property
    def Asset_Base_Value(self):
        return self.Asset_Base_Value

    @Asset_Base_Value.setter
    def Asset_Base_Value(self, value):
        self._Asset_Base_Value = value

    @property
    def Asset_Type(self):
        return self.Asset_Type

    @Asset_Type.setter
    def Asset_Type(self, value):
        self._Asset_Type = value

    @property
    def Asset_Status(self):
        return self.Asset_Status

    @Asset_Status.setter
    def Asset_Status(self, value):
        self._Asset_Status = value

    @property
    def Reason_Code(self):
        return self.Reason_Code

    @Reason_Code.setter
    def Reason_Code(self, value):
        self._Reason_Code = value


# Published every morning before trading, but may also be published during the day in case one or more
# parameters have been changed.
class MessageM:
    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Segment_ID, English_Symbol, Local_Symbol,
                 English_Name, Local_Name, Sector, Sub_Sector, Instrument_Type, Instrument_Sub_Type,
                 Instrument_Tik_Group_ID, Issued_during_trading_day, Underlying_asset_ID, Underlying_asset_type,
                 Asset_original_entity_ID, ISIN_code, Minimum_order_size, Exceptional_order_size,
                 Floor_price_for_continuous_phase, Ceiling_price_for_continuous_phase, Base_price, Instrument_status,
                 Expiration_date, Strike_price, Volume_multiplication_factor, Calculate_turnover, Initialization_code,
                 Adjusted_option, Exact_expiration_date):
        self.Market_ID = Market_ID
        self.Instrument_ID = Instrument_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Segment_ID = Segment_ID
        self.English_Symbol = English_Symbol
        self.Local_Symbol = Local_Symbol
        self.English_Name = English_Name
        self.Local_Name = Local_Name
        self.Sector = Sector
        self.Sub_Sector = Sub_Sector
        self.Instrument_Type = Instrument_Type
        self.Instrument_Sub_Type = Instrument_Sub_Type
        self.Instrument_Tik_Group_ID = Instrument_Tik_Group_ID
        self.Issued_during_trading_day = Issued_during_trading_day
        self.Underlying_asset_ID = Underlying_asset_ID
        self.Underlying_asset_type = Underlying_asset_type
        self.Asset_original_entity_ID = Asset_original_entity_ID
        self.ISIN_code = ISIN_code
        self.Minimum_order_size = Minimum_order_size
        self.Exceptional_order_size = Exceptional_order_size
        self.Floor_price_for_continuous_phase = Floor_price_for_continuous_phase
        self.Ceiling_price_for_continuous_phase = Ceiling_price_for_continuous_phase
        self.Base_price = Base_price
        self.Instrument_status = Instrument_status
        self.Expiration_date = Expiration_date
        self.Strike_price = Strike_price
        self.Volume_multiplication_factor = Volume_multiplication_factor
        self.Calculate_turnover = Calculate_turnover
        self.Initialization_code = Initialization_code
        self.Adjusted_option = Adjusted_option
        self.Exact_expiration_date = Exact_expiration_date

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self._Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self._RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self._RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Segment_ID(self):
        return self._Segment_ID

    @Segment_ID.setter
    def Segment_ID(self, value):
        self._Segment_ID = value

    @property
    def English_Symbol(self):
        return self.English_Symbol

    @English_Symbol.setter
    def English_Symbol(self, value):
        self._English_Symbol = value

    @property
    def Local_Symbol(self):
        return self.Local_Symbol

    @Local_Symbol.setter
    def Local_Symbol(self, value):
        self._Local_Symbol = value

    @property
    def English_Name(self):
        return self.English_Name

    @English_Name.setter
    def English_Name(self, value):
        self._English_Name = value

    @property
    def Local_Name(self):
        return self.Local_Name

    @Local_Name.setter
    def Local_Name(self, value):
        self._Local_Name = value

    @property
    def Sector(self):
        return self.Sector

    @Sector.setter
    def Sector(self, value):
        self._Sector = value

    @property
    def Sub_Sector(self):
        return self.Sub_Sector

    @Sub_Sector.setter
    def Sub_Sector(self, value):
        self._Sub_Sector = value

    @property
    def Instrument_Type(self):
        return self.Instrument_Type

    @Instrument_Type.setter
    def Instrument_Type(self, value):
        self._Instrument_Type = value

    @property
    def Instrument_Sub_Type(self):
        return self.Instrument_Sub_Type

    @Instrument_Sub_Type.setter
    def Instrument_Sub_Type(self, value):
        self._Instrument_Sub_Type = value

    @property
    def Instrument_Tik_Group_ID(self):
        return self.Instrument_Tik_Group_ID

    @Instrument_Tik_Group_ID.setter
    def Instrument_Tik_Group_ID(self, value):
        self._Instrument_Tik_Group_ID = value

    @property
    def Issued_during_trading_day(self):
        return self.Issued_during_trading_day

    @Issued_during_trading_day.setter
    def Issued_during_trading_day(self, value):
        self._Issued_during_trading_day = value

    @property
    def Underlying_asset_ID(self):
        return self._Underlying_asset_ID

    @Underlying_asset_ID.setter
    def Underlying_asset_ID(self, value):
        self._Underlying_asset_ID = value

    @property
    def Underlying_asset_type(self):
        return self._Underlying_asset_type

    @Underlying_asset_type.setter
    def Underlying_asset_type(self, value):
        self._Underlying_asset_type = value

    @property
    def Asset_original_entity_ID(self):
        return self._Asset_original_entity_ID

    @Asset_original_entity_ID.setter
    def Asset_original_entity_ID(self, value):
        self._Asset_original_entity_ID = value

    @property
    def ISIN_code(self):
        return self._ISIN_code

    @ISIN_code.setter
    def ISIN_code(self, value):
        self._ISIN_code = value

    @property
    def Minimum_order_size(self):
        return self.Minimum_order_size

    @Minimum_order_size.setter
    def Minimum_order_size(self, value):
        self._Minimum_order_size = value

    @property
    def Exceptional_order_size(self):
        return self.Exceptional_order_size

    @Exceptional_order_size.setter
    def Exceptional_order_size(self, value):
        self._Exceptional_order_size = value

    @property
    def Floor_price_for_continuous_phase(self):
        return self.Floor_price_for_continuous_phase

    @Floor_price_for_continuous_phase.setter
    def Floor_price_for_continuous_phase(self, value):
        self._Floor_price_for_continuous_phase = value

    @property
    def Ceiling_price_for_continuous_phase(self):
        return self.Ceiling_price_for_continuous_phase

    @Ceiling_price_for_continuous_phase.setter
    def Ceiling_price_for_continuous_phase(self, value):
        self._Ceiling_price_for_continuous_phase = value

    @property
    def Base_price(self):
        return self.Base_price

    @Base_price.setter
    def Base_price(self, value):
        self._Base_price = value

    @property
    def Instrument_status(self):
        return self.Instrument_status

    @Instrument_status.setter
    def Instrument_status(self, value):
        self._Instrument_status = value

    @property
    def Expiration_date(self):
        return self.Expiration_date

    @Expiration_date.setter
    def Expiration_date(self, value):
        self._Expiration_date = value

    @property
    def Strike_price(self):
        return self.Strike_price

    @Strike_price.setter
    def Strike_price(self, value):
        self._Strike_price = value

    @property
    def Volume_multiplication_factor(self):
        return self.Volume_multiplication_factor

    @Volume_multiplication_factor.setter
    def Volume_multiplication_factor(self, value):
        self._Volume_multiplication_factor = value

    @property
    def Calculate_turnover(self):
        return self.Calculate_turnover

    @Calculate_turnover.setter
    def Calculate_turnover(self, value):
        self._Calculate_turnover = value

    @property
    def Initialization_code(self):
        return self.Initialization_code

    @Initialization_code.setter
    def Initialization_code(self, value):
        self._Initialization_code = value

    @property
    def Adjusted_option(self):
        return self.Adjusted_option

    @Adjusted_option.setter
    def Adjusted_option(self, value):
        self._Adjusted_option = value

    @property
    def Exact_expiration_date(self):
        return self.Exact_expiration_date

    @Exact_expiration_date.setter
    def Exact_expiration_date(self, value):
        self._Exact_expiration_date = value


# Published every morning before trading, but may also be published during the day in case one or more
# parameters have been changed.
class MessageR:
    def __init__(self, Market_ID, Instrument_ID, RESERVED_1, RESERVED_2, Segment_ID, English_Symbol, Local_Symbol,
                 English_Name, Local_Name, Sector, Sub_Sector, Instrument_Type, Instrument_Sub_Type,
                 Instrument_Tik_Group_ID, Currency_Code, Company_id, ISIN_code,
                 Pre_open_Minimum_order_size, Continuous_Minimum_order_size, Pre_close_Minimum_order_size,
                 Exceptional_order_size, Floor_price_for_pre_open_phase, Ceiling_price_for_pre_open_phase,
                 Floor_price_for_continuous_phase, Ceiling_price_for_continuous_phase, Base_price, Instrument_status,
                 Ex_code, Dual_registered_code, New_Instrument_Indicator, Market_Making_Indicator,
                 Maintenance_Or_low_liquidity_Indicator, Base_yield, Maturity_date, Accrued_interest,
                 Static_price_monitoring_boundary, Dynamic_price_monitoring_boundary, Initialization_code):
        self._Ceiling_price_for_pre_open_phase = Ceiling_price_for_pre_open_phase
        self.Market_ID = Market_ID
        self.Instrument_ID = Instrument_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Segment_ID = Segment_ID
        self.English_Symbol = English_Symbol
        self.Local_Symbol = Local_Symbol
        self.English_Name = English_Name
        self.Local_Name = Local_Name
        self.Sector = Sector
        self.Sub_Sector = Sub_Sector
        self.Instrument_Type = Instrument_Type
        self.Instrument_Sub_Type = Instrument_Sub_Type
        self.Instrument_Tik_Group_ID = Instrument_Tik_Group_ID
        self.Currency_Code = Currency_Code
        self.Company_id = Company_id
        self.ISIN_code = ISIN_code
        self.Pre_open_Minimum_order_size = Pre_open_Minimum_order_size
        self.Continuous_Minimum_order_size = Continuous_Minimum_order_size
        self.Pre_close_Minimum_order_size = Pre_close_Minimum_order_size
        self.Exceptional_order_size = Exceptional_order_size
        self.Floor_price_for_pre_open_phase = Floor_price_for_pre_open_phase
        self.Floor_price_for_continuous_phase = Floor_price_for_continuous_phase
        self.Ceiling_price_for_continuous_phase = Ceiling_price_for_continuous_phase
        self.Base_price = Base_price
        self.Instrument_status = Instrument_status
        self.Ex_code = Ex_code
        self.Dual_registered_code = Dual_registered_code
        self.New_Instrument_Indicator = New_Instrument_Indicator
        self.Market_Making_Indicator = Market_Making_Indicator
        self.Maintenance_Or_low_liquidity_Indicator = Maintenance_Or_low_liquidity_Indicator
        self.Base_yield = Base_yield
        self.Maturity_date = Maturity_date
        self.Accrued_interest = Accrued_interest
        self.Static_price_monitoring_boundary = Static_price_monitoring_boundary
        self.Dynamic_price_monitoring_boundary = Dynamic_price_monitoring_boundary
        self.Initialization_code = Initialization_code

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Instrument_ID(self):
        return self._Instrument_ID

    @Instrument_ID.setter
    def Instrument_ID(self, value):
        self._Instrument_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Segment_ID(self):
        return self.Segment_ID

    @Segment_ID.setter
    def Segment_ID(self, value):
        self._Segment_ID = value

    @property
    def English_Symbol(self):
        return self.English_Symbol

    @English_Symbol.setter
    def English_Symbol(self, value):
        self._English_Symbol = value

    @property
    def Local_Symbol(self):
        return self.Local_Symbol

    @Local_Symbol.setter
    def Local_Symbol(self, value):
        self._Local_Symbol = value

    @property
    def English_Name(self):
        return self.English_Name

    @English_Name.setter
    def English_Name(self, value):
        self._English_Name = value

    @property
    def Local_Name(self):
        return self.Local_Name

    @Local_Name.setter
    def Local_Name(self, value):
        self._Local_Name = value

    @property
    def Sector(self):
        return self.Sector

    @Sector.setter
    def Sector(self, value):
        self._Sector = value

    @property
    def Sub_Sector(self):
        return self.Sub_Sector

    @Sub_Sector.setter
    def Sub_Sector(self, value):
        self._Sub_Sector = value

    @property
    def Instrument_Type(self):
        return self.Instrument_Type

    @Instrument_Type.setter
    def Instrument_Type(self, value):
        self._Instrument_Type = value

    @property
    def Instrument_Sub_Type(self):
        return self.Instrument_Sub_Type

    @Instrument_Sub_Type.setter
    def Instrument_Sub_Type(self, value):
        self._Instrument_Sub_Type = value

    @property
    def Instrument_Tik_Group_ID(self):
        return self.Instrument_Tik_Group_ID

    @Instrument_Tik_Group_ID.setter
    def Instrument_Tik_Group_ID(self, value):
        self._Instrument_Tik_Group_ID = value

    @property
    def Issued_during_trading_day(self):
        return self.Issued_during_trading_day

    @Issued_during_trading_day.setter
    def Issued_during_trading_day(self, value):
        self._Issued_during_trading_day = value

    @property
    def Currency_Code(self):
        return self.Currency_Code

    @Currency_Code.setter
    def Currency_Code(self, value):
        self._Currency_Code = value

    @property
    def Company_id(self):
        return self.Company_id

    @Company_id.setter
    def Company_id(self, value):
        self._Company_id = value

    @property
    def ISIN_code(self):
        return self.ISIN_code

    @ISIN_code.setter
    def ISIN_code(self, value):
        self._ISIN_code = value

    @property
    def Pre_open_Minimum_order_size(self):
        return self.Pre_open_Minimum_order_size

    @Pre_open_Minimum_order_size.setter
    def Pre_open_Minimum_order_size(self, value):
        self._Pre_open_Minimum_order_size = value

    @property
    def Continuous_Minimum_order_size(self):
        return self.Continuous_Minimum_order_size

    @Continuous_Minimum_order_size.setter
    def Continuous_Minimum_order_size(self, value):
        self._Continuous_Minimum_order_size = value

    @property
    def Pre_close_Minimum_order_size(self):
        return self.Pre_close_Minimum_order_size

    @Pre_close_Minimum_order_size.setter
    def Pre_close_Minimum_order_size(self, value):
        self._Pre_close_Minimum_order_size = value

    @property
    def Exceptional_order_size(self):
        return self.Exceptional_order_size

    @Exceptional_order_size.setter
    def Exceptional_order_size(self, value):
        self._Exceptional_order_size = value

    @property
    def Floor_price_for_pre_open_phase(self):
        return self.Floor_price_for_pre_open_phase

    @Floor_price_for_pre_open_phase.setter
    def Floor_price_for_pre_open_phase(self, value):
        self._Floor_price_for_pre_open_phase = value

    @property
    def Ceiling_price_for_pre_open_phase(self):
        return self.Ceiling_price_for_pre_open_phase

    @Ceiling_price_for_pre_open_phase.setter
    def Ceiling_price_for_pre_open_phase_price(self, value):
        pass

    @property
    def Floor_price_for_continuous_phase(self):
        return self.Floor_price_for_continuous_phase

    @Floor_price_for_continuous_phase.setter
    def Floor_price_for_continuous_phase(self, value):
        self._Floor_price_for_continuous_phase = value

    @property
    def Ceiling_price_for_continuous_phase(self):
        return self.Ceiling_price_for_continuous_phase

    @Ceiling_price_for_continuous_phase.setter
    def Ceiling_price_for_continuous_phase(self, value):
        self._Ceiling_price_for_continuous_phase = value

    @property
    def Base_price(self):
        return self.Base_price

    @Base_price.setter
    def Base_price(self, value):
        self._Base_price = value

    @property
    def Instrument_status(self):
        return self.Instrument_status

    @Instrument_status.setter
    def Instrument_status(self, value):
        self._Instrument_status = value

    @property
    def Ex_code(self):
        return self.Ex_code

    @Ex_code.setter
    def Ex_code(self, value):
        self._Ex_code = value

    @property
    def Dual_registered_code(self):
        return self.Dual_registered_code

    @Dual_registered_code.setter
    def Dual_registered_code(self, value):
        self._Dual_registered_code = value

    @property
    def New_Instrument_Indicator(self):
        return self.New_Instrument_Indicator

    @New_Instrument_Indicator.setter
    def New_Instrument_Indicator(self, value):
        self._New_Instrument_Indicator = value

    @property
    def Market_Making_Indicator(self):
        return self.Market_Making_Indicator

    @Market_Making_Indicator.setter
    def Market_Making_Indicator(self, value):
        self._Market_Making_Indicator = value

    @property
    def Maintenance_Or_low_liquidity_Indicator(self):
        return self.Maintenance_Or_low_liquidity_Indicator

    @Maintenance_Or_low_liquidity_Indicator.setter
    def Maintenance_Or_low_liquidity_Indicator(self, value):
        self._Maintenance_Or_low_liquidity_Indicator = value

    @property
    def Base_yield(self):
        return self.Base_yield

    @Base_yield.setter
    def Base_yield(self, value):
        self._Base_yield = value

    @property
    def Maturity_date(self):
        return self.Maturity_date

    @Maturity_date.setter
    def Maturity_date(self, value):
        self._Maturity_date = value

    @property
    def Accrued_interest(self):
        return self.Accrued_interest

    @Accrued_interest.setter
    def Accrued_interest(self, value):
        self._Accrued_interest = value

    @property
    def Static_price_monitoring_boundary(self):
        return self.Static_price_monitoring_boundary

    @Static_price_monitoring_boundary.setter
    def Static_price_monitoring_boundary(self, value):
        self._Static_price_monitoring_boundary = value

    @property
    def Dynamic_price_monitoring_boundary(self):
        return self.Dynamic_price_monitoring_boundary

    @Dynamic_price_monitoring_boundary.setter
    def Dynamic_price_monitoring_boundary(self, value):
        self._Dynamic_price_monitoring_boundary = value

    @property
    def Initialization_code(self):
        return self.Initialization_code

    @Initialization_code.setter
    def Initialization_code(self, value):
        self._Initialization_code = value


# Each Tick Size message contains information about a tick size of a price range in a tick group within a
# market. A set of ‘L’ messages with the same Market ID and the same Tick group ID describe the complete
# tick size table for that combination of Market ID - Tick group ID. The reference data message for each
# instrument will refer to its Market ID and the Tick Group ID.
class MessageL:
    def __init__(self, Market_ID, Tick_group_ID, RESERVED_1, RESERVED_2, Range_Count, Range_Position,
                 Beginning_of_the_range, End_of_the_range, Tick_value_inside_range):
        self.Market_ID = Market_ID
        self.Tick_group_ID = Tick_group_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Range_Count = Range_Count
        self.Range_Position = Range_Position
        self.Beginning_of_the_range = Beginning_of_the_range
        self.End_of_the_range = End_of_the_range
        self.Tick_value_inside_range = Tick_value_inside_range

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Tick_group_ID(self):
        return self.Tick_group_ID

    @Tick_group_ID.setter
    def Tick_group_ID(self, value):
        self._Tick_group_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Range_Count(self):
        return self.Range_Count

    @Range_Count.setter
    def Range_Count(self, value):
        self._Range_Count = value

    @property
    def Range_Position(self):
        return self.Range_Position

    @Range_Position.setter
    def Range_Position(self, value):
        self._Range_Position = value

    @property
    def Beginning_of_the_range(self):
        return self.Beginning_of_the_range

    @Beginning_of_the_range.setter
    def Beginning_of_the_range(self, value):
        self._Beginning_of_the_range = value

    @property
    def End_of_the_range(self):
        return self.End_of_the_range

    @End_of_the_range.setter
    def End_of_the_range(self, value):
        self._End_of_the_range = value

    @property
    def Tick_value_inside_range(self):
        return self.Tick_value_inside_range

    @Tick_value_inside_range.setter
    def Tick_value_inside_range(self, value):
        self._Tick_value_inside_range = value


# Will be used rarely, in case of Sent when an order book should be cleared.
# a) If market is empty – this is for all Order Books in that feed.
# b) If Market ID field is not empty, and Entity ID field is empty – this is for all instruments traded in this
# market.
# c) If Market ID field and Entity ID field are not empty, this is for the entity's instrument[s] according to the
# value in the Entity Type field: a single instrument, or all underlying asset's instruments (e.g.
# derivatives on TEVA stock)
class MessageY:
    def __init__(self, Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type):
        self.Market_ID = Market_ID
        self.Entity_ID = Entity_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Entity_Type = Entity_Type

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Entity_ID(self):
        return self.Entity_ID

    @Entity_ID.setter
    def Entity_ID(self, value):
        self._Entity_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Entity_Type(self):
        return self.Entity_Type

    @Entity_Type.setter
    def Entity_Type(self, value):
        self._Entity_Type = value


# This message may be sent on the incremental stream in case of Disaster Recovery scenario, indicating
# that all recovered order book has been transmitted and the system is back to continuous trading.
class MessageG:
    def __init__(self, Market_ID, Entity_ID, RESERVED_1, RESERVED_2, Entity_Type):
        self.Market_ID = Market_ID
        self.Entity_ID = Entity_ID
        self.RESERVED_1 = RESERVED_1
        self.RESERVED_2 = RESERVED_2
        self.Entity_Type = Entity_Type

    @property
    def Market_ID(self):
        return self._Market_ID

    @Market_ID.setter
    def Market_ID(self, value):
        self._Market_ID = value

    @property
    def Entity_ID(self):
        return self.Entity_ID

    @Entity_ID.setter
    def Entity_ID(self, value):
        self._Entity_ID = value

    @property
    def RESERVED_1(self):
        return self.RESERVED_1

    @RESERVED_1.setter
    def RESERVED_1(self, value):
        self._RESERVED_1 = value

    @property
    def RESERVED_2(self):
        return self.RESERVED_2

    @RESERVED_2.setter
    def RESERVED_2(self, value):
        self._RESERVED_2 = value

    @property
    def Entity_Type(self):
        return self.Entity_Type

    @Entity_Type.setter
    def Entity_Type(self, value):
        self._Entity_Type = value
