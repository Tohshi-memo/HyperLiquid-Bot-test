# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T10:52:33.019655+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.1378` n `133` status `ready` deltaP `7.9314` edge `1.6871` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.1378` n `133` status `ready` deltaP `7.9314` edge `1.6871` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `12.9349` n `188` status `ready` deltaP `10.8069` edge `1.0754` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.1772` n `133` status `ready` deltaP `-0.9039` edge `1.0785` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.1772` n `133` status `ready` deltaP `-0.9039` edge `1.0785` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.1155` n `200` status `ready` deltaP `-0.3174` edge `0.8248` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.5304` n `167` status `ready` deltaP `16.1095` edge `0.4547` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `1.3604` n `61` status `ready` deltaP `11.4979` edge `0.0568` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.6157` n `61` status `ready` deltaP `8.9538` edge `0.0089` maxDD `-0.0495`
- `risk_on_high->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1498` n `133` status `ready` deltaP `12.8619` edge `0.0047` maxDD `-1.699`
- `risk_on_high->equity_24h` score `0.0778` n `133` status `ready` deltaP `10.7248` edge `0.3495` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.0778` n `133` status `ready` deltaP `10.7248` edge `0.3495` maxDD `-19.828`
- `news_risk_high->index_1h` score `-0.0517` n `61` status `ready` deltaP `4.8321` edge `-0.0035` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.092` n `61` status `ready` deltaP `5.2592` edge `0.0019` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.2034` n `133` status `ready` deltaP `3.0942` edge `-0.0022` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2034` n `133` status `ready` deltaP `3.0942` edge `-0.0022` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2929` n `133` status `ready` deltaP `4.4516` edge `0.0476` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2929` n `133` status `ready` deltaP `4.4516` edge `0.0476` maxDD `-5.4685`
- `market_context_high->metal_1h` score `-0.324` n `200` status `ready` deltaP `6.4521` edge `0.0011` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
