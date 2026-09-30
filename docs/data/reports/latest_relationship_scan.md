# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T03:52:28.453761+00:00`
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

- `news_risk_high->unknown_24h` score `1055.6008` n `132` status `ready` deltaP `1.9097` edge `87.954` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.9129` n `132` status `ready` deltaP `30.4292` edge `1.4775` maxDD `-1.0093`
- `news_risk_high->crypto_major_24h` score `9.0279` n `132` status `ready` deltaP `25.4104` edge `0.8983` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `8.9053` n `132` status `ready` deltaP `29.9243` edge `0.7775` maxDD `-9.4579`
- `news_risk_high->index_24h` score `4.1182` n `132` status `ready` deltaP `36.2847` edge `0.1491` maxDD `-0.4916`
- `news_risk_high->equity_4h` score `3.003` n `135` status `ready` deltaP `30.0858` edge `0.2098` maxDD `-9.143`
- `news_risk_high->metal_24h` score `2.4525` n `132` status `ready` deltaP `27.8883` edge `0.2559` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.122` n `135` status `ready` deltaP `12.1793` edge `0.3616` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1581` n `135` status `ready` deltaP `9.5509` edge `0.1239` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9739` n `135` status `ready` deltaP `10.0` edge `0.0768` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5341` n `135` status `ready` deltaP `9.267` edge `0.0115` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0213` n `135` status `ready` deltaP `8.1685` edge `0.0291` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.41` n `135` status `ready` deltaP `3.0882` edge `0.0735` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.467` n `135` status `ready` deltaP `1.3074` edge `0.0153` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2389` n `135` status `ready` deltaP `-7.2369` edge `0.0302` maxDD `-2.9297`
- `news_risk_high->crypto_major_4h` score `-1.4225` n `135` status `ready` deltaP `-3.0736` edge `0.1096` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4369` n `135` status `ready` deltaP `6.7706` edge `-0.008` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8468` n `135` status `ready` deltaP `-8.9676` edge `-0.0095` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9176` n `135` status `ready` deltaP `-10.1031` edge `-0.0044` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2459` n `135` status `ready` deltaP `-8.8449` edge `0.0129` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
