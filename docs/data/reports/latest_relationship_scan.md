# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T12:07:26.932906+00:00`
- Price records: `672`
- Market context records: `7773`
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

- `market_context_high->equity_24h` score `6.6482` n `132` status `ready` deltaP `26.1904` edge `0.5136` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.2475` n `133` status `ready` deltaP `12.2298` edge `0.2315` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9638` n `133` status `ready` deltaP `12.8585` edge `0.0387` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.6335` n `132` status `ready` deltaP `22.5716` edge `0.0395` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4622` n `133` status `ready` deltaP `7.8958` edge `0.0718` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4575` n `133` status `ready` deltaP `12.3647` edge `0.1275` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3728` n `133` status `ready` deltaP `1.6636` edge `0.228` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3242` n `133` status `ready` deltaP `8.3441` edge `0.0144` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2388` n `133` status `ready` deltaP `6.8276` edge `0.0861` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.1929` n `133` status `ready` deltaP `6.4691` edge `0.0323` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1232` n `133` status `ready` deltaP `4.2783` edge `0.025` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0439` n `133` status `ready` deltaP `4.8963` edge `0.0096` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.3091` n `133` status `ready` deltaP `9.794` edge `0.0409` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.387` n `133` status `ready` deltaP `0.9743` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.925` n `133` status `ready` deltaP `0.8183` edge `0.0178` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-0.9816` n `132` status `ready` deltaP `8.6475` edge `0.0189` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.438` n `133` status `ready` deltaP `-3.2443` edge `0.0001` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.717` n `133` status `ready` deltaP `-0.8436` edge `0.068` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.9302` n `132` status `ready` deltaP `-12.7046` edge `0.0475` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2488` n `133` status `ready` deltaP `-1.2741` edge `-0.1199` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
