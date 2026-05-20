# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T03:22:19.299231+00:00`
- Price records: `672`
- Market context records: `1282`
- Flow alert records: `5601`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.7445` n `128` status `ready` deltaP `41.5798` edge `1.3147` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.2489` n `128` status `ready` deltaP `7.6389` edge `1.0532` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.9477` n `128` status `ready` deltaP `25.7812` edge `0.7754` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.4845` n `128` status `ready` deltaP `28.6458` edge `0.3747` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8956` n `128` status `ready` deltaP `25.1736` edge `0.5643` maxDD `-14.2815`
- `market_context_high->unknown_4h` score `3.6327` n `140` status `ready` deltaP `3.6978` edge `0.4337` maxDD `-7.7833`
- `market_context_high->equity_4h` score `2.7019` n `140` status `ready` deltaP `13.3929` edge `0.2022` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3586` n `128` status `ready` deltaP `1.5625` edge `0.4591` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5397` n `128` status `ready` deltaP `-13.3681` edge `0.3656` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.0109` n `140` status `ready` deltaP `8.8415` edge `0.1022` maxDD `-2.1521`
- `market_context_high->metal_4h` score `0.4266` n `140` status `ready` deltaP `15.2177` edge `0.0772` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.3635` n `152` status `ready` deltaP `4.6211` edge `0.0422` maxDD `-1.7505`
- `market_context_high->fx_24h` score `0.279` n `128` status `ready` deltaP `5.2952` edge `0.0344` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.1589` n `152` status `ready` deltaP `6.8666` edge `0.02` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.091` n `152` status `ready` deltaP `10.223` edge `0.0084` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3283` n `152` status `ready` deltaP `1.044` edge `0.038` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5461` n `152` status `ready` deltaP `0.5949` edge `-0.0039` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.6216` n `140` status `ready` deltaP `5.0217` edge `0.1362` maxDD `-12.6166`
- `market_context_high->crypto_major_1h` score `-0.736` n `152` status `ready` deltaP `0.0315` edge `0.0075` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8712` n `140` status `ready` deltaP `8.4844` edge `0.1637` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
