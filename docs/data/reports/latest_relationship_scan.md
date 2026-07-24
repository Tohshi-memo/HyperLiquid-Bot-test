# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T06:22:24.036252+00:00`
- Price records: `672`
- Market context records: `7749`
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

- `market_context_high->equity_24h` score `4.9621` n `132` status `ready` deltaP `22.1835` edge `0.3998` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8607` n `133` status `ready` deltaP `12.11` edge `0.0351` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.616` n `133` status `ready` deltaP `8.2367` edge `0.2055` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `0.4937` n `133` status `ready` deltaP `12.5172` edge `0.1295` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.4634` n `133` status `ready` deltaP `8.046` edge `0.0709` maxDD `-4.2072`
- `market_context_high->fx_24h` score `0.3843` n `132` status `ready` deltaP `18.7388` edge `0.0331` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.365` n `133` status `ready` deltaP `8.7946` edge `0.0148` maxDD `-0.7743`
- `market_context_high->equity_4h` score `0.3642` n `133` status `ready` deltaP `1.6636` edge `0.2269` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.2606` n `133` status `ready` deltaP `6.9801` edge `0.0869` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0249` n `133` status `ready` deltaP `3.5298` edge `0.0218` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1952` n `133` status `ready` deltaP `3.5449` edge `0.006` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2561` n `133` status `ready` deltaP `10.5585` edge `0.0426` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3297` n `133` status `ready` deltaP `2.9523` edge `0.0122` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4651` n `133` status `ready` deltaP `0.0734` edge `-0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7764` n `133` status `ready` deltaP `2.3153` edge `0.0202` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4163` n `133` status `ready` deltaP `1.5954` edge `0.0768` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4761` n `133` status `ready` deltaP `-3.8559` edge `-0.0007` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6541` n `132` status `ready` deltaP `5.6858` edge `-0.0174` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.2548` n `133` status `ready` deltaP `-1.2741` edge `-0.1204` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.3375` n `132` status `ready` deltaP `-16.7116` edge `0.022` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
