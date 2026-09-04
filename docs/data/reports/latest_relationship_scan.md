# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T12:07:24.454178+00:00`
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

- `risk_on_high->unknown_4h` score `20.0642` n `133` status `ready` deltaP `7.6265` edge `1.683` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.0642` n `133` status `ready` deltaP `7.6265` edge `1.683` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `12.1448` n `133` status `ready` deltaP `-0.7542` edge `1.0748` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.1448` n `133` status `ready` deltaP `-0.7542` edge `1.0748` maxDD `-1.95`
- `market_context_high->unknown_4h` score `11.7206` n `193` status `ready` deltaP `9.4575` edge `0.9832` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.46` n `205` status `ready` deltaP `-0.8018` edge `0.7734` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.392` n `61` status `ready` deltaP `11.8028` edge `0.0574` maxDD `-0.2737`
- `market_context_high->equity_24h` score `1.0793` n `167` status `ready` deltaP `15.2414` edge `0.4229` maxDD `-20.7654`
- `news_risk_high->commodity_24h` score `0.7336` n `61` status `ready` deltaP `9.6483` edge `0.0141` maxDD `-0.0495`
- `risk_on_high->metal_1h` score `0.1607` n `133` status `ready` deltaP `13.0116` edge `0.0051` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1607` n `133` status `ready` deltaP `13.0116` edge `0.0051` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0354` n `61` status `ready` deltaP `5.1315` edge `-0.0034` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.1148` n `61` status `ready` deltaP `5.1095` edge `0.001` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1871` n `133` status `ready` deltaP `3.3936` edge `-0.0021` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1871` n `133` status `ready` deltaP `3.3936` edge `-0.0021` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.2822` n `205` status `ready` deltaP `7.1506` edge `0.0018` maxDD `-2.1858`
- `risk_on_high->equity_24h` score `-0.3733` n `133` status `ready` deltaP `9.8567` edge `0.3177` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `-0.3733` n `133` status `ready` deltaP `9.8567` edge `0.3177` maxDD `-19.828`
- `risk_on_high->crypto_alt_1h` score `-0.402` n `133` status `ready` deltaP `3.7031` edge `0.0435` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.402` n `133` status `ready` deltaP `3.7031` edge `0.0435` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
