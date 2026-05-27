# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T10:22:23.968107+00:00`
- Price records: `672`
- Market context records: `2033`
- Flow alert records: `7743`
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

- `market_context_high->crypto_major_4h` score `8.8715` n `205` status `ready` deltaP `30.7927` edge `0.587` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3548` n `205` status `ready` deltaP `24.3903` edge `0.6481` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8871` n `205` status `ready` deltaP `18.8414` edge `0.4399` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0011` n `205` status `ready` deltaP `17.2561` edge `0.2445` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5332` n `205` status `ready` deltaP `12.4777` edge `0.1432` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4522` n `205` status `ready` deltaP `12.9269` edge `0.1032` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2845` n `205` status `ready` deltaP `10.2322` edge `0.1502` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.0782` n `202` status `ready` deltaP `16.9792` edge `0.5087` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.4722` n `202` status `ready` deltaP `16.0637` edge `0.4221` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3528` n `202` status `ready` deltaP `4.4758` edge `0.1224` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.1972` n `205` status `ready` deltaP `6.7607` edge `0.0502` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0158` n `205` status `ready` deltaP `3.7462` edge `0.0483` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2834` n `205` status `ready` deltaP `2.7034` edge `0.0174` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5431` n `202` status `ready` deltaP `10.5961` edge `0.0217` maxDD `-2.6745`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8994` n `205` status `ready` deltaP `3.6585` edge `0.0194` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1498` n `205` status `ready` deltaP `8.872` edge `0.1073` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5829` n `205` status `ready` deltaP `-6.2805` edge `-0.0019` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.6207` n `202` status `ready` deltaP `9.7704` edge `0.1356` maxDD `-19.8634`
- `market_context_high->commodity_1h` score `-1.8371` n `205` status `ready` deltaP `2.7552` edge `0.0019` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
