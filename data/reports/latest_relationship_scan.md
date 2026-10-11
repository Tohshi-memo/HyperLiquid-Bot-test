# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T14:07:28.812735+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7286`

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

- `market_context_high->unknown_24h` score `918.3939` n `45` status `ready` deltaP `-16.6666` edge `76.6803` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `49.9584` n `77` status `ready` deltaP `-9.1265` edge `4.2821` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9093` n `45` status `ready` deltaP `30.6944` edge `0.5807` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.0381` n `45` status `ready` deltaP `42.1875` edge `0.1625` maxDD `-0.2463`
- `market_context_high->crypto_major_24h` score `2.5742` n `45` status `ready` deltaP `-12.1875` edge `0.7261` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.4724` n `45` status `ready` deltaP `29.618` edge `0.0324` maxDD `-0.239`
- `market_context_high->fx_4h` score `1.0563` n `77` status `ready` deltaP `16.0932` edge `0.0091` maxDD `-0.2692`
- `market_context_high->unknown_1h` score `0.6231` n `82` status `ready` deltaP `-5.2285` edge `0.1204` maxDD `-1.0231`
- `market_context_high->commodity_4h` score `0.3495` n `77` status `ready` deltaP `10.5995` edge `0.0118` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2831` n `82` status `ready` deltaP `5.8639` edge `0.0096` maxDD `-0.3417`
- `market_context_high->fx_1h` score `-0.3584` n `82` status `ready` deltaP `-0.9822` edge `0.0009` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.4934` n `82` status `ready` deltaP `2.3551` edge `0.0466` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.5318` n `77` status `ready` deltaP `-2.1005` edge `0.0181` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.6205` n `82` status `ready` deltaP `0.7923` edge `0.0021` maxDD `-0.7275`
- `market_context_high->crypto_major_1h` score `-1.1177` n `82` status `ready` deltaP `-3.0378` edge `0.016` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.1649` n `77` status `ready` deltaP `-11.6488` edge `-0.0002` maxDD `-1.052`
- `market_context_high->index_1h` score `-1.2332` n `82` status `ready` deltaP `-10.2052` edge `-0.0039` maxDD `-0.5603`
- `market_context_high->equity_1h` score `-1.2734` n `82` status `ready` deltaP `-10.0956` edge `-0.009` maxDD `-2.2898`
- `market_context_high->crypto_major_4h` score `-1.3354` n `77` status `ready` deltaP `-6.0818` edge `0.0799` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.0718` n `77` status `ready` deltaP `-8.9662` edge `0.05` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
