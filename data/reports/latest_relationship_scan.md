# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T02:58:55.782987+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3456`

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

- `news_risk_high->unknown_1h` score `3218.0316` n `31` status `ready` deltaP `1.9316` edge `268.174` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3189.129` n `31` status `ready` deltaP `4.3962` edge `265.7371` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.5301` n `31` status `ready` deltaP `34.2014` edge `1.8995` maxDD `0.0`
- `news_risk_high->equity_24h` score `22.6648` n `31` status `ready` deltaP `33.6806` edge `1.6642` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.5339` n `31` status `ready` deltaP `33.3333` edge `1.4056` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4254` n `31` status `ready` deltaP `23.7116` edge `0.7144` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.9784` n `31` status `ready` deltaP `34.0234` edge `0.4861` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `6.199` n `31` status `ready` deltaP `16.9305` edge `0.8236` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `6.0463` n `31` status `ready` deltaP `21.0966` edge `0.3907` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.8976` n `31` status `ready` deltaP `41.3643` edge `0.1452` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.0038` n `31` status `ready` deltaP `35.2431` edge `0.0987` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.9015` n `31` status `ready` deltaP `17.5922` edge `0.1432` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.8211` n `31` status `ready` deltaP `32.0417` edge `0.0475` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4925` n `31` status `ready` deltaP `30.0464` edge `0.0159` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1516` n `31` status `ready` deltaP `7.316` edge `0.2732` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9112` n `31` status `ready` deltaP `10.31` edge `0.212` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2111` n `31` status `ready` deltaP `25.9899` edge `0.0099` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.5395` n `31` status `ready` deltaP `12.5098` edge `0.0415` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.1366` n `31` status `ready` deltaP `8.2169` edge `0.0025` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5677` n `31` status `ready` deltaP `-4.0081` edge `0.0056` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
