# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T23:37:15.738240+00:00`
- Price records: `672`
- Market context records: `1062`
- Flow alert records: `4962`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.1957` n `174` status `ready` deltaP `34.3291` edge `1.0838` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.0097` n `174` status `ready` deltaP `11.8015` edge `0.4622` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.9791` n `174` status `ready` deltaP `12.7233` edge `0.3006` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.2343` n `174` status `ready` deltaP `11.9836` edge `0.2371` maxDD `-2.1308`
- `market_context_high->metal_24h` score `2.7665` n `174` status `ready` deltaP `-5.7357` edge `0.4355` maxDD `-6.3373`
- `market_context_high->fx_1h` score `-0.0578` n `176` status `ready` deltaP `5.6784` edge `0.0003` maxDD `-0.3124`
- `market_context_high->equity_4h` score `-0.2394` n `176` status `ready` deltaP `3.0627` edge `0.0904` maxDD `-6.4615`
- `market_context_high->crypto_major_1h` score `-0.3122` n `176` status `ready` deltaP `7.2639` edge `0.0189` maxDD `-5.4676`
- `market_context_high->index_4h` score `-0.4566` n `176` status `ready` deltaP `1.5521` edge `0.0501` maxDD `-4.2134`
- `market_context_high->index_1h` score `-0.4835` n `176` status `ready` deltaP `3.8105` edge `0.0123` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.511` n `176` status `ready` deltaP `0.3096` edge `0.0281` maxDD `-4.1532`
- `market_context_high->fx_4h` score `-0.7067` n `176` status `ready` deltaP `1.0116` edge `0.0023` maxDD `-1.6381`
- `market_context_high->metal_1h` score `-0.7515` n `176` status `ready` deltaP `4.3584` edge `-0.0291` maxDD `-5.038`
- `market_context_high->commodity_1h` score `-0.885` n `176` status `ready` deltaP `-0.4457` edge `0.01` maxDD `-3.7959`
- `market_context_high->crypto_alt_1h` score `-1.0473` n `176` status `ready` deltaP `1.5174` edge `0.0112` maxDD `-5.3538`
- `market_context_high->crypto_major_4h` score `-1.7635` n `176` status `ready` deltaP `8.3841` edge `0.0775` maxDD `-15.4284`
- `market_context_high->crypto_alt_4h` score `-2.1798` n `176` status `ready` deltaP `2.0371` edge `0.0552` maxDD `-13.0347`
- `market_context_high->commodity_4h` score `-2.5567` n `176` status `ready` deltaP `-6.6934` edge `0.0336` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-2.655` n `176` status `ready` deltaP `0.6236` edge `-0.1299` maxDD `-10.8383`
- `market_context_high->fx_24h` score `-3.1053` n `174` status `ready` deltaP `4.5636` edge `-0.0209` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
