# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T21:52:16.625499+00:00`
- Price records: `672`
- Market context records: `1882`
- Flow alert records: `7319`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.0331` n `199` status `ready` deltaP `22.5089` edge `0.5505` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7783` n `199` status `ready` deltaP `27.7148` edge `0.5047` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3711` n `199` status `ready` deltaP `18.2628` edge `0.4449` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.4286` n `181` status `ready` deltaP `18.8421` edge `0.4027` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3936` n `199` status `ready` deltaP `14.582` edge `0.2117` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.0007` n `181` status `ready` deltaP `11.724` edge `0.2114` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.7922` n `181` status `ready` deltaP `12.7187` edge `0.5966` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5518` n `199` status `ready` deltaP `6.6448` edge `0.1003` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4543` n `199` status `ready` deltaP `9.7882` edge `0.0815` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.2653` n `199` status `ready` deltaP `5.7571` edge `0.0951` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2508` n `181` status `ready` deltaP `14.8807` edge `0.0266` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.2313` n `181` status `ready` deltaP `10.6834` edge `0.4379` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.0097` n `181` status `ready` deltaP `18.7635` edge `0.7343` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1815` n `199` status `ready` deltaP `4.2383` edge `0.036` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4437` n `199` status `ready` deltaP `3.5868` edge `0.0343` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5154` n `199` status `ready` deltaP `12.6953` edge `0.1416` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5219` n `199` status `ready` deltaP `6.5808` edge `0.0228` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.702` n `199` status `ready` deltaP `-0.7545` edge `0.0097` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7103` n `199` status `ready` deltaP `-4.1006` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
