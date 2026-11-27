# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T04:07:26.949408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3552`

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

- `news_risk_high->unknown_1h` score `3218.1709` n `31` status `ready` deltaP `1.6322` edge `268.1876` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3191.3172` n `31` status `ready` deltaP `3.9388` edge `265.9225` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.4479` n `31` status `ready` deltaP `33.3333` edge `1.8151` maxDD `0.0`
- `news_risk_high->equity_24h` score `21.7674` n `31` status `ready` deltaP `32.8125` edge `1.5952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.652` n `31` status `ready` deltaP `32.4653` edge `1.3379` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2546` n `31` status `ready` deltaP `23.4067` edge `0.7022` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.6198` n `31` status `ready` deltaP `33.2612` edge `0.4613` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.0387` n `31` status `ready` deltaP `16.4732` edge `0.8061` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.8972` n `31` status `ready` deltaP `20.4021` edge `0.3829` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8186` n `31` status `ready` deltaP `40.4962` edge `0.1444` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.8468` n `31` status `ready` deltaP `34.375` edge `0.0914` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.7732` n `31` status `ready` deltaP `16.9934` edge `0.1365` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.7472` n `31` status `ready` deltaP `31.432` edge `0.0454` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4242` n `31` status `ready` deltaP `29.2979` edge `0.0152` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0558` n `31` status `ready` deltaP `6.7172` edge `0.2649` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8411` n `31` status `ready` deltaP `9.8609` edge `0.206` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1948` n `31` status `ready` deltaP `25.8402` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4935` n `31` status `ready` deltaP `12.5098` edge `0.0356` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0782` n `31` status `ready` deltaP `7.4547` edge `0.0001` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5689` n `31` status `ready` deltaP `-4.0081` edge `0.0055` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
