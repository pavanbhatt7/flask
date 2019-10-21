from flask import Flask
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity


aisles = pd.read_csv('aisles.csv')
departments = pd.read_csv('departments.csv')
order_products_prior = pd.read_csv('order_products__prior.csv')
order_products_train = pd.read_csv('order_products__train.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
df = pd.read_csv('orders_products_departments_aisles.csv')
order_products_total=pd.read_csv('order_products_total.csv')



app = Flask(__name__)
IMAGE_FOLDER = os.path.join('static','graph')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# merge order_products_total with products to get product names
order_products_total = order_products_total.drop('add_to_cart_order', axis = 1)
order_products_total = order_products_total.merge(products[['product_id', 'product_name']],how='left', on='product_id')
def recommend():
    reorders = order_products_total[order_products_total['reordered'] == 1]
    orders2 = orders[['order_id', 'user_id']]
    user_orders = reorders.merge(orders2, on='order_id')
    user_orders['high_volume'] = (user_orders['product_id'].value_counts().sort_values(ascending=False)>1)
    high_volume = user_orders[user_orders['high_volume'] == True]
    high_volume_users = high_volume.groupby(['user_id', 'product_name']).size().sort_values(ascending=False).unstack().fillna(0)
    cosine_dists = pd.DataFrame(cosine_similarity(high_volume_users),index=high_volume_users.index, columns=high_volume_users.index)
    


    def Recommender_System(user_id):
    
   
        p = high_volume.groupby(['product_name','user_id']).size().sort_values(ascending=False).unstack().fillna(0)
    
    
        recommendations = pd.Series(np.dot(p.values,cosine_dists[user_id]), index=p.index)
        return recommendations.sort_values(ascending=False).head()
    return Recommender_System(175965)
    


 


def graph1():
    orders_amount_for_customer = orders.groupby('user_id')['order_number'].count().value_counts()
    plt.figure(figsize=(20,8))
    sns.barplot(x=orders_amount_for_customer.index, y=orders_amount_for_customer.values, color='mediumseagreen')
    plt.title('Amount of Orders Distribution', fontsize=16)
    plt.ylabel('Number of Customers', fontsize=16)
    plt.xlabel('Amount of Orders', fontsize=16)
    plt.xticks(rotation='vertical');
   
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Amount_of_Orders_Distribution.png')
    return filename

def graph2():
    plt.figure(figsize=(12,8))
    sns.countplot(x=orders.order_dow, color='mediumseagreen')

    plt.title("Order Amounts by Days", fontsize=16)
    plt.xlabel('', fontsize=16)
    plt.xticks(fontsize=15)
    plt.ylabel('Order Counts', fontsize=16)
    plt.yticks(fontsize=15)
        
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Order_Amounts_by_Days.png')
    return filename

def graph3():
    plt.figure(figsize=(12,8))
    sns.countplot(x=orders.order_hour_of_day, color='mediumseagreen')

    plt.title("Order Amounts by Hours", fontsize=16)
    plt.xlabel('Hour of Day', fontsize=16)
    plt.xticks(fontsize=15)
    plt.ylabel('Order Counts', fontsize=16)
    plt.yticks(fontsize=15)
     
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Order_Amounts_by_Hour.png')
    return filename

def graph4():
    plt.figure(figsize=(12,8))
    sns.countplot(x=orders.days_since_prior_order, color= 'mediumseagreen')

    plt.title("Number of Orders per Days Since Last Purchase", fontsize=16)
    plt.xlabel('Days Since Last Purchase', fontsize=16)
    plt.xticks(np.arange(31), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                              24, 25, 26, 27, 28, 29, 30],  fontsize=15)
    plt.xticks(rotation='vertical')
    plt.ylabel('Order Counts', fontsize=16)
    plt.yticks(fontsize=15)
     
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Number of Orders per Days Since Last Purchase.png')
    return filename

  

def graph5():
    frequency_per_number_of_order = order_products_total.groupby('order_id')['product_id'].count().value_counts()
    plt.figure(figsize=(20,8))
    sns.barplot(x=frequency_per_number_of_order.index, y=frequency_per_number_of_order.values, color='mediumseagreen')
    plt.title('Amount of Items Per Order', fontsize=16)
    plt.ylabel('Order Counts', fontsize=16)
    plt.xlabel('Number of Items', fontsize=16)
    plt.xticks(rotation='vertical');
    
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Amount of Items Per Order.png')
    return filename



    
df.groupby('department')

reorder_ratio_per_dep = df.groupby('department')['reordered'].mean().reset_index()
reorder_ratio_per_dep.columns = ['department', 'reorder_ratio']
reorder_ratio_per_dep.sort_values(by='reorder_ratio', ascending=False)

