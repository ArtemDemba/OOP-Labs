using System.Drawing;

namespace Lab_2_OOP
{
    enum Shapes
    {
        Line = 1,
        Rect,
        Circle
    }
    abstract class Shape
    {
        public Point FirstPoint { get; set; }
        public Point SecondPoint { get; set; }
        public Pen _pen { get; set; }

        public Shape(Pen pen, Point first, Point second)
        {
            _pen = pen;
            FirstPoint = first;
            SecondPoint = second;
        }

        public abstract void Draw(Graphics g);
    }
}