namespace CarRental2._0
{
    partial class EmployeeLogin
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.EmployeeID = new System.Windows.Forms.Label();
            this.Password = new System.Windows.Forms.Label();
            this.EmployeeIDBox = new System.Windows.Forms.TextBox();
            this.EmployeePasswordBox = new System.Windows.Forms.TextBox();
            this.Exit = new System.Windows.Forms.Button();
            this.LoginButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // EmployeeID
            // 
            this.EmployeeID.AutoSize = true;
            this.EmployeeID.Location = new System.Drawing.Point(44, 52);
            this.EmployeeID.Name = "EmployeeID";
            this.EmployeeID.Size = new System.Drawing.Size(183, 32);
            this.EmployeeID.TabIndex = 0;
            this.EmployeeID.Text = "Employee ID:";
            // 
            // Password
            // 
            this.Password.AutoSize = true;
            this.Password.Location = new System.Drawing.Point(81, 120);
            this.Password.Name = "Password";
            this.Password.Size = new System.Drawing.Size(146, 32);
            this.Password.TabIndex = 1;
            this.Password.Text = "Password:";
            // 
            // EmployeeIDBox
            // 
            this.EmployeeIDBox.Location = new System.Drawing.Point(250, 46);
            this.EmployeeIDBox.Name = "EmployeeIDBox";
            this.EmployeeIDBox.Size = new System.Drawing.Size(338, 38);
            this.EmployeeIDBox.TabIndex = 2;
            // 
            // EmployeePasswordBox
            // 
            this.EmployeePasswordBox.Location = new System.Drawing.Point(250, 114);
            this.EmployeePasswordBox.Name = "EmployeePasswordBox";
            this.EmployeePasswordBox.Size = new System.Drawing.Size(338, 38);
            this.EmployeePasswordBox.TabIndex = 3;
            // 
            // Exit
            // 
            this.Exit.Location = new System.Drawing.Point(613, 185);
            this.Exit.Name = "Exit";
            this.Exit.Size = new System.Drawing.Size(169, 68);
            this.Exit.TabIndex = 5;
            this.Exit.Text = "Exit";
            this.Exit.UseVisualStyleBackColor = true;
            this.Exit.Click += new System.EventHandler(this.Exit_Click);
            // 
            // LoginButton
            // 
            this.LoginButton.Location = new System.Drawing.Point(419, 185);
            this.LoginButton.Name = "LoginButton";
            this.LoginButton.Size = new System.Drawing.Size(169, 68);
            this.LoginButton.TabIndex = 6;
            this.LoginButton.Text = "Login";
            this.LoginButton.UseVisualStyleBackColor = true;
            this.LoginButton.Click += new System.EventHandler(this.LoginButton_Click);
            // 
            // EmployeeLogin
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(16F, 31F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(818, 277);
            this.Controls.Add(this.LoginButton);
            this.Controls.Add(this.Exit);
            this.Controls.Add(this.EmployeePasswordBox);
            this.Controls.Add(this.EmployeeIDBox);
            this.Controls.Add(this.Password);
            this.Controls.Add(this.EmployeeID);
            this.Name = "EmployeeLogin";
            this.Text = "Employee Login";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label EmployeeID;
        private System.Windows.Forms.Label Password;
        private System.Windows.Forms.TextBox EmployeeIDBox;
        private System.Windows.Forms.TextBox EmployeePasswordBox;
        private System.Windows.Forms.Button Exit;
        private System.Windows.Forms.Button LoginButton;
    }
}