# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T07:07:29.248952+00:00`
- Price records: `672`
- Market context records: `3155`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8852`

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

- `market_context_high->commodity_24h` score `14.1017` n `110` status `ready` deltaP `47.6799` edge `0.9001` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.2142` n `110` status `ready` deltaP `14.5392` edge `2.4666` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.9813` n `110` status `ready` deltaP `22.3705` edge `0.8981` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.6634` n `110` status `ready` deltaP `31.4899` edge `0.8998` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.0326` n `110` status `ready` deltaP `12.9483` edge `1.4005` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.8883` n `143` status `ready` deltaP `18.8534` edge `0.1608` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1994` n `143` status `ready` deltaP `4.646` edge `0.0279` maxDD `-1.7142`
- `market_context_high->fx_24h` score `-0.0807` n `110` status `ready` deltaP `7.9103` edge `0.0008` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5247` n `143` status `ready` deltaP `3.4955` edge `0.0157` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.5641` n `143` status `ready` deltaP `6.2927` edge `0.124` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.9207` n `143` status `ready` deltaP `2.4968` edge `0.0139` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9988` n `143` status `ready` deltaP `3.1405` edge `0.0773` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.1134` n `143` status `ready` deltaP `-10.3922` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1597` n `143` status `ready` deltaP `11.9596` edge `0.0625` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.319` n `143` status `ready` deltaP `7.1711` edge `0.0645` maxDD `-14.7778`
- `market_context_high->fx_4h` score `-1.4501` n `143` status `ready` deltaP `-13.3848` edge `-0.0082` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.075` n `143` status `ready` deltaP `-4.1477` edge `-0.0059` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.8921` n `143` status `ready` deltaP `13.1524` edge `0.0721` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.8928` n `143` status `ready` deltaP `19.412` edge `0.434` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.283` n `143` status `ready` deltaP `1.5536` edge `-0.0813` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
