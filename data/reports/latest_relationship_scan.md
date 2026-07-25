# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T03:07:29.642525+00:00`
- Price records: `672`
- Market context records: `7838`
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

- `market_context_high->equity_24h` score `9.9858` n `132` status `ready` deltaP `28.5507` edge `0.776` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3694` n `133` status `ready` deltaP `6.0978` edge `0.3262` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.1885` n `133` status `ready` deltaP `10.9381` edge `0.2352` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1173` n `133` status `ready` deltaP `14.0415` edge `0.1713` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1041` n `133` status `ready` deltaP `13.4573` edge `0.0464` maxDD `-1.5286`
- `market_context_high->commodity_24h` score `0.8647` n `132` status `ready` deltaP `19.0356` edge `0.1035` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8288` n `132` status `ready` deltaP `25.2187` edge `0.0469` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7598` n `133` status `ready` deltaP `8.1961` edge `0.0946` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7382` n `133` status `ready` deltaP `7.8947` edge `0.1206` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4589` n `133` status `ready` deltaP `8.6098` edge `0.0402` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3638` n `133` status `ready` deltaP `8.4943` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2791` n `133` status `ready` deltaP `5.1765` edge `0.032` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0978` n `133` status `ready` deltaP `6.0975` edge `0.0134` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0658` n `133` status `ready` deltaP `12.8521` edge `0.0517` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8375` n `133` status `ready` deltaP `1.5668` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2385` n `132` status `ready` deltaP `-5.3136` edge `0.0869` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.4115` n `133` status `ready` deltaP `1.5954` edge `0.0772` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4318` n `133` status `ready` deltaP `-3.2443` edge `0.0009` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-2.0447` n `133` status `ready` deltaP `14.7431` edge `0.1691` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
