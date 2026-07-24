# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T00:52:28.723182+00:00`
- Price records: `672`
- Market context records: `7725`
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

- `market_context_high->equity_24h` score `3.6675` n `132` status `ready` deltaP `19.396` edge `0.3105` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0825` n `133` status `ready` deltaP `13.4573` edge `0.0446` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.004` n `133` status `ready` deltaP `14.6513` edge `0.1578` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6659` n `133` status `ready` deltaP `8.6569` edge `0.1095` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6267` n `133` status `ready` deltaP `8.7968` edge `0.0795` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4906` n `133` status `ready` deltaP `1.6636` edge `0.2431` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3974` n `133` status `ready` deltaP `9.0949` edge `0.0155` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.164` n `133` status `ready` deltaP `4.1286` edge `0.0294` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.1374` n `132` status `ready` deltaP `14.9061` edge `0.027` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2036` n `133` status `ready` deltaP `3.3948` edge `0.0063` maxDD `-0.6722`
- `market_context_high->metal_24h` score `-0.2103` n `133` status `ready` deltaP `4.4173` edge `0.1621` maxDD `-2.3927`
- `market_context_high->commodity_4h` score `-0.2421` n `133` status `ready` deltaP `3.7168` edge `0.0144` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2592` n `133` status `ready` deltaP `10.5585` edge `0.0422` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4915` n `133` status `ready` deltaP `-0.2269` edge `-0.0007` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8171` n `133` status `ready` deltaP `1.8662` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5159` n `133` status `ready` deltaP `0.6808` edge `0.0746` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5767` n `133` status `ready` deltaP `-5.385` edge `-0.0034` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7441` n `132` status `ready` deltaP `5.6858` edge `-0.0249` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1745` n `133` status `ready` deltaP `-1.1244` edge `-0.1147` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5872` n `132` status `ready` deltaP `-18.4537` edge `0.0016` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
