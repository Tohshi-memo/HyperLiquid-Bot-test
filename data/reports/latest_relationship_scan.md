# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T02:52:25.491781+00:00`
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

- `market_context_high->unknown_1h` score `32251.0345` n `45` status `ready` deltaP `2.1656` edge `2687.5812` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21989.1757` n `45` status `ready` deltaP `3.1776` edge `1832.424` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1016.0795` n `31` status `ready` deltaP `2.3807` edge `84.675` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `736.2282` n `31` status `ready` deltaP `4.3962` edge `61.3287` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.9639` n `31` status `ready` deltaP `50.1736` edge `2.9125` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.7425` n `31` status `ready` deltaP `44.2708` edge `2.9334` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.1611` n `31` status `ready` deltaP `48.9583` edge `2.6037` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8939` n `31` status `ready` deltaP `27.5226` edge `0.8947` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1986` n `31` status `ready` deltaP `41.2355` edge `0.6858` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4251` n `31` status `ready` deltaP `34.9381` edge `0.6839` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3861` n `31` status `ready` deltaP `17.8452` edge `0.9697` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.818` n `31` status `ready` deltaP `43.0556` edge `0.1978` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4931` n `31` status `ready` deltaP `46.5726` edge `0.1601` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.716` n `31` status `ready` deltaP `19.2389` edge `0.2001` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1293` n `31` status `ready` deltaP `33.7186` edge `0.062` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.772` n `31` status `ready` deltaP `12.7052` edge `0.3168` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6248` n `45` status `ready` deltaP `32.0698` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.6171` n `31` status `ready` deltaP `30.9446` edge `0.0203` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.4187` n `31` status `ready` deltaP `12.7052` edge `0.2611` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5687` n `31` status `ready` deltaP `29.8821` edge `0.0298` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
