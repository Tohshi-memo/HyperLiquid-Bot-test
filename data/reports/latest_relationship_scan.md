# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T22:43:04.548796+00:00`
- Price records: `672`
- Market context records: `5085`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.126` n `73` status `ready` deltaP `26.8883` edge `0.8655` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `10.4158` n `105` status `ready` deltaP `0.6801` edge `0.9276` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `9.1509` n `93` status `ready` deltaP `21.4496` edge `0.7218` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.9651` n `93` status `ready` deltaP `16.9388` edge `0.5061` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.0075` n `93` status `ready` deltaP `15.398` edge `0.4999` maxDD `-10.4875`
- `market_context_high->equity_4h` score `2.4281` n `93` status `ready` deltaP `13.2885` edge `0.2269` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.3271` n `105` status `ready` deltaP `11.9048` edge `0.0844` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.8234` n `105` status `ready` deltaP `6.3815` edge `0.1106` maxDD `-4.0957`
- `market_context_high->index_1h` score `0.5391` n `105` status `ready` deltaP `8.4488` edge `0.0184` maxDD `-0.3843`
- `market_context_high->crypto_major_1h` score `0.5125` n `105` status `ready` deltaP `7.6205` edge `0.1251` maxDD `-5.8161`
- `market_context_high->metal_1h` score `0.4865` n `105` status `ready` deltaP `11.688` edge `0.0341` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.4503` n `93` status `ready` deltaP `8.3284` edge `0.0899` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.3464` n `93` status `ready` deltaP `8.8021` edge `0.0463` maxDD `-1.0893`
- `market_context_high->commodity_4h` score `-0.4412` n `93` status `ready` deltaP `8.9217` edge `0.0116` maxDD `-3.6276`
- `market_context_high->fx_24h` score `-0.7011` n `73` status `ready` deltaP `-1.1678` edge `-0.0059` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.7832` n `105` status `ready` deltaP `0.0142` edge `0.0028` maxDD `-1.4532`
- `market_context_high->commodity_24h` score `-1.2661` n `73` status `ready` deltaP `11.758` edge `0.0555` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.8767` n `105` status `ready` deltaP `-13.0197` edge `-0.0055` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.0988` n `93` status `ready` deltaP `-9.1398` edge `-0.0103` maxDD `-1.6267`
- `market_context_high->metal_24h` score `-4.5706` n `73` status `ready` deltaP `-5.1441` edge `-0.0062` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
