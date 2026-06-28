# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T15:52:32.938486+00:00`
- Price records: `672`
- Market context records: `5055`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `12.0892` n `100` status `ready` deltaP `3.9042` edge `1.0315` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9055` n `99` status `ready` deltaP `21.5463` edge `0.7007` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.5266` n `99` status `ready` deltaP `16.5897` edge `0.4883` maxDD `-7.7348`
- `market_context_high->crypto_major_4h` score `5.2529` n `99` status `ready` deltaP `16.4373` edge `0.4866` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `0.8819` n `100` status `ready` deltaP `7.491` edge `0.1123` maxDD `-4.4335`
- `market_context_high->metal_4h` score `0.8485` n `99` status `ready` deltaP `9.4805` edge `0.1154` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.5001` n `100` status `ready` deltaP `7.7485` edge `0.0698` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.4763` n `99` status `ready` deltaP `4.507` edge `0.165` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3818` n `100` status `ready` deltaP `6.7904` edge `0.0362` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2154` n `100` status `ready` deltaP `5.6467` edge `0.0905` maxDD `-5.3758`
- `market_context_high->fx_24h` score `-0.0717` n `76` status `ready` deltaP `8.7902` edge `0.0084` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0963` n `99` status `ready` deltaP `4.4685` edge `0.0383` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3469` n `100` status `ready` deltaP `1.0958` edge `0.0142` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4774` n `100` status `ready` deltaP `0.1497` edge `0.0119` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.5304` n `99` status `ready` deltaP `7.4787` edge `0.0074` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0018` n `99` status `ready` deltaP `-4.0497` edge `-0.0025` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4791` n `100` status `ready` deltaP `-8.6048` edge `-0.0049` maxDD `-0.5464`
- `market_context_high->unknown_24h` score `-3.275` n `76` status `ready` deltaP `27.3209` edge `-0.4208` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.5404` n `76` status `ready` deltaP `6.2226` edge `0.0501` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.5217` n `76` status `ready` deltaP `0.4843` edge `-0.0863` maxDD `-26.7306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
