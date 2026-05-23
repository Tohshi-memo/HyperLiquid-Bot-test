# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T13:52:19.699406+00:00`
- Price records: `672`
- Market context records: `1635`
- Flow alert records: `6618`
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

- `market_context_high->metal_24h` score `10.051` n `180` status `ready` deltaP `27.252` edge `0.8985` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.3609` n `180` status `ready` deltaP `19.3463` edge `0.2889` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `2.486` n `185` status `ready` deltaP `17.7276` edge `0.3554` maxDD `-16.3135`
- `market_context_high->equity_4h` score `1.4231` n `185` status `ready` deltaP `11.5866` edge `0.1508` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.8705` n `180` status `ready` deltaP `17.8173` edge `0.4436` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.7662` n `185` status `ready` deltaP `13.4872` edge `0.2792` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.1422` n `196` status `ready` deltaP `2.1355` edge `0.0699` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.3451` n `180` status `ready` deltaP `23.4036` edge `0.6738` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3679` n `180` status `ready` deltaP `7.1173` edge `0.0268` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.5296` n `196` status `ready` deltaP `0.9777` edge `0.0302` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6435` n `196` status `ready` deltaP `0.5622` edge `0.0058` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8025` n `196` status `ready` deltaP `-0.0825` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.8233` n `196` status `ready` deltaP `-0.9593` edge `0.0338` maxDD `-5.9702`
- `market_context_high->index_4h` score `-0.8653` n `185` status `ready` deltaP `-0.0009` edge `0.0368` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.8969` n `196` status `ready` deltaP `1.7139` edge `0.0018` maxDD `-4.7041`
- `market_context_high->crypto_alt_24h` score `-1.3638` n `180` status `ready` deltaP `23.7243` edge `0.9091` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-1.4071` n `196` status `ready` deltaP `2.0133` edge `0.0029` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5173` n `185` status `ready` deltaP `7.3266` edge `0.0939` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0077` n `185` status `ready` deltaP `-9.153` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.8429` n `185` status `ready` deltaP `8.0818` edge `-0.147` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
