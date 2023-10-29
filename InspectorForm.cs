using System;
using System.IO;
using System.Text;
using System.Diagnostics;
using System.Windows.Forms;

namespace MemoryInspector
{
    public partial class MainForm : Form
    {
        string m_strExeName = "";
        private Process m_process = null;

        public MainForm()
        {
            InitializeComponent();
        }

        private void btnSelectPath_Click(object sender, EventArgs e)
        {
            string strExePath = "";
            string[] strInputArr = GetFileNameFromDialog("exe files (*.exe)|*.exe", false);
            if (strInputArr != null)
            {
                strExePath = strInputArr[0];
            }
            else
            {
                strExePath = null;
            }
            tbExePath.Text = strExePath;
            btnRun.Enabled = true;
        }

        private void btnEnter_Click(object sender, EventArgs e)
        {
            if (IsExePathSetted(tbExePath.Text))
            {
                m_strExeName = Path.GetFileNameWithoutExtension(tbExePath.Text);
                SetCmd(m_strExeName, tbDatabase.Text, tbUser.Text, tbPassword.Text, tbHost.Text, tbPort.Text);
            }
            btnRun.Enabled = false;
            btnStop.Enabled = true;
        }

        private string[] GetFileNameFromDialog(string filter, bool bMultiselect)
        {
            OpenFileDialog dialog = new OpenFileDialog
            {
                Title = "Select File",
                InitialDirectory = "./",
                Filter = filter,
                FilterIndex = 2,
                Multiselect = bMultiselect
            };
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                if (bMultiselect)
                {
                    return dialog.FileNames;
                }
                else
                {
                    return new[] { dialog.FileName };
                }
            }
            return null;
        }

        private bool IsExePathSetted(string strPath)
        {
            if (strPath == null)
            {
                return false;
            }
            else
            {
                string strExtension = Path.GetExtension(strPath).ToLower();

                if (strExtension == ".exe")
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        private void SetCmd(string strExeName, string strDatabase, string strUser, string strPassword, string strHost, string strPort)
        {
            Control.CheckForIllegalCrossThreadCalls = false;
            m_process = new Process();
            m_process.StartInfo.FileName = "./memory_measurement_app/memory_measurement_app.exe";
            m_process.StartInfo.Arguments = string.Format("--exe_name \"{0}\" --del_table \"{1}\" --database \"{2}\" --user \"{3}\" --password \"{4}\" --host \"{5}\" --port \"{6}\"",
                strExeName,
                "yes",
                strDatabase,
                strUser,
                strPassword,
                strHost,
                strPort);
            m_process.StartInfo.UseShellExecute = false;
            m_process.EnableRaisingEvents = true;
            m_process.Start();
        }

        //private void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        //{
        //    if (!String.IsNullOrEmpty(outLine.Data))
        //    {
        //        StringBuilder sb = new StringBuilder(this.tbOutput.Text);
        //        this.tbOutput.Text = sb.AppendLine(outLine.Data).ToString();
        //        this.tbOutput.SelectionStart = this.tbOutput.Text.Length; // update last print text.
        //        this.tbOutput.ScrollToCaret();
        //    }
        //}

        private void btnStop_Click(object sender, EventArgs e)
        {
            if (!m_process.HasExited)
            {
                m_process.Kill();
            }
            btnStop.Enabled = false;
            btnRun.Enabled = true;
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }
    }
}
