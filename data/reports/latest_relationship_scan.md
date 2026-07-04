# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T08:13:18.809985+00:00`
- Price records: `672`
- Market context records: `5643`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.7439` n `175` status `ready` deltaP `14.0783` edge `0.6427` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3269` n `175` status `ready` deltaP `21.7252` edge `0.0632` maxDD `-1.4633`
- `market_context_high->crypto_major_4h` score `0.6216` n `237` status `ready` deltaP `9.9374` edge `0.2148` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4771` n `237` status `ready` deltaP `7.5338` edge `0.1534` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.249` n `237` status `ready` deltaP `5.1547` edge `0.1298` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2719` n `237` status `ready` deltaP `1.749` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3463` n `237` status `ready` deltaP `5.6154` edge `0.0344` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5574` n `237` status `ready` deltaP `-0.6058` edge `0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5962` n `237` status `ready` deltaP `1.5861` edge `0.0359` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6241` n `237` status `ready` deltaP `4.131` edge `0.045` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9537` n `237` status `ready` deltaP `0.2792` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0548` n `237` status `ready` deltaP `-0.878` edge `-0.0055` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3256` n `237` status `ready` deltaP `1.0658` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.9843` n `237` status `ready` deltaP `-1.0792` edge `0.009` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.2732` n `175` status `ready` deltaP `11.0625` edge `0.0335` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0195` n `237` status `ready` deltaP `-14.0643` edge `-0.055` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.825` n `237` status `ready` deltaP `-2.3399` edge `-0.0356` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5786` n `175` status `ready` deltaP `4.2411` edge `0.0442` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2705` n `175` status `ready` deltaP `-11.1647` edge `-0.2498` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-13.1834` n `175` status `ready` deltaP `-17.2837` edge `-0.1225` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
