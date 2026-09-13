# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T23:52:28.350865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12438`

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

- `news_risk_high->unknown_1h` score `435.532` n `82` status `ready` deltaP `-5.6996` edge `36.3745` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.999` n `82` status `ready` deltaP `36.8923` edge `1.3861` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3448` n `82` status `ready` deltaP `38.0236` edge `1.4223` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.3744` n `82` status `ready` deltaP `30.8915` edge `0.8366` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5667` n `82` status `ready` deltaP `54.6635` edge `0.2838` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.4782` n `56` status `ready` deltaP `39.8276` edge `0.191` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0206` n `82` status `ready` deltaP `29.0707` edge `0.27` maxDD `-0.6334`
- `market_context_high->fx_24h` score `2.1157` n `56` status `ready` deltaP `44.9507` edge `0.0338` maxDD `-1.3114`
- `risk_on_high->commodity_4h` score `1.8977` n `51` status `ready` deltaP `26.1029` edge `0.0191` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8977` n `51` status `ready` deltaP `26.1029` edge `0.0191` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5625` n `126` status `ready` deltaP `21.5278` edge `0.0285` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4837` n `82` status `ready` deltaP `13.5671` edge `0.0344` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.4135` n `137` status `ready` deltaP `9.1438` edge `0.0112` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.1797` n `52` status `ready` deltaP `6.4487` edge `0.0072` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1797` n `52` status `ready` deltaP `6.4487` edge `0.0072` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.127` n `126` status `ready` deltaP `8.1156` edge `0.0098` maxDD `-0.1435`
- `risk_on_high->metal_1h` score `0.0618` n `52` status `ready` deltaP `5.0668` edge `0.0047` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.0618` n `52` status `ready` deltaP `5.0668` edge `0.0047` maxDD `-0.1115`
- `risk_on_high->fx_1h` score `-0.0696` n `52` status `ready` deltaP `2.0958` edge `0.0025` maxDD `-0.0318`
- `risk_on_and_context->fx_1h` score `-0.0696` n `52` status `ready` deltaP `2.0958` edge `0.0025` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
