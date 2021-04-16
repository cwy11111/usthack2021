# Food Ordering Helper
## hackUST2021
## Team: whyou888
 

**Introduction**
<br>This project is mainly for small restaurants like Cha Chaan Teng in Hong Kong. They can install this *portable,light text-line interface program* on their computer and use it to help with ordering.
  
**How to Use**
1. Make a `.csv` file as to store all the information about all dishes in your restaurant. Store the `.csv` file into the folder *`data`*. Please follow the format as shown in the `example.csv` under *`data`* folder. You can simply change the content below **Row 1** of `example.csv`. You can also keep the `example.csv` and use it in the application as demonstration. (Remember to store the `.csv` file in UTF-8 encoding.) <br><br>
2. Open `main.exe` to start using the application.<br><br>
3. Type in the filename of your `.csv` file storing in *`data`* folder.<br><br>
4. The whole menu in `.csv` data file will be shown on the screen.<br><br>
5. Try the program with different functions as shown in the text line interface.<br><br>

**Main Function**
- **`Make order`**: **Make order** of food by inputting the **`dish ID`** of food. 

- **`Food aviliable today`**: Show all the food can be provided today from the `.csv` data file with their **`dish ID`**.<br>
- **`Queue`**: **Rearrange** the order of all dishes stored in the **`unserved list`** to enhance the efficiency of serving. It works by grouping the similar unserved dishes together with criteria, including **cooking method** and **ingredients**.<br>
- **`Show unserved dish`**: Show all the dish(es) on the **`unserved list`** with their `ordering time`.<br>
- **`Update unserved dish`**: Manually **delete** those served dish(es).<br>
- **`Order history`**: Show the record of all the ordered dish(es) in the **`ordered history list`** since the program started. 
- **`Quit`**: **Exit** the application.
