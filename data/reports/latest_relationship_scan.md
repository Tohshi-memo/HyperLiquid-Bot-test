# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T19:52:27.410200+00:00`
- Price records: `672`
- Market context records: `6952`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11729`

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

- `market_context_high->fx_1h` score `-0.26` n `237` status `ready` deltaP `2.0345` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.37` n `237` status `ready` deltaP `2.5797` edge `0.0218` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7247` n `237` status `ready` deltaP `-0.2388` edge `-0.0002` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7442` n `237` status `ready` deltaP `-2.3895` edge `-0.0027` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.9533` n `234` status `ready` deltaP `11.4082` edge `0.0081` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2389` n `237` status `ready` deltaP `2.7294` edge `0.0138` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2909` n `237` status `ready` deltaP `-2.9738` edge `-0.0156` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.5769` n `237` status `ready` deltaP `-1.8312` edge `-0.0291` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.5882` n `223` status `ready` deltaP `-8.9134` edge `0.3056` maxDD `-18.3163`
- `market_context_high->commodity_4h` score `-1.6515` n `234` status `ready` deltaP `-4.3581` edge `-0.0337` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7955` n `234` status `ready` deltaP `7.4448` edge `-0.0145` maxDD `-11.8926`
- `market_context_high->equity_1h` score `-2.0224` n `237` status `ready` deltaP `2.0888` edge `-0.0178` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.1211` n `234` status `ready` deltaP `3.4032` edge `0.0037` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.9714` n `234` status `ready` deltaP `0.2449` edge `-0.0215` maxDD `-20.8861`
- `market_context_high->unknown_4h` score `-3.2401` n `234` status `ready` deltaP `-8.4676` edge `0.023` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.5906` n `234` status `ready` deltaP `-1.3094` edge `-0.0494` maxDD `-22.5094`
- `market_context_high->commodity_24h` score `-3.7094` n `223` status `ready` deltaP `-6.0736` edge `-0.0818` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.383` n `223` status `ready` deltaP `-7.098` edge `-0.0143` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5761` n `234` status `ready` deltaP `4.0233` edge `-0.0966` maxDD `-65.121`
- `market_context_high->metal_24h` score `-9.3883` n `223` status `ready` deltaP `-14.1796` edge `-0.1231` maxDD `-38.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
