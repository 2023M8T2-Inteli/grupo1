from socket_robot import Robot
import time




def main():
    robo_instancia = Robot()
    while True:
        robo_instancia.comunicacao()
        time.sleep(1)
        input_data = robo_instancia.requicoes()
        print("Vinda do ZAP: ",input_data)
        if input_data == "quit":
            break

    
       

if __name__ == "__main__":
    main()