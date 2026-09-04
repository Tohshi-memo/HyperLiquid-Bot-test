# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T12:37:27.727150+00:00`
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

- `risk_on_high->unknown_4h` score `20.0136` n `133` status `ready` deltaP `7.4741` edge `1.6798` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.0136` n `133` status `ready` deltaP `7.4741` edge `1.6798` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `12.0944` n `133` status `ready` deltaP `-0.9039` edge `1.0716` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.0944` n `133` status `ready` deltaP `-0.9039` edge `1.0716` maxDD `-1.95`
- `market_context_high->unknown_4h` score `11.2559` n `195` status `ready` deltaP `9.0049` edge `0.9475` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.2129` n `207` status `ready` deltaP `-1.1` edge `0.7548` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.3956` n `61` status `ready` deltaP `11.8028` edge `0.0577` maxDD `-0.2737`
- `market_context_high->equity_24h` score `0.9207` n `167` status `ready` deltaP `14.8942` edge `0.412` maxDD `-20.7654`
- `news_risk_high->commodity_24h` score `0.789` n `61` status `ready` deltaP `9.9955` edge `0.0164` maxDD `-0.0495`
- `risk_on_high->metal_1h` score `0.174` n `133` status `ready` deltaP `13.1613` edge `0.0058` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.174` n `133` status `ready` deltaP `13.1613` edge `0.0058` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0175` n `61` status `ready` deltaP `5.4309` edge `-0.0031` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.1124` n `61` status `ready` deltaP `5.1095` edge `0.0012` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1692` n `133` status `ready` deltaP `3.693` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1692` n `133` status `ready` deltaP `3.693` edge `-0.0018` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.2871` n `207` status `ready` deltaP `7.2225` edge `0.0007` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.372` n `133` status `ready` deltaP `3.7031` edge `0.046` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.372` n `133` status `ready` deltaP `3.7031` edge `0.046` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.4298` n `133` status `ready` deltaP `-0.0427` edge `-0.0003` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4298` n `133` status `ready` deltaP `-0.0427` edge `-0.0003` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
