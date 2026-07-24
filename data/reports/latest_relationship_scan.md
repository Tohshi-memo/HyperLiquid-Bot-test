# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T13:37:28.998569+00:00`
- Price records: `672`
- Market context records: `7779`
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

- `market_context_high->equity_24h` score `6.9214` n `132` status `ready` deltaP `27.2357` edge `0.5294` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3836` n `133` status `ready` deltaP `13.2715` edge `0.2359` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9338` n `133` status `ready` deltaP `12.7088` edge `0.0372` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.7034` n `132` status `ready` deltaP `23.6169` edge `0.0415` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.5793` n `133` status `ready` deltaP `12.822` edge `0.1346` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.4872` n `133` status `ready` deltaP `2.1223` edge `0.2396` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.387` n `133` status `ready` deltaP `7.2849` edge `0.0954` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.3866` n `133` status `ready` deltaP `7.4454` edge `0.0685` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.2834` n `133` status `ready` deltaP `7.8937` edge `0.014` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2099` n `133` status `ready` deltaP `6.622` edge `0.0327` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1064` n `133` status `ready` deltaP `4.1286` edge `0.0246` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0523` n `133` status `ready` deltaP `4.7461` edge `0.0099` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2728` n `133` status `ready` deltaP `10.2527` edge `0.0425` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.363` n `133` status `ready` deltaP `1.2746` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.7864` n `132` status `ready` deltaP `9.6928` edge `0.0282` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9621` n `133` status `ready` deltaP `0.3692` edge `0.0177` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3825` n `133` status `ready` deltaP `-2.3269` edge `0.0011` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6528` n `133` status `ready` deltaP `-0.3863` edge `0.0703` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.8431` n `132` status `ready` deltaP `-11.6593` edge `0.0517` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.1709` n `133` status `ready` deltaP `-0.5256` edge `-0.1184` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
