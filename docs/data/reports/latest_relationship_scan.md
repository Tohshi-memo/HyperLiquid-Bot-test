# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T11:07:30.259885+00:00`
- Price records: `672`
- Market context records: `7769`
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

- `market_context_high->equity_24h` score `6.4461` n `132` status `ready` deltaP `25.4936` edge `0.5014` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.1511` n `133` status `ready` deltaP `11.5354` edge `0.2281` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.941` n `133` status `ready` deltaP `12.7088` edge `0.0378` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5879` n `132` status `ready` deltaP `21.8747` edge `0.0383` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4766` n `133` status `ready` deltaP `7.8958` edge `0.073` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4323` n `133` status `ready` deltaP `12.3647` edge `0.1254` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3501` n `133` status `ready` deltaP `1.5107` edge `0.2261` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3386` n `133` status `ready` deltaP `8.4943` edge `0.0146` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2052` n `133` status `ready` deltaP `6.8276` edge `0.0833` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.1223` n `133` status `ready` deltaP `5.8575` edge `0.0305` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1196` n `133` status `ready` deltaP `4.2783` edge `0.0247` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0571` n `133` status `ready` deltaP `4.7461` edge `0.0095` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2924` n `133` status `ready` deltaP `10.0998` edge `0.041` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4122` n `133` status `ready` deltaP `0.674` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9214` n `133` status `ready` deltaP `0.8183` edge `0.0181` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.1153` n `132` status `ready` deltaP `7.9506` edge `0.0124` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4666` n `133` status `ready` deltaP `-3.703` edge `-0.0005` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6878` n `133` status `ready` deltaP `-0.5387` edge `0.0684` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.9929` n `132` status `ready` deltaP `-13.4014` edge `0.0441` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3123` n `133` status `ready` deltaP `-1.8729` edge `-0.1212` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
