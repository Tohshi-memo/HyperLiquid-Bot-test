# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T02:52:24.534873+00:00`
- Price records: `672`
- Market context records: `7837`
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

- `market_context_high->equity_24h` score `9.9426` n `132` status `ready` deltaP `28.5507` edge `0.7724` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3804` n `133` status `ready` deltaP `6.2507` edge `0.3266` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.2072` n `133` status `ready` deltaP `11.1114` edge `0.2356` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1355` n `133` status `ready` deltaP `14.194` edge `0.1718` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1041` n `133` status `ready` deltaP `13.4573` edge `0.0464` maxDD `-1.5286`
- `market_context_high->commodity_24h` score `0.834` n `132` status `ready` deltaP `18.8617` edge `0.1021` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8288` n `132` status `ready` deltaP `25.2187` edge `0.0469` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7634` n `133` status `ready` deltaP `8.1961` edge `0.0949` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7576` n `133` status `ready` deltaP `8.0471` edge `0.1212` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4565` n `133` status `ready` deltaP `8.6098` edge `0.04` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3638` n `133` status `ready` deltaP `8.4943` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2791` n `133` status `ready` deltaP `5.1765` edge `0.032` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0822` n `133` status `ready` deltaP `5.9473` edge `0.0131` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0651` n `133` status `ready` deltaP `12.8521` edge `0.0518` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8375` n `133` status `ready` deltaP `1.5668` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2401` n `132` status `ready` deltaP `-5.3136` edge `0.0867` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.4115` n `133` status `ready` deltaP `1.5954` edge `0.0772` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4326` n `133` status `ready` deltaP `-3.2443` edge `0.0008` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-2.0548` n `133` status `ready` deltaP `14.7431` edge `0.1678` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
