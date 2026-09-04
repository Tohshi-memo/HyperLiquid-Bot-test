# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T13:37:28.191211+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10980`

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

- `risk_on_high->unknown_4h` score `20.117` n `133` status `ready` deltaP `7.6265` edge `1.6874` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.117` n `133` status `ready` deltaP `7.6265` edge `1.6874` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.5701` n `133` status `ready` deltaP `-1.353` edge `1.0309` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.5701` n `133` status `ready` deltaP `-1.353` edge `1.0309` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.5591` n `199` status `ready` deltaP `8.5749` edge `0.8923` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.7169` n `211` status `ready` deltaP `-0.8897` edge `0.7954` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4478` n `61` status `ready` deltaP `12.2601` edge `0.059` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.8926` n `61` status `ready` deltaP `10.6899` edge `0.0204` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.6444` n `167` status `ready` deltaP `14.1997` edge `0.3936` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1779` n `133` status `ready` deltaP `13.1613` edge `0.0063` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1779` n `133` status `ready` deltaP `13.1613` edge `0.0063` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0073` n `61` status `ready` deltaP `5.5806` edge `-0.0028` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0944` n `61` status `ready` deltaP `5.2592` edge `0.0017` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.159` n `133` status `ready` deltaP `3.8427` edge `-0.0015` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.159` n `133` status `ready` deltaP `3.8427` edge `-0.0015` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2832` n `133` status `ready` deltaP `3.7031` edge `0.0534` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2832` n `133` status `ready` deltaP `3.7031` edge `0.0534` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.4181` n `133` status `ready` deltaP `0.107` edge `0.0002` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4181` n `133` status `ready` deltaP `0.107` edge `0.0002` maxDD `-1.0281`
- `market_context_high->metal_1h` score `-0.4265` n `211` status `ready` deltaP `6.5975` edge `-0.0029` maxDD `-2.9947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
