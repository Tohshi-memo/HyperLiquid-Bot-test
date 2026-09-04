# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T02:52:24.523125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11538`

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

- `risk_on_high->unknown_4h` score `22.6565` n `133` status `ready` deltaP `9.7607` edge `1.8848` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.6565` n `133` status `ready` deltaP `9.7607` edge `1.8848` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.8915` n `167` status `ready` deltaP `11.359` edge `1.3181` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `13.8558` n `133` status `ready` deltaP `-0.0057` edge `1.2124` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `13.8558` n `133` status `ready` deltaP `-0.0057` edge `1.2124` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.6676` n `170` status `ready` deltaP `0.4632` edge `0.8656` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.8242` n `139` status `ready` deltaP `16.237` edge `0.395` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.3905` n `117` status `ready` deltaP `11.859` edge `0.368` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.3905` n `117` status `ready` deltaP `11.859` edge `0.368` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.3121` n `67` status `ready` deltaP `5.795` edge `0.0373` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0774` n `133` status `ready` deltaP `11.9637` edge `0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0774` n `133` status `ready` deltaP `11.9637` edge `0.0014` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0562` n `67` status `ready` deltaP `4.6251` edge `-0.0027` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0944` n `133` status `ready` deltaP `5.0403` edge `-0.0012` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0944` n `133` status `ready` deltaP `5.0403` edge `-0.0012` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1714` n `67` status `ready` deltaP `4.4517` edge `-0.0247` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.1993` n `67` status `ready` deltaP `4.1581` edge `0.0003` maxDD `-0.9036`
- `news_risk_high->fx_4h` score `-0.261` n `67` status `ready` deltaP `6.2978` edge `0.0019` maxDD `-1.2507`
- `risk_on_high->crypto_alt_1h` score `-0.2738` n `133` status `ready` deltaP `4.6013` edge `0.0482` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2738` n `133` status `ready` deltaP `4.6013` edge `0.0482` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