def graph6():
    plt.figure(figsize=(12,8))
    sns.barplot(x=reorder_ratio_per_dep.department, y=reorder_ratio_per_dep.reorder_ratio, color='mediumseagreen')
    plt.title('Reorder Ratio Per Department', fontsize=16)
    plt.xlabel('Department', fontsize=16)
    plt.xticks(fontsize=15)
    plt.xticks(rotation='vertical')
    plt.ylabel('Reorder Ratio', fontsize=16)
    plt.yticks(fontsize=15)
   
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Reorder Ratio Per Department.png')
    return filename

reorder_ratio_per_aisle = df.groupby('aisle')['reordered'].mean().reset_index()
reorder_ratio_per_aisle.columns = ['aisle', 'reorder_ratio']

add_to_cart_order_reordered_ratio = df.groupby('add_to_cart_order')['reordered'].mean().reset_index()
add_to_cart_order_reordered_ratio.head()

def graph7():
    plt.figure(figsize=(25,8))
    sns.pointplot(add_to_cart_order_reordered_ratio.add_to_cart_order, add_to_cart_order_reordered_ratio.reordered, color='mediumseagreen')
    plt.title('Add To Cart Order vs. Reorder Ratio', fontsize=16)
    plt.xlabel('Add To Cart Order', fontsize=16)
    plt.xticks(fontsize=15)
    plt.xticks(rotation='vertical')
    plt.ylabel('Reorder Ratio', fontsize=16)
    plt.yticks(fontsize=15);
    
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Add To Cart Order vs. Reorder Ratio.png')
    return filename

def graph8():
    productsCount = order_products_train["product_id"].value_counts().to_frame()
    productsCount["count"] = productsCount.product_id
    productsCount["product_id"] = productsCount.index
    mergedData = pd.merge(productsCount,products,how="left",on="product_id").sort_values(by="count",ascending=False)
    fig,ax = plt.subplots()
    fig.set_size_inches(25,10)
    sns.barplot(data=mergedData.head(30),x="product_name",y="count",ax=ax,orient="v",color="#34495e")
    ax.set(xlabel='Product Names',ylabel="Count",title="Best Selling Products")
    plt.xticks(rotation=90)
    
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Best Selling Products.png')
    return filename


productsCount = order_products_train["product_id"].value_counts().to_frame()    
productsCount["count"] = productsCount.product_id
productsCount["product_id"] = productsCount.index
def graph9():
    productsCountReordered = order_products_train[order_products_train["reordered"]==1]["product_id"].value_counts().to_frame()
    productsCountReordered["reordered_count"] = productsCountReordered.product_id
    productsCountReordered["product_id"] = productsCountReordered.index
    productCountReorderedMerged = pd.merge(productsCount,productsCountReordered,how="left",on="product_id").sort_values(by="count",ascending=False)
    productCountReorderedMerged["reordered_ratio"] = productCountReorderedMerged["reordered_count"]/productCountReorderedMerged["count"]
    productCountReorderedMerged.sort_values(by="reordered_ratio",ascending=False,inplace=True)
    productMerged = pd.merge(productCountReorderedMerged,products,how="left",on="product_id")
    fig,ax = plt.subplots()
    fig.set_size_inches(25,10)
    sns.barplot(data=productMerged[productMerged["count"]>40].head(30),x="product_name",y="reordered_ratio",color="#34495e",ax=ax,orient="v")
    ax.set(xlabel='Product Names',ylabel="Count",title="Top Reordered Products")
    ax.set_ylim(0.85,.95)
    plt.xticks(rotation=90)
     
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Top Reordered Products.png')
    return filename

products_details = pd.merge(left=products,right=departments,how="left")
products_details = pd.merge(left=products_details,right=aisles,how="left")

def graph10():
    plt.figure(figsize=(8,4))
    g=sns.countplot(x="department",data=products_details)
    g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
    
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Number of products in each department.png')
    return filename
order_products_train.groupby("add_to_cart_order")["reordered"].aggregate({'reordered_percnt': 'mean'}).sort_values(by="reordered_percnt",ascending= False).reset_index().head(20)
def graph11():
    order_products_name_train = pd.merge(left=order_products_train,right=products.loc[:,["product_id","product_name"]],on="product_id",how="left")
    common_Products=order_products_name_train[order_products_name_train.reordered == 1]["product_name"].value_counts().to_frame().reset_index()
    plt.figure(figsize=(16,10))
    plt.xticks(rotation=90)
    sns.barplot(x="product_name", y="index", data=common_Products.head(20))
    plt.ylabel('product_name', fontsize=12)
    plt.xlabel('count', fontsize=12) 
    
    filename=os.path.join(app.config['UPLOAD_FOLDER'], 'Most common buying choice.png')
    return filename


     