from flask import Flask, render_template, request
from serial.tools import list_ports
import pydobot

#Lists the available ports
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

port = "COM7"

#Connection error control test
try:
    device = pydobot.Dobot(port=port, verbose=True)
except OSError as e:
    print("[ERRO] A porta selecionada não respondeu -->", e)
    exit()

presetArray = [[225.76258850097656, 0.0, 150.50729370117188], [215.70765686035156, -91.61711120605469, 151.1934356689453], [144.9072723388672, -184.18841552734375, 151.3003387451172], [55.55394744873047, -227.6288604736328, 151.4481964111328], [-11.707974433898926, -234.06497192382812, 151.3929901123047], [-13.78620433807373, -275.1808166503906, 87.1156234741211], [-14.243218421936035, -285.3124084472656, 38.00505065917969], [-17.99175453186035, -288.7402648925781, -38.55540466308594], [-17.99175453186035, -288.7402648925781, -38.55540466308594], [-14.115690231323242, -226.24984741210938, -45.617515563964844], [-10.29824161529541, -206.28878784179688, -41.667938232421875], [56.535072326660156, -198.74525451660156, -41.643436431884766], [60.988826751708984, -224.83328247070312, -47.77442169189453], [54.7111701965332, -267.3271179199219, -47.004398345947266], [92.509521484375, -284.2472229003906, -46.200721740722656], [113.86739349365234, -241.50514221191406, -45.372886657714844], [127.7650146484375, -175.3705596923828, -53.09781265258789], [177.94131469726562, -170.82774353027344, -48.440208435058594], [175.59222412109375, -223.0862579345703, -50.22549819946289], [171.24110412597656, -277.301513671875, -50.563045501708984], [211.328369140625, -275.4686584472656, -49.235008239746094], [221.4658203125, -235.23825073242188, -52.88153839111328], [224.4705810546875, -180.5019073486328, -56.93218994140625], [225.1380157470703, -190.57508850097656, -11.468500137329102], [230.5420684814453, -154.20941162109375, 12.92957592010498], [232.4996795654297, -81.67562866210938, 15.019186019897461], [220.54783630371094, 2.9042861461639404, 9.621973037719727], [220.54783630371094, 2.9042861461639404, 9.621973037719727], [274.6875305175781, 10.439388275146484, -50.12482452392578], [348.1271667480469, 13.298884391784668, -52.977237701416016], [295.6872253417969, 3.824066638946533, -48.3410530090332], [217.66415405273438, 0.0767543762922287, -40.765628814697266], [217.66415405273438, 0.0767543762922287, -40.765628814697266], [358.6139831542969, 9.11790943145752, -34.702205657958984], [294.0994567871094, 0.10370756685733795, 18.736251831054688], [268.3634948730469, 91.30065155029297, 47.43052291870117], [233.68569946289062, 203.8674774169922, 39.63060760498047], [231.02755737304688, 252.6437530517578, -28.5361270904541], [200.9203338623047, 284.62713623046875, -52.58450698852539], [139.7712860107422, 279.5975341796875, -55.640262603759766], [25.273664474487305, 288.81884765625, -59.69245529174805], [147.15626525878906, 268.1078186035156, -50.81307601928711], [226.30406188964844, 212.55235290527344, 14.704792022705078], [265.3917236328125, 120.90518188476562, 76.98482513427734], [279.8749694824219, 17.52342987060547, 116.24952697753906], [225.76258850097656, 0.0, 150.50729370117188]]

app = Flask(__name__)



print("flaskei")

@app.route("/robot" , methods=["GET", "POST"])
def robot():
    if request.method == "POST":
       for i in presetArray:
        device.move_to(i[0], i[1], i[2], 0, wait=True)
        print(request.form)
    return "Hello World"

@app.route("/robot/getroutes", methods=["GET"])
def getroutes():
    print("Pegando rotas...")
    # function to get routes from database, if i had imported the database module
    return "rotasfodinasss"

@app.get("/magnet_on")
def magnet_on():
    import serial
    import time
    try:
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM5", taxa_transmissao, timeout = tempo_espera)
        comunicacao_serial.write(b"on\n") # Escreve "on" na serial
        time.sleep(1)
        return "on"
    except Exception as e:
        return str(e)
    
@app.get("/magnet_off")
def magnet_off():
    import serial
    import time
    try:
        tempo_espera = 2
        taxa_transmissao = 115200
        comunicacao_serial = serial.Serial("COM5", taxa_transmissao, timeout = tempo_espera)
        comunicacao_serial.write(b"off\n") # Escreve "on" na serial
        time.sleep(1)
        return "off"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host='localhost', port=5000)

