# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T13:22:28.452053+00:00`
- Price records: `672`
- Market context records: `4831`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.7415` n `109` status `ready` deltaP `11.038` edge `1.1133` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.7918` n `106` status `ready` deltaP `19.354` edge `0.7185` maxDD `-4.1903`
- `market_context_high->unknown_24h` score `3.4266` n `99` status `ready` deltaP `17.3611` edge `0.2325` maxDD `-2.3484`
- `market_context_high->index_4h` score `0.7669` n `106` status `ready` deltaP `9.9862` edge `0.044` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.6029` n `106` status `ready` deltaP `11.9018` edge `0.1361` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.3248` n `106` status `ready` deltaP `14.3782` edge `0.063` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1893` n `109` status `ready` deltaP `6.0361` edge `0.0322` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.1608` n `109` status `ready` deltaP `3.0421` edge `0.0207` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.3617` n `106` status `ready` deltaP `3.7448` edge `0.002` maxDD `-1.2006`
- `market_context_high->index_1h` score `-0.5703` n `109` status `ready` deltaP `-0.5892` edge `0.0063` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1192` n `109` status `ready` deltaP `-3.5873` edge `-0.0044` maxDD `-0.8626`
- `market_context_high->crypto_alt_4h` score `-2.0114` n `106` status `ready` deltaP `10.6535` edge `0.0818` maxDD `-28.8561`
- `market_context_high->crypto_alt_1h` score `-2.158` n `109` status `ready` deltaP `4.09` edge `-0.0189` maxDD `-12.7225`
- `market_context_high->metal_1h` score `-2.2512` n `109` status `ready` deltaP `-0.7046` edge `-0.0736` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.2715` n `99` status `ready` deltaP `-10.4798` edge `-0.0184` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-2.6121` n `99` status `ready` deltaP `16.3195` edge `0.0672` maxDD `-27.5371`
- `market_context_high->crypto_major_1h` score `-3.4605` n `109` status `ready` deltaP `2.0477` edge `-0.0445` maxDD `-17.9354`
- `market_context_high->index_24h` score `-4.092` n `99` status `ready` deltaP `-3.8194` edge `-0.1083` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-4.4601` n `106` status `ready` deltaP `7.3085` edge `-0.0214` maxDD `-43.9306`
- `market_context_high->metal_4h` score `-6.0839` n `106` status `ready` deltaP `6.8598` edge `-0.2373` maxDD `-43.7401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
