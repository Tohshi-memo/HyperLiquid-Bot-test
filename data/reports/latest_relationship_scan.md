# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T07:37:33.150213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_24h` score `872.8253` n `108` status `ready` deltaP `9.9537` edge `72.7071` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `32.2103` n `108` status `ready` deltaP `-1.7728` edge `2.7499` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.872` n `62` status `ready` deltaP `34.6184` edge `0.6122` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5807` n `62` status `ready` deltaP `22.0201` edge `0.536` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6323` n `108` status `ready` deltaP `16.757` edge `0.2874` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3622` n `62` status `ready` deltaP `24.1319` edge `0.1193` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8542` n `62` status `ready` deltaP `32.0024` edge `0.0507` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.2508` n `62` status `ready` deltaP `4.8331` edge `0.1653` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0152` n `62` status `ready` deltaP `7.1808` edge `0.1556` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9528` n `62` status `ready` deltaP `24.7248` edge `0.0129` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8368` n `62` status `ready` deltaP `17.3191` edge `0.0974` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.4517` n `108` status `ready` deltaP `0.3952` edge `0.2907` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3989` n `62` status `ready` deltaP `20.0285` edge `0.0874` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.0598` n `108` status `ready` deltaP `7.5232` edge `0.3831` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.8984` n `62` status `ready` deltaP `2.1103` edge `0.1127` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.837` n `108` status `ready` deltaP `19.0831` edge `0.0182` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7364` n `108` status `ready` deltaP `12.7578` edge `0.0047` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.5965` n `62` status `ready` deltaP `26.8482` edge `0.0541` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.2581` n `108` status `ready` deltaP `10.2573` edge `0.0536` maxDD `-3.7778`
- `market_context_high->commodity_4h` score `0.2193` n `108` status `ready` deltaP `9.2818` edge `0.0264` maxDD `-1.6002`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
