# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T11:37:28.587512+00:00`
- Price records: `672`
- Market context records: `4719`
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

- `market_context_high->unknown_1h` score `77.0395` n `144` status `ready` deltaP `14.6125` edge `6.3643` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2615` n `144` status `ready` deltaP `14.1599` edge `0.4651` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.13` n `135` status `ready` deltaP `16.1806` edge `0.2453` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2835` n `144` status `ready` deltaP `2.7071` edge `0.0252` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6603` n `144` status `ready` deltaP `4.624` edge `-0.0032` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8889` n `144` status `ready` deltaP `9.4343` edge `0.0339` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9232` n `144` status `ready` deltaP `-1.2026` edge `-0.0021` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-1.0137` n `144` status `ready` deltaP `3.0996` edge `0.0263` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1498` n `144` status `ready` deltaP `-1.5926` edge `0.0135` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2816` n `144` status `ready` deltaP `-4.9859` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6361` n `144` status `ready` deltaP `-3.9338` edge `-0.0097` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.134` n `144` status `ready` deltaP `-0.4907` edge `-0.0698` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.6319` n `144` status `ready` deltaP `-0.682` edge `-0.0858` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3907` n `135` status `ready` deltaP `17.1065` edge `0.0705` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4006` n `144` status `ready` deltaP `-5.1772` edge `-0.0754` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8069` n `135` status `ready` deltaP `-13.044` edge `-0.0176` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.0097` n `144` status `ready` deltaP `-2.185` edge `-0.1466` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4299` n `135` status `ready` deltaP `-10.6366` edge `-0.0941` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.6943` n `144` status `ready` deltaP `2.7439` edge `-0.2476` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.6371` n `144` status `ready` deltaP `-1.9648` edge `-0.2606` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
