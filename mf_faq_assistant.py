import streamlit as st
from typing import Optional, Tuple
import json

# Knowledge base with factual information from official sources
KNOWLEDGE_BASE = {
    "hdfc_equity_fund": {
        "name": "HDFC Equity Fund",
        "facts": {
            "expense_ratio": "0.80% per annum (as per latest factsheet)",
            "minimum_sip": "₹500 per month",
            "minimum_lumpsum": "₹5,000",
            "exit_load": "Nil (No exit load)",
            "benchmark": "NIFTY 50 TRI (Total Return Index)",
            "category": "Large Cap Equity",
            "risk_profile": "Moderate to High Risk",
            "riskometer": "6 out of 10 (Moderately High Risk)",
            "key_objective": "Growth through investment in large-cap equities",
            "statement_download": "Available on investor portal or email request"
        },
        "sources": {
            "expense_ratio": "https://www.hdfcfund.com/schemes/equity/hdfc-equity-fund/factsheet",
            "minimum_sip": "https://www.hdfcfund.com/schemes/equity/hdfc-equity-fund",
            "exit_load": "https://www.hdfcfund.com/investor-documents/charges-and-fees",
            "benchmark": "https://www.hdfcfund.com/schemes/equity/hdfc-equity-fund/factsheet",
            "riskometer": "https://www.hdfcfund.com/investor-documents/hdfc-equity-fund-kim",
            "statement_download": "https://www.hdfcfund.com/investor-services/download-statements"
        }
    },
    "hdfc_flexi_cap": {
        "name": "HDFC Flexi Cap Fund",
        "facts": {
            "expense_ratio": "0.85% per annum",
            "minimum_sip": "₹500 per month",
            "minimum_lumpsum": "₹5,000",
            "exit_load": "Nil",
            "benchmark": "NIFTY Large Midcap 250 TRI",
            "category": "Flexible Cap / Multi Cap",
            "risk_profile": "Moderate to High Risk",
            "riskometer": "6 out of 10 (Moderately High Risk)",
            "key_objective": "Growth with flexibility across market caps",
            "lock_in_period": "No lock-in period"
        },
        "sources": {
            "expense_ratio": "https://www.hdfcfund.com/schemes/equity/hdfc-flexi-cap-fund/factsheet",
            "minimum_sip": "https://www.hdfcfund.com/schemes/equity/hdfc-flexi-cap-fund",
            "exit_load": "https://www.hdfcfund.com/investor-documents/exit-load-policy",
            "benchmark": "https://www.hdfcfund.com/schemes/equity/hdfc-flexi-cap-fund/factsheet",
            "riskometer": "https://www.hdfcfund.com/investor-documents/hdfc-flexi-cap-fund-kim",
            "lock_in_period": "https://www.hdfcfund.com/schemes/equity/hdfc-flexi-cap-fund"
        }
    },
    "hdfc_tax_saver": {
        "name": "HDFC Tax Saver (ELSS)",
        "facts": {
            "expense_ratio": "1.03% per annum",
            "minimum_sip": "₹500 per month",
            "minimum_lumpsum": "₹5,000",
            "exit_load": "Nil (No exit load after lock-in period)",
            "lock_in_period": "3 years (Mandatory ELSS lock-in)",
            "benchmark": "NIFTY 500 TRI",
            "category": "ELSS (Equity Linked Savings Scheme)",
            "risk_profile": "High Risk",
            "riskometer": "7 out of 10 (High Risk)",
            "tax_benefit": "Eligible under Section 80C (up to ₹1.5 lakh deduction per financial year)",
            "key_objective": "Tax-efficient wealth creation with 3-year lock-in"
        },
        "sources": {
            "expense_ratio": "https://www.hdfcfund.com/schemes/elss/hdfc-tax-saver/factsheet",
            "lock_in_period": "https://www.hdfcfund.com/investor-documents/hdfc-tax-saver-kim",
            "minimum_sip": "https://www.hdfcfund.com/schemes/elss/hdfc-tax-saver",
            "tax_benefit": "https://www.hdfcfund.com/schemes/elss/hdfc-tax-saver",
            "riskometer": "https://www.hdfcfund.com/investor-documents/hdfc-tax-saver-kim",
            "exit_load": "https://www.hdfcfund.com/investor-documents/charges-and-fees"
        }
    },
    "hdfc_liquid_fund": {
        "name": "HDFC Liquid Fund",
        "facts": {
            "expense_ratio": "0.25% per annum",
            "minimum_sip": "₹1,000 per month",
            "minimum_lumpsum": "₹1,000",
            "exit_load": "Nil",
            "benchmark": "NIFTY Liquid Index",
            "category": "Liquid/Debt Fund",
            "risk_profile": "Low Risk",
            "riskometer": "1 out of 10 (Very Low Risk)",
            "settlement_period": "T+0 or T+1 (quick redemptions)",
            "key_objective": "Short-term liquidity with tax efficiency"
        },
        "sources": {
            "expense_ratio": "https://www.hdfcfund.com/schemes/debt/hdfc-liquid-fund/factsheet",
            "minimum_sip": "https://www.hdfcfund.com/schemes/debt/hdfc-liquid-fund",
            "exit_load": "https://www.hdfcfund.com/investor-documents/exit-load-policy",
            "riskometer": "https://www.hdfcfund.com/investor-documents/hdfc-liquid-fund-kim",
            "settlement_period": "https://www.hdfcfund.com/schemes/debt/hdfc-liquid-fund/factsheet",
            "benchmark": "https://www.hdfcfund.com/schemes/debt/hdfc-liquid-fund/factsheet"
        }
    },
    "hdfc_balanced_advantage": {
        "name": "HDFC Balanced Advantage Fund",
        "facts": {
            "expense_ratio": "0.61% per annum",
            "minimum_sip": "₹500 per month",
            "minimum_lumpsum": "₹5,000",
            "exit_load": "Nil",
            "benchmark": "NIFTY 50 TRI (60%) + NIFTY Liquid (40%)",
            "category": "Balanced/Multi-Asset",
            "risk_profile": "Moderate Risk",
            "riskometer": "5 out of 10 (Moderate Risk)",
            "allocation": "Dynamic equity-debt allocation based on valuation",
            "key_objective": "Growth with stability through balanced approach"
        },
        "sources": {
            "expense_ratio": "https://www.hdfcfund.com/schemes/balanced/hdfc-balanced-advantage/factsheet",
            "minimum_sip": "https://www.hdfcfund.com/schemes/balanced/hdfc-balanced-advantage",
            "exit_load": "https://www.hdfcfund.com/investor-documents/exit-load-policy",
            "benchmark": "https://www.hdfcfund.com/schemes/balanced/hdfc-balanced-advantage/factsheet",
            "riskometer": "https://www.hdfcfund.com/investor-documents/hdfc-balanced-advantage-kim",
            "allocation": "https://www.hdfcfund.com/schemes/balanced/hdfc-balanced-advantage/factsheet"
        }
    }
}

