# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T22:22:27.401543+00:00`
- Price records: `672`
- Market context records: `7713`
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

- `market_context_high->equity_24h` score `3.6027` n `132` status `ready` deltaP `19.396` edge `0.3051` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.1426` n `133` status `ready` deltaP `15.1086` edge `0.1663` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1389` n `133` status `ready` deltaP `13.607` edge `0.0483` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.7271` n `133` status `ready` deltaP `8.6569` edge `0.1146` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.699` n `133` status `ready` deltaP `2.581` edge `0.2637` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6963` n `133` status `ready` deltaP `9.0971` edge `0.0833` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4371` n `133` status `ready` deltaP `9.5453` edge `0.0158` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1977` n `133` status `ready` deltaP `3.9789` edge `0.0332` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.0304` n `132` status `ready` deltaP `13.1639` edge `0.0249` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.18` n `133` status `ready` deltaP `4.3285` edge `0.0155` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.1858` n `133` status `ready` deltaP `11.4759` edge `0.0455` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.1916` n `133` status `ready` deltaP `3.5449` edge `0.0063` maxDD `-0.6722`
- `market_context_high->metal_24h` score `-0.4599` n `133` status `ready` deltaP `3.202` edge `0.1494` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5311` n `133` status `ready` deltaP `-0.6773` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8519` n `133` status `ready` deltaP `1.4171` edge `0.0199` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4259` n `133` status `ready` deltaP `1.5954` edge `0.076` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5703` n `133` status `ready` deltaP `-5.2321` edge `-0.0036` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7549` n `132` status `ready` deltaP `5.6858` edge `-0.0258` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1181` n `133` status `ready` deltaP `-0.6753` edge `-0.113` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5911` n `132` status `ready` deltaP `-18.4537` edge `0.0011` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
