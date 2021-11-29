import amrvis


amr_text = """(p / permit-01
   :ARG1 (g / go-02
            :ARG0 (b / boy))
   :polarity -)
"""
amrvis.draw(amr_text, reverse=True, view=True)
