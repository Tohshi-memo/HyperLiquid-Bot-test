# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T07:52:31.556532+00:00`
- Price records: `672`
- Market context records: `6796`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11656`

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

- `market_context_high->unknown_24h` score `0.8527` n `176` status `ready` deltaP `-1.3731` edge `0.4937` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1812` n `176` status `ready` deltaP `8.8384` edge `0.143` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2551` n `185` status `ready` deltaP `6.4986` edge `0.0214` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.4189` n `185` status `ready` deltaP `3.4965` edge `0.0182` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4192` n `185` status `ready` deltaP `-0.7857` edge `0.0` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6603` n `185` status `ready` deltaP `-1.8587` edge `-0.0007` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.7073` n `185` status `ready` deltaP `-1.8255` edge `-0.0102` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7117` n `185` status `ready` deltaP `-5.2929` edge `-0.0031` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.2966` n `185` status `ready` deltaP `2.2326` edge `-0.0185` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3857` n `181` status `ready` deltaP `4.6969` edge `-0.0026` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.482` n `181` status `ready` deltaP `3.1515` edge `-0.0208` maxDD `-5.8833`
- `market_context_high->commodity_4h` score `-1.4827` n `181` status `ready` deltaP `-3.0016` edge `-0.0211` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5335` n `185` status `ready` deltaP `-4.9935` edge `-0.0044` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6582` n `181` status `ready` deltaP `-5.3994` edge `-0.0073` maxDD `-5.4666`
- `market_context_high->crypto_major_4h` score `-3.0472` n `181` status `ready` deltaP `1.0182` edge `-0.066` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.1181` n `181` status `ready` deltaP `0.1229` edge `-0.0561` maxDD `-19.5576`
- `market_context_high->unknown_4h` score `-3.316` n `181` status `ready` deltaP `-13.4963` edge `0.0502` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4869` n `176` status `ready` deltaP `-9.6117` edge `-0.0062` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.5005` n `181` status `ready` deltaP `0.5609` edge `-0.1515` maxDD `-27.3382`
- `market_context_high->metal_24h` score `-9.2981` n `176` status `ready` deltaP `-19.192` edge `-0.2156` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
