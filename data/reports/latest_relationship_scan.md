# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T22:52:28.998295+00:00`
- Price records: `672`
- Market context records: `7820`
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

- `market_context_high->equity_24h` score `9.0162` n `132` status `ready` deltaP `28.5507` edge `0.6952` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.465` n `133` status `ready` deltaP `13.8844` edge `0.2386` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.2864` n `133` status `ready` deltaP `5.0275` edge `0.3227` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.184` n `133` status `ready` deltaP `14.6513` edge `0.1728` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1233` n `133` status `ready` deltaP `13.607` edge `0.047` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.835` n `133` status `ready` deltaP `8.5045` edge `0.1246` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8265` n `132` status `ready` deltaP `25.2187` edge `0.0466` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7142` n `133` status `ready` deltaP `7.7457` edge `0.0938` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4894` n `133` status `ready` deltaP `8.9156` edge `0.0407` maxDD `-1.0817`
- `market_context_high->commodity_24h` score `0.3929` n `132` status `ready` deltaP `16.0791` edge `0.0839` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2611` n `133` status `ready` deltaP `5.0268` edge `0.0315` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0389` n `133` status `ready` deltaP `5.4969` edge `0.0125` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0903` n `133` status `ready` deltaP `12.5463` edge `0.0506` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3714` n `133` status `ready` deltaP `1.1245` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9022` n `133` status `ready` deltaP `0.8183` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3143` n `133` status `ready` deltaP `-1.1036` edge `0.0017` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4285` n `133` status `ready` deltaP `1.443` edge `0.0768` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.4675` n `132` status `ready` deltaP `-8.0962` edge `0.0761` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.1921` n `133` status `ready` deltaP `14.7431` edge `0.1502` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
