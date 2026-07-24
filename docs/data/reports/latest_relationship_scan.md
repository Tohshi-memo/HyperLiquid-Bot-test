# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T23:07:28.686908+00:00`
- Price records: `672`
- Market context records: `7821`
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

- `market_context_high->equity_24h` score `9.081` n `132` status `ready` deltaP `28.5507` edge `0.7006` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4512` n `133` status `ready` deltaP `13.7111` edge `0.2386` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.288` n `133` status `ready` deltaP `5.0275` edge `0.3229` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.184` n `133` status `ready` deltaP `14.6513` edge `0.1728` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1065` n `133` status `ready` deltaP `13.4573` edge `0.0466` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8495` n `133` status `ready` deltaP `8.6569` edge `0.1248` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8273` n `132` status `ready` deltaP `25.2187` edge `0.0467` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7286` n `133` status `ready` deltaP `7.8958` edge `0.094` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4736` n `133` status `ready` deltaP `8.7627` edge `0.0404` maxDD `-1.0817`
- `market_context_high->commodity_24h` score `0.4189` n `132` status `ready` deltaP `16.253` edge `0.0849` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.3386` n `133` status `ready` deltaP `8.194` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2611` n `133` status `ready` deltaP `5.0268` edge `0.0315` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0521` n `133` status `ready` deltaP `5.647` edge `0.0126` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0824` n `133` status `ready` deltaP `12.6992` edge `0.0506` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3846` n `133` status `ready` deltaP `0.9743` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9022` n `133` status `ready` deltaP `0.8183` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.323` n `133` status `ready` deltaP `-1.2565` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4273` n `133` status `ready` deltaP `1.443` edge `0.0769` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.4514` n `132` status `ready` deltaP `-7.9223` edge `0.077` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.1804` n `133` status `ready` deltaP `14.7431` edge `0.1517` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
