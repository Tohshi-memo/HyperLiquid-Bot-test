# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T16:52:28.955684+00:00`
- Price records: `672`
- Market context records: `6835`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `0.949` n `176` status `ready` deltaP `-1.5467` edge `0.5072` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1396` n `176` status `ready` deltaP `9.5329` edge `0.1349` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3105` n `213` status `ready` deltaP `1.1533` edge `0.001` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.4539` n `213` status `ready` deltaP `4.4938` edge `0.0182` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.5349` n `213` status `ready` deltaP `2.3165` edge `0.0164` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.9243` n `213` status `ready` deltaP `-3.2217` edge `-0.0059` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0138` n `213` status `ready` deltaP `-6.4603` edge `-0.011` maxDD `-2.0728`
- `market_context_high->fx_4h` score `-1.1065` n `203` status `ready` deltaP `9.1824` edge `0.0033` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1289` n `213` status `ready` deltaP `-2.8204` edge `-0.0068` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.5935` n `213` status `ready` deltaP `-3.2829` edge `-0.0208` maxDD `-3.2083`
- `market_context_high->index_4h` score `-2.222` n `203` status `ready` deltaP `0.4821` edge `-0.0365` maxDD `-10.7939`
- `market_context_high->commodity_4h` score `-2.3374` n `203` status `ready` deltaP `-4.6204` edge `-0.015` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7256` n `203` status `ready` deltaP `-3.3912` edge `-0.0285` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9272` n `203` status `ready` deltaP `0.2013` edge `-0.0439` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1234` n `203` status `ready` deltaP `0.2125` edge `-0.0435` maxDD `-20.6678`
- `market_context_high->equity_1h` score `-3.1864` n `213` status `ready` deltaP `-0.6023` edge `-0.0435` maxDD `-13.1084`
- `market_context_high->unknown_4h` score `-3.2041` n `203` status `ready` deltaP `-9.6075` edge `0.0336` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6202` n `203` status `ready` deltaP `-1.782` edge `-0.2232` maxDD `-52.3497`
- `market_context_high->metal_24h` score `-9.338` n `176` status `ready` deltaP `-19.5392` edge `-0.2184` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
