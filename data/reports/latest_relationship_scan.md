# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T08:07:25.401050+00:00`
- Price records: `672`
- Market context records: `3053`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.6746` n `99` status `ready` deltaP `14.2834` edge `2.436` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.5721` n `99` status `ready` deltaP `44.9811` edge `0.8552` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.5287` n `99` status `ready` deltaP `24.6686` edge `1.0094` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.2104` n `99` status `ready` deltaP `25.4577` edge `1.4145` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.6388` n `99` status `ready` deltaP `23.8321` edge `0.7699` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5824` n `131` status `ready` deltaP `17.6422` edge `0.1623` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1661` n `136` status `ready` deltaP `1.0083` edge `0.0217` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3926` n `131` status `ready` deltaP `2.3726` edge `0.0568` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5436` n `136` status `ready` deltaP `2.9676` edge `0.0168` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5444` n `136` status `ready` deltaP `-4.8345` edge `-0.0003` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.5832` n `136` status `ready` deltaP `5.9088` edge `0.0988` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7938` n `136` status `ready` deltaP `2.6286` edge `0.0261` maxDD `-8.6319`
- `market_context_high->unknown_1h` score `-0.9276` n `136` status `ready` deltaP `4.4822` edge `-0.0341` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9301` n `136` status `ready` deltaP `4.491` edge `0.0771` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0821` n `131` status `ready` deltaP `-7.7138` edge `-0.0036` maxDD `-1.0295`
- `market_context_high->metal_1h` score `-1.1364` n `136` status `ready` deltaP `-1.092` edge `-0.0016` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.1537` n `99` status `ready` deltaP `0.4577` edge `-0.012` maxDD `-0.6418`
- `market_context_high->index_4h` score `-1.1705` n `131` status `ready` deltaP `11.3678` edge `0.0589` maxDD `-17.4468`
- `market_context_high->crypto_alt_4h` score `-3.0295` n `131` status `ready` deltaP `18.8373` edge `0.2905` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.1348` n `131` status `ready` deltaP `9.2359` edge `0.049` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
