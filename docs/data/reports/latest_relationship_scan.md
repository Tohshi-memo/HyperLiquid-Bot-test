# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T21:22:28.678547+00:00`
- Price records: `672`
- Market context records: `6431`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.9114` n `32` status `ready` deltaP `30.7292` edge `0.8025` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.9435` n `146` status `ready` deltaP `20.3078` edge `0.8566` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5218` n `32` status `ready` deltaP `54.6875` edge `0.1789` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1339` n `32` status `ready` deltaP `43.064` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1113` n `32` status `ready` deltaP `35.2431` edge `0.1282` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.383` n `32` status `ready` deltaP `12.3264` edge `0.4295` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4709` n `32` status `ready` deltaP `29.7904` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4734` n `32` status `ready` deltaP `13.8286` edge `0.1434` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.139` n `196` status `ready` deltaP `-5.8169` edge `0.2238` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8256` n `32` status `ready` deltaP `9.6744` edge `0.0875` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.1619` n `192` status `ready` deltaP `8.689` edge `0.0232` maxDD `-0.4108`
- `market_context_high->metal_4h` score `0.129` n `192` status `ready` deltaP `9.286` edge `0.041` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2106` n `32` status `ready` deltaP `7.1295` edge `-0.0306` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4071` n `146` status `ready` deltaP `16.5525` edge `0.0943` maxDD `-11.8809`
- `market_context_high->unknown_4h` score `-0.5049` n `192` status `ready` deltaP `-14.596` edge `0.2958` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-0.5457` n `196` status `ready` deltaP `0.8707` edge `0.002` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5885` n `32` status `ready` deltaP `-0.1497` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6185` n `196` status `ready` deltaP `-1.3473` edge `-0.002` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.6284` n `192` status `ready` deltaP `6.4533` edge `0.0463` maxDD `-8.2573`
- `market_context_high->index_1h` score `-0.6688` n `196` status `ready` deltaP `-2.5174` edge `0.003` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
