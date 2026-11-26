# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T14:07:27.668284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3479`

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

- `news_risk_high->unknown_1h` score `3231.3912` n `31` status `ready` deltaP `1.7819` edge `269.2883` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3218.7907` n `31` status `ready` deltaP `3.4815` edge `268.215` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `34.333` n `31` status `ready` deltaP `42.8819` edge `2.5752` maxDD `0.0`
- `news_risk_high->equity_24h` score `33.4511` n `31` status `ready` deltaP `42.0139` edge `2.5075` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.3626` n `31` status `ready` deltaP `42.1875` edge `2.0823` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.5001` n `31` status `ready` deltaP `26.1506` edge `0.7877` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.2218` n `31` status `ready` deltaP `38.2917` edge `0.6446` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.1652` n `31` status `ready` deltaP `28.5619` edge `0.5175` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8592` n `31` status `ready` deltaP `19.2171` edge `0.893` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6322` n `31` status `ready` deltaP `43.4028` edge `0.18` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9029` n `31` status `ready` deltaP `41.1907` edge `0.1468` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7986` n `31` status `ready` deltaP `20.5862` edge `0.198` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3842` n `31` status `ready` deltaP `36.9198` edge `0.0619` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7716` n `31` status `ready` deltaP `32.741` edge `0.0212` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5039` n `31` status `ready` deltaP `10.0106` edge `0.3004` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2627` n `31` status `ready` deltaP `12.8549` edge `0.2401` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4604` n `31` status `ready` deltaP `28.6845` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9859` n `31` status `ready` deltaP `15.5586` edge `0.0784` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.4421` n `31` status `ready` deltaP `12.6377` edge `0.0122` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3831` n `31` status `ready` deltaP `-2.2117` edge `0.009` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
