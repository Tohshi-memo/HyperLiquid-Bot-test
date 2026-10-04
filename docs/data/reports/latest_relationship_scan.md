# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T22:22:28.623898+00:00`
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

- `market_context_high->unknown_1h` score `97.328` n `97` status `ready` deltaP `-0.1605` edge `8.1532` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7286` n `97` status `ready` deltaP `2.7564` edge `6.5735` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.1266` n `65` status `ready` deltaP `35.2955` edge `0.6289` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.9808` n `46` status `ready` deltaP `28.0193` edge `0.5435` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.3029` n `46` status `ready` deltaP `21.5806` edge `0.592` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.2127` n `65` status `ready` deltaP `23.1402` edge `0.5812` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.9362` n `65` status `ready` deltaP `19.0198` edge `0.3779` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.46` n `97` status `ready` deltaP `19.2765` edge `0.3135` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7366` n `65` status `ready` deltaP `26.5625` edge `0.1343` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.4789` n `65` status `ready` deltaP `23.7781` edge `0.1924` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.137` n `65` status `ready` deltaP `34.3528` edge `0.0586` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6631` n `65` status `ready` deltaP `10.9143` edge `0.1847` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.432` n `65` status `ready` deltaP `21.5174` edge `0.1008` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1393` n `65` status `ready` deltaP `26.3657` edge `0.0175` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9246` n `97` status `ready` deltaP `13.8327` edge `0.1132` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5342` n `65` status `ready` deltaP `5.3178` edge `0.1443` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4322` n `97` status `ready` deltaP `25.2782` edge `0.0265` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3716` n `46` status `ready` deltaP `25.536` edge `0.1074` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.3259` n `97` status `ready` deltaP `4.9959` edge `0.2561` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
