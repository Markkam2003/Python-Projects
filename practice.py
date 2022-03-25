def my_function():
    print("Hello from a function")

my_function()

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

x = lambda a : a + 10
print(x(5))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

x = format(0.5, '%')
print(x)
