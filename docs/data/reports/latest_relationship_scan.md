# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T10:07:28.804024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4152`

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

- `market_context_high->unknown_1h` score `32228.9665` n `45` status `ready` deltaP `2.1656` edge `2685.7422` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21963.0061` n `45` status `ready` deltaP `3.1776` edge `1830.2432` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `994.0115` n `31` status `ready` deltaP `2.3807` edge `82.836` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `710.0586` n `31` status `ready` deltaP `4.3962` edge `59.1479` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `697.4375` n `31` status `ready` deltaP `5.7292` edge `58.0816` maxDD `0.0`
- `news_risk_high->equity_24h` score `42.2277` n `31` status `ready` deltaP `47.3958` edge `3.203` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.2803` n `31` status `ready` deltaP `50.1736` edge `3.0222` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.112` n `31` status `ready` deltaP `51.9097` edge `2.7466` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8169` n `31` status `ready` deltaP `27.3701` edge `0.8893` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.5466` n `31` status `ready` deltaP `41.2355` edge `0.7148` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2939` n `31` status `ready` deltaP `37.682` edge `0.738` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5672` n `31` status `ready` deltaP `18.9123` edge `0.9858` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.6024` n `31` status `ready` deltaP `48.0903` edge `0.2296` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.132` n `31` status `ready` deltaP `43.274` edge `0.152` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0577` n `31` status `ready` deltaP `21.0353` edge `0.2166` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3832` n `31` status `ready` deltaP `36.1576` edge `0.0669` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7861` n `31` status `ready` deltaP `12.2561` edge `0.3216` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6662` n `45` status `ready` deltaP `32.5271` edge `0.0338` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.432` n `31` status `ready` deltaP `13.0046` edge `0.2608` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
