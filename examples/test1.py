import amrvis


amr_text = """(s / see-01
   :ARG0 (b / boy)
   :ARG1 (g / girl
            :ARG0-of (w / want-01
                        :ARG1 b)))
"""
amrvis.draw(amr_text, reverse=True, view=True)
