# HDFC Mutual Fund - Facts-Only FAQ Assistant

A RAG-based (Retrieval-Augmented Generation) chatbot that answers **factual questions only** about HDFC mutual fund schemes using verified sources from AMC, SEBI, and AMFI. Provides concise, citation-backed responses while strictly avoiding any investment advice.

## 🎯 Product & Use Cases

- **Product Owner:** INDMoney (Fintech Investment Platform)
- **Use Cases:**
  - Retail users comparing HDFC scheme facts
  - Support teams answering repetitive MF questions
  - Educational content about mutual funds
  - Self-service FAQ before contacting support

---

## 📋 Project Scope

### Corpus Coverage
- **AMC:** HDFC Mutual Fund (Asset Management Company)
- **Schemes Covered:** 5 schemes
  1. **HDFC Equity Fund** (Large-cap equity)
  2. **HDFC Flexi Cap Fund** (Flexible cap equity)
  3. **HDFC Tax Saver** (ELSS - Equity Linked Savings Scheme)
  4. **HDFC Liquid Fund** (Liquid/debt fund)
  5. **HDFC Balanced Advantage Fund** (Balanced/multi-asset)

### Information Sources
- **25 Public Pages** from official sources:
  - HDFC Mutual Fund website (scheme pages, factsheets, KIM/SID, charges documents)
  - SEBI website (regulations, riskometer guidelines, investor education)
  - AMFI website (industry standards, SIP guides, tax documentation)

**See:** `sources.csv` for complete list of all 25 sources.

### Factual Topics Covered
✅ **Answered:**
- Expense ratios
- Minimum SIP and lumpsum investments
- Exit loads
- Lock-in periods (especially ELSS 3-year requirement)
- Benchmarks and indices
- Riskometer ratings (SEBI standard)
- Risk profiles
- Fund objectives
- How to download statements and tax documents

❌ **NOT Answered (By Design):**
- "Should I buy/sell this fund?"
- "Which fund is better for me?"
- "What will be my returns?"
- Performance comparisons
- Portfolio recommendations
- Market predictions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Clone/Navigate to Repository:**
   ```bash
   cd /home/user/AnishPM
   ```

2. **Create Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install streamlit
   ```

4. **Run the Application:**
   ```bash
   streamlit run mf_faq_assistant.py
   ```

5. **Access the App:**
   - Opens automatically at: `http://localhost:8501`
   - Or open the URL shown in terminal

### Using the Assistant

1. **Read the disclaimer** - This is facts-only, no investment advice
2. **Choose your question type:**
   - Factual about schemes (e.g., "What's the expense ratio of HDFC Equity Fund?")
   - Process/how-to (e.g., "How do I download my statement?")
3. **Specify the scheme** - The assistant will ask if unclear
4. **Get answer with citation** - Every response includes an official source link

---

## 📚 Project Deliverables

### 1. **Working Prototype** ✅
- **File:** `mf_faq_assistant.py`
- **Type:** Streamlit web application
- **Features:**
  - Interactive Q&A interface
  - Smart pattern matching for queries
  - Investment advice detection and refusal
  - Citation links for every answer
  - Example questions display
  - Factual disclaimers

### 2. **Source List** ✅
- **File:** `sources.csv`
- **Contains:** 25 public sources
- **Columns:**
  - Source_ID
  - Scheme_Name
  - Topic
  - URL (full link)
  - Source_Type (AMC/SEBI/AMFI)

### 3. **Sample Q&A** ✅
- **File:** `sample_qa.md`
- **Contains:** 10 sample queries with:
  - Full assistant responses
  - Citation links
  - Explanation of response type (factual vs. refusal)
  - Key patterns demonstrated

### 4. **This README** ✅
- Setup instructions
- Scope and limitations
- Architecture explanation
- Disclaimer and compliance notes

---

## 🛠️ Technical Architecture

### Components

```
┌─────────────────────────────────────────┐
│      User Query Input                   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Query Analysis Layer                   │
│  - Investment Advice Detection          │
│  - Scheme Identification                │
│  - Fact Type Identification             │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Knowledge Base Layer                   │
│  - HDFC scheme facts (embedded)         │
│  - Citation mappings                    │
│  - Source links                         │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  Response Generation                    │
│  - Format answer with citation          │
│  - Add source link                      │
│  - Add disclaimer note                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Formatted Response to User         │
│      (Fact + Citation Link)             │
└─────────────────────────────────────────┘
```

### Data Flow (RAG Concept)

1. **Query Understanding:** Identify scheme + fact type
2. **Retrieval:** Look up fact in knowledge base
3. **Augmentation:** Add official source link
4. **Generation:** Format response with disclaimer

---

## 🔒 Data Privacy & Compliance

