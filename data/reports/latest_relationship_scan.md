# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T06:22:30.109377+00:00`
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

- `market_context_high->unknown_24h` score `1156.554` n `113` status `ready` deltaP `10.7731` edge `96.3457` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.6145` n `113` status `ready` deltaP `-0.8714` edge `2.6109` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.9034` n `62` status `ready` deltaP `34.7709` edge `0.6138` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5253` n `62` status `ready` deltaP `21.8677` edge `0.5324` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6439` n `113` status `ready` deltaP `17.1717` edge `0.2856` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.2555` n `62` status `ready` deltaP `23.2639` edge `0.1162` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8128` n `62` status `ready` deltaP `31.5451` edge `0.0503` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.0685` n `62` status `ready` deltaP `3.9651` edge `0.1559` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0656` n `62` status `ready` deltaP `7.4802` edge `0.1578` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9397` n `62` status `ready` deltaP `24.5751` edge `0.0128` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7942` n `62` status `ready` deltaP `16.8618` edge `0.0969` maxDD `-2.7837`
- `market_context_high->crypto_major_24h` score `1.7921` n `113` status `ready` deltaP `8.089` edge `0.3928` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `1.7103` n `113` status `ready` deltaP `2.1274` edge `0.3007` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.346` n `62` status `ready` deltaP `19.2663` edge `0.0857` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9727` n `62` status `ready` deltaP `2.5594` edge `0.1159` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.909` n `113` status `ready` deltaP `19.8778` edge `0.0189` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7841` n `113` status `ready` deltaP `13.2942` edge `0.0051` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.7282` n `62` status `ready` deltaP `27.7162` edge `0.0652` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.3966` n `113` status `ready` deltaP `11.0026` edge `0.0297` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.237` n `113` status `ready` deltaP `9.3358` edge `0.0464` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
