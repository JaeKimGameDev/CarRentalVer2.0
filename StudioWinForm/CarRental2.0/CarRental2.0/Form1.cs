using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Runtime.Remoting.Contexts;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;


namespace CarRental2._0
{
    public partial class EmployeeLogin : Form
    {
        private MySqlConnection connection;
        private string connectionString = "Server=localhost;Database=carrentaldatabase;Uid=root;Pwd=THk]Qz2>]46-j]H;";
        
        public EmployeeLogin()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void Exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            try
            {
                connection = new MySqlConnection(connectionString);
                connection.Open();

                if (connection.State == ConnectionState.Open)
                {
                    string query = "SELECT * FROM Employees where EmployeeID = '" + EmployeeIDBox.Text + "' AND Password = '" + EmployeePasswordBox.Text + "'";
                    MySqlCommand cmd = new MySqlCommand(query, connection);
                    MySqlDataReader dataReader = cmd.ExecuteReader();
                }
                ////Create Command
                //MySqlCommand cmd = new MySqlCommand(query, connection);
                ////Create a data reader and Execute the command
                //MySqlDataReader dataReader = cmd.ExecuteReader();

                ////Read the data and store them in the list
                //while (dataReader.Read())
                //{
                //    list[0].Add(dataReader["id"] + "");
                //    list[1].Add(dataReader["name"] + "");
                //    list[2].Add(dataReader["age"] + "");
                //}

                //MySqlCommand cmd = new MySqlCommand();
                //cmd.CommandText = "Select * from employee where EmployeeID=@user and Password=@pass";
                //cmd.Parameters.AddWithValue("@user", EmployeeIDBox);
                //cmd.Parameters.AddWithValue("@pass", EmployeePasswordBox);
                //cmd.Connection = connect;
                //Debug.Print("something1");
                //MySqlDataReader login = cmd.ExecuteReader();

            }
            catch (MySqlException)
            {
                throw;
            }
        }
    }
}
