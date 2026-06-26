# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T17:37:36.721590+00:00`
- Price records: `672`
- Market context records: `4850`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.4922` n `110` status `ready` deltaP `10.4709` edge `1.0963` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.5943` n `100` status `ready` deltaP `28.7134` edge `0.8279` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `5.4403` n `100` status `ready` deltaP `18.2378` edge `0.467` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.3496` n `100` status `ready` deltaP `14.7622` edge `0.4698` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.288` n `89` status `ready` deltaP `25.7432` edge `0.3033` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.6285` n `100` status `ready` deltaP `12.3354` edge `0.1197` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7381` n `100` status `ready` deltaP `11.0671` edge `0.159` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5167` n `100` status `ready` deltaP `10.8293` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4438` n `110` status `ready` deltaP `6.3201` edge `0.1186` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4285` n `110` status `ready` deltaP `8.1709` edge `0.1027` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2075` n `110` status `ready` deltaP `4.2352` edge `0.0581` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.1656` n `100` status `ready` deltaP `5.7622` edge `0.0089` maxDD `-0.8166`
- `market_context_high->commodity_1h` score `-0.2246` n `110` status `ready` deltaP `3.2825` edge `0.0153` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2313` n `110` status `ready` deltaP `-0.2042` edge `0.0297` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5266` n `110` status `ready` deltaP `-0.2885` edge `0.0099` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7009` n `100` status `ready` deltaP `7.7561` edge `0.0071` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.331` n `110` status `ready` deltaP `-6.8672` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9803` n `89` status `ready` deltaP `-7.6799` edge `-0.0128` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8756` n `89` status `ready` deltaP `-9.4062` edge `-0.1589` maxDD `-24.2771`
- `market_context_high->commodity_24h` score `-5.5735` n `89` status `ready` deltaP `9.7827` edge `-0.0188` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
