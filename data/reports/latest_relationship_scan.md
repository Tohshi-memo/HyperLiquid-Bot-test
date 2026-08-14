# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T15:07:30.993176+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `115.1771` n `137` status `ready` deltaP `-33.0545` edge `10.1097` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8531` n `32` status `ready` deltaP `-45.4861` edge `4.5902` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8531` n `32` status `ready` deltaP `-45.4861` edge `4.5902` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.6876` n `36` status `ready` deltaP `10.4166` edge `0.7758` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1974` n `36` status `ready` deltaP `38.2622` edge `0.3447` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7829` n `32` status `ready` deltaP `32.2917` edge `0.1833` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7829` n `32` status `ready` deltaP `32.2917` edge `0.1833` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.4541` n `137` status `ready` deltaP `23.5326` edge `0.1958` maxDD `-2.1876`
- `risk_on_high->commodity_4h` score `2.9394` n `32` status `ready` deltaP `20.503` edge `0.1265` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9394` n `32` status `ready` deltaP `20.503` edge `0.1265` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0893` n `36` status `ready` deltaP `14.2361` edge `0.0792` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.0842` n `32` status `ready` deltaP `16.6667` edge `0.2717` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0842` n `32` status `ready` deltaP `16.6667` edge `0.2717` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.6818` n `36` status `ready` deltaP `8.5829` edge `0.1148` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.6799` n `36` status `ready` deltaP `19.7662` edge `0.0214` maxDD `-0.0546`
- `risk_on_high->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2935` n `32` status `ready` deltaP `13.6602` edge `0.04` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2032` n `32` status `ready` deltaP `14.2361` edge `0.0238` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2032` n `32` status `ready` deltaP `14.2361` edge `0.0238` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.1839` n `137` status `ready` deltaP `14.6408` edge `0.0649` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
