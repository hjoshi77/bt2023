# My first program in R Programming
# My first program in R Programming
if(FALSE) {
   "This is a demo for multi-line comments and it should be put inside either a 
      single OR double quote"
}

myString <- "Hello, World!"
print ( myString)

# VECTOR
#LOGICAL
v <- TRUE
print(class(v))
#Numerical 
v <- 23.5
print(class(v))
#Integer 
v <- 1L
print(class(v))

#Complex 
v <- 2+5i
print(class(v))

# Raw
v <- charToRaw("Hi")
print(class(v))
print( v)

#Character 
v <- "TRUE"
print(class(v))


### LIST

list1 <- list(c(2,5,3),21.3,sin)
print (list1)

# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = FALSE)
print(M)


