using System.Drawing;

namespace Lab_2_OOP
{
    class Rect : Shape
    {
        protected int Width { get; set; }
        protected int Height { get; set; }

        protected Rectangle rectangle;
        public Rect(Pen _pen, Point first, Point second) : base(_pen, first, second)
        {
            if (SecondPoint.X > FirstPoint.X && SecondPoint.Y > FirstPoint.Y)                   
                rectangle = new Rectangle(FirstPoint.X, FirstPoint.Y, SecondPoint.X - FirstPoint.X, SecondPoint.Y - FirstPoint.Y);
            else if (SecondPoint.X < FirstPoint.X && SecondPoint.Y > FirstPoint.Y)              
                rectangle = new Rectangle(SecondPoint.X, FirstPoint.Y, FirstPoint.X - SecondPoint.X, SecondPoint.Y - FirstPoint.Y);
            else if (SecondPoint.X > FirstPoint.X && SecondPoint.Y < FirstPoint.Y)              
                rectangle = new Rectangle(FirstPoint.X, SecondPoint.Y, SecondPoint.X - FirstPoint.X, FirstPoint.Y - SecondPoint.Y);
            else                                                                                
                rectangle = new Rectangle(SecondPoint.X, SecondPoint.Y, FirstPoint.X - SecondPoint.X, FirstPoint.Y - SecondPoint.Y);
        }
        bool isNew = false;
        public override void Draw(Graphics g)
        {   
            
            if(!isNew)
            {
                g.DrawRectangle(_pen, rectangle);
                //isNew = true;
            }
        }
    }
}