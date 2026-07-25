# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T05:37:25.208993+00:00`
- Price records: `672`
- Market context records: `7848`
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

- `market_context_high->equity_24h` score `10.4286` n `132` status `ready` deltaP `28.5507` edge `0.8129` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.2423` n `133` status `ready` deltaP `4.5688` edge `0.3201` maxDD `-6.9701`
- `market_context_high->commodity_24h` score `1.1634` n `132` status `ready` deltaP `20.7747` edge `0.1168` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.0298` n `133` status `ready` deltaP `12.7088` edge `0.0452` maxDD `-1.5286`
- `market_context_high->metal_24h` score `1.0103` n `133` status `ready` deltaP `9.205` edge `0.2319` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `0.9973` n `133` status `ready` deltaP `13.1269` edge `0.1674` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.8351` n `132` status `ready` deltaP `25.2187` edge `0.0477` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6998` n `133` status `ready` deltaP `7.5955` edge `0.0936` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6162` n `133` status `ready` deltaP `7.2849` edge `0.1145` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5331` n `133` status `ready` deltaP `9.2214` edge `0.0423` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.6444` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1808` n `133` status `ready` deltaP `4.2783` edge `0.0298` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0966` n `133` status `ready` deltaP `6.0975` edge `0.0133` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1182` n `133` status `ready` deltaP `11.9347` edge `0.0511` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3354` n `133` status `ready` deltaP `1.5749` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7884` n `133` status `ready` deltaP `2.1656` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2025` n `132` status `ready` deltaP `-4.9658` edge `0.0892` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.2835` n `133` status `ready` deltaP `3.1198` edge `0.0777` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.381` n `133` status `ready` deltaP `-2.3269` edge `0.0013` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.8898` n `133` status `ready` deltaP `14.9164` edge `0.1878` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
