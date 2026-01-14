"""
PDF Generator using FPDF2
Compatible with Python 3.8+
"""
from fpdf import FPDF
import os
from datetime import datetime
import re

def generate_improved_srs_pdf(session, filename="improved_srs.pdf"):
    """
    Generate PDF using FPDF2 and return bytes
    """
    try:
        # Create PDF instance
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Title
        pdf.set_font('helvetica', 'B', 20)
        pdf.set_text_color(102, 126, 234)  # #667eea
        pdf.cell(0, 10, 'Improved SRS Document', align='C', new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)
        
        # Metadata
        pdf.set_font('helvetica', '', 10)
        pdf.set_text_color(0, 0, 0)
        
        date_str = datetime.now().strftime('%B %d, %Y at %I:%M %p')
        pdf.cell(0, 6, f"Generated: {date_str}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 6, f"Total Requirements: {len(session['requirements'])}", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 6, f"Clarifications Provided: {len(session['clarifications'])}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(10)

        # Clarifications
        if session['clarifications']:
            pdf.set_font('helvetica', 'B', 14)
            pdf.set_text_color(118, 75, 162)  # #764ba2
            pdf.cell(0, 10, 'User-Provided Clarifications', new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
            
            pdf.set_font('helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            
            for term, value in session['clarifications'].items():
                # Bold the term
                pdf.set_font('helvetica', 'B', 11)
                pdf.write(6, f"{term}: ")
                pdf.set_font('helvetica', '', 11)
                pdf.write(6, f"{value}")
                pdf.ln(6)
            
            pdf.ln(10)
        
        # Requirements
        pdf.set_font('helvetica', 'B', 14)
        pdf.set_text_color(118, 75, 162)
        pdf.cell(0, 10, 'Improved Requirements', new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)
        
        for i, req_data in enumerate(session['requirements'], 1):
            
            # Improve text
            improved_text = req_data['original']
            for ambiguous_word in req_data['ambiguous']:
                if ambiguous_word in session['clarifications']:
                    user_clarification = session['clarifications'][ambiguous_word]
                    pattern = re.compile(re.escape(ambiguous_word), re.IGNORECASE)
                    improved_text = pattern.sub(user_clarification, improved_text, count=1)
            
            # Header
            pdf.set_font('helvetica', 'B', 12)
            pdf.set_text_color(102, 126, 234)
            # Check space
            if pdf.get_y() > 250:
                pdf.add_page()
                
            pdf.cell(0, 8, f"Requirement {i} - {req_data['category']}", new_x="LMARGIN", new_y="NEXT")
            
            # Before
            pdf.set_font('helvetica', 'B', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.write(6, "Before: ")
            pdf.set_font('helvetica', '', 11)
            pdf.multi_cell(0, 6, req_data['original'])
            
            # After
            if improved_text != req_data['original']:
                pdf.set_font('helvetica', 'B', 11)
                pdf.write(6, "After: ")
                pdf.set_font('helvetica', '', 11)
                pdf.set_text_color(0, 168, 107)  # Green
                pdf.multi_cell(0, 6, improved_text)
            else:
                pdf.set_font('helvetica', 'B', 11)
                pdf.set_text_color(0, 0, 0)
                pdf.write(6, "Status: ")
                pdf.set_font('helvetica', '', 11)
                pdf.set_text_color(0, 168, 107)
                pdf.multi_cell(0, 6, "No ambiguities detected - requirement is clear")
                
            pdf.ln(5)
            pdf.set_text_color(0, 0, 0)

        # Return bytes
        return pdf.output()
        
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        raise e
