# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T04:52:29.558347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `28.9494` n `136` status `ready` deltaP `-16.5657` edge `2.7683` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.7238` n `169` status `ready` deltaP `10.7662` edge `0.06` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6765` n `180` status `ready` deltaP `9.3114` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5983` n `136` status `ready` deltaP `18.6851` edge `0.0329` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.2201` n `169` status `ready` deltaP `4.2077` edge `0.0042` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.2528` n `180` status `ready` deltaP `2.0925` edge `-0.0012` maxDD `-0.613`
- `market_context_high->commodity_24h` score `-0.3961` n `136` status `ready` deltaP `10.8564` edge `0.1393` maxDD `-14.6631`
- `market_context_high->index_1h` score `-0.8397` n `180` status `ready` deltaP `-6.67` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->index_4h` score `-1.0064` n `169` status `ready` deltaP `-4.3807` edge `-0.0104` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.3357` n `180` status `ready` deltaP `-5.6254` edge `-0.0102` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4786` n `180` status `ready` deltaP `-6.4604` edge `-0.0188` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.2163` n `136` status `ready` deltaP `0.9516` edge `-0.0586` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.5654` n `136` status `ready` deltaP `-12.3703` edge `-0.0369` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.584` n `180` status `ready` deltaP `-8.7026` edge `-0.0388` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.2447` n `169` status `ready` deltaP `-8.3399` edge `-0.0384` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.4106` n `180` status `ready` deltaP `-7.3952` edge `-0.0445` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.1219` n `169` status `ready` deltaP `-13.8652` edge `-0.1251` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.4723` n `169` status `ready` deltaP `-11.0931` edge `-0.1306` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.9367` n `136` status `ready` deltaP `-14.5329` edge `-0.2153` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.1239` n `136` status `ready` deltaP `-11.1159` edge `-0.2064` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
