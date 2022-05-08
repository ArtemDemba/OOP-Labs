using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Lab_2_OOP
{
    public partial class Form1 : Form
    { 
        int q = 0;
        Point m_down;
        Point m_move;
        bool isPressed = false;
        Shapes CurrentShape = Shapes.Line;
        Bitmap map = new Bitmap(100, 100);
        Graphics g;
        ArrayPoint arrayPoints = new ArrayPoint(2);
        List<Shape> shapes = new List<Shape>();
        Pen pen = new Pen(Color.Black, 1);

        public Form1()
        {
            InitializeComponent();
            SetSize();
            g.Clear(Color.White);
        }

        private class ArrayPoint
        {
            private int index = 0;
            private Point[] points;

            public ArrayPoint(int size)
            {
                if (size <= 0)
                {
                    size = 2;
                }
                points = new Point[size];
            }
            public void SetPoint(int x, int y)
            {
                if (index >= points.Length)
                {
                    index = 0;
                }
                points[index] = new Point(x, y);
                index++;
            }
            public void Reset()
            {
                index = 0;
            }

            public int GetPointsCount()
            {
                return index;
            }
            public Point[] GetPoints()
            {
                return points;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isPressed = true;
            if (q != 0)
            {
                m_down = e.Location;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isPressed = false;
            if (q == 0)
            {
                arrayPoints.Reset();
            }
            else if(q == 1)
            {
                Shape shape = ObjectShape(CurrentShape);
                shapes.Add(shape);
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Graphics graphics = e.Graphics;
            if (isPressed)
            {
                Shape shape = ObjectShape(CurrentShape);
                shape.Draw(graphics);
            }

            foreach (Shape item in shapes)
            {
                item.Draw(graphics);
            }
        }
        private void SetSize()
        {
            Rectangle rectangle = Screen.PrimaryScreen.Bounds;
            map = new Bitmap(rectangle.Width, rectangle.Height);
            g = Graphics.FromImage(map);
            pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isPressed)
            {
                if (q == 0)
                {
                    arrayPoints.SetPoint(e.X, e.Y);
                    if (arrayPoints.GetPointsCount() >= 2)
                    {
                        g.DrawLines(pen, arrayPoints.GetPoints());
                        pictureBox1.Image = map;
                        arrayPoints.SetPoint(e.X, e.Y);
                        pictureBox1.Refresh();
                    }
                    pictureBox1.Refresh();
                }
                else if(q != 0)
                {
                    m_move = e.Location;
                    pictureBox1.Refresh();
                }
            }
        }

        private void linebtn_Click(object sender, EventArgs e)
        {
            CurrentShape = Shapes.Line;
            q = 1;
        }

        private void circlebtn_Click(object sender, EventArgs e)
        {
            CurrentShape = Shapes.Circle;
            q = 1;
        }

        private void rectbtn_Click(object sender, EventArgs e)
        {
            CurrentShape = Shapes.Rect;
            q = 1;
        }

        private Shape ObjectShape(Shapes shape)
        {
            switch (shape)
            {
                case Shapes.Line:
                    return new Line(pen, m_down, m_move);

                case Shapes.Rect:
                    return new Rect(pen, m_down, m_move);

                case Shapes.Circle:
                    return new Circle(pen, m_down, m_move);

                default:
                    throw new Exception("object error!");
            }
        }

        private void ChangeColor_Click(object sender, EventArgs e)
        {
            pen.Color = ((Button)sender).BackColor;
        }

        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            pen.Width = trackBar1.Value;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            q = 0;
        }

        private void clear_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);
            shapes.Clear();
            pictureBox1.Refresh();
        }

        private void save_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "JPG(*.JPG)|*.jpg";
            if(saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if (pictureBox1.Image == null)
                {
                    pictureBox1.Image.Save(saveFileDialog1.FileName);
                }
            }
        }
    }
}