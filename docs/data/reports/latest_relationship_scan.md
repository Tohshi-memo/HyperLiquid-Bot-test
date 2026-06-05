# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T23:52:21.888303+00:00`
- Price records: `672`
- Market context records: `3018`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `21.7712` n `98` status `ready` deltaP `9.4565` edge `2.1429` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.9992` n `98` status `ready` deltaP `43.3355` edge `0.8054` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.7795` n `98` status `ready` deltaP `21.6943` edge `0.9668` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.8407` n `98` status `ready` deltaP `20.4295` edge `1.0509` maxDD `-12.6963`
- `market_context_high->index_24h` score `7.3791` n `98` status `ready` deltaP `20.0397` edge `0.5794` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4527` n `109` status `ready` deltaP `18.3612` edge `0.1467` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5032` n `109` status `ready` deltaP `13.1587` edge `0.1677` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.2441` n `109` status `ready` deltaP `23.6687` edge `0.4283` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.0875` n `109` status `ready` deltaP `16.1991` edge `0.093` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `-0.0152` n `121` status `ready` deltaP `2.2938` edge `0.0257` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3982` n `121` status `ready` deltaP `3.2043` edge `0.0354` maxDD `-5.6254`
- `market_context_high->fx_1h` score `-0.428` n `121` status `ready` deltaP `-2.8146` edge `0.0005` maxDD `-0.2615`
- `market_context_high->index_1h` score `-0.4285` n `121` status `ready` deltaP `3.7908` edge `0.0212` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.7562` n `121` status `ready` deltaP `5.821` edge `0.0772` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.9063` n `121` status `ready` deltaP `3.5037` edge `-0.0258` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1009` n `109` status `ready` deltaP `-9.1729` edge `-0.001` maxDD `-0.6521`
- `market_context_high->metal_1h` score `-1.2098` n `121` status `ready` deltaP `-2.6835` edge `-0.0054` maxDD `-6.8783`
- `market_context_high->crypto_major_1h` score `-1.2205` n `121` status `ready` deltaP `3.5569` edge `0.0461` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-1.2972` n `109` status `ready` deltaP `-1.8251` edge `0.0094` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7095` n `98` status `ready` deltaP `-4.5705` edge `-0.0248` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
