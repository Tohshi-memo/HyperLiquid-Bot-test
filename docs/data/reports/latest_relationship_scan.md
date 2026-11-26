# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T21:07:27.883886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3360`

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

- `news_risk_high->unknown_1h` score `3218.2776` n `31` status `ready` deltaP `2.231` edge `268.1925` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3195.3546` n `31` status `ready` deltaP `4.3962` edge `266.2559` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.7877` n `31` status `ready` deltaP `38.0208` edge `2.1455` maxDD `0.0`
- `news_risk_high->equity_24h` score `26.0266` n `31` status `ready` deltaP `37.1528` edge `1.9212` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.6601` n `31` status `ready` deltaP `37.3264` edge `1.6395` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.9975` n `31` status `ready` deltaP `24.4738` edge `0.757` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.7313` n `31` status `ready` deltaP `36.31` edge `0.5336` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.6027` n `31` status `ready` deltaP `23.7008` edge `0.4197` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.4413` n `31` status `ready` deltaP `17.5403` edge `0.8506` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9211` n `31` status `ready` deltaP `41.5379` edge `0.146` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.6025` n `31` status `ready` deltaP `38.5417` edge `0.1266` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1929` n `31` status `ready` deltaP `18.7898` edge `0.1595` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0921` n `31` status `ready` deltaP `34.6332` edge `0.0528` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.562` n `31` status `ready` deltaP `30.6452` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2156` n `31` status `ready` deltaP `7.6154` edge `0.2794` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0165` n `31` status `ready` deltaP `10.7591` edge `0.2225` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3631` n `31` status `ready` deltaP `27.4869` edge `0.0194` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.803` n `31` status `ready` deltaP `14.1866` edge `0.0641` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2993` n `31` status `ready` deltaP `10.656` edge `0.0071` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4167` n `31` status `ready` deltaP `-2.3614` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
