# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T07:52:24.115300+00:00`
- Price records: `672`
- Market context records: `7858`
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

- `market_context_high->equity_24h` score `10.9791` n `131` status `ready` deltaP `28.7713` edge `0.8573` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.3843` n `131` status `ready` deltaP `22.2011` edge `0.1257` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.2592` n `132` status `ready` deltaP `4.2257` edge `0.3197` maxDD `-6.915`
- `market_context_high->crypto_major_4h` score `1.0949` n `132` status `ready` deltaP `13.9274` edge `0.1702` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0386` n `132` status `ready` deltaP `12.7291` edge `0.0458` maxDD `-1.5286`
- `market_context_high->metal_24h` score `1.025` n `132` status `ready` deltaP `8.672` edge `0.2325` maxDD `-2.3918`
- `market_context_high->fx_24h` score `0.8583` n `131` status `ready` deltaP `25.5599` edge `0.0484` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6723` n `132` status `ready` deltaP `7.2822` edge `0.0934` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6681` n `132` status `ready` deltaP `7.7235` edge `0.1159` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.588` n `132` status `ready` deltaP `9.7582` edge `0.0433` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.4116` n `132` status `ready` deltaP `9.0773` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2211` n `132` status `ready` deltaP `4.5273` edge `0.0315` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1119` n `132` status `ready` deltaP `6.2585` edge `0.0135` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1423` n `132` status `ready` deltaP `11.5027` edge `0.0509` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.2717` n `132` status `ready` deltaP `0.5869` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8194` n `132` status `ready` deltaP `1.7782` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1649` n `131` status `ready` deltaP `-4.6824` edge `0.0918` maxDD `-2.1282`
- `market_context_high->metal_4h` score `-1.232` n `132` status `ready` deltaP `3.6585` edge `0.0784` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4148` n `132` status `ready` deltaP `-2.9469` edge `0.0011` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.5998` n `132` status `ready` deltaP `16.1743` edge `0.2166` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
