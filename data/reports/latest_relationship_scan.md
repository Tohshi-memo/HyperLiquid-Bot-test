# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T10:52:29.791186+00:00`
- Price records: `672`
- Market context records: `7768`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `6.3829` n `132` status `ready` deltaP `25.3194` edge `0.4973` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.1276` n `133` status `ready` deltaP `11.3617` edge `0.2273` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9398` n `133` status `ready` deltaP `12.7088` edge `0.0377` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5765` n `132` status `ready` deltaP `21.7005` edge `0.038` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4574` n `133` status `ready` deltaP `7.7457` edge `0.0724` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4251` n `133` status `ready` deltaP `12.3647` edge `0.1248` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3454` n `133` status `ready` deltaP `1.5107` edge `0.2255` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3374` n `133` status `ready` deltaP `8.4943` edge `0.0145` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.1968` n `133` status `ready` deltaP `6.8276` edge `0.0826` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.1184` n `133` status `ready` deltaP `4.2783` edge `0.0246` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.1005` n `133` status `ready` deltaP `5.7046` edge `0.0297` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0571` n `133` status `ready` deltaP `4.7461` edge `0.0095` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2924` n `133` status `ready` deltaP `10.0998` edge `0.041` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4122` n `133` status `ready` deltaP `0.674` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.907` n `133` status `ready` deltaP `0.968` edge `0.0183` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.1485` n `132` status `ready` deltaP `7.7764` edge `0.0108` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4753` n `133` status `ready` deltaP `-3.8559` edge `-0.0006` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6708` n `133` status `ready` deltaP `-0.3863` edge `0.0688` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.0106` n `132` status `ready` deltaP `-13.5757` edge `0.043` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3123` n `133` status `ready` deltaP `-1.8729` edge `-0.1212` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
