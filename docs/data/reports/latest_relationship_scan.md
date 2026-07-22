# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T21:37:27.524634+00:00`
- Price records: `672`
- Market context records: `7604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->unknown_24h` score `1.0377` n `147` status `ready` deltaP `12.8827` edge `0.128` maxDD `-5.1929`
- `market_context_high->equity_24h` score `0.695` n `146` status `ready` deltaP `16.4575` edge `0.5174` maxDD `-38.3748`
- `market_context_high->commodity_24h` score `0.4664` n `146` status `ready` deltaP `15.9777` edge `0.0907` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0847` n `147` status `ready` deltaP `7.0448` edge `0.0118` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1431` n `147` status `ready` deltaP `8.0543` edge `0.024` maxDD `-4.0162`
- `market_context_high->commodity_4h` score `-0.1609` n `147` status `ready` deltaP `6.6592` edge `0.0182` maxDD `-2.4139`
- `market_context_high->commodity_1h` score `-0.2279` n `147` status `ready` deltaP `4.1399` edge `0.0004` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.2386` n `147` status `ready` deltaP `1.8504` edge `0.0203` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3573` n `146` status `ready` deltaP `8.9686` edge `0.0192` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4759` n `147` status `ready` deltaP `6.2144` edge `0.0538` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.585` n `147` status `ready` deltaP `9.8952` edge `0.0308` maxDD `-3.4082`
- `market_context_high->metal_1h` score `-0.6316` n `147` status `ready` deltaP `1.3615` edge `0.0145` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6495` n `147` status `ready` deltaP `-0.3585` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9929` n `147` status `ready` deltaP `3.2956` edge `0.0564` maxDD `-9.7866`
- `market_context_high->unknown_1h` score `-1.0215` n `147` status `ready` deltaP `-1.1701` edge `-0.0608` maxDD `-1.3217`
- `market_context_high->crypto_major_4h` score `-1.1056` n `147` status `ready` deltaP `9.3361` edge `0.068` maxDD `-14.7592`
- `market_context_high->equity_4h` score `-1.4579` n `147` status `ready` deltaP `3.3982` edge `0.2154` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6236` n `147` status `ready` deltaP `-1.2206` edge `0.0463` maxDD `-4.7051`
- `market_context_high->metal_24h` score `-1.8571` n `147` status `ready` deltaP `-1.2614` edge `0.1111` maxDD `-8.2622`
- `market_context_high->fx_4h` score `-2.5968` n `147` status `ready` deltaP `-6.5905` edge `-0.004` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
