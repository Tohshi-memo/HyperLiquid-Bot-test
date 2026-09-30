# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T03:37:28.810822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7162`

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

- `news_risk_high->unknown_24h` score `1111.024` n `132` status `ready` deltaP `1.9097` edge `92.5726` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.0624` n `132` status `ready` deltaP `30.6029` edge `1.4888` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.1426` n `132` status `ready` deltaP `25.584` edge `0.9067` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `8.9755` n `132` status `ready` deltaP `30.0979` edge `0.7822` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.1417` n `132` status `ready` deltaP `36.4583` edge `0.1499` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `2.9848` n `135` status `ready` deltaP `29.9333` edge `0.2093` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.4732` n `132` status `ready` deltaP `28.0619` edge `0.2574` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.1328` n `135` status `ready` deltaP `12.1793` edge `0.3625` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1485` n `135` status `ready` deltaP `9.5509` edge `0.1231` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9583` n `135` status `ready` deltaP `9.8503` edge `0.0765` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5341` n `135` status `ready` deltaP `9.267` edge `0.0115` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0347` n `135` status `ready` deltaP `8.016` edge `0.029` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4364` n `135` status `ready` deltaP `2.9385` edge `0.0723` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4814` n `135` status `ready` deltaP `1.1577` edge `0.0151` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2381` n `135` status `ready` deltaP `-7.2369` edge `0.0303` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4163` n `135` status `ready` deltaP `-3.0736` edge `0.1104` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4471` n `135` status `ready` deltaP `6.6181` edge `-0.0083` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8382` n `135` status `ready` deltaP `-8.8179` edge `-0.0094` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9044` n `135` status `ready` deltaP `-9.9534` edge `-0.0043` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2466` n `135` status `ready` deltaP `-8.8449` edge `0.0128` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
