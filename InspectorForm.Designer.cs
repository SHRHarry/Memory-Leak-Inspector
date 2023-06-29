namespace MemoryInspector
{
    partial class MainForm
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
            this.tbExePath = new System.Windows.Forms.TextBox();
            this.btnSelectPath = new System.Windows.Forms.Button();
            this.btnRun = new System.Windows.Forms.Button();
            this.btnStop = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tbExePath
            // 
            this.tbExePath.Font = new System.Drawing.Font("PMingLiU", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tbExePath.Location = new System.Drawing.Point(12, 12);
            this.tbExePath.Name = "tbExePath";
            this.tbExePath.Size = new System.Drawing.Size(591, 27);
            this.tbExePath.TabIndex = 0;
            // 
            // btnSelectPath
            // 
            this.btnSelectPath.Font = new System.Drawing.Font("PMingLiU", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnSelectPath.Location = new System.Drawing.Point(609, 12);
            this.btnSelectPath.Name = "btnSelectPath";
            this.btnSelectPath.Size = new System.Drawing.Size(63, 27);
            this.btnSelectPath.TabIndex = 1;
            this.btnSelectPath.Text = "...";
            this.btnSelectPath.UseVisualStyleBackColor = true;
            this.btnSelectPath.Click += new System.EventHandler(this.btnSelectPath_Click);
            // 
            // btnRun
            // 
            this.btnRun.Enabled = false;
            this.btnRun.Font = new System.Drawing.Font("PMingLiU", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnRun.Location = new System.Drawing.Point(540, 64);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(63, 27);
            this.btnRun.TabIndex = 2;
            this.btnRun.Text = "Run";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnEnter_Click);
            // 
            // btnStop
            // 
            this.btnStop.Enabled = false;
            this.btnStop.Font = new System.Drawing.Font("PMingLiU", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnStop.Location = new System.Drawing.Point(609, 64);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(63, 27);
            this.btnStop.TabIndex = 5;
            this.btnStop.Text = "Stop";
            this.btnStop.UseVisualStyleBackColor = true;
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 102);
            this.Controls.Add(this.btnStop);
            this.Controls.Add(this.btnRun);
            this.Controls.Add(this.btnSelectPath);
            this.Controls.Add(this.tbExePath);
            this.Name = "MainForm";
            this.Text = "Memory Inspector";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbExePath;
        private System.Windows.Forms.Button btnSelectPath;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.Button btnStop;
    }
}

