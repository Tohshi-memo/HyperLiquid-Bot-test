# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T07:07:23.228281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5976`

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

- `market_context_high->unknown_4h` score `42.4347` n `85` status `ready` deltaP `-12.9484` edge `3.6806` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6046` n `73` status `ready` deltaP `38.3656` edge `0.5875` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.6181` n `73` status `ready` deltaP `13.3205` edge `1.2027` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.5338` n `85` status `ready` deltaP `21.702` edge `0.0115` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.2471` n `97` status `ready` deltaP `6.4665` edge `0.0017` maxDD `-0.271`
- `market_context_high->index_24h` score `0.0738` n `73` status `ready` deltaP `10.3501` edge `0.0998` maxDD `-1.7476`
- `market_context_high->commodity_4h` score `-0.0469` n `85` status `ready` deltaP `6.1693` edge `0.0062` maxDD `-1.6002`
- `market_context_high->crypto_major_4h` score `-0.0792` n `85` status `ready` deltaP `5.5327` edge `0.143` maxDD `-10.2028`
- `market_context_high->commodity_1h` score `-0.1177` n `97` status `ready` deltaP `2.5094` edge `0.0069` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.1255` n `97` status `ready` deltaP `4.9046` edge `0.0401` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.5682` n `97` status `ready` deltaP `-2.1622` edge `0.0011` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.75` n `73` status `ready` deltaP `0.8014` edge `0.047` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8497` n `97` status `ready` deltaP `-2.6282` edge `0.0245` maxDD `-4.9401`
- `market_context_high->fx_24h` score `-1.1883` n `73` status `ready` deltaP `1.0321` edge `0.0021` maxDD `-1.9066`
- `market_context_high->crypto_alt_24h` score `-1.3921` n `73` status `ready` deltaP `0.4138` edge `0.43` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.4024` n `85` status `ready` deltaP `-13.7483` edge `0.0133` maxDD `-1.1153`
- `market_context_high->index_4h` score `-1.4783` n `85` status `ready` deltaP `-14.401` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7117` n `97` status `ready` deltaP `-8.0314` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.8402` n `97` status `ready` deltaP `-8.8647` edge `-0.0073` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-3.0732` n `85` status `ready` deltaP `-13.2873` edge `-0.0086` maxDD `-6.3804`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
