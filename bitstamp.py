import json
import ssl

import websocket

def comprar():
    pass


def vender():
    pass


def ao_abrir(ws):
    print('Abriu a conecção')
    json_subscribe = '''
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_[btcusd]"
    }
}
'''
    ws.send(json_subscribe)


def ao_fechar(ws):
    print('Fechou a conecção')


def erro(ws, erro):
    print('Deu erro:{}'.format(erro))


def ao_receber_menssaem(ws, menssagem):
    menssagem = json.load(menssagem)
    price = menssagem['data']['price']
    print(price)

    if price > 9000:
        vender()
    elif price < 8000:
        comprar()
    else:
        print('Aguardar')


if __name__ == '__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_menssaem,
                                on_error=erro)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})