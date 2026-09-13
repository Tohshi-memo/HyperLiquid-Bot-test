# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T03:07:28.853834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12565`

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

- `market_context_high->unknown_24h` score `16601.1753` n `59` status `ready` deltaP `12.2352` edge `1383.3549` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `380.2407` n `82` status `ready` deltaP `-5.1008` edge `31.7629` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.0528` n `82` status `ready` deltaP `32.5796` edge `1.336` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0126` n `82` status `ready` deltaP `39.1515` edge `1.3871` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.6173` n `59` status `ready` deltaP `47.3958` edge `0.5688` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.1543` n `59` status `ready` deltaP `22.5342` edge `0.7787` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.3601` n `82` status `ready` deltaP `16.908` edge `0.5953` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.1753` n `82` status `ready` deltaP `43.0005` edge `0.2456` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.9087` n `82` status `ready` deltaP `27.1765` edge `0.2733` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2378` n `59` status `ready` deltaP `42.1875` edge `0.0719` maxDD `0.0`
- `market_context_high->index_24h` score `4.0539` n `59` status `ready` deltaP `43.6` edge `0.0864` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.2996` n `59` status `ready` deltaP `7.9743` edge `0.105` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.2006` n `82` status `ready` deltaP `8.9939` edge `0.0286` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.1423` n `53` status `ready` deltaP `7.366` edge `0.1366` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1423` n `53` status `ready` deltaP `7.366` edge `0.1366` maxDD `-6.7304`
- `risk_on_high->metal_1h` score `-0.0284` n `60` status `ready` deltaP `4.2116` edge `0.0013` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0284` n `60` status `ready` deltaP `4.2116` edge `0.0013` maxDD `-0.3081`
- `risk_on_high->fx_1h` score `-0.0508` n `60` status `ready` deltaP `2.3952` edge `0.0031` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `-0.0508` n `60` status `ready` deltaP `2.3952` edge `0.0031` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.1383` n `118` status `ready` deltaP `2.3952` edge `-0.0021` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
