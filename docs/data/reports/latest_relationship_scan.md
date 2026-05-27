# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T17:37:24.234583+00:00`
- Price records: `672`
- Market context records: `2061`
- Flow alert records: `7827`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.6556` n `205` status `ready` deltaP `33.9939` edge `0.631` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.939` n `205` status `ready` deltaP `26.0671` edge `0.6856` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.5223` n `205` status `ready` deltaP `20.9756` edge `0.4786` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `4.5941` n `205` status `ready` deltaP `18.5527` edge `0.7912` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5522` n `205` status `ready` deltaP `19.3902` edge `0.2762` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0639` n `205` status `ready` deltaP `15.5183` edge `0.1369` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.809` n `206` status `ready` deltaP `14.005` edge `0.156` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.4556` n `205` status `ready` deltaP `19.432` edge `0.4816` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.4284` n `206` status `ready` deltaP `10.8613` edge `0.158` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.2583` n `205` status `ready` deltaP `7.934` edge `0.1748` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.468` n `206` status `ready` deltaP `8.5708` edge `0.0607` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3395` n `206` status `ready` deltaP `5.2584` edge `0.0652` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.0636` n `206` status `ready` deltaP `4.2062` edge `0.0257` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `-0.0721` n `205` status `ready` deltaP `19.6456` edge `0.7216` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.332` n `205` status `ready` deltaP `13.0255` edge `0.0248` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.6105` n `205` status `ready` deltaP `11.1586` edge `0.137` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7404` n `206` status `ready` deltaP `4.2963` edge `0.0284` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8287` n `206` status `ready` deltaP `-1.0479` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.404` n `205` status `ready` deltaP `-4.2988` edge `-0.0002` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9668` n `206` status `ready` deltaP `1.9417` edge `-0.0093` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
