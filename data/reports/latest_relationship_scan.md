# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T04:07:25.340483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3923`

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

- `market_context_high->unknown_1h` score `39850.3192` n `37` status `ready` deltaP `2.5287` edge `3320.8525` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3193.9145` n `31` status `ready` deltaP `3.3291` edge `266.143` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `886.7293` n `31` status `ready` deltaP `1.4825` edge `73.9018` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `42.8867` n `31` status `ready` deltaP `48.9583` edge `3.2475` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.3545` n `31` status `ready` deltaP `49.8264` edge `3.0307` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.9386` n `31` status `ready` deltaP `49.1319` edge `2.584` maxDD `0.0`
- `market_context_high->unknown_4h` score `23.5475` n `37` status `ready` deltaP `1.1495` edge `1.9685` maxDD `-0.7765`
- `news_risk_high->crypto_alt_4h` score `10.7621` n `31` status `ready` deltaP `26.4555` edge `0.8075` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.5375` n `31` status `ready` deltaP `35.5063` edge `0.6689` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1857` n `31` status `ready` deltaP `37.2247` edge `0.6487` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.011` n `31` status `ready` deltaP `50.3472` edge `0.2486` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7749` n `31` status `ready` deltaP `17.2354` edge `0.8954` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3643` n `31` status `ready` deltaP `45.8782` edge `0.154` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5875` n `31` status `ready` deltaP `19.688` edge `0.1864` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3268` n `31` status `ready` deltaP `36.1576` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6578` n `31` status `ready` deltaP `31.5434` edge `0.0197` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4408` n `31` status `ready` deltaP `9.8609` edge `0.2933` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3753` n `37` status `ready` deltaP `29.2518` edge `0.0314` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2323` n `31` status `ready` deltaP `12.5555` edge `0.2382` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5001` n `31` status `ready` deltaP `29.433` edge `0.024` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
