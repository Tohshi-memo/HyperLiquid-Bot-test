# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T21:52:32.282908+00:00`
- Price records: `672`
- Market context records: `2803`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.7767` n `142` status `ready` deltaP `4.1642` edge `0.2501` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.2004` n `142` status `ready` deltaP `1.4867` edge `0.4818` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.138` n `142` status `ready` deltaP `7.4051` edge `0.1508` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.6163` n `142` status `ready` deltaP `11.2114` edge `0.286` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.3247` n `142` status `ready` deltaP `13.3009` edge `0.0371` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.031` n `142` status `ready` deltaP `4.7799` edge `0.0438` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.047` n `142` status `ready` deltaP `4.6471` edge `0.0124` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5757` n `142` status `ready` deltaP `1.1807` edge `0.0029` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.7176` n `142` status `ready` deltaP `-1.1807` edge `-0.0088` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7701` n `142` status `ready` deltaP `4.9465` edge `0.0443` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.8583` n `142` status `ready` deltaP `-2.3003` edge `0.0271` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.9552` n `142` status `ready` deltaP `3.7763` edge `0.0393` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.1202` n `142` status `ready` deltaP `2.2673` edge `0.0295` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1593` n `142` status `ready` deltaP `-3.9054` edge `0.0073` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.6349` n `142` status `ready` deltaP `-0.4488` edge `-0.0146` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6596` n `142` status `ready` deltaP `-4.1422` edge `-0.0235` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.6709` n `142` status `ready` deltaP `13.8805` edge `0.2023` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.0419` n `142` status `ready` deltaP `0.1439` edge `-0.0077` maxDD `-11.4038`
- `market_context_high->index_24h` score `-2.1464` n `142` status `ready` deltaP `-1.3938` edge `-0.0715` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
