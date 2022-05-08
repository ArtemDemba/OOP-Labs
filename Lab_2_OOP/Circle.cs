using System.Drawing;

namespace Lab_2_OOP
{
    class Circle : Rect
    {
        public Circle(Pen pen, Point first, Point second) : base(pen, first, second)
        {

        }

        public override void Draw(Graphics g)
        {
            g.DrawEllipse(_pen, rectangle);
        }
    }
}