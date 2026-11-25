# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T03:07:24.476923+00:00`
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

- `market_context_high->unknown_1h` score `32251.0969` n `45` status `ready` deltaP `2.1656` edge `2687.5864` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21983.1925` n `45` status `ready` deltaP `3.1776` edge `1831.9254` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.1419` n `31` status `ready` deltaP `2.3807` edge `84.6802` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `730.245` n `31` status `ready` deltaP `4.3962` edge `60.8301` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.9555` n `31` status `ready` deltaP `50.1736` edge `2.9118` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.8301` n `31` status `ready` deltaP `44.2708` edge `2.9407` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.1923` n `31` status `ready` deltaP `48.9583` edge `2.6063` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.93` n `31` status `ready` deltaP `27.675` edge `0.8967` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2011` n `31` status `ready` deltaP `41.2355` edge `0.686` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4853` n `31` status `ready` deltaP `35.0905` edge `0.6879` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4151` n `31` status `ready` deltaP `17.9976` edge `0.9724` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8427` n `31` status `ready` deltaP `43.2292` edge `0.1987` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4732` n `31` status `ready` deltaP `46.399` edge `0.1596` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.74` n `31` status `ready` deltaP `19.3886` edge `0.2011` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1463` n `31` status `ready` deltaP `33.871` edge `0.0624` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7611` n `31` status `ready` deltaP `12.5555` edge `0.3164` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6303` n `31` status `ready` deltaP `31.0943` edge `0.0204` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6236` n `45` status `ready` deltaP `32.0698` edge `0.0333` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4195` n `31` status `ready` deltaP `12.7052` edge `0.2612` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5687` n `31` status `ready` deltaP `29.8821` edge `0.0298` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
