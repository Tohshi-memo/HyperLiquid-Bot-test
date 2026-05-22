# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T18:07:17.228275+00:00`
- Price records: `672`
- Market context records: `1551`
- Flow alert records: `6376`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.3372` n `182` status `ready` deltaP `23.1227` edge `0.974` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.875` n `182` status `ready` deltaP `26.9974` edge `0.9279` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2721` n `182` status `ready` deltaP `26.7399` edge `0.7076` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.11` n `182` status `ready` deltaP `20.7799` edge `0.3126` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6435` n `182` status `ready` deltaP `13.721` edge `0.3615` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.6326` n `182` status `ready` deltaP `16.0084` edge `0.0509` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3231` n `199` status `ready` deltaP `5.3959` edge `0.1004` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.163` n `199` status `ready` deltaP `13.2545` edge `0.2227` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.2593` n `199` status `ready` deltaP `9.1272` edge `0.1768` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4416` n `199` status `ready` deltaP `0.668` edge `0.0413` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6249` n `199` status `ready` deltaP `-1.9942` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6845` n `199` status `ready` deltaP `0.1016` edge `0.0037` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7431` n `199` status `ready` deltaP `5.1478` edge `0.004` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7944` n `199` status `ready` deltaP `-0.4235` edge `-0.0002` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8308` n `199` status `ready` deltaP `-1.1825` edge `0.0195` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9745` n `199` status `ready` deltaP `-0.8929` edge `0.0167` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3378` n `199` status `ready` deltaP `10.516` edge `0.0876` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3634` n `199` status `ready` deltaP `-10.2448` edge `-0.0136` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4414` n `199` status `ready` deltaP `-4.5923` edge `0.0194` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.144` n `199` status `ready` deltaP `-14.5476` edge `-0.0998` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
