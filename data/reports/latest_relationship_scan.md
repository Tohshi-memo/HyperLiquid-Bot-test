# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T02:22:24.361607+00:00`
- Price records: `672`
- Market context records: `7732`
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

- `market_context_high->equity_24h` score `3.8475` n `132` status `ready` deltaP `19.396` edge `0.3255` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.013` n `133` status `ready` deltaP `13.0082` edge `0.0418` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9427` n `133` status `ready` deltaP `14.4989` edge `0.1537` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6697` n `133` status `ready` deltaP `8.8093` edge `0.1088` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.545` n `133` status `ready` deltaP `8.3463` edge `0.0757` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4266` n `133` status `ready` deltaP `1.6636` edge `0.2349` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3938` n `133` status `ready` deltaP `9.0949` edge `0.0152` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.2042` n `132` status `ready` deltaP `15.9514` edge `0.0286` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.0873` n `133` status `ready` deltaP `3.6795` edge `0.026` maxDD `-1.4603`
- `market_context_high->metal_24h` score `-0.0094` n `133` status `ready` deltaP `5.459` edge `0.1719` maxDD `-2.3927`
- `market_context_high->commodity_1h` score `-0.182` n `133` status `ready` deltaP `3.5449` edge `0.0071` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2385` n `133` status `ready` deltaP `3.7168` edge `0.0147` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2662` n `133` status `ready` deltaP `10.5585` edge `0.0413` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4759` n `133` status `ready` deltaP `-0.0767` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7812` n `133` status `ready` deltaP `2.3153` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5255` n `133` status `ready` deltaP `0.6808` edge `0.0738` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5545` n `133` status `ready` deltaP `-5.0792` edge `-0.0026` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7273` n `132` status `ready` deltaP `5.6858` edge `-0.0235` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1409` n `133` status `ready` deltaP `-0.9747` edge `-0.1129` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5606` n `132` status `ready` deltaP `-18.4537` edge `0.005` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
