# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T15:37:23.554809+00:00`
- Price records: `672`
- Market context records: `2052`
- Flow alert records: `7802`
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

- `market_context_high->crypto_major_4h` score `9.3655` n `205` status `ready` deltaP `32.8582` edge `0.6144` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.6754` n `205` status `ready` deltaP `25.233` edge `0.6692` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.302` n `205` status `ready` deltaP `19.9918` edge `0.4668` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.4401` n `205` status `ready` deltaP `17.6876` edge `0.7008` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.2451` n `205` status `ready` deltaP `18.2663` edge `0.2581` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.8013` n `205` status `ready` deltaP `14.3951` edge `0.1225` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.6699` n `206` status `ready` deltaP `13.2565` edge `0.1494` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2773` n `206` status `ready` deltaP `10.2625` edge `0.1494` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.0677` n `205` status `ready` deltaP `18.0479` edge `0.4585` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.9435` n `205` status `ready` deltaP `6.5499` edge `0.1578` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4069` n `206` status `ready` deltaP `8.2714` edge `0.0576` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2784` n `206` status `ready` deltaP `4.6596` edge `0.0641` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1487` n `206` status `ready` deltaP `3.6074` edge `0.0226` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4282` n `205` status `ready` deltaP `11.9875` edge `0.0237` maxDD `-2.811`
- `market_context_high->crypto_major_24h` score `-0.7145` n `205` status `ready` deltaP `18.2615` edge `0.6773` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.7555` n `205` status `ready` deltaP `10.7711` edge `0.1275` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7783` n `206` status `ready` deltaP `-0.4491` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8004` n `206` status `ready` deltaP `4.1466` edge `0.0244` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4374` n `205` status `ready` deltaP `-4.6716` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9473` n `206` status `ready` deltaP `1.6423` edge `-0.0048` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
