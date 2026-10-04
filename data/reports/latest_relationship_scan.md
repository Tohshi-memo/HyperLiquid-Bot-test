# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T12:07:29.369066+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `140.4806` n `78` status `ready` deltaP `5.8122` edge `11.6865` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `115.4604` n `90` status `ready` deltaP `-1.0113` edge `9.6699` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.5935` n `46` status `ready` deltaP `28.6987` edge `0.9021` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.0918` n `46` status `ready` deltaP `35.1373` edge `0.7553` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.7389` n `65` status `ready` deltaP `38.3443` edge `0.6596` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.6088` n `61` status `ready` deltaP `25.7343` edge `0.6392` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.2555` n `65` status `ready` deltaP `23.75` edge `0.5807` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2018` n `78` status `ready` deltaP `25.5238` edge `0.417` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.3265` n `61` status `ready` deltaP `29.1667` edge `0.1661` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8826` n `65` status `ready` deltaP `26.522` edge `0.208` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.1564` n `78` status `ready` deltaP `10.4167` edge `0.335` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.116` n `65` status `ready` deltaP `33.8954` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.006` n `65` status `ready` deltaP `13.0101` edge `0.1993` maxDD `-1.5096`
- `market_context_high->equity_24h` score `2.7766` n `46` status `ready` deltaP `6.2047` edge `0.2897` maxDD `-6.3081`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4521` n `90` status `ready` deltaP `16.8563` edge `0.137` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.7669` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6374` n `65` status `ready` deltaP `5.4675` edge `0.1519` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3689` n `46` status `ready` deltaP `25.7096` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.055` n `90` status `ready` deltaP `16.1144` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
