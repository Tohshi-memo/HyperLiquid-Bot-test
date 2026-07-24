# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T00:07:24.838038+00:00`
- Price records: `672`
- Market context records: `7722`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.5895` n `132` status `ready` deltaP `19.396` edge `0.304` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0369` n `133` status `ready` deltaP `13.1579` edge `0.0428` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9509` n `133` status `ready` deltaP `14.3464` edge `0.1554` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.6291` n `133` status `ready` deltaP `8.7968` edge `0.0797` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.5912` n `133` status `ready` deltaP `8.352` edge `0.1053` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.5023` n `133` status `ready` deltaP `1.6636` edge `0.2446` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3962` n `133` status `ready` deltaP `9.0949` edge `0.0154` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1221` n `133` status `ready` deltaP `3.8292` edge `0.0279` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.1055` n `132` status `ready` deltaP `14.3834` edge `0.0264` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2024` n `133` status `ready` deltaP `3.3948` edge `0.0064` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2116` n `133` status `ready` deltaP `4.0227` edge `0.0149` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2584` n `133` status `ready` deltaP `10.5585` edge `0.0423` maxDD `-1.3325`
- `market_context_high->metal_24h` score `-0.3012` n `133` status `ready` deltaP `3.8965` edge `0.158` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5167` n `133` status `ready` deltaP `-0.5272` edge `-0.0008` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8159` n `133` status `ready` deltaP `1.8662` edge `0.0199` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5159` n `133` status `ready` deltaP `0.6808` edge `0.0746` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5782` n `133` status `ready` deltaP `-5.385` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7489` n `132` status `ready` deltaP `5.6858` edge `-0.0253` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1541` n `133` status `ready` deltaP `-0.9747` edge `-0.114` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5957` n `132` status `ready` deltaP `-18.4537` edge `0.0005` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
