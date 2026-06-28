# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T19:22:28.186333+00:00`
- Price records: `672`
- Market context records: `5071`
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

- `market_context_high->unknown_1h` score `11.6062` n `102` status `ready` deltaP `5.0663` edge `0.9835` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.2494` n `97` status `ready` deltaP `21.3305` edge `0.7308` maxDD `-5.5109`
- `market_context_high->unknown_24h` score `9.0818` n `81` status `ready` deltaP `27.9707` edge `0.6046` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `6.1812` n `97` status `ready` deltaP `18.4546` edge `0.514` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5418` n `97` status `ready` deltaP `17.0025` edge `0.5069` maxDD `-8.3416`
- `market_context_high->metal_4h` score `0.9666` n `97` status `ready` deltaP `10.4319` edge `0.1189` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8351` n `102` status `ready` deltaP `6.669` edge `0.113` maxDD `-4.3625`
- `market_context_high->equity_1h` score `0.7027` n `102` status `ready` deltaP `7.08` edge `0.0687` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6918` n `97` status `ready` deltaP `6.0112` edge `0.1701` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.5708` n `102` status `ready` deltaP `9.0936` edge `0.0366` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2998` n `102` status `ready` deltaP `5.4861` edge `0.0942` maxDD `-4.7207`
- `market_context_high->index_4h` score `0.0162` n `97` status `ready` deltaP `5.8147` edge `0.0387` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2835` n `102` status `ready` deltaP `1.8786` edge `0.0122` maxDD `-0.552`
- `market_context_high->fx_24h` score `-0.3252` n `81` status `ready` deltaP `4.321` edge `0.0057` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.5117` n `102` status `ready` deltaP `1.4148` edge `0.0139` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8625` n `97` status `ready` deltaP `7.1426` edge `0.0054` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.944` n `97` status `ready` deltaP `-3.2232` edge `-0.0006` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.5664` n `102` status `ready` deltaP `-9.6689` edge `-0.0047` maxDD `-0.5766`
- `market_context_high->commodity_24h` score `-3.536` n `81` status `ready` deltaP `5.5748` edge `-0.0364` maxDD `-24.3277`
- `market_context_high->metal_24h` score `-3.6643` n `81` status `ready` deltaP `2.0254` edge `0.0622` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
