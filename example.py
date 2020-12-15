from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, title=None, logo=None, watermark_text=None):
        self.title = title
        self.logo = logo
        self.watermark_text = watermark_text
        super(PDF, self).__init__()

    def header(self):
        # Watermark Text
        # if self.watermark_text != None:
        #     self.set_font('Arial', 'B', 50);
        #     self.set_text_color(255, 192, 203);
        #     self.rotate_text(0, self.w/2 - self.t_margin - (0.7 * self.get_string_width(self.watermark_text)), 
        #         f'{self.watermark_text}', 45);

        # Logo
        if self.logo != None:
            self.image(f'{self.logo}', 150, 8, 33)

        if self.title != None:
            # Arial bold 15
            self.set_font('Arial', 'B', 15)
            self.set_text_color(0, 0, 0)
            # Move to the right
            self.cell(self.w/2-(self.get_string_width(self.title) + 10)/2 - self.l_margin)
            # Title
            self.cell(self.get_string_width(self.title) + 10, 10, f'{self.title}', 1, 0, 'C')
            # Line break
            self.ln(20)



    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
    
    def rotate_text(self, x, y, txt, angle):
        # Text rotated around its origin
        self.rotate(angle,x,y);
        self.text(x,y,txt);
        self.rotate(0);

# Instantiation of inherited class
pdf = PDF("Cheng Guan's Report", "cg.png", "W a t e r m a r k   D e m o")
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 12)

msg = 'This method allows printing text with line breaks. They can be automatic (as soon as the text reaches the right border of the cell) or explicit (via the CR character). As many cells as necessary are output, one below the other. Text can be aligned, centered or justified. The cell block can be framed and the background painted.'

for i in range(1, 41):
    pdf.cell(0, 5, 'Printing line number ' + str(i), 0, 1)

pdf.multi_cell(0, 5, msg, 0, 1)

pdf.output('example.pdf', 'F')