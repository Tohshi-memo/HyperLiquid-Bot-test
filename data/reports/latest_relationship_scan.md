# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T09:52:29.184698+00:00`
- Price records: `672`
- Market context records: `4712`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7424`

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

- `market_context_high->unknown_1h` score `76.94` n `144` status `ready` deltaP `14.0137` edge `6.36` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.0614` n `143` status `ready` deltaP `13.4744` edge `0.453` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.866` n `135` status `ready` deltaP `14.9653` edge `0.2314` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3147` n `144` status `ready` deltaP `2.258` edge `0.0242` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6932` n `143` status `ready` deltaP `4.5455` edge `-0.0069` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9606` n `143` status `ready` deltaP `-1.8911` edge `-0.0023` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-0.9617` n `143` status `ready` deltaP `8.77` edge `0.029` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.1507` n `143` status `ready` deltaP `2.4742` edge `0.0129` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.2013` n `144` status `ready` deltaP `-1.7423` edge `0.0102` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.3331` n `144` status `ready` deltaP `-5.5847` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6457` n `144` status `ready` deltaP `-3.9338` edge `-0.0105` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2135` n `144` status `ready` deltaP `-1.0895` edge `-0.076` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.7216` n `144` status `ready` deltaP `-1.2808` edge `-0.0933` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3823` n `135` status `ready` deltaP `17.1065` edge `0.0712` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4581` n `144` status `ready` deltaP `-5.6263` edge `-0.0772` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7973` n `135` status `ready` deltaP `-13.044` edge `-0.0168` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0886` n `143` status `ready` deltaP `-2.3218` edge `-0.1558` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4011` n `135` status `ready` deltaP `-10.6366` edge `-0.0917` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.6218` n `143` status `ready` deltaP `3.4176` edge `-0.2428` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.8665` n `143` status `ready` deltaP `-2.7162` edge `-0.285` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
