# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T14:22:26.235887+00:00`
- Price records: `672`
- Market context records: `5780`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8718`

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

- `market_context_high->equity_24h` score `0.5794` n `237` status `ready` deltaP `15.491` edge `0.4789` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1193` n `294` status `ready` deltaP `7.5908` edge `0.1232` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2723` n `305` status `ready` deltaP `1.9245` edge `0.0008` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5874` n `305` status `ready` deltaP `3.7411` edge `0.0268` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6203` n `305` status `ready` deltaP `2.5086` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7609` n `305` status `ready` deltaP `-1.7959` edge `-0.0051` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8743` n `305` status `ready` deltaP `3.4711` edge `0.0361` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9389` n `305` status `ready` deltaP `0.7196` edge `0.0038` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.9432` n `237` status `ready` deltaP `14.4778` edge `0.0409` maxDD `-3.6674`
- `market_context_high->crypto_alt_1h` score `-1.0028` n `305` status `ready` deltaP `2.2166` edge `0.0351` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1998` n `294` status `ready` deltaP `0.646` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3179` n `294` status `ready` deltaP `1.6892` edge `0.005` maxDD `-1.4844`
- `market_context_high->commodity_4h` score `-2.45` n `294` status `ready` deltaP `-3.0519` edge `-0.0262` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8575` n `237` status `ready` deltaP `2.747` edge `0.0298` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8838` n `294` status `ready` deltaP `7.6832` edge `0.1457` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8924` n `294` status `ready` deltaP `-6.0623` edge `-0.048` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.4491` n `294` status `ready` deltaP `5.3841` edge `0.0942` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.4842` n `237` status `ready` deltaP `3.1821` edge `-0.0742` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0604` n `237` status `ready` deltaP `-7.8674` edge `-0.2458` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9147` n `237` status `ready` deltaP `-13.7614` edge `-0.0802` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
