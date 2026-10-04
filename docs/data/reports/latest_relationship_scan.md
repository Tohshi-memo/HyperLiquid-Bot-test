# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T11:52:32.900964+00:00`
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

- `market_context_high->unknown_4h` score `144.6966` n `77` status `ready` deltaP `6.8419` edge `12.0268` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `118.6784` n `89` status `ready` deltaP `-0.2371` edge `9.9329` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.7178` n `46` status `ready` deltaP `28.8723` edge `0.9113` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.1897` n `46` status `ready` deltaP `35.311` edge `0.7623` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.7751` n `65` status `ready` deltaP `38.4967` edge `0.6616` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.7496` n `60` status `ready` deltaP `25.7986` edge `0.6505` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.2723` n `65` status `ready` deltaP `23.75` edge `0.5821` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2443` n `77` status `ready` deltaP `25.4098` edge `0.4213` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.3848` n `60` status `ready` deltaP `29.3403` edge `0.1698` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8984` n `65` status `ready` deltaP `26.6745` edge `0.2083` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.3944` n `77` status `ready` deltaP `11.2825` edge `0.3449` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1282` n `65` status `ready` deltaP `34.0479` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0036` n `65` status `ready` deltaP `13.0101` edge `0.1991` maxDD `-1.5096`
- `market_context_high->equity_24h` score `2.8504` n `46` status `ready` deltaP `6.3783` edge `0.2947` maxDD `-6.3081`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4288` n `89` status `ready` deltaP `16.5192` edge `0.1373` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.7669` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6362` n `65` status `ready` deltaP `5.4675` edge `0.1518` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3689` n `46` status `ready` deltaP `25.7096` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.0211` n `89` status `ready` deltaP `15.69` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
