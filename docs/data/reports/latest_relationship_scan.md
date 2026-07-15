# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T15:37:32.452495+00:00`
- Price records: `672`
- Market context records: `6830`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9225` n `176` status `ready` deltaP `-1.5467` edge `0.5038` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1913` n `176` status `ready` deltaP `9.8801` edge `0.1369` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1994` n `208` status `ready` deltaP `5.7549` edge `0.031` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3189` n `208` status `ready` deltaP `3.5324` edge `0.0263` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3315` n `208` status `ready` deltaP `0.7802` edge `0.0008` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.8696` n `208` status `ready` deltaP `-3.184` edge `-0.0051` maxDD `-1.8127`
- `market_context_high->metal_1h` score `-0.9445` n `208` status `ready` deltaP `-5.7779` edge `-0.0087` maxDD `-1.9098`
- `market_context_high->fx_4h` score `-1.1837` n `198` status `ready` deltaP `8.0131` edge `0.0012` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2014` n `208` status `ready` deltaP `-3.4201` edge `-0.0089` maxDD `-2.1399`
- `market_context_high->unknown_1h` score `-1.6103` n `208` status `ready` deltaP `-3.8231` edge `-0.0186` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.939` n `198` status `ready` deltaP `1.1256` edge `-0.0312` maxDD `-8.6582`
- `market_context_high->commodity_4h` score `-2.2923` n `198` status `ready` deltaP `-4.0112` edge `-0.0153` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-2.4823` n `208` status `ready` deltaP `0.0403` edge `-0.037` maxDD `-9.2766`
- `market_context_high->metal_4h` score `-2.6548` n `198` status `ready` deltaP `-2.7362` edge `-0.0238` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9075` n `198` status `ready` deltaP `0.4588` edge `-0.0431` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.0741` n `198` status `ready` deltaP `0.6206` edge `-0.0399` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2405` n `198` status `ready` deltaP `-10.5122` edge `0.0366` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.1395` n `198` status `ready` deltaP `-1.238` edge `-0.191` maxDD `-40.0285`
- `market_context_high->metal_24h` score `-9.4463` n `176` status `ready` deltaP `-20.4072` edge `-0.2265` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
