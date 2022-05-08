using System.Drawing;

namespace Lab_2_OOP
{
    class Line : Shape
    {
        public Line(Pen pen, Point first, Point second) : base(pen, first, second)
        {

        }
        public override void Draw(Graphics g)
        {
            g.DrawLine(_pen, FirstPoint, SecondPoint);
        }
    }
}