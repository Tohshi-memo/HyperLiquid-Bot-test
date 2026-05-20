# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T05:22:16.672548+00:00`
- Price records: `672`
- Market context records: `1290`
- Flow alert records: `5625`
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

- `market_context_high->crypto_major_24h` score `17.4985` n `128` status `ready` deltaP `41.5798` edge `1.2942` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.978` n `128` status `ready` deltaP `9.0278` edge `1.1047` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.271` n `128` status `ready` deltaP `26.8229` edge `0.7954` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.7269` n `128` status `ready` deltaP `29.8611` edge `0.3868` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9561` n `128` status `ready` deltaP `25.3472` edge `0.5709` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.3634` n `128` status `ready` deltaP `1.5625` edge `0.4595` maxDD `-10.1706`
- `market_context_high->equity_4h` score `2.347` n `148` status `ready` deltaP `12.0262` edge `0.1859` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `1.1593` n `128` status `ready` deltaP `-14.5833` edge `0.342` maxDD `-6.8535`
- `market_context_high->unknown_4h` score `0.9632` n `148` status `ready` deltaP `2.8923` edge `0.2881` maxDD `-11.1695`
- `market_context_high->fx_24h` score `0.4273` n `128` status `ready` deltaP `6.6841` edge `0.0375` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.1756` n `157` status `ready` deltaP `3.5174` edge `0.0339` maxDD `-1.7505`
- `market_context_high->index_4h` score `0.1237` n `148` status `ready` deltaP `5.7679` edge `0.0863` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.1053` n `157` status `ready` deltaP `6.2121` edge `0.0175` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0867` n `157` status `ready` deltaP `10.1396` edge `0.0086` maxDD `-2.8509`
- `market_context_high->metal_4h` score `-0.0209` n `148` status `ready` deltaP `12.5783` edge `0.0575` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.5373` n `157` status `ready` deltaP `0.6589` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5629` n `157` status `ready` deltaP `0.9964` edge `0.0335` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-0.7917` n `157` status `ready` deltaP `-0.0191` edge `0.0007` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8384` n `148` status `ready` deltaP `9.3112` edge `0.1624` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9361` n `148` status `ready` deltaP `5.051` edge `0.1172` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
