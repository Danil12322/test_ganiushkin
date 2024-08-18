import matplotlib.pyplot as plt
from collections import defaultdict  
def read_sales_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data_sales = []
        for lines in file:
            data = lines.strip().split(', ')
            sale = {'product_name': data[0], 'quantity': int(data[1]), 'price': int(data[2]), 'date': data[3]}
            data_sales.append(sale)
    return data_sales        
def total_sales_per_product(sales_data):
    total_sales = defaultdict(int)
    for sale in sales_data:
        total_sales[sale['product_name']] += (sale['quantity'] * sale['price'])
    return total_sales  
def sales_over_time(sales_data):
    total_sales_per_date = defaultdict(int)
    for sale in sales_data:
        total_sales_per_date[sale['date']] += (sale['quantity'] * sale['price'])
    return total_sales_per_date
15
def main(): 
    file_path = r'C:/Users/danil/Desktop/learn project/test_data.txt'
    sales_data = read_sales_data(file_path) 
    total_sales_per_product_data = total_sales_per_product(sales_data)
    max_revenue_product = max(total_sales_per_product_data, key=total_sales_per_product_data.get)
    print("Продукт с наибольшей выручкой:", max_revenue_product.capitalize())
    sales_over_time_data = sales_over_time(sales_data)
    max_sales_date = max(sales_over_time_data, key=sales_over_time_data.get)
    print("День с наибольшей суммой продаж:", max_sales_date)
    plt.figure(1)
    plt.bar(total_sales_per_product_data.keys(), total_sales_per_product_data.values(), color = 'green', width = 0.15)
    plt.title('Общая сумма продаж по каждому продукту')
    plt.xlabel('Название продукта')
    plt.ylabel('Сумма продаж')
    plt.figure(2)
    plt.bar(sales_over_time_data.keys(), sales_over_time_data.values(), color = 'orange', width = 0.19)
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж')
    plt.show()






main()