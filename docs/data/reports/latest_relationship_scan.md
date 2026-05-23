# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T14:37:14.624213+00:00`
- Price records: `672`
- Market context records: `1639`
- Flow alert records: `6627`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.8217` n `177` status `ready` deltaP `27.1617` edge `0.88` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.4078` n `177` status `ready` deltaP `19.2277` edge `0.2936` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `2.8648` n `185` status `ready` deltaP `18.8926` edge `0.3792` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4675` n `185` status `ready` deltaP `11.5866` edge `0.1545` maxDD `-5.0894`
- `market_context_high->crypto_major_4h` score `1.4399` n `185` status `ready` deltaP `14.6521` edge `0.2932` maxDD `-13.3376`
- `market_context_high->equity_24h` score `1.0297` n `177` status `ready` deltaP `18.0076` edge `0.4556` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.0894` n `195` status `ready` deltaP `2.6263` edge `0.0734` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.1358` n `177` status `ready` deltaP `23.6505` edge `0.6896` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4076` n `177` status `ready` deltaP `6.8913` edge `0.025` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.4886` n `195` status `ready` deltaP `0.5528` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.5105` n `195` status `ready` deltaP `1.1262` edge `0.0308` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6492` n `195` status `ready` deltaP `0.3555` edge `0.0067` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.6571` n `195` status `ready` deltaP `1.986` edge `-0.0021` maxDD `-5.297`
- `market_context_high->crypto_major_1h` score `-0.7509` n `195` status `ready` deltaP `-0.4921` edge `0.0366` maxDD `-5.7003`
- `market_context_high->index_4h` score `-0.8197` n `185` status `ready` deltaP `-0.0009` edge `0.0406` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `-0.9341` n `177` status `ready` deltaP `24.0559` edge `0.9427` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-1.3937` n `195` status `ready` deltaP `2.1357` edge `0.0032` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5065` n `185` status `ready` deltaP `7.3266` edge `0.0948` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0699` n `185` status `ready` deltaP `-9.9296` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.6726` n `185` status `ready` deltaP `8.4702` edge `-0.1354` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
