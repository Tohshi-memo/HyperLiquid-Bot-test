# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T12:37:34.987185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `24490.8267` n `58` status `ready` deltaP `-0.1652` edge `2040.9195` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `16512.2315` n `58` status `ready` deltaP `4.4785` edge `1376.0033` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1300.7542` n `31` status `ready` deltaP `3.728` edge `108.3889` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1097.3794` n `31` status `ready` deltaP `4.701` edge `91.4226` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.1835` n `31` status `ready` deltaP `50.1736` edge `3.4308` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9741` n `31` status `ready` deltaP `48.6111` edge `2.7571` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5816` n `31` status `ready` deltaP `48.7847` edge `2.3899` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.4157` n `31` status `ready` deltaP `50.7841` edge `0.8069` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3114` n `31` status `ready` deltaP `32.9564` edge `0.6878` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.116` n `31` status `ready` deltaP `21.425` edge `0.7872` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0728` n `31` status `ready` deltaP `48.0903` edge `0.2688` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2975` n `31` status `ready` deltaP `53.3434` edge `0.182` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1543` n `31` status `ready` deltaP `10.9854` edge `0.8575` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6931` n `31` status `ready` deltaP `18.7898` edge `0.2012` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2621` n `31` status `ready` deltaP `34.3283` edge `0.069` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6363` n `31` status `ready` deltaP `30.9446` edge `0.0219` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3371` n `31` status `ready` deltaP `8.9627` edge `0.286` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9263` n `31` status `ready` deltaP `7.4657` edge `0.2329` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5314` n `31` status `ready` deltaP `29.1336` edge `0.03` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4295` n `31` status `ready` deltaP `19.9793` edge `0.1058` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
