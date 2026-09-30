# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T07:07:31.935626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7458`

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

- `news_risk_high->unknown_24h` score `1105.828` n `135` status `ready` deltaP `1.9097` edge `92.1396` maxDD `0.0`
- `market_context_high->unknown_1h` score `709.4456` n `34` status `ready` deltaP `9.7305` edge `59.0556` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2917` n `135` status `ready` deltaP `28.5532` edge `1.3549` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.229` n `135` status `ready` deltaP `28.206` edge `0.7326` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.7589` n `135` status `ready` deltaP `23.9931` edge `0.802` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.8437` n `135` status `ready` deltaP `34.3981` edge `0.1388` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.4915` n `135` status `ready` deltaP `26.5741` edge `0.2412` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9762` n `135` status `ready` deltaP `29.7809` edge `0.2096` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.9386` n `135` status `ready` deltaP `11.4171` edge `0.3514` maxDD `-15.9436`
- `market_context_high->fx_1h` score `1.3804` n `34` status `ready` deltaP `19.3466` edge `0.0083` maxDD `-0.113`
- `market_context_high->crypto_alt_1h` score `1.201` n `34` status `ready` deltaP `8.3744` edge `0.1057` maxDD `-3.5821`
- `news_risk_high->crypto_alt_1h` score `1.1401` n `135` status `ready` deltaP `9.5509` edge `0.1224` maxDD `-4.2849`
- `market_context_high->crypto_major_1h` score `0.9618` n `34` status `ready` deltaP `4.3413` edge `0.1122` maxDD `-3.546`
- `news_risk_high->equity_1h` score `0.932` n `135` status `ready` deltaP `9.5509` edge `0.0763` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.6778` n `34` status `ready` deltaP `11.3156` edge `0.054` maxDD `-2.4027`
- `news_risk_high->index_1h` score `0.5329` n `135` status `ready` deltaP `9.267` edge `0.0114` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.4724` n `34` status `ready` deltaP `6.6837` edge `0.0169` maxDD `-0.4338`
- `market_context_high->index_1h` score `0.0304` n `34` status `ready` deltaP `3.6897` edge `0.013` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.115` n `135` status `ready` deltaP `7.1014` edge `0.0284` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.506` n `135` status `ready` deltaP `2.4894` edge `0.0695` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
