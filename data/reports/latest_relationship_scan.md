# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T13:37:23.833334+00:00`
- Price records: `672`
- Market context records: `2044`
- Flow alert records: `7777`
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

- `market_context_high->crypto_major_4h` score `9.0349` n `205` status `ready` deltaP `31.7259` edge `0.5944` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4231` n `205` status `ready` deltaP `24.5534` edge `0.6527` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.1859` n `205` status `ready` deltaP `19.7709` edge `0.4586` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9575` n `205` status `ready` deltaP `17.1458` edge `0.2416` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.3331` n `205` status `ready` deltaP `17.5146` edge `0.6097` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6483` n `205` status `ready` deltaP `13.0765` edge `0.1488` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.5005` n `205` status `ready` deltaP `13.2753` edge `0.1049` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.3037` n `205` status `ready` deltaP `10.2322` edge `0.1518` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.7416` n `205` status `ready` deltaP `16.8368` edge `0.4394` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.6012` n `205` status `ready` deltaP `5.1658` edge `0.1385` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2847` n `205` status `ready` deltaP `7.3595` edge `0.0535` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0781` n `205` status `ready` deltaP `4.1953` edge `0.0505` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2271` n `205` status `ready` deltaP `3.1525` edge `0.0191` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5419` n `205` status `ready` deltaP `10.7764` edge `0.0223` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.7112` n `205` status `ready` deltaP `4.8561` edge `0.0271` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8134` n `205` status `ready` deltaP `-0.8427` edge `0.0006` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-0.9744` n `205` status `ready` deltaP `9.6249` edge `0.1169` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.4307` n `205` status `ready` deltaP `-4.5874` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->crypto_major_24h` score `-1.4912` n `205` status `ready` deltaP `16.8774` edge `0.6218` maxDD `-62.3533`
- `market_context_high->commodity_1h` score `-1.8948` n `205` status `ready` deltaP `2.1564` edge `-0.0015` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
