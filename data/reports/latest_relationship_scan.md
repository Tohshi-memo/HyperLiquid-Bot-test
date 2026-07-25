# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T06:22:28.134022+00:00`
- Price records: `672`
- Market context records: `7851`
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

- `market_context_high->equity_24h` score `10.5738` n `132` status `ready` deltaP `28.5507` edge `0.825` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.2471` n `132` status `ready` deltaP `21.2965` edge `0.1203` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.2075` n `133` status `ready` deltaP `4.11` edge `0.3187` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.037` n `133` status `ready` deltaP `12.7088` edge `0.0458` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0167` n `133` status `ready` deltaP `13.2794` edge `0.168` maxDD `-6.7444`
- `market_context_high->metal_24h` score `0.9567` n `133` status `ready` deltaP `8.6851` edge `0.2309` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.8366` n `132` status `ready` deltaP `25.2187` edge `0.0479` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7118` n `133` status `ready` deltaP `7.7457` edge `0.0936` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6102` n `133` status `ready` deltaP `7.2849` edge `0.114` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5794` n `133` status `ready` deltaP `9.6802` edge `0.0431` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.401` n `133` status `ready` deltaP `8.9447` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1868` n `133` status `ready` deltaP `4.2783` edge `0.0303` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0834` n `133` status `ready` deltaP `5.9473` edge `0.0132` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1198` n `133` status `ready` deltaP `11.9347` edge `0.0509` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3486` n `133` status `ready` deltaP `1.4248` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7513` n `133` status `ready` deltaP `2.6147` edge `0.0203` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1986` n `132` status `ready` deltaP `-4.9658` edge `0.0897` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.2458` n `133` status `ready` deltaP `3.5771` edge `0.0778` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.3723` n `133` status `ready` deltaP `-2.174` edge `0.0014` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.7996` n `133` status `ready` deltaP `15.4364` edge `0.1959` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
