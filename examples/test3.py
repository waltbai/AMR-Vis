import amrvis


amr_text = """(a / attack-01
   :ARG0 (c / country :name (n / name :op1 "Iraq"))
   :instrument (m / missile))
"""
amrvis.draw(amr_text, reverse=True, view=True)
