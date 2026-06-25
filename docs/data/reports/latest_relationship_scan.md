# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T12:52:31.977269+00:00`
- Price records: `672`
- Market context records: `4724`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `77.0959` n `144` status `ready` deltaP `14.9119` edge `6.367` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.7185` n `144` status `ready` deltaP `14.9221` edge `0.4981` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2322` n `135` status `ready` deltaP `16.5278` edge `0.2515` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2874` n `144` status `ready` deltaP `2.5574` edge `0.0257` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6327` n `144` status `ready` deltaP `4.9289` edge `-0.0017` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8473` n `144` status `ready` deltaP `9.7391` edge `0.0372` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.8986` n `144` status `ready` deltaP `-0.7452` edge `-0.002` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9384` n `144` status `ready` deltaP `3.5569` edge `0.0329` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1306` n `144` status `ready` deltaP `-1.4429` edge `0.0141` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2816` n `144` status `ready` deltaP `-4.9859` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.5822` n `144` status `ready` deltaP `-3.4847` edge `-0.0082` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.113` n `144` status `ready` deltaP `-0.341` edge `-0.0681` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.5828` n `144` status `ready` deltaP `-0.3826` edge `-0.0815` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.4123` n `135` status `ready` deltaP `17.1065` edge `0.0687` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4749` n `144` status `ready` deltaP `-5.776` edge `-0.0776` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8418` n `135` status `ready` deltaP `-13.3912` edge `-0.0182` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-7.9597` n `144` status `ready` deltaP `-2.0326` edge `-0.1412` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.5443` n `135` status `ready` deltaP `-11.331` edge `-0.099` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.7846` n `144` status `ready` deltaP `1.9817` edge `-0.2541` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.4758` n `144` status `ready` deltaP `-1.2026` edge `-0.245` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