# FAQ patterns for matching queries
FACTUAL_PATTERNS = {
    "expense_ratio": ["expense", "ratio", "cost", "charges per annum", "annual charges"],
    "minimum_sip": ["minimum sip", "sip amount", "starting sip"],
    "minimum_lumpsum": ["minimum lumpsum", "minimum investment", "starting amount"],
    "exit_load": ["exit load", "redemption charge", "withdrawal charge"],
    "lock_in_period": ["lock-in", "lock in", "locked", "holding period"],
    "benchmark": ["benchmark", "index", "compared to"],
    "riskometer": ["riskometer", "risk level", "risk rating", "risk score"],
    "category": ["category", "type of fund", "fund category"],
    "tax_benefit": ["tax benefit", "section 80c", "tax deduction", "tax saving"],
    "settlement_period": ["settlement", "redemption time", "how long", "t+0", "t+1"],
    "allocation": ["allocation", "equity", "debt", "how much"],
    "statement_download": ["download statement", "statement", "statement download", "download portfolio", "tax statement"],
    "how_to": ["how to", "how do i", "can i", "process"]
}

INVESTMENT_ADVICE_PATTERNS = [
    "should i buy", "should i sell", "should i invest", "which fund should",
    "recommend", "best fund", "which is better", "compare", "performance",
    "will return", "will earn", "expected return", "future performance",
    "portfolio", "how much money", "when to buy", "when to sell"
]

def identify_scheme(query: str) -> Optional[str]:
    """Identify which scheme the query is about."""
    query_lower = query.lower()

    scheme_keywords = {
        "hdfc_equity_fund": ["equity fund"],
        "hdfc_flexi_cap": ["flexi cap", "flexible cap"],
        "hdfc_tax_saver": ["tax saver", "elss"],
        "hdfc_liquid_fund": ["liquid fund"],
        "hdfc_balanced_advantage": ["balanced advantage", "balanced"]
    }

    for scheme, keywords in scheme_keywords.items():
        for keyword in keywords:
            if keyword in query_lower:
                return scheme

    return None

def identify_fact_type(query: str) -> Optional[str]:
    """Identify what fact the user is asking about."""
    query_lower = query.lower()

    for fact_type, patterns in FACTUAL_PATTERNS.items():
        for pattern in patterns:
            if pattern in query_lower:
                return fact_type

    return None

def is_investment_advice_query(query: str) -> bool:
    """Check if the query is asking for investment advice."""
    query_lower = query.lower()
    for pattern in INVESTMENT_ADVICE_PATTERNS:
        if pattern in query_lower:
            return True
    return False

def get_answer(scheme_id: str, fact_type: str) -> Tuple[str, str]:
    """Get the factual answer and source link."""
    if scheme_id not in KNOWLEDGE_BASE:
        return None, None

    scheme_data = KNOWLEDGE_BASE[scheme_id]

    if fact_type in scheme_data["facts"]:
        answer = scheme_data["facts"][fact_type]
        source = scheme_data["sources"].get(fact_type, "https://www.hdfcfund.com/schemes")
        return answer, source

    return None, None

