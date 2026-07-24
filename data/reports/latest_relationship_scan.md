# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T21:07:30.445014+00:00`
- Price records: `672`
- Market context records: `7811`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `8.5758` n `132` status `ready` deltaP `28.5507` edge `0.6585` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.421` n `133` status `ready` deltaP `13.3644` edge `0.2384` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.1699` n `133` status `ready` deltaP `3.9571` edge `0.3149` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1199` n `133` status `ready` deltaP `14.194` edge `0.1705` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0861` n `133` status `ready` deltaP `13.3076` edge `0.0459` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8195` n `132` status `ready` deltaP `25.2187` edge `0.0457` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7236` n `133` status `ready` deltaP `7.7423` edge `0.1204` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6998` n `133` status `ready` deltaP `7.5955` edge `0.0936` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5645` n `133` status `ready` deltaP `9.3743` edge `0.0439` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2299` n `133` status `ready` deltaP `4.7274` edge `0.0309` maxDD `-1.4603`
- `market_context_high->commodity_24h` score `0.2044` n `132` status `ready` deltaP `14.8617` edge `0.0763` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.0019` n `133` status `ready` deltaP `5.0464` edge `0.0121` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1474` n `133` status `ready` deltaP `11.6288` edge `0.0494` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.321` n `133` status `ready` deltaP `1.7251` edge `0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3381` n `133` status `ready` deltaP `-1.5624` edge `0.0017` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5342` n `133` status `ready` deltaP `0.3759` edge `0.0751` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.5776` n `132` status `ready` deltaP `-9.3136` edge `0.0701` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2678` n `133` status `ready` deltaP `14.7431` edge `0.1405` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
