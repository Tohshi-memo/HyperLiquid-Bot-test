# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T09:07:31.073149+00:00`
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

- `market_context_high->unknown_1h` score `32233.5061` n `45` status `ready` deltaP `2.1656` edge `2686.1205` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21969.3781` n `45` status `ready` deltaP `3.1776` edge `1830.7742` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `998.5511` n `31` status `ready` deltaP `2.3807` edge `83.2143` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `748.4399` n `31` status `ready` deltaP `5.7292` edge `62.3318` maxDD `0.0`
- `news_risk_high->unknown_4h` score `716.4306` n `31` status `ready` deltaP `4.3962` edge `59.6789` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `41.7329` n `31` status `ready` deltaP `46.7014` edge `3.1664` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.0763` n `31` status `ready` deltaP `50.1736` edge `3.0052` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.8644` n `31` status `ready` deltaP `51.2153` edge `2.7306` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8073` n `31` status `ready` deltaP `27.3701` edge `0.8885` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.4902` n `31` status `ready` deltaP `41.2355` edge `0.7101` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2555` n `31` status `ready` deltaP `37.682` edge `0.7348` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5672` n `31` status `ready` deltaP `18.9123` edge `0.9858` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4941` n `31` status `ready` deltaP `47.3958` edge `0.2252` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1157` n `31` status `ready` deltaP `43.1004` edge `0.1518` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0085` n `31` status `ready` deltaP `21.0353` edge `0.2125` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3808` n `31` status `ready` deltaP `36.1576` edge `0.0667` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7767` n `31` status `ready` deltaP `12.2561` edge `0.3204` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7022` n `31` status `ready` deltaP `31.8428` edge `0.0214` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.626` n `45` status `ready` deltaP `32.0698` edge `0.0335` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4078` n `31` status `ready` deltaP `12.8549` edge `0.2587` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
