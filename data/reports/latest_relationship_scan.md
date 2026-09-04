# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T13:52:30.489765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10956`

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

- `risk_on_high->unknown_4h` score `20.2226` n `133` status `ready` deltaP `7.6265` edge `1.6962` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.2226` n `133` status `ready` deltaP `7.6265` edge `1.6962` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3145` n `133` status `ready` deltaP `-1.353` edge `1.0096` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3145` n `133` status `ready` deltaP `-1.353` edge `1.0096` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.5366` n `200` status `ready` deltaP `8.6829` edge `0.8897` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.139` n `212` status `ready` deltaP `-0.7288` edge `0.8295` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4683` n `61` status `ready` deltaP `12.4125` edge `0.0597` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.9221` n `61` status `ready` deltaP `10.8635` edge `0.0217` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.5633` n `167` status `ready` deltaP `14.0261` edge `0.388` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1654` n `133` status `ready` deltaP `13.0116` edge `0.0057` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1654` n `133` status `ready` deltaP `13.0116` edge `0.0057` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0081` n `61` status `ready` deltaP `5.5806` edge `-0.0029` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0764` n `61` status `ready` deltaP `5.4089` edge `0.0022` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1598` n `133` status `ready` deltaP `3.8427` edge `-0.0016` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1598` n `133` status `ready` deltaP `3.8427` edge `-0.0016` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.2856` n `133` status `ready` deltaP `3.7031` edge `0.0532` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2856` n `133` status `ready` deltaP `3.7031` edge `0.0532` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.4064` n `133` status `ready` deltaP `0.2567` edge `0.0007` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4064` n `133` status `ready` deltaP `0.2567` edge `0.0007` maxDD `-1.0281`
- `market_context_high->metal_1h` score `-0.4223` n `212` status `ready` deltaP `6.649` edge `-0.0027` maxDD `-2.9947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
