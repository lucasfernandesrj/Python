from math import pow,sqrt, sin, atan, hypot
co=float(input("cateto oposto: "))
ca=float(input("cateto adjacente: "))
print("A hipotenusa é {:.2f}.".format((co**2 +ca**2)**(1/2)))
print("A hipotenusa é {:.3f}.".format(co / sin(atan(co /ca))))
print("A hipotenusa é {:.4f"
      "}.".format(hypot(co, ca))) # (x, y) = sqrt(x*x + y*y)
