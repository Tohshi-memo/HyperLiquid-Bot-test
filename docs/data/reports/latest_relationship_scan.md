# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T06:52:21.960341+00:00`
- Price records: `672`
- Market context records: `1922`
- Flow alert records: `7431`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6020`

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

- `market_context_high->crypto_alt_4h` score `7.6669` n `201` status `ready` deltaP `23.8009` edge `0.5947` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.1835` n `201` status `ready` deltaP `29.0893` edge `0.5293` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8511` n `201` status `ready` deltaP `17.253` edge `0.4083` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6061` n `201` status `ready` deltaP `15.8741` edge `0.2208` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.8459` n `213` status `ready` deltaP `9.046` edge `0.1088` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.812` n `194` status `ready` deltaP `13.6812` edge `0.5085` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.6782` n `213` status `ready` deltaP `8.1886` edge `0.1133` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.6314` n `194` status `ready` deltaP `13.0674` edge `0.2081` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.4847` n `201` status `ready` deltaP `10.3932` edge `0.08` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.3859` n `194` status `ready` deltaP `5.0544` edge `0.1213` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.0648` n `213` status `ready` deltaP `5.4869` edge `0.0374` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1497` n `194` status `ready` deltaP `10.9841` edge `0.0192` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6061` n `213` status `ready` deltaP `0.5201` edge `0.0092` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6119` n `213` status `ready` deltaP `5.4194` edge `0.019` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6812` n `213` status `ready` deltaP `-3.6912` edge `0.0005` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.7476` n `201` status `ready` deltaP `11.3381` edge `0.1313` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.8179` n `201` status `ready` deltaP `-2.4951` edge `0.0006` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-1.1838` n `213` status `ready` deltaP `1.8063` edge `-0.0155` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.2227` n `194` status `ready` deltaP `6.7583` edge `0.3429` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-2.0818` n `213` status `ready` deltaP `0.5545` edge `-0.0148` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
