# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T22:07:29.032208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.3268` n `97` status `ready` deltaP `-0.1605` edge `8.1531` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7202` n `97` status `ready` deltaP `2.7564` edge `6.5728` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.1736` n `65` status `ready` deltaP `35.4479` edge `0.6318` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.0846` n `46` status `ready` deltaP `28.1929` edge `0.551` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.4284` n `46` status `ready` deltaP `21.7542` edge `0.6013` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.2489` n `65` status `ready` deltaP `23.2927` edge `0.5832` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.0197` n `65` status `ready` deltaP `19.1934` edge `0.3837` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.507` n `97` status `ready` deltaP `19.4289` edge `0.3164` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7414` n `65` status `ready` deltaP `26.5625` edge `0.1347` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.5163` n `65` status `ready` deltaP `23.9306` edge `0.1945` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1516` n `65` status `ready` deltaP `34.5052` edge `0.0588` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6883` n `65` status `ready` deltaP `11.064` edge `0.1858` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.455` n `65` status `ready` deltaP `21.6698` edge `0.1017` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1525` n `65` status `ready` deltaP `26.5154` edge `0.0176` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9498` n `97` status `ready` deltaP `13.9824` edge `0.1143` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5402` n `65` status `ready` deltaP `5.3178` edge `0.1448` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4298` n `97` status `ready` deltaP `25.2782` edge `0.0263` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3708` n `46` status `ready` deltaP `25.536` edge `0.1073` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.3621` n `97` status `ready` deltaP `5.1484` edge `0.2581` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
