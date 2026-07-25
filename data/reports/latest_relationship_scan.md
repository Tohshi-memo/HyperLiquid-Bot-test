# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T05:52:29.935233+00:00`
- Price records: `672`
- Market context records: `7849`
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

- `market_context_high->equity_24h` score `10.479` n `132` status `ready` deltaP `28.5507` edge `0.8171` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.2312` n `133` status `ready` deltaP `4.4159` edge `0.3197` maxDD `-6.9701`
- `market_context_high->commodity_24h` score `1.1917` n `132` status `ready` deltaP `20.9486` edge `0.118` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.0334` n `133` status `ready` deltaP `12.7088` edge `0.0455` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0131` n `133` status `ready` deltaP `13.2794` edge `0.1677` maxDD `-6.7444`
- `market_context_high->metal_24h` score `0.9916` n `133` status `ready` deltaP `9.0317` edge `0.2315` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.8351` n `132` status `ready` deltaP `25.2187` edge `0.0477` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.713` n `133` status `ready` deltaP `7.7457` edge `0.0937` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6174` n `133` status `ready` deltaP `7.2849` edge `0.1146` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5489` n `133` status `ready` deltaP `9.3743` edge `0.0426` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.389` n `133` status `ready` deltaP `8.7946` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1844` n `133` status `ready` deltaP `4.2783` edge `0.0301` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0834` n `133` status `ready` deltaP `5.9473` edge `0.0132` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.119` n `133` status `ready` deltaP `11.9347` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3354` n `133` status `ready` deltaP `1.5749` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7764` n `133` status `ready` deltaP `2.3153` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2002` n `132` status `ready` deltaP `-4.9658` edge `0.0895` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.2713` n `133` status `ready` deltaP `3.2722` edge `0.0777` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.3802` n `133` status `ready` deltaP `-2.3269` edge `0.0014` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.8613` n `133` status `ready` deltaP `15.0897` edge `0.1903` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
