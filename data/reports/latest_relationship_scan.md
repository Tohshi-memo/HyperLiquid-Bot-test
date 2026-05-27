# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T19:07:32.538116+00:00`
- Price records: `672`
- Market context records: `2067`
- Flow alert records: `7845`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.6546` n `206` status `ready` deltaP `34.1774` edge `0.6297` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.9816` n `206` status `ready` deltaP `26.4504` edge `0.6866` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.6156` n `206` status `ready` deltaP `21.5279` edge `0.4827` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.7212` n `205` status `ready` deltaP `19.5907` edge `0.8782` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5513` n `206` status `ready` deltaP `19.4545` edge `0.2757` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0486` n `206` status `ready` deltaP `15.4467` edge `0.1361` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8234` n `206` status `ready` deltaP `14.005` edge `0.1572` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.6755` n `205` status `ready` deltaP `20.4701` edge `0.493` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.48` n `206` status `ready` deltaP `11.011` edge `0.1613` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.4205` n `205` status `ready` deltaP `8.9721` edge `0.1814` maxDD `-4.1604`
- `market_context_high->unknown_1h` score `0.4211` n `206` status `ready` deltaP `5.4081` edge `0.071` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4189` n `206` status `ready` deltaP `8.1217` edge `0.0596` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.3985` n `205` status `ready` deltaP `20.6836` edge `0.7539` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0816` n `206` status `ready` deltaP `4.0565` edge `0.0252` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2797` n `205` status `ready` deltaP `13.5446` edge `0.0257` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5609` n `206` status `ready` deltaP `11.6741` edge `0.1377` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7739` n `206` status `ready` deltaP `3.9969` edge `0.0276` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8035` n `206` status `ready` deltaP `-0.7485` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3957` n `206` status `ready` deltaP `-4.2402` edge `0.0001` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.9047` n `205` status `ready` deltaP `10.7089` edge `0.16` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
