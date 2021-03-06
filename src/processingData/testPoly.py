# from pyspark import SparkContext
# from pyspark import SparkConf, SparkContext


# conf = SparkConf()
# conf.setMaster("local")
# conf.setAppName("My application")
# conf.set("spark.executor.memory", "1g")
# sc = SparkContext(conf = conf)


# Improved point in polygon test which includes edge
# and vertex points

def point_in_poly(x,y,poly):

   # check if point is a vertex
   if (x,y) in poly: return "IN"

   # check if point is on a boundary
   for i in range(len(poly)):
      p1 = None
      p2 = None
      if i==0:
         p1 = poly[1]
         p2 = poly[0]
      else:
         p1 = poly[i]
         p2 = poly[i-1]
      if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
         return "IN"
      
   n = len(poly)
   inside = False

   p1y,p1x = poly[0]
   for i in range(n+1):
      p2y,p2x = poly[i % n]
      if y > min(p1y,p2y):
         if y <= max(p1y,p2y):
            if x <= max(p1x,p2x):
               if p1y != p2y:
                  xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
               if p1x == p2x or x <= xints:
                  inside = not inside
      p1x,p1y = p2x,p2y

   if inside: return "IN"
   else: return "OUT"


if __name__ == "__main__":
	poligono = [(-33.416032,-70.593016), (-33.415370,-70.589604), (-33.417340,-70.589046), (-33.417949,-70.592351), (-33.416032,-70.593016)]
	lat= -33.416032
	lon= -70.593016

	print point_in_poly(lat, lon, poligono)




