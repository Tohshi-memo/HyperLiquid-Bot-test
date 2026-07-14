# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T11:22:29.509193+00:00`
- Price records: `672`
- Market context records: `6704`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.0996` n `181` status `ready` deltaP `1.3495` edge `0.5072` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.3186` n `181` status `ready` deltaP `9.3799` edge `0.05` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1319` n `181` status `ready` deltaP `6.4214` edge `0.0446` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.137` n `181` status `ready` deltaP `8.8964` edge `0.1161` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3548` n `181` status `ready` deltaP `0.3474` edge `0.0007` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5487` n `181` status `ready` deltaP `-0.3333` edge `0.0033` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5921` n `181` status `ready` deltaP `-3.659` edge `0.001` maxDD `-1.2017`
- `market_context_high->unknown_1h` score `-0.5946` n `181` status `ready` deltaP `-6.7564` edge `0.0856` maxDD `-3.2083`
- `market_context_high->commodity_1h` score `-0.6506` n `181` status `ready` deltaP `-0.4507` edge `-0.0121` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9622` n `181` status `ready` deltaP `3.3025` edge `0.0005` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9673` n `181` status `ready` deltaP `9.7444` edge `-0.001` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2664` n `181` status `ready` deltaP `7.1933` edge `-0.0002` maxDD `-2.4756`
- `market_context_high->crypto_major_4h` score `-1.6111` n `181` status `ready` deltaP `7.5159` edge `0.0748` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8339` n `181` status `ready` deltaP `-5.8407` edge `-0.0472` maxDD `-5.5853`
- `market_context_high->crypto_alt_4h` score `-1.8394` n `181` status `ready` deltaP `5.6487` edge `0.0667` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.318` n `181` status `ready` deltaP `-3.7992` edge `0.0142` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.9141` n `181` status `ready` deltaP `-16.9831` edge `0.0236` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4925` n `181` status `ready` deltaP `-8.833` edge `-0.0008` maxDD `-6.5083`
- `market_context_high->equity_4h` score `-5.4343` n `181` status `ready` deltaP `6.5633` edge `-0.0697` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0694` n `181` status `ready` deltaP `-6.4821` edge `-0.0146` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
