# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T07:22:30.281117+00:00`
- Price records: `672`
- Market context records: `7753`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `5.2854` n `132` status `ready` deltaP `22.8803` edge `0.4221` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8259` n `133` status `ready` deltaP `11.9603` edge `0.0332` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.7508` n `133` status `ready` deltaP `8.9312` edge `0.2121` maxDD `-2.3927`
- `market_context_high->equity_1h` score `0.4778` n `133` status `ready` deltaP `8.1961` edge `0.0711` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4697` n `133` status `ready` deltaP `12.5172` edge `0.1275` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.4283` n `132` status `ready` deltaP `19.4357` edge `0.0341` maxDD `-3.0343`
- `market_context_high->equity_4h` score `0.3887` n `133` status `ready` deltaP `1.9694` edge `0.228` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.9447` edge `0.0147` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2184` n `133` status `ready` deltaP `6.8276` edge `0.0844` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0038` n `133` status `ready` deltaP `3.3801` edge `0.0204` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1592` n `133` status `ready` deltaP `3.8452` edge `0.007` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2411` n `133` status `ready` deltaP `3.5639` edge `0.0155` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2577` n `133` status `ready` deltaP `10.5585` edge `0.0424` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4771` n `133` status `ready` deltaP `-0.0767` edge `-0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8231` n `133` status `ready` deltaP `1.8662` edge `0.0193` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4345` n `133` status `ready` deltaP `1.443` edge `0.0763` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4761` n `133` status `ready` deltaP `-3.8559` edge `-0.0007` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.5941` n `132` status `ready` deltaP `5.6858` edge `-0.0124` maxDD `-7.0012`
- `market_context_high->index_24h` score `-2.2622` n `132` status `ready` deltaP `-16.0147` edge `0.027` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.298` n `133` status `ready` deltaP `-1.7232` edge `-0.121` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
