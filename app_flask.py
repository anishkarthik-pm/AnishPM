from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Knowledge base (same as Streamlit version)
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

INVESTMENT_ADVICE_PATTERNS = [
    "should i buy", "should i sell", "should i invest", "which fund should",
    "recommend", "best fund", "which is better", "compare", "performance",
    "will return", "will earn", "expected return", "future performance",
    "portfolio", "how much money", "when to buy", "when to sell"
]

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
    "statement_download": ["download statement", "statement", "statement download"],
}

def identify_scheme(query):
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

def identify_fact_type(query):
    query_lower = query.lower()
    for fact_type, patterns in FACTUAL_PATTERNS.items():
        for pattern in patterns:
            if pattern in query_lower:
                return fact_type
    return None

def is_investment_advice_query(query):
    query_lower = query.lower()
    for pattern in INVESTMENT_ADVICE_PATTERNS:
        if pattern in query_lower:
            return True
    return False

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HDFC Mutual Fund FAQ</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .container {
                background: white;
                border-radius: 10px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                max-width: 700px;
                width: 100%;
                padding: 30px;
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
                font-size: 28px;
            }
            .subtitle {
                color: #666;
                margin-bottom: 20px;
                font-size: 14px;
            }
            .disclaimer {
                background: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 15px;
                margin: 20px 0;
                border-radius: 4px;
                font-size: 13px;
                color: #333;
            }
            .examples {
                background: #f8f9fa;
                border-left: 4px solid #007bff;
                padding: 15px;
                margin: 20px 0;
                border-radius: 4px;
                font-size: 13px;
            }
            .examples h3 {
                color: #007bff;
                margin-bottom: 10px;
                font-size: 14px;
            }
            .examples ul {
                margin-left: 20px;
                color: #555;
            }
            .examples li {
                margin: 5px 0;
            }
            .input-group {
                display: flex;
                gap: 10px;
                margin: 20px 0;
            }
            input {
                flex: 1;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 14px;
            }
            input:focus {
                outline: none;
                border-color: #667eea;
            }
            button {
                padding: 12px 30px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
                font-weight: bold;
            }
            button:hover {
                background: #764ba2;
            }
            .response {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                font-size: 14px;
                line-height: 1.6;
            }
            .response.success {
                background: #d4edda;
                border-left: 4px solid #28a745;
                color: #155724;
            }
            .response.error {
                background: #f8d7da;
                border-left: 4px solid #dc3545;
                color: #721c24;
            }
            .response.info {
                background: #d1ecf1;
                border-left: 4px solid #17a2b8;
                color: #0c5460;
            }
            .source {
                margin-top: 10px;
                padding: 10px;
                background: rgba(0,0,0,0.05);
                border-radius: 3px;
                font-size: 12px;
            }
            .source a {
                color: #667eea;
                text-decoration: none;
            }
            .source a:hover {
                text-decoration: underline;
            }
            .loading {
                display: none;
                color: #667eea;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 HDFC Mutual Fund FAQ</h1>
            <p class="subtitle">Facts-Only Assistant for HDFC Schemes</p>

            <div class="disclaimer">
                <strong>⚠️ FACTS-ONLY • NO INVESTMENT ADVICE</strong><br>
                This assistant provides factual information about HDFC schemes from official sources only.
                It does NOT provide investment advice or recommendations.
            </div>

            <div class="examples">
                <h3>📋 Example Questions:</h3>
                <ul>
                    <li>"What is the expense ratio of HDFC Equity Fund?"</li>
                    <li>"What is the lock-in period for HDFC Tax Saver?"</li>
                    <li>"Minimum SIP for HDFC Liquid Fund?"</li>
                    <li>"How do I download my statement?"</li>
                </ul>
            </div>

            <div class="input-group">
                <input type="text" id="query" placeholder="Ask your question about HDFC schemes..."
                       onkeypress="if(event.key==='Enter') ask()">
                <button onclick="ask()">Ask</button>
            </div>

            <div id="loading" class="loading">Thinking...</div>
            <div id="response"></div>
        </div>

        <script>
            function ask() {
                const query = document.getElementById('query').value;
                if (!query.trim()) return;

                document.getElementById('loading').style.display = 'block';
                document.getElementById('response').innerHTML = '';

                fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: query})
                })
                .then(r => r.json())
                .then(data => {
                    document.getElementById('loading').style.display = 'none';
                    let html = '<div class="response ' + data.type + '">';
                    html += data.message;
                    if (data.source) {
                        html += '<div class="source">📎 Source: <a href="' + data.source + '" target="_blank">' +
                                data.source.split('/').pop() + '</a></div>';
                    }
                    html += '</div>';
                    document.getElementById('response').innerHTML = html;
                })
                .catch(e => {
                    document.getElementById('loading').style.display = 'none';
                    document.getElementById('response').innerHTML =
                        '<div class="response error">Error: ' + e + '</div>';
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '').strip()

    if not query:
        return jsonify({'type': 'error', 'message': 'Please enter a question.'})

    # Check for investment advice
    if is_investment_advice_query(query):
        return jsonify({
            'type': 'error',
            'message': '❌ I can only provide factual information. I cannot offer investment advice or recommendations. For investment guidance, please consult a qualified financial advisor or visit https://www.sebi.gov.in/investor-education'
        })

    # Identify scheme
    scheme_id = identify_scheme(query)
    if not scheme_id:
        return jsonify({
            'type': 'info',
            'message': 'Please specify which HDFC scheme: Equity Fund, Flexi Cap Fund, Tax Saver, Liquid Fund, or Balanced Advantage Fund.'
        })

    # Identify fact type
    fact_type = identify_fact_type(query)
    if not fact_type:
        return jsonify({
            'type': 'info',
            'message': 'Please ask about: expense ratio, minimum SIP, exit load, lock-in period, benchmark, or riskometer rating.'
        })

    # Get answer
    scheme_data = KNOWLEDGE_BASE[scheme_id]
    if fact_type in scheme_data['facts']:
        answer = scheme_data['facts'][fact_type]
        source = scheme_data['sources'].get(fact_type, '')
        return jsonify({
            'type': 'success',
            'message': f"<strong>{scheme_data['name']} - {fact_type.replace('_', ' ').title()}:</strong><br><br>{answer}<br><br><em>Last updated from official sources.</em>",
            'source': source
        })
    else:
        return jsonify({
            'type': 'error',
            'message': f"No information available about '{fact_type}' for this scheme."
        })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 HDFC Mutual Fund FAQ Assistant")
    print("="*60)
    print("\n📍 Open your browser at: http://localhost:5000")
    print("\n💡 Try asking: 'What is the expense ratio of HDFC Equity Fund?'")
    print("\n⚠️  Press Ctrl+C to stop the server")
    print("\n" + "="*60 + "\n")
    app.run(debug=True, port=5000)
