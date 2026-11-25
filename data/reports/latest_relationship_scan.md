# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T01:52:26.815094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32251.7389` n `45` status `ready` deltaP `2.0159` edge `2687.6409` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21993.6757` n `45` status `ready` deltaP `3.1776` edge `1832.799` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.784` n `31` status `ready` deltaP `2.231` edge `84.7347` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `740.7282` n `31` status `ready` deltaP `4.3962` edge `61.7037` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.8379` n `31` status `ready` deltaP `50.1736` edge `2.902` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.3043` n `31` status `ready` deltaP `43.9236` edge `2.8992` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.9055` n `31` status `ready` deltaP `48.9583` edge `2.5824` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7575` n `31` status `ready` deltaP `26.9128` edge `0.8874` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1674` n `31` status `ready` deltaP `41.2355` edge `0.6832` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.212` n `31` status `ready` deltaP `34.3283` edge `0.6702` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2655` n `31` status `ready` deltaP `17.2354` edge `0.9583` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.7121` n `31` status `ready` deltaP `42.3611` edge `0.1936` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.5726` n `31` status `ready` deltaP `47.267` edge `0.1621` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6153` n `31` status `ready` deltaP `18.7898` edge `0.1947` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0589` n `31` status `ready` deltaP `33.1088` edge `0.0602` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7252` n `31` status `ready` deltaP `12.4058` edge `0.3128` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6248` n `45` status `ready` deltaP `32.0698` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5584` n `31` status `ready` deltaP `30.3458` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3876` n `31` status `ready` deltaP `12.4058` edge `0.2591` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6007` n `31` status `ready` deltaP `30.3312` edge `0.0309` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
