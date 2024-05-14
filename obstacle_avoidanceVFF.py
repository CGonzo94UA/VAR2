from GUI import GUI
from HAL import HAL
import math
# Enter sequential code!

def check_target(currentTarget, posx, posy, targetx, targety):
    if(abs(targetx - posx) <= 6 and abs(targety - posy) <= 6):
        currentTarget.setReached(True)
        currentTarget = GUI.map.getNextTarget()
        print("Target Reached")
        if(currentTarget != None):
            return 1
        else:
            return 0

index = 0
while True:
    # Enter iterative code!
    currentTarget = GUI.map.getNextTarget()
    targetx = currentTarget.getPose().x
    targety = currentTarget.getPose().y
    posx = HAL.getPose3d().x
    posy = HAL.getPose3d().y
    targetid = currentTarget.getId()
    imagen = HAL.getImage()
    GUI.showImage(image)

    k_obstacle = 0.6
    k_car = 0.2
    k_target = -0.2

    target_vector = [targetx - posx, targety - posy]
    rot_angle = (-1) * (HAL.getPose3d().yaw + math.pi/2)
    target_vector = [target_vector[0] * math.cos(rot_angle) - target_vector[1] * math.sin(rot_angle), target_vector[0] * math.sin(rot_angle) + target_vector[1] * math.cos(rot_angle)]
    target_marker = [target_vector[0], target_vector[1]]

    target_vector[0] = k_target * target_vector[0]
    target_vector[1] = k_target * target_vector[1]

    obstacle_vector = [0, 0]
    angle = 180

    laser_data = HAL.getLaserData()

    for r in laser_data.values:
        if angle > 45 and angle < 135:
            obstacle_vector[0] += k_obstacle * (100/(r ** 2)) *  math.cos(math.radians(angle))
        else:			
            obstacle_vector[0] += k_obstacle * (10/(r ** 2)) *  math.cos(math.radians(angle))		
        angle -= 1

    if(abs(obstacle_vector[0]) > 20):
        obstacle_vector[0] = 20 *(abs(obstacle_vector[0])/obstacle_vector[0])
    
    car_vector = [0, 0]

    running = check_target(currentTarget, posx, posy, targetx, targety)
    if(running == 0):
        v_speed = 0
        w_speed = 0
        HAL.setV(v_speed)
        HAL.setW(w_speed)
        
    car_vector[0] = k_car * (target_vector[0] + obstacle_vector[0])
    car_vector[1] = k_car * (target_vector[1] + obstacle_vector[1])

    v_speed = 5
    HAL.setV(speed)
    #Add PID to angle actual - where it should be headed times a constant
    k_angle = -0.3
    w_speed = k_angle * (car_vector[0])
    HAL.setW(w_speed)

    # Car direction <GREEN>
    carx = -1 * car_vector[0]
    cary = car_vector[1]
    green = [carx, cary]

    # Obstacles direction <RED>
    obsx = -1 * obstacle_vector[0]
    obsy = obstacle_vector[1]
    red = [obsx, obsy]

    # Target Vector <BLACK>
    avgx = -1 * target_vector[0]
    avgy = target_vector[1]
    black = [avgx, avgy]
    
    GUI.showForces(green, red, black)

    # Target
    GUI.showLocalTarget(target_marker)

    # Save the image, the lidar data, the W value and the V value
    filename = str(index)+"_.npy"
    np.save("data/imgs/"+filename, image) #save image
    # Concatenate the lidar data with the V and W values
    lasers = np.concatenate((laser_data.values, np.array([v_speed, w_speed])))
    np.save("data/lasers/"+filename, lasers) # save lasers
    index += 1