# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T19:37:27.908941+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5625`

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

- `market_context_high->unknown_4h` score `69.925` n `39` status `ready` deltaP `-4.6591` edge `5.9029` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.5555` n `37` status `ready` deltaP `12.6361` edge `0.8082` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3734` n `43` status `ready` deltaP `13.3895` edge `0.2378` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.6782` n `39` status `ready` deltaP `28.6156` edge `0.0414` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.803` n `39` status `ready` deltaP `23.8743` edge `0.0381` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2298` n `43` status `ready` deltaP `12.9299` edge `0.0978` maxDD `-3.1881`
- `market_context_high->index_24h` score `1.1` n `37` status `ready` deltaP `13.6496` edge `0.1131` maxDD `-2.7123`
- `market_context_high->crypto_major_1h` score `1.0078` n `43` status `ready` deltaP `10.6844` edge `0.0713` maxDD `-3.0172`
- `market_context_high->fx_24h` score `0.8186` n `37` status `ready` deltaP `10.9422` edge `0.0041` maxDD `-0.0397`
- `market_context_high->index_1h` score `0.6626` n `43` status `ready` deltaP `6.8619` edge `0.0365` maxDD `-0.1621`
- `market_context_high->metal_1h` score `0.2757` n `43` status `ready` deltaP `6.1134` edge `0.015` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.1481` n `37` status `ready` deltaP `3.0875` edge `0.1179` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.0328` n `43` status `ready` deltaP `2.7503` edge `0.0115` maxDD `-0.1681`
- `market_context_high->commodity_1h` score `0.007` n `43` status `ready` deltaP `7.3214` edge `0.0067` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0884` n `39` status `ready` deltaP `1.4072` edge `0.0247` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6695` n `39` status `ready` deltaP `22.2522` edge `0.0938` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8078` n `39` status `ready` deltaP `-3.514` edge `-0.0351` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-1.0074` n `39` status `ready` deltaP `15.8615` edge `0.0094` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.7965` n `37` status `ready` deltaP `5.7902` edge `-0.133` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.9004` n `39` status `ready` deltaP `1.6416` edge `-0.111` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
