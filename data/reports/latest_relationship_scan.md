# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T05:37:25.458941+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11556`

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

- `risk_on_high->unknown_4h` score `21.2913` n `133` status `ready` deltaP `9.1509` edge `1.7751` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.2913` n `133` status `ready` deltaP `9.1509` edge `1.7751` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.2289` n `169` status `ready` deltaP `10.9972` edge `1.2653` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.7087` n `133` status `ready` deltaP `-0.6045` edge `1.1208` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.7087` n `133` status `ready` deltaP `-0.6045` edge `1.1208` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.1407` n `181` status `ready` deltaP `0.8328` edge `0.9859` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.2465` n `150` status `ready` deltaP `16.7014` edge `0.4271` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.106` n `128` status `ready` deltaP `13.1076` edge `0.4193` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.106` n `128` status `ready` deltaP `13.1076` edge `0.4193` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2608` n `67` status `ready` deltaP `5.0328` edge `0.0358` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0821` n `133` status `ready` deltaP `11.9637` edge `0.002` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0821` n `133` status `ready` deltaP `11.9637` edge `0.002` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1411` n `67` status `ready` deltaP `3.1281` edge `-0.0036` maxDD `-0.8275`
- `news_risk_high->commodity_24h` score `-0.1738` n `67` status `ready` deltaP `4.4517` edge `-0.0249` maxDD `-0.2074`
- `risk_on_high->index_1h` score `-0.1793` n `133` status `ready` deltaP `3.5433` edge `-0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1793` n `133` status `ready` deltaP `3.5433` edge `-0.0021` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1837` n `67` status `ready` deltaP `4.3078` edge `0.0006` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2282` n `133` status `ready` deltaP `4.9007` edge `0.05` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2282` n `133` status `ready` deltaP `4.9007` edge `0.05` maxDD `-5.4685`
- `market_context_high->metal_1h` score `-0.3707` n `181` status `ready` deltaP `6.0649` edge `-0.0023` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
