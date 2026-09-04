# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T05:22:26.693701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11550`

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

- `risk_on_high->unknown_4h` score `21.4619` n `133` status `ready` deltaP `9.3034` edge `1.7883` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.4619` n `133` status `ready` deltaP `9.3034` edge `1.7883` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.0513` n `168` status `ready` deltaP `11.0265` edge `1.2503` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.7015` n `133` status `ready` deltaP `-0.6045` edge `1.1202` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.7015` n `133` status `ready` deltaP `-0.6045` edge `1.1202` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.3612` n `180` status `ready` deltaP `1.2042` edge `1.0018` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.1735` n `149` status `ready` deltaP `16.6737` edge `0.4212` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.0003` n `127` status `ready` deltaP `13.0167` edge `0.4111` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.0003` n `127` status `ready` deltaP `13.0167` edge `0.4111` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2521` n `67` status `ready` deltaP `4.8803` edge `0.0357` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0719` n `133` status `ready` deltaP `11.814` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0719` n `133` status `ready` deltaP `11.814` edge `0.0017` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1333` n `67` status `ready` deltaP `3.2778` edge `-0.0036` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1715` n `133` status `ready` deltaP `3.693` edge `-0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1715` n `133` status `ready` deltaP `3.693` edge `-0.0021` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1726` n `67` status `ready` deltaP `4.4517` edge `-0.0248` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1969` n `67` status `ready` deltaP `4.1581` edge `0.0005` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2546` n `133` status `ready` deltaP `4.751` edge `0.0488` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2546` n `133` status `ready` deltaP `4.751` edge `0.0488` maxDD `-5.4685`
- `market_context_high->metal_1h` score `-0.3633` n `180` status `ready` deltaP `6.2375` edge `-0.0025` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
