# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T11:07:24.106427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3384.7824` n `31` status `ready` deltaP `2.0813` edge `282.0689` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3254.9926` n `31` status `ready` deltaP `3.7864` edge `271.2298` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.6988` n `31` status `ready` deltaP `34.3154` edge `1.6628` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4545` n `31` status `ready` deltaP `32.2357` edge `1.1563` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.5228` n `31` status `ready` deltaP `27.7296` edge `0.8587` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.7002` n `31` status `ready` deltaP `22.4921` edge `0.6621` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.5187` n `31` status `ready` deltaP `16.7781` edge `0.7374` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.4933` n `31` status `ready` deltaP `30.3649` edge `0.3034` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0232` n `31` status `ready` deltaP `41.4491` edge `0.1551` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8621` n `31` status `ready` deltaP `16.1738` edge `0.2415` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.466` n `31` status `ready` deltaP `30.2125` edge `0.0301` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3701` n `31` status `ready` deltaP `25.9965` edge `0.0242` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3127` n `31` status `ready` deltaP `28.3997` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.122` n `31` status `ready` deltaP `13.9994` edge `0.1022` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9512` n `31` status `ready` deltaP `6.8669` edge `0.2505` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7374` n `31` status `ready` deltaP `9.1124` edge `0.1977` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1231` n `31` status `ready` deltaP `24.4929` edge `0.0086` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.6904` n `37` status `ready` deltaP `9.6119` edge `0.0346` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4133` n `31` status `ready` deltaP `9.8938` edge `0.0268` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3436` n `31` status `ready` deltaP `11.4427` edge `0.0235` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
