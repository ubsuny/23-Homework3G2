def elastic_collision(m1,m2,u1,u2):
    #m1 is the mass of object 1, m2 is the mass of object 2, u1 is the initial velocity of object 1 before collision, u2 is the initial velocity of object 2 before collision
    v1=(m1-m2)*u1/(m1+m2)+(2*m2*u2)/(m1+m2)
    v2=(m2-m1)*u2/(m1+m2)+(2*m1*u1)/(m1+m2)
    return(v1,v2)
#v1 is the final velocity of object 1 after collision, v2 is the final velocity of object 2 after collision

print(elastic_collision(2,1.5,3,-2))