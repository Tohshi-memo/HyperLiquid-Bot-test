# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T18:52:51.267166+00:00`
- Price records: `672`
- Market context records: `5068`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `12.208` n `100` status `ready` deltaP `4.2036` edge `1.0394` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.1866` n `97` status `ready` deltaP `21.0256` edge `0.7276` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.1968` n `97` status `ready` deltaP `18.4546` edge `0.5153` maxDD `-6.4213`
- `market_context_high->unknown_24h` score `5.8662` n `79` status `ready` deltaP `27.7206` edge `0.3383` maxDD `-1.4072`
- `market_context_high->crypto_major_4h` score `5.549` n `97` status `ready` deltaP `17.0025` edge `0.5075` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.0492` n `100` status `ready` deltaP `7.5389` edge `0.1188` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9654` n `97` status `ready` deltaP `10.4319` edge `0.1188` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8209` n `100` status `ready` deltaP `8.1976` edge `0.0711` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6996` n `97` status `ready` deltaP `6.0112` edge `0.1711` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.5286` n `100` status `ready` deltaP `8.491` edge `0.0371` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.3907` n `100` status `ready` deltaP `6.5449` edge `0.0988` maxDD `-4.7207`
- `market_context_high->index_4h` score `0.0186` n `97` status `ready` deltaP `5.8147` edge `0.0389` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2429` n `100` status `ready` deltaP `2.5988` edge `0.0126` maxDD `-0.552`
- `market_context_high->fx_24h` score `-0.2663` n `79` status `ready` deltaP `5.349` edge `0.0064` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.5705` n `100` status `ready` deltaP `0.6946` edge `0.0138` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8455` n `97` status `ready` deltaP `7.2951` edge `0.0058` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.944` n `97` status `ready` deltaP `-3.2232` edge `-0.0006` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4971` n `100` status `ready` deltaP `-8.9042` edge `-0.0044` maxDD `-0.5464`
- `market_context_high->commodity_24h` score `-3.6628` n `79` status `ready` deltaP `4.5469` edge `-0.0458` maxDD `-24.3277`
- `market_context_high->metal_24h` score `-3.6849` n `79` status `ready` deltaP `2.7097` edge `0.055` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