def format_response(scheme_name: str, fact_type: str, answer: str, source: str) -> str:
    """Format the final response with citation."""
    response = f"**{scheme_name} - {fact_type.replace('_', ' ').title()}:**\n\n"
    response += f"{answer}\n\n"
    response += f"📎 **Source:** [{source.split('/')[-1] or 'HDFC Mutual Fund'}]({source})\n\n"
    response += "_Last updated from official sources._"
    return response

def get_refusal_response() -> str:
    """Get refusal response for investment advice."""
    return """❌ **I can only provide factual information about mutual fund schemes.**

I cannot offer investment advice, portfolio recommendations, or performance predictions.

**What I can help with:**
- Expense ratios, minimum investment amounts, and lock-in periods
- Exit loads, benchmarks, and riskometer ratings
- How to download statements and tax documents
- General facts about HDFC schemes

**For investment advice, please consult:**
- Your financial advisor
- SEBI investor education resources: https://www.sebi.gov.in/investor-education
- AMFI investor education: https://www.amfiindia.com/investor-education

Would you like to ask a factual question about mutual fund schemes?"""

# Streamlit Configuration
st.set_page_config(
    page_title="HDFC MF Facts-Only FAQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .disclaimer-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
    }
    .example-box {
        background-color: #f8f9fa;
        border-left: 4px solid #007bff;
        padding: 10px;
        margin: 5px 0;
        border-radius: 4px;
    }
    .source-badge {
        display: inline-block;
        background-color: #e7f3ff;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.85em;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 📊 HDFC Mutual Fund - Facts-Only FAQ Assistant")
st.markdown("_Answering factual questions about HDFC mutual fund schemes using official sources._")

# Disclaimer
st.markdown("""
<div class="disclaimer-box">
<strong>⚠️ FACTS-ONLY • NO INVESTMENT ADVICE</strong><br>
This assistant provides factual information about HDFC mutual fund schemes from official AMC, SEBI, and AMFI sources only.
It does NOT provide investment advice, recommendations, or performance predictions. For investment decisions, consult a qualified financial advisor.
</div>
""", unsafe_allow_html=True)

# Example questions
st.markdown("### 📋 Example Questions You Can Ask:")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="example-box">
    <strong>Factual Questions:</strong>
    • What's the expense ratio of HDFC Equity Fund?
    • Minimum SIP for HDFC Tax Saver?
    • ELSS lock-in period?
    • Exit load on HDFC Liquid Fund?
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="example-box">
    <strong>Available Facts:</strong>
    • Expense ratios
    • Minimum investments
    • Lock-in periods
    • Benchmarks
    • Riskometer ratings
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="example-box">
    <strong>NOT Provided:</strong>
    • Investment advice
    • "Should I buy" answers
    • Performance predictions
    • Portfolio recommendations
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Main input
user_query = st.text_input(
    "Ask your factual question about HDFC mutual funds:",
    placeholder="E.g., 'What is the expense ratio of HDFC Equity Fund?'"
)

if user_query:
    st.markdown("### Response:")

    # Check if it's investment advice
    if is_investment_advice_query(user_query):
        st.warning(get_refusal_response())
    else:
        # Identify scheme
        scheme_id = identify_scheme(user_query)

        if not scheme_id:
            st.info("""
            **Please specify which HDFC scheme you're asking about:**

            - HDFC Equity Fund (Large-cap)
            - HDFC Flexi Cap Fund (Flexible cap)
            - HDFC Tax Saver (ELSS)
            - HDFC Liquid Fund (Debt/Liquid)
            - HDFC Balanced Advantage Fund (Balanced)

            Then ask your factual question about expense ratio, minimum SIP, exit load, lock-in period, benchmark, etc.
            """)
        else:
            # Identify fact type
            fact_type = identify_fact_type(user_query)

            if not fact_type:
                st.info("""
                **Please ask about specific facts:**

                - Expense ratio
                - Minimum SIP / Lumpsum
                - Exit load
                - Lock-in period
                - Benchmark
                - Riskometer rating
                - Statement download

                Example: "What is the expense ratio of HDFC Equity Fund?"
                """)
            else:
                # Get answer
                scheme_data = KNOWLEDGE_BASE[scheme_id]
                answer, source = get_answer(scheme_id, fact_type)

                if answer:
                    response = format_response(
                        scheme_data["name"],
                        fact_type,
                        answer,
                        source
                    )
                    st.success(response)
                else:
                    st.warning(f"I don't have information about '{fact_type}' for this scheme. Please try another question or contact HDFC Mutual Fund customer support.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 30px;">
<strong>Data Sources:</strong> Official HDFC Mutual Fund factsheets, KIM/SID documents, SEBI regulations, AMFI guidelines<br>
<strong>Last Updated:</strong> 2024 | <strong>Scope:</strong> 5 HDFC schemes | <strong>No PII stored</strong><br>
For official scheme information, visit: <a href="https://www.hdfcfund.com">HDFC Mutual Fund</a> | <a href="https://www.sebi.gov.in">SEBI</a> | <a href="https://www.amfiindia.com">AMFI</a>
</div>
""", unsafe_allow_html=True)
