# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T04:22:26.051147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3947`

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

- `market_context_high->unknown_1h` score `41047.9347` n `36` status `ready` deltaP `2.3785` edge `3420.6548` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3194.5049` n `31` status `ready` deltaP `3.3291` edge `266.1922` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `887.3761` n `31` status `ready` deltaP `1.4825` edge `73.9557` maxDD `-0.7395`
- `market_context_high->unknown_4h` score `58.0139` n `36` status `ready` deltaP `0.9993` edge `4.8417` maxDD `-0.7765`
- `news_risk_high->equity_24h` score `42.7036` n `31` status `ready` deltaP `48.7847` edge `3.2334` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.2266` n `31` status `ready` deltaP `49.6528` edge `3.0212` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.7819` n `31` status `ready` deltaP `48.9583` edge `2.5721` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7585` n `31` status `ready` deltaP `26.4555` edge `0.8072` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.4768` n `31` status `ready` deltaP `35.3327` edge `0.665` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1965` n `31` status `ready` deltaP `37.2247` edge `0.6496` maxDD `-2.178`
- `news_risk_high->index_24h` score `6.9815` n `31` status `ready` deltaP `50.1736` edge `0.2473` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.778` n `31` status `ready` deltaP `17.2354` edge `0.8958` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3794` n `31` status `ready` deltaP `46.0518` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5647` n `31` status `ready` deltaP `19.5383` edge `0.1855` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3292` n `31` status `ready` deltaP `36.1576` edge `0.0624` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6447` n `31` status `ready` deltaP `31.3937` edge `0.0196` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4306` n `31` status `ready` deltaP `9.7112` edge `0.293` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3383` n `36` status `ready` deltaP `28.8788` edge `0.0308` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2284` n `31` status `ready` deltaP `12.5555` edge `0.2377` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4994` n `31` status `ready` deltaP `29.433` edge `0.0239` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
