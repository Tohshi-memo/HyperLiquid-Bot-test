# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T08:22:28.005175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4128`

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

- `market_context_high->unknown_1h` score `32237.0185` n `45` status `ready` deltaP `2.1656` edge `2686.4132` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21975.3733` n `45` status `ready` deltaP `3.1776` edge `1831.2738` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1002.0635` n `31` status `ready` deltaP `2.3807` edge `83.507` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `791.4983` n `31` status `ready` deltaP `5.7292` edge `65.92` maxDD `0.0`
- `news_risk_high->unknown_4h` score `722.4258` n `31` status `ready` deltaP `4.3962` edge `60.1785` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `41.366` n `31` status `ready` deltaP `46.1806` edge `3.1393` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.9467` n `31` status `ready` deltaP `50.1736` edge `2.9944` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.6728` n `31` status `ready` deltaP `50.6944` edge `2.7181` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8762` n `31` status `ready` deltaP `27.8275` edge `0.8912` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.4459` n `31` status `ready` deltaP `41.2355` edge `0.7064` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2495` n `31` status `ready` deltaP `37.682` edge `0.7343` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5867` n `31` status `ready` deltaP `18.9123` edge `0.9883` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4152` n `31` status `ready` deltaP `46.875` edge `0.2221` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1181` n `31` status `ready` deltaP `43.1004` edge `0.152` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0121` n `31` status `ready` deltaP `20.8856` edge `0.2138` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3832` n `31` status `ready` deltaP `36.1576` edge `0.0669` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.8125` n `31` status `ready` deltaP `12.5555` edge `0.323` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7046` n `31` status `ready` deltaP `31.8428` edge `0.0216` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6114` n `45` status `ready` deltaP `31.9173` edge `0.0333` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4211` n `31` status `ready` deltaP `12.8549` edge `0.2604` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
