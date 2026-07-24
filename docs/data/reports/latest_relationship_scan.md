# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T06:07:33.374276+00:00`
- Price records: `672`
- Market context records: `7748`
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

- `market_context_high->equity_24h` score `4.8833` n `132` status `ready` deltaP `22.0093` edge `0.3944` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8847` n `133` status `ready` deltaP `12.2597` edge `0.0361` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.5769` n `133` status `ready` deltaP `8.0631` edge `0.2034` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `0.5191` n `133` status `ready` deltaP `12.6696` edge `0.1306` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.4466` n `133` status `ready` deltaP `7.8958` edge `0.0705` maxDD `-4.2072`
- `market_context_high->fx_24h` score `0.3729` n `132` status `ready` deltaP `18.5646` edge `0.0328` maxDD `-3.0343`
- `market_context_high->equity_4h` score `0.3674` n `133` status `ready` deltaP `1.6636` edge `0.2273` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3506` n `133` status `ready` deltaP `8.6444` edge `0.0146` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2896` n `133` status `ready` deltaP `7.1325` edge `0.0883` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0477` n `133` status `ready` deltaP `3.6795` edge `0.0227` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.194` n `133` status `ready` deltaP `3.5449` edge `0.0061` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2561` n `133` status `ready` deltaP `10.5585` edge `0.0426` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3467` n `133` status `ready` deltaP `2.7994` edge `0.0118` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4639` n `133` status `ready` deltaP `0.0734` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.78` n `133` status `ready` deltaP `2.3153` edge `0.0199` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4321` n `133` status `ready` deltaP `1.443` edge `0.0765` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6625` n `132` status `ready` deltaP `5.6858` edge `-0.0181` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.2548` n `133` status `ready` deltaP `-1.2741` edge `-0.1204` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.3567` n `132` status `ready` deltaP `-16.8858` edge `0.0207` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
