# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T16:22:26.780842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7506`

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

- `news_risk_high->unknown_1h` score `3429.0443` n `31` status `ready` deltaP `2.3807` edge `285.7554` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3261.8121` n `31` status `ready` deltaP `3.634` edge `271.7991` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.8193` n `31` status `ready` deltaP `37.7816` edge `1.8164` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.794` n `31` status `ready` deltaP `35.8752` edge `1.327` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.0592` n `31` status `ready` deltaP `29.2894` edge `0.893` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3636` n `31` status `ready` deltaP `24.1689` edge `0.7062` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9492` n `31` status `ready` deltaP `18.6074` edge `0.7804` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.9398` n `31` status `ready` deltaP `33.2612` edge `0.3213` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.1075` n `31` status `ready` deltaP `42.1424` edge `0.1575` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9302` n `31` status `ready` deltaP `17.0403` edge `0.2414` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6681` n `31` status `ready` deltaP `32.499` edge `0.0317` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4645` n `31` status `ready` deltaP `26.5165` edge `0.0286` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3678` n `31` status `ready` deltaP `28.9985` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2922` n `31` status `ready` deltaP `15.197` edge `0.1084` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0815` n `31` status `ready` deltaP `7.0166` edge `0.2662` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9658` n `31` status `ready` deltaP `10.7591` edge `0.216` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5027` n `31` status `ready` deltaP `11.4182` edge `0.0281` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4408` n `31` status `ready` deltaP `12.9671` edge `0.0258` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.4243` n `65` status `ready` deltaP `11.2391` edge `0.0016` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