### No PII Collection ✅
- **Explicitly blocked:**
  - PAN (Permanent Account Number)
  - Aadhaar numbers
  - Account numbers
  - OTPs
  - Email addresses (not used for auth)
  - Phone numbers

- **Implementation:**
  - Streamlit runs locally (no data transmission)
  - No login/authentication required
  - No data storage or backend database
  - No cookies or tracking

### Source Verification ✅
- All sources are **official public pages only**
  - ✅ HDFC Mutual Fund official website
  - ✅ SEBI official website
  - ✅ AMFI official website
  - ❌ No third-party blogs or financial websites
  - ❌ No unverified sources

### Accuracy & Transparency ✅
- **Every answer includes:**
  - Clear source link
  - "Last updated from official sources" note
  - No performance claims or predictions
  - No unsourced statements

---

## 📊 Disclaimer & Compliance

### Full Disclaimer (Used in UI)
```
❌ FACTS-ONLY • NO INVESTMENT ADVICE

This assistant provides factual information about HDFC mutual fund
schemes from official AMC, SEBI, and AMFI sources only.

It does NOT provide:
- Investment advice
- Portfolio recommendations
- Performance predictions
- Buy/sell recommendations
- Financial planning

For investment decisions, consult a qualified financial advisor.
For investor education: https://www.sebi.gov.in/investor-education
```

### Regulatory Boundaries
- Complies with **SEBI regulations** on investment advice
- Adheres to **AMFI standards** for investor communication
- References **SEBI riskometer** classifications
- Uses **official KIM/SID documents** as sources
- No unlicensed financial advice

---

## 🧪 Testing & Quality Assurance

### Test Categories

#### ✅ Factual Questions (Should Answer)
- "What is the expense ratio of HDFC Equity Fund?"
- "What is the lock-in period for HDFC Tax Saver?"
- "What's the minimum SIP for HDFC Liquid Fund?"
- "How do I download my statement?"

#### ❌ Investment Advice (Should Refuse)
- "Should I buy HDFC Equity Fund?"
- "Which fund is better?"
- "Will I earn ₹50,000 in 5 years?"
- "What's your recommendation?"

#### ⚠️ Edge Cases (Should Handle Gracefully)
- Typos in scheme names → Asks for clarification
- Ambiguous queries → Asks to specify scheme or topic
- Out-of-scope questions → Polite refusal + educational links

### Sample Test Cases (See `sample_qa.md`)
- 6 factual Q&A pairs (with correct citations)
- 2 investment advice refusals (with explanations)
- 2 process-based questions (how-to format)

---

## ⚙️ Configuration & Customization

### Knowledge Base Structure
Located in `mf_faq_assistant.py`:
```python
KNOWLEDGE_BASE = {
    "scheme_id": {
        "name": "Scheme Name",
        "facts": {
            "fact_type": "fact_value",
            ...
        },
        "sources": {
            "fact_type": "https://source-url",
            ...
        }
    }
}
```

### To Add More Schemes
1. Add new scheme entry to `KNOWLEDGE_BASE`
2. Include facts for: expense_ratio, minimum_sip, minimum_lumpsum, exit_load, lock_in_period, benchmark, riskometer, etc.
3. Map each fact to official source URL
4. Update scheme_keywords in `identify_scheme()` function
5. Test with sample queries

### To Update Sources
- Edit `sources.csv` with new URLs
- Ensure URLs point to **official pages only**
- Update corresponding source links in knowledge base

---

## 📈 Known Limitations

### By Design (Intentional Boundaries)
1. **No performance data** - Cannot compare returns or predict future performance
2. **No portfolio advice** - Cannot recommend which funds to choose
3. **No investment strategy** - Cannot plan asset allocation
4. **No market predictions** - Cannot forecast market movements
5. **Static knowledge base** - Does not update in real-time (requires manual update)

### Technical Limitations
1. **Embedded knowledge base only** - Does not retrieve from live web pages (for accuracy & control)
2. **HDFC schemes only** - Focused on 5 HDFC schemes (can be expanded)
3. **English language only** - Does not support regional languages
4. **Local deployment** - Not deployed on cloud; runs locally via Streamlit
5. **Pattern-matching based** - Uses keyword matching (not semantic search/embeddings in current version)

### Future Enhancement Opportunities
- [ ] Add more AMCs (ICICI, SBI, Axis, etc.)
- [ ] Implement semantic search with embeddings
- [ ] Add real-time factsheet updates
- [ ] Multi-language support
- [ ] Cloud deployment
- [ ] Integration with INDMoney platform
- [ ] Analytics on frequently asked questions
- [ ] Performance comparison (facts only, no advice)

---

## 📞 Support & Maintenance

### Troubleshooting

