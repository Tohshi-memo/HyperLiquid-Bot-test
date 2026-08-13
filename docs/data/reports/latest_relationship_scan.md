# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T13:37:27.874603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `51.2595` n `161` status `ready` deltaP `-23.6898` edge `4.7208` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `19.5649` n `32` status `ready` deltaP `-42.1875` edge `2.8646` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `19.5649` n `32` status `ready` deltaP `-42.1875` edge `2.8646` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.4275` n `32` status `ready` deltaP `7.9861` edge `0.687` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.882` n `36` status `ready` deltaP `36.5854` edge `0.3296` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.6965` n `32` status `ready` deltaP `26.7361` edge `0.1298` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.6965` n `32` status `ready` deltaP `26.7361` edge `0.1298` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6056` n `32` status `ready` deltaP `18.5213` edge `0.1119` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6056` n `32` status `ready` deltaP `18.5213` edge `0.1119` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4591` n `32` status `ready` deltaP `15.7986` edge `0.0996` maxDD `0.0`
- `risk_on_high->fx_24h` score `2.0199` n `32` status `ready` deltaP `22.5694` edge `0.0363` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0199` n `32` status `ready` deltaP `22.5694` edge `0.0363` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.8131` n `36` status `ready` deltaP `20.6809` edge `0.0264` maxDD `-0.0546`
- `market_context_high->commodity_24h` score `1.7275` n `161` status `ready` deltaP `16.7982` edge `0.1123` maxDD `-2.4263`
- `news_risk_high->equity_1h` score `1.5176` n `36` status `ready` deltaP `7.3853` edge `0.1091` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4241` n `161` status `ready` deltaP `16.1727` edge `0.0747` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.3173` n `32` status `ready` deltaP `12.6736` edge `0.2` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3173` n `32` status `ready` deltaP `12.6736` edge `0.2` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2168` n `32` status `ready` deltaP `13.0614` edge `0.0376` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2168` n `32` status `ready` deltaP `13.0614` edge `0.0376` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
