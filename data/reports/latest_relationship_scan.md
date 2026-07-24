# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T05:22:30.484154+00:00`
- Price records: `672`
- Market context records: `7745`
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

- `market_context_high->equity_24h` score `4.6519` n `132` status `ready` deltaP `21.4866` edge `0.3786` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.9614` n `133` status `ready` deltaP `12.7088` edge `0.0395` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.6073` n `133` status `ready` deltaP `13.1269` edge `0.1349` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.5018` n `133` status `ready` deltaP `8.1961` edge `0.0731` maxDD `-4.2072`
- `market_context_high->metal_24h` score `0.4561` n `133` status `ready` deltaP `7.5423` edge `0.1968` maxDD `-2.3927`
- `market_context_high->equity_4h` score `0.3869` n `133` status `ready` deltaP `1.6636` edge `0.2298` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.3814` n `133` status `ready` deltaP `7.5898` edge `0.0929` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.365` n `133` status `ready` deltaP `8.7946` edge `0.0148` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.3394` n `132` status `ready` deltaP `18.0419` edge `0.032` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.0933` n `133` status `ready` deltaP `3.8292` edge `0.0255` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1892` n `133` status `ready` deltaP `3.5449` edge `0.0065` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2569` n `133` status `ready` deltaP `10.5585` edge `0.0425` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3443` n `133` status `ready` deltaP `2.7994` edge `0.012` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4759` n `133` status `ready` deltaP `-0.0767` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7932` n `133` status `ready` deltaP `2.1656` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4515` n `133` status `ready` deltaP `1.2905` edge `0.0759` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4864` n `133` status `ready` deltaP `-4.0088` edge `-0.001` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6769` n `132` status `ready` deltaP `5.6858` edge `-0.0193` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.25` n `133` status `ready` deltaP `-1.2741` edge `-0.12` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.4143` n `132` status `ready` deltaP `-17.4084` edge `0.0168` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
