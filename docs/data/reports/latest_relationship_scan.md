# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T07:37:40.130703+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4104`

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

- `market_context_high->unknown_1h` score `32237.6797` n `45` status `ready` deltaP `2.1656` edge `2686.4683` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21979.6525` n `45` status `ready` deltaP `3.1776` edge `1831.6304` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1002.7247` n `31` status `ready` deltaP `2.3807` edge `83.5621` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `835.7183` n `31` status `ready` deltaP `5.7292` edge `69.605` maxDD `0.0`
- `news_risk_high->unknown_4h` score `726.705` n `31` status `ready` deltaP `4.3962` edge `60.5351` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `40.9416` n `31` status `ready` deltaP `45.6597` edge `3.1074` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.7775` n `31` status `ready` deltaP `50.1736` edge `2.9803` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.4729` n `31` status `ready` deltaP `50.5208` edge `2.7026` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.904` n `31` status `ready` deltaP `27.9799` edge `0.8925` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.3955` n `31` status `ready` deltaP `41.2355` edge `0.7022` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1871` n `31` status `ready` deltaP `37.682` edge `0.7291` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5797` n `31` status `ready` deltaP `18.9123` edge `0.9874` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3279` n `31` status `ready` deltaP `46.3542` edge `0.2183` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1356` n `31` status `ready` deltaP `43.274` edge `0.1523` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9582` n `31` status `ready` deltaP `20.5862` edge `0.2113` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3772` n `31` status `ready` deltaP `36.1576` edge `0.0664` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.786` n `31` status `ready` deltaP `12.5555` edge `0.3196` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.689` n `31` status `ready` deltaP `31.6931` edge `0.0213` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3868` n `31` status `ready` deltaP `12.5555` edge `0.258` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
