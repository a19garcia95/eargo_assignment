
CREATE TABLE IF NOT EXISTS `Output_table` (
  `Page` varchar(20) NOT NULL,
  `Counts` int(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`Page`)
) DEFAULT CHARSET=utf8;
/* Creating the table with two columns, Page and Counts
Page type is varchar and Counts type is int */
INSERT INTO Output_table (Page,Counts)  /* Inserting data of Home_Page */
  SELECT 'Home_Page',sum(Home_Page) from input_table;
INSERT INTO Output_table (Page,Counts) /* Inserting data of Product_Page */
  SELECT 'Product_Page',sum(Product_Page) from input_table;
INSERT INTO Output_table (Page,Counts) /* Inserting data of Warranty_Page */
  SELECT 'Warranty_Page',sum(Warranty_Page) from input_table;


/* 

Approach: At first I have created the Output_table with two column Page and Counts. 
Page type is varchar and Counts type is int. 
Then I have used INSERT INTO to insert individual row of data with page name and sum function to calculate the sum of that column.

Complexity: The time complexity of the program is O(n) where n is the number of columns.


*/