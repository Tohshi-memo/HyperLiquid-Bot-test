# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T18:22:28.655688+00:00`
- Price records: `672`
- Market context records: `5066`
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

- `market_context_high->unknown_1h` score `12.7913` n `98` status `ready` deltaP `3.3056` edge `1.094` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.1166` n `97` status `ready` deltaP `20.7207` edge `0.7238` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2052` n `97` status `ready` deltaP `18.4546` edge `0.516` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5562` n `97` status `ready` deltaP `17.0025` edge `0.5081` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `2.4287` n `77` status `ready` deltaP `27.4576` edge `0.0536` maxDD `-1.4072`
- `market_context_high->crypto_major_1h` score `1.1485` n `98` status `ready` deltaP `8.3007` edge `0.122` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9788` n `97` status `ready` deltaP `10.5843` edge `0.1189` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8443` n `98` status `ready` deltaP `8.3405` edge `0.0721` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7035` n `97` status `ready` deltaP `6.0112` edge `0.1716` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.4667` n `98` status `ready` deltaP `7.7019` edge `0.0372` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.4582` n `98` status `ready` deltaP `7.3475` edge `0.1021` maxDD `-4.7207`
- `market_context_high->index_4h` score `0.021` n `97` status `ready` deltaP `5.8147` edge `0.0391` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.2037` n `77` status `ready` deltaP `6.4485` edge `0.0071` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2478` n `98` status `ready` deltaP `2.4899` edge `0.0127` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.5714` n `98` status `ready` deltaP `0.6538` edge `0.014` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8419` n `97` status `ready` deltaP `7.2951` edge `0.0061` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9432` n `97` status `ready` deltaP `-3.2232` edge `-0.0005` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.431` n `98` status `ready` deltaP `-8.1083` edge `-0.0042` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.7042` n `77` status `ready` deltaP `3.4474` edge `0.0476` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-3.7917` n `77` status `ready` deltaP `3.4474` edge `-0.055` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
