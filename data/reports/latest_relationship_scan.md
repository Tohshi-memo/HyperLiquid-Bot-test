# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T21:37:24.233429+00:00`
- Price records: `672`
- Market context records: `7814`
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

- `market_context_high->equity_24h` score `8.7066` n `132` status `ready` deltaP `28.5507` edge `0.6694` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4361` n `133` status `ready` deltaP `13.5378` edge `0.2385` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.21` n `133` status `ready` deltaP `4.263` edge `0.318` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1441` n `133` status `ready` deltaP `14.3464` edge `0.1715` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1269` n `133` status `ready` deltaP `13.607` edge `0.0473` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.821` n `132` status `ready` deltaP `25.2187` edge `0.0459` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7636` n `133` status `ready` deltaP `8.0471` edge `0.1217` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7154` n `133` status `ready` deltaP `7.7457` edge `0.0939` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5549` n `133` status `ready` deltaP `9.3743` edge `0.0431` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3386` n `133` status `ready` deltaP `8.194` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2635` n `133` status `ready` deltaP `5.0268` edge `0.0317` maxDD `-1.4603`
- `market_context_high->commodity_24h` score `0.2598` n `132` status `ready` deltaP `15.2095` edge `0.0786` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.0031` n `133` status `ready` deltaP `5.0464` edge `0.012` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1363` n `133` status `ready` deltaP `11.7818` edge `0.0498` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3222` n `133` status `ready` deltaP `1.7251` edge `0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8782` n `133` status `ready` deltaP `1.1177` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3389` n `133` status `ready` deltaP `-1.5624` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5027` n `133` status `ready` deltaP `0.6808` edge `0.0757` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.5455` n `132` status `ready` deltaP `-8.9658` edge `0.0719` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2467` n `133` status `ready` deltaP `14.7431` edge `0.1432` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
