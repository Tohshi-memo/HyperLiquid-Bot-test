# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T21:22:20.096761+00:00`
- Price records: `672`
- Market context records: `2077`
- Flow alert records: `7873`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `9.9781` n `202` status `ready` deltaP `35.5651` edge `0.6474` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.4111` n `202` status `ready` deltaP `28.2933` edge `0.7101` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.0141` n `202` status `ready` deltaP `22.9987` edge `0.5061` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.9372` n `201` status `ready` deltaP `20.8662` edge `0.8877` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.6304` n `202` status `ready` deltaP `19.6027` edge `0.2813` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0781` n `202` status `ready` deltaP `15.6801` edge `0.137` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.9894` n `202` status `ready` deltaP `14.9552` edge `0.1647` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.8081` n `201` status `ready` deltaP `21.1684` edge `0.4994` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.6476` n `201` status `ready` deltaP `10.1602` edge `0.1924` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.61` n `202` status `ready` deltaP `11.6159` edge `0.1681` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.4979` n `202` status `ready` deltaP `8.6441` edge `0.0627` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.4546` n `202` status `ready` deltaP `5.0765` edge `0.076` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.4498` n `201` status `ready` deltaP `21.1004` edge `0.7554` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.1026` n `202` status `ready` deltaP `3.913` edge `0.0244` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2055` n `201` status `ready` deltaP `14.2024` edge `0.0275` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.3949` n `202` status `ready` deltaP `11.9989` edge `0.1416` maxDD `-11.3602`
- `market_context_high->fx_1h` score `-0.5839` n `202` status `ready` deltaP `-1.8883` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.7674` n `202` status `ready` deltaP `4.0182` edge `0.028` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.4121` n `202` status `ready` deltaP `-4.46` edge `0.0002` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.6468` n `201` status `ready` deltaP `11.1725` edge `0.1784` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
