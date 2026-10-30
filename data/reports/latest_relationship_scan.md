# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T02:22:27.103891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1663.5494` n `134` status `ready` deltaP `-2.7908` edge `138.6907` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.6023` n `134` status `ready` deltaP `5.142` edge `3.0292` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.7669` n `134` status `ready` deltaP `31.6179` edge `0.0381` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3065` n `134` status `ready` deltaP `9.8557` edge `0.0115` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1451` n `134` status `ready` deltaP `12.566` edge `0.0502` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.138` n `134` status `ready` deltaP `7.3152` edge `0.0655` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.1176` n `134` status `ready` deltaP `13.3919` edge `0.0154` maxDD `-1.8344`
- `market_context_high->equity_24h` score `0.0413` n `134` status `ready` deltaP `14.2284` edge `0.1843` maxDD `-14.0571`
- `market_context_high->equity_1h` score `-0.0512` n `134` status `ready` deltaP `3.2845` edge `0.0614` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1189` n `134` status `ready` deltaP `3.28` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3583` n `134` status `ready` deltaP `1.3451` edge `0.0126` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.5623` n `134` status `ready` deltaP `0.562` edge `0.0826` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5892` n `134` status `ready` deltaP `-1.6927` edge `-0.0044` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.6544` n `134` status `ready` deltaP `4.1961` edge `0.0746` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8762` n `134` status `ready` deltaP `-2.5449` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.4456` n `134` status `ready` deltaP `1.0209` edge `0.0058` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5009` n `134` status `ready` deltaP `3.9257` edge `0.0461` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.5233` n `134` status `ready` deltaP `8.1612` edge `0.0798` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.1131` n `134` status `ready` deltaP `-4.3002` edge `-0.0154` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.9955` n `134` status `ready` deltaP `0.4892` edge `0.072` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
