import plotly.graph_objs as go  # objetos de imagenes para funcion principal
import plotly.io as pio  # renderizador para visualizar imagenes
import numpy as np  # funciones numericas

pio.renderers.default = "notebook"  # render de imagenes para correr en script


def g_velas(p0_de):
    """
    :param p0_de: data frame con datos a graficar
    :return fig:

    p0_de = datos_dd
    p1_pa = 'sell'
    datos_dd = pd.DataFrame({'timestamp': [], 'open': [], 'high': [], 'low': [], 'close': []}, index=[])
    """
    p0_de.columns = [list(p0_de.columns)[i].lower() for i in range(0, len(p0_de.columns))]

    # Calculo de media y desviacion estandar con rolling
    mean = p0_de['close'].rolling(window=20).mean()
    std = p0_de['close'].rolling(window=20).std()
    # Agregar al DataFrame datos de bandas
    p0_de['Mean'] = mean
    p0_de['Upper'] = mean + (std * 2)
    p0_de['Lower'] = mean - (std * 2)

    fig = go.Figure(data=[go.Candlestick(x=p0_de['timestamp'],
                                       open=p0_de['open'], high=p0_de['high'],
                                       low=p0_de['low'], close=p0_de['close'])])

    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['Mean'], name='mean',
                             line=dict(color='black', width=1.5)))

    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['Upper'], name='Upper band',
                             line=dict(color='dodgerblue', width=1)))

    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['Lower'], name='Lower band',
                             line=dict(color='deepskyblue', width=1)))

    fig.update_layout(margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=0),
                      title=dict(x=0.5, y=1, text='Precios Historicos OHLC'),
                      xaxis=dict(title_text='Hora del dia', rangeslider=dict(visible=False)),
                      yaxis=dict(title_text='Precio'))

    fig.layout.autosize = False
    fig.layout.width = 940
    fig.layout.height = 520
    return fig.show()
