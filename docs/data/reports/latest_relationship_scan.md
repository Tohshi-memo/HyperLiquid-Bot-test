# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T17:52:28.512423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7475`

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

- `market_context_high->unknown_24h` score `2854.2285` n `100` status `ready` deltaP `-9.1875` edge `237.9566` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `82.6919` n `100` status `ready` deltaP `0.9268` edge `6.8981` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.1773` n `108` status `ready` deltaP `-5.9436` edge `6.4997` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.6953` n `65` status `ready` deltaP `45.5342` edge `1.2595` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.0083` n `100` status `ready` deltaP `26.2153` edge `1.0183` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.9924` n `105` status `ready` deltaP `18.3406` edge `0.4324` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8823` n `100` status `ready` deltaP `43.5556` edge `0.1348` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6863` n `100` status `ready` deltaP `20.8963` edge `0.0437` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8389` n `100` status `ready` deltaP `12.0479` edge `0.0186` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.7461` n `100` status `ready` deltaP `6.2378` edge `0.1934` maxDD `-4.48`
- `news_risk_high->crypto_alt_1h` score `0.6742` n `108` status `ready` deltaP `7.9785` edge `0.0984` maxDD `-3.9659`
- `market_context_high->crypto_major_1h` score `0.5473` n `100` status `ready` deltaP `9.4012` edge `0.0857` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.4998` n `100` status `ready` deltaP `7.7006` edge `0.1003` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2263` n `100` status `ready` deltaP `8.4551` edge `-0.0006` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2216` n `100` status `ready` deltaP `8.561` edge `0.0005` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.171` n `100` status `ready` deltaP `12.7927` edge `0.0572` maxDD `-0.978`
- `market_context_high->metal_24h` score `0.0427` n `100` status `ready` deltaP `13.2847` edge `0.1816` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.1056` n `100` status `ready` deltaP `16.6463` edge `0.1495` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.2811` n `100` status `ready` deltaP `4.503` edge `0.0024` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3425` n `100` status `ready` deltaP `-0.9581` edge `0.0139` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
