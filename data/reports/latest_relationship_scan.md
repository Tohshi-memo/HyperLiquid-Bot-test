# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T14:37:22.914593+00:00`
- Price records: `672`
- Market context records: `2048`
- Flow alert records: `7790`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `9.2168` n `205` status `ready` deltaP `32.3338` edge `0.6055` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.541` n `205` status `ready` deltaP `24.8573` edge `0.6605` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2399` n `205` status `ready` deltaP `19.7709` edge `0.4631` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.1033` n `205` status `ready` deltaP `17.7537` edge `0.2497` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.9307` n `205` status `ready` deltaP `17.5146` edge `0.6595` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6939` n `205` status `ready` deltaP `13.2262` edge `0.1516` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.6535` n `205` status `ready` deltaP `13.8832` edge `0.1136` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.3169` n `205` status `ready` deltaP `10.2322` edge `0.1529` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.8851` n `205` status `ready` deltaP `17.3559` edge `0.4479` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.7694` n `205` status `ready` deltaP `5.8579` edge `0.1479` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.3507` n `205` status `ready` deltaP `7.8086` edge `0.056` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2292` n `205` status `ready` deltaP `4.6444` edge `0.0601` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1348` n `205` status `ready` deltaP `3.7513` edge `0.0228` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4908` n `205` status `ready` deltaP `11.2954` edge `0.0231` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.7699` n `205` status `ready` deltaP `4.407` edge `0.0252` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8003` n `205` status `ready` deltaP `-0.693` edge `0.0007` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-0.8454` n `205` status `ready` deltaP `10.2328` edge `0.1236` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-1.0566` n `205` status `ready` deltaP `17.5694` edge `0.6534` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.444` n `205` status `ready` deltaP `-4.7394` edge `-0.0006` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9275` n `205` status `ready` deltaP `1.857` edge `-0.0037` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
