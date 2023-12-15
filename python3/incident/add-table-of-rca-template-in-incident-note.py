# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# Script to add a table which is used as a template for root cause analysis in incident's note

hint_for_severity = "(Please specify Critical/High/Medium/Low here)"
hint_for_impact_assessment = "(Please describe impact summary here)"
hint_for_action_items = "(Please describe detailed action here)"
table_content = '<table><tbody><tr><td colspan="3"><p data-node-text-align="center" style=" text-align:center"><span style=" font-size:18px"><strong>Impact Assessment</strong></span></p></td></tr><tr><td><p>Customer Impact</p></td><td><p><span style=" color:rgb(187,187,187)" data-text-color-mark="rgb(187,187,187)">' + hint_for_severity + '</span></p></td><td rowspan="7"><p data-node-text-align="center" style=" text-align:center"><span style=" color:rgb(187,187,187)" data-text-color-mark="rgb(187,187,187)">' + hint_for_impact_assessment + '</span></p></td></tr><tr><td><p>Brand Impact</p></td><td><p></p></td></tr><tr><td><p>Contractual Impacts</p></td><td><p></p></td></tr><tr><td><p>Financial Impact</p></td><td><p></p></td></tr><tr><td><p>Productivity Impact</p></td><td><p></p></td></tr><tr><td><p>Data Loss</p></td><td><p></p></td></tr><tr><td><p>Privacy Breach</p></td><td><p></p></td></tr><tr><td colspan="3"><p data-node-text-align="center" style=" text-align:center"><span style=" font-size:18px"><strong>Action Items</strong></span></p></td></tr><tr><td><p>1</p></td><td colspan="2"><p><span style=" color:rgb(187,187,187)" data-text-color-mark="rgb(187,187,187)">' + hint_for_action_items + '</span></p></td></tr><tr><td><p>2</p></td><td colspan="2"><p></p></td></tr><tr><td><p>3</p></td><td colspan="2"><p></p></td></tr></tbody></table><p></p></div>'

incident.addNote(table_content)
