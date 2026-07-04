# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T11:54:48.434369+00:00`
- Price records: `672`
- Market context records: `5660`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.3419` n `188` status `ready` deltaP `15.2482` edge `0.6014` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9121` n `238` status `ready` deltaP `11.3484` edge `0.2296` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.5168` n `238` status `ready` deltaP `7.8794` edge `0.1544` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.3553` n `188` status `ready` deltaP `17.8671` edge `0.0552` maxDD `-2.2431`
- `market_context_high->crypto_alt_4h` score `0.1448` n `238` status `ready` deltaP `7.303` edge `0.1483` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2641` n `250` status `ready` deltaP `1.8994` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4205` n `250` status `ready` deltaP `5.0623` edge `0.0319` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5255` n `250` status `ready` deltaP `0.0515` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6074` n `250` status `ready` deltaP `1.6563` edge `0.0345` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8506` n `250` status `ready` deltaP `2.6503` edge `0.036` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8531` n `250` status `ready` deltaP `1.2982` edge `-0.0032` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9221` n `250` status `ready` deltaP `0.7042` edge `0.0053` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2546` n `238` status `ready` deltaP `2.3686` edge `0.0068` maxDD `-1.3415`
- `market_context_high->index_4h` score `-2.0191` n `238` status `ready` deltaP `-1.4834` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.346` n `188` status `ready` deltaP `9.0463` edge `0.0376` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0537` n `238` status `ready` deltaP `-14.7059` edge `-0.0551` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7889` n `238` status `ready` deltaP `-2.0829` edge `-0.0343` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7525` n `188` status `ready` deltaP `3.6126` edge `0.0339` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.43` n `188` status `ready` deltaP `-13.7965` edge `-0.2527` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.6484` n `188` status `ready` deltaP `-13.8963` edge `-0.1005` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
