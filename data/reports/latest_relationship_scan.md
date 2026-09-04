# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T14:07:25.308282+00:00`
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

- `risk_on_high->unknown_4h` score `20.2396` n `133` status `ready` deltaP `7.779` edge `1.6966` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.2396` n `133` status `ready` deltaP `7.779` edge `1.6966` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3025` n `133` status `ready` deltaP `-1.353` edge `1.0086` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3025` n `133` status `ready` deltaP `-1.353` edge `1.0086` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.3003` n `201` status `ready` deltaP `8.4449` edge `0.8716` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.127` n `212` status `ready` deltaP `-0.7288` edge `0.8285` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4865` n `61` status `ready` deltaP `12.565` edge `0.0602` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.9516` n `61` status `ready` deltaP `11.0372` edge `0.023` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.4774` n `167` status `ready` deltaP `13.8525` edge `0.382` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.167` n `133` status `ready` deltaP `13.0116` edge `0.0059` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.167` n `133` status `ready` deltaP `13.0116` edge `0.0059` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0089` n `61` status `ready` deltaP `5.5806` edge `-0.003` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0585` n `61` status `ready` deltaP `5.5586` edge `0.0027` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1606` n `133` status `ready` deltaP `3.8427` edge `-0.0017` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1606` n `133` status `ready` deltaP `3.8427` edge `-0.0017` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.276` n `133` status `ready` deltaP `3.7031` edge `0.054` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.276` n `133` status `ready` deltaP `3.7031` edge `0.054` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.3947` n `133` status `ready` deltaP `0.4064` edge `0.0012` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.3947` n `133` status `ready` deltaP `0.4064` edge `0.0012` maxDD `-1.0281`
- `market_context_high->metal_1h` score `-0.4207` n `212` status `ready` deltaP `6.649` edge `-0.0025` maxDD `-2.9947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
