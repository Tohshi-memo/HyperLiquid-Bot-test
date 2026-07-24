# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T03:07:29.832955+00:00`
- Price records: `672`
- Market context records: `7735`
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

- `market_context_high->equity_24h` score `4.0201` n `132` status `ready` deltaP `19.9187` edge `0.3364` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0142` n `133` status `ready` deltaP `13.0082` edge `0.0419` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9067` n `133` status `ready` deltaP `14.4989` edge `0.1507` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6323` n `133` status `ready` deltaP `8.6569` edge `0.1067` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5426` n `133` status `ready` deltaP `8.3463` edge `0.0755` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4071` n `133` status `ready` deltaP `1.6636` edge `0.2324` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3998` n `133` status `ready` deltaP `9.0949` edge `0.0157` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.2384` n `132` status `ready` deltaP `16.474` edge `0.0295` maxDD `-3.0343`
- `market_context_high->metal_24h` score `0.1055` n `133` status `ready` deltaP `5.9798` edge `0.178` maxDD `-2.3927`
- `market_context_high->crypto_alt_1h` score `0.0933` n `133` status `ready` deltaP `3.8292` edge `0.0255` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.2277` n `133` status `ready` deltaP `3.0945` edge `0.0063` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2627` n `133` status `ready` deltaP `3.5639` edge `0.0137` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2639` n `133` status `ready` deltaP `10.5585` edge `0.0416` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4507` n `133` status `ready` deltaP `0.2236` edge `-0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7668` n `133` status `ready` deltaP `2.465` edge `0.02` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5195` n `133` status `ready` deltaP `0.6808` edge `0.0743` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5427` n `133` status `ready` deltaP `-4.9263` edge `-0.0021` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7177` n `132` status `ready` deltaP `5.6858` edge `-0.0227` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1097` n `133` status `ready` deltaP `-0.825` edge `-0.1113` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5411` n `132` status `ready` deltaP `-18.4537` edge `0.0075` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
