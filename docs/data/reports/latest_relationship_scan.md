# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T01:52:24.864792+00:00`
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

- `risk_on_high->unknown_4h` score `22.8515` n `133` status `ready` deltaP `10.218` edge `1.898` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.8515` n `133` status `ready` deltaP `10.218` edge `1.898` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `16.0865` n `167` status `ready` deltaP `11.8163` edge `1.3313` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `14.0263` n `133` status `ready` deltaP `-0.1554` edge `1.2276` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `14.0263` n `133` status `ready` deltaP `-0.1554` edge `1.2276` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.5465` n `167` status `ready` deltaP `0.2994` edge `0.8566` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.6698` n `135` status `ready` deltaP `15.9723` edge `0.3839` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `0.3201` n `67` status `ready` deltaP `5.9474` edge `0.0373` maxDD `-0.8733`
- `risk_on_high->equity_24h` score `0.1116` n `113` status `ready` deltaP `11.2525` edge `0.3488` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.1116` n `113` status `ready` deltaP `11.2525` edge `0.3488` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.0673` n `133` status `ready` deltaP `11.814` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0673` n `133` status `ready` deltaP `11.814` edge `0.0011` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0485` n `67` status `ready` deltaP `4.7748` edge `-0.0027` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.0866` n `133` status `ready` deltaP `5.19` edge `-0.0012` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0866` n `133` status `ready` deltaP `5.19` edge `-0.0012` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.1754` n `133` status `ready` deltaP `4.9007` edge `0.0544` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1754` n `133` status `ready` deltaP `4.9007` edge `0.0544` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.1786` n `67` status `ready` deltaP `4.4517` edge `-0.0253` maxDD `-0.2074`
- `news_risk_high->fx_4h` score `-0.2062` n `67` status `ready` deltaP `6.9075` edge `0.0024` maxDD `-1.2507`
- `news_risk_high->commodity_1h` score `-0.2125` n `67` status `ready` deltaP `4.0084` edge `0.0002` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
