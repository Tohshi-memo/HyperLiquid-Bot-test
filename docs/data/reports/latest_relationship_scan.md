# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T21:52:26.413326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2814`

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

- `news_risk_high->unknown_1h` score `3299.3269` n `31` status `ready` deltaP `1.6322` edge `274.9506` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3172.7589` n `31` status `ready` deltaP `3.3191` edge `264.3801` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.154` n `31` status `ready` deltaP `27.2097` edge `1.2481` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4181` n `31` status `ready` deltaP `27.0364` edge `0.8546` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.2465` n `31` status `ready` deltaP `23.9168` edge `0.8611` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2435` n `31` status `ready` deltaP `21.0438` edge `0.6337` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4641` n `31` status `ready` deltaP `29.6853` edge `0.3055` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1538` n `31` status `ready` deltaP `14.4105` edge `0.7064` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6706` n `31` status `ready` deltaP `38.6762` edge `0.1442` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6428` n `31` status `ready` deltaP `12.1877` edge `0.2498` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.345` n `31` status `ready` deltaP `28.9243` edge `0.0286` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2469` n `31` status `ready` deltaP `27.6512` edge `0.0114` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2088` n `31` status `ready` deltaP `24.6101` edge `0.02` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.2083` n `31` status `ready` deltaP `15.0473` edge `0.1024` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9108` n `31` status `ready` deltaP `6.1184` edge `0.2503` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6821` n `31` status `ready` deltaP `8.3639` edge `0.1956` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1239` n `31` status `ready` deltaP `24.4929` edge `0.0087` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.429` n `31` status `ready` deltaP `10.2715` edge `0.0263` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3625` n `31` status `ready` deltaP `11.6708` edge `0.0244` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3256` n `31` status `ready` deltaP `-1.9123` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