**Issue: "The app won't start"**
```bash
# Reinstall Streamlit
pip install --upgrade streamlit

# Try running with debug
streamlit run mf_faq_assistant.py --logger.level=debug
```

**Issue: "Sources are outdated"**
- HDFC scheme pages change occasionally
- Verify links in `sources.csv` are still valid
- Update URLs if needed
- Re-run assistant

**Issue: "Query not understood"**
- Be specific about scheme name (Equity, Flexi Cap, Tax Saver, Liquid, Balanced)
- Use common terms (expense ratio, SIP, lock-in, exit load)
- See example questions in the UI

### Maintenance Checklist
- [ ] Monthly: Verify all source links are working
- [ ] Quarterly: Update scheme factsheets if changed
- [ ] Annually: Add new schemes or AMCs
- [ ] Ongoing: Monitor user questions for edge cases

---

## 📚 Learning Skills Demonstrated

### W1 - Thinking Like a Model ✅
- Exact fact identification from queries
- Decision logic: answer vs. refuse
- Boundary setting for investment advice
- Handling ambiguous queries

### W2 - LLMs & Prompting ✅
- Concise instruction-style response format
- Polite safe-refusals with alternatives
- Citation wording (clear source attribution)
- Consistent tone and formatting

### W3 - RAGs (Retrieval-Augmented Generation) ✅
- Small-corpus retrieval (embedded knowledge base)
- Accurate citations from 25 official sources
- Query-to-source mapping
- Grounded responses (no hallucination)

---

## 📝 Sample Commands to Test

```bash
# Test with common queries (manually in Streamlit UI):

# Factual - Should Answer ✅
"What is the expense ratio of HDFC Equity Fund?"
"What is the lock-in period for HDFC Tax Saver?"
"Minimum SIP for HDFC Liquid Fund?"
"How do I download my statement from HDFC?"

# Investment Advice - Should Refuse ❌
"Should I buy HDFC Equity Fund?"
"Which HDFC fund is best for me?"
"What will I earn in 5 years?"
"Recommend a fund for my portfolio"

# Process Questions - Should Answer ✅
"How to download capital gains statement?"
"Where can I see my investment statement?"
```

---

## 📄 File Structure

```
AnishPM/
├── README.md                    # This file (setup & scope)
├── mf_faq_assistant.py         # Streamlit app (main prototype)
├── sample_qa.md                # 10 sample Q&A pairs + patterns
├── sources.csv                 # 25 official source URLs
└── requirements.txt            # Python dependencies (if needed)
```

---

## 🔗 Official References

### Links to Official Resources
- **HDFC Mutual Fund:** https://www.hdfcfund.com
- **SEBI Investor Education:** https://www.sebi.gov.in/investor-education
- **AMFI (Association of MF India):** https://www.amfiindia.com/investor-education
- **SEBI Riskometer Guidelines:** https://www.sebi.gov.in/media/pressrelease/2020/jan/riskometer-faqs
- **Tax Documents (AMFI):** https://www.amfiindia.com/investor-education/tax-documents

---

## 🎓 About This Project

### Purpose
Build a factual, citation-based FAQ assistant for mutual fund schemes that:
- Answers ONLY facts (no advice)
- Always provides source links
- Refuses investment recommendations
- Protects user privacy
- Educates retail investors

### Why Facts-Only?
1. **Regulatory Compliance** - Avoid unlicensed investment advice
2. **User Safety** - Prevent poor investment decisions
3. **Accuracy** - Focus on verifiable facts from official sources
4. **Trustworthiness** - Clear citations build credibility

### Accessibility
- Free, public-source based
- No login required
- Runs on any computer with Python
- Streamlit makes it web-accessible

---

## ✅ Checklist for Submission

- [x] Working prototype (Streamlit app)
- [x] Source list (CSV with 25 URLs)
- [x] Sample Q&A (10 queries with responses)
- [x] README (this file - setup, scope, limits)
- [x] Disclaimer snippet (in UI and this README)
- [x] No PII collection
- [x] Public sources only
- [x] Clear citations in every answer
- [x] Refusal logic for investment advice
- [x] 5 HDFC schemes covered
- [x] 25+ official sources used

---

**Last Updated:** November 2024
**Version:** 1.0 (MVP - Minimum Viable Product)
**Status:** Ready for Testing & Deployment

---

## 📧 Questions or Feedback?

For issues, feature requests, or questions about this FAQ assistant:
1. Check the limitations section above
2. Review sample_qa.md for examples
3. Verify source links in sources.csv
4. Test with the provided sample queries

**Key Principle:** When in doubt, ask for a **factual question** about **specific scheme details** - that's what this assistant does best!

---

*Built for INDMoney - Empowering Retail Investors with Facts*
