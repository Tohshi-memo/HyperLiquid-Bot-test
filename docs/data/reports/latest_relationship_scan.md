# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T11:37:29.183231+00:00`
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

- `risk_on_high->unknown_4h` score `20.0738` n `133` status `ready` deltaP `7.6265` edge `1.6838` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.0738` n `133` status `ready` deltaP `7.6265` edge `1.6838` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `12.2694` n `191` status `ready` deltaP `10.2876` edge `1.0234` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.146` n `133` status `ready` deltaP `-0.7542` edge `1.0749` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.146` n `133` status `ready` deltaP `-0.7542` edge `1.0749` maxDD `-1.95`
- `market_context_high->unknown_1h` score `8.8139` n `203` status `ready` deltaP `-0.1578` edge `0.7986` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.3786` n `61` status `ready` deltaP `11.6503` edge `0.0573` maxDD `-0.2737`
- `market_context_high->equity_24h` score `1.2583` n `167` status `ready` deltaP `15.5886` edge `0.4355` maxDD `-20.7654`
- `news_risk_high->commodity_24h` score `0.6759` n `61` status `ready` deltaP `9.301` edge `0.0116` maxDD `-0.0495`
- `risk_on_high->metal_1h` score `0.1592` n `133` status `ready` deltaP `13.0116` edge `0.0049` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1592` n `133` status `ready` deltaP `13.0116` edge `0.0049` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0517` n `61` status `ready` deltaP `4.8321` edge `-0.0035` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0992` n `61` status `ready` deltaP `5.2592` edge `0.0013` maxDD `-0.9036`
- `risk_on_high->equity_24h` score `-0.1943` n `133` status `ready` deltaP `10.2039` edge `0.3303` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `-0.1943` n `133` status `ready` deltaP `10.2039` edge `0.3303` maxDD `-19.828`
- `risk_on_high->index_1h` score `-0.2034` n `133` status `ready` deltaP `3.0942` edge `-0.0022` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.2034` n `133` status `ready` deltaP `3.0942` edge `-0.0022` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.3061` n `203` status `ready` deltaP `6.7373` edge `0.0015` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.3625` n `133` status `ready` deltaP `4.0025` edge `0.0448` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3625` n `133` status `ready` deltaP `4.0025` edge `0.0448` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
