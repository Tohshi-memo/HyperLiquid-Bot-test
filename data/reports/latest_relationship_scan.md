# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T06:52:27.080146+00:00`
- Price records: `672`
- Market context records: `3560`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13196`

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

- `risk_on_high->crypto_major_24h` score `50.8533` n `32` status `ready` deltaP `55.6272` edge `3.8712` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `50.8533` n `32` status `ready` deltaP `55.6272` edge `3.8712` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `45.4536` n `32` status `ready` deltaP `55.2805` edge `3.4344` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `45.4536` n `32` status `ready` deltaP `55.2805` edge `3.4344` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.554` n `32` status `ready` deltaP `53.8995` edge `3.3535` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.554` n `32` status `ready` deltaP `53.8995` edge `3.3535` maxDD `0.0`
- `risk_on_high->index_24h` score `25.606` n `32` status `ready` deltaP `53.8995` edge `1.7745` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.606` n `32` status `ready` deltaP `53.8995` edge `1.7745` maxDD `0.0`
- `market_context_high->equity_24h` score `18.91` n `156` status `ready` deltaP `30.8226` edge `2.0116` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6667` n `32` status `ready` deltaP `37.0342` edge `1.3348` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6667` n `32` status `ready` deltaP `37.0342` edge `1.3348` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `15.4192` n `156` status `ready` deltaP `20.9317` edge `1.9185` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2213` n `156` status `ready` deltaP `38.5149` edge `1.15` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.5471` n `32` status `ready` deltaP `25.7622` edge `1.0694` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.5471` n `32` status `ready` deltaP `25.7622` edge `1.0694` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `11.3664` n `156` status `ready` deltaP `15.4568` edge `1.6484` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6249` n `156` status `ready` deltaP `31.1047` edge `1.2242` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.1002` n `32` status `ready` deltaP `6.0213` edge `0.5693` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1002` n `32` status `ready` deltaP `6.0213` edge `0.5693` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.679` n `32` status `ready` deltaP `15.1677` edge `0.484` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
