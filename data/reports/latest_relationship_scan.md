# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T11:07:25.834448+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4964`

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

- `market_context_high->unknown_4h` score `157.4764` n `74` status `ready` deltaP `8.9239` edge `13.0779` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `128.5494` n `86` status `ready` deltaP `1.2011` edge `10.7459` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `12.0883` n `46` status `ready` deltaP `29.3931` edge `0.9387` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.4774` n `46` status `ready` deltaP `35.8318` edge `0.7828` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.8812` n `65` status `ready` deltaP `38.954` edge `0.6674` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.0462` n `59` status `ready` deltaP `26.2064` edge `0.6725` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.3263` n `65` status `ready` deltaP `23.75` edge `0.5866` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3395` n `74` status `ready` deltaP `25.0247` edge `0.4318` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.4829` n `59` status `ready` deltaP `29.8611` edge `0.1745` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.0914` n `74` status `ready` deltaP `14.0203` edge `0.3764` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.9421` n `65` status `ready` deltaP `27.1318` edge `0.2089` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.166` n `65` status `ready` deltaP `34.5052` edge `0.06` maxDD `-0.4296`
- `market_context_high->equity_24h` score `3.0721` n `46` status `ready` deltaP `6.8991` edge `0.3097` maxDD `-6.3081`
- `news_risk_high->crypto_major_1h` score `2.9484` n `65` status `ready` deltaP `12.561` edge `0.1975` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.658` n `86` status `ready` deltaP `18.5002` edge `0.1432` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1333` n `65` status `ready` deltaP `26.216` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5883` n `65` status `ready` deltaP `5.0184` edge `0.1508` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3501` n `46` status `ready` deltaP `25.3624` edge `0.1058` maxDD `-1.8102`
- `market_context_high->crypto_alt_1h` score `1.1097` n `86` status `ready` deltaP `7.022` edge `0.1328` maxDD `-3.6376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
