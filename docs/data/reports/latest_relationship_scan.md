# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T16:07:29.317716+00:00`
- Price records: `672`
- Market context records: `8638`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.8634` n `60` status `ready` deltaP `34.2345` edge `432.3858` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.9774` n `53` status `ready` deltaP `54.4979` edge `1.0912` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.4082` n `60` status `ready` deltaP `22.9979` edge `0.4404` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.5972` n `60` status `ready` deltaP `22.6931` edge `0.0842` maxDD `-0.191`
- `market_context_high->commodity_24h` score `1.8646` n `53` status `ready` deltaP `29.2371` edge `0.2399` maxDD `-10.6615`
- `news_risk_high->equity_1h` score `1.4321` n `62` status `ready` deltaP `13.2171` edge `0.0846` maxDD `-2.6031`
- `news_risk_high->crypto_major_4h` score `1.2906` n `60` status `ready` deltaP `7.7439` edge `0.1914` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.5877` n `54` status `ready` deltaP `8.9318` edge `0.1115` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.516` n `60` status `ready` deltaP `11.5244` edge `0.1285` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.3416` n `62` status `ready` deltaP `7.0504` edge `0.052` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2778` n `60` status `ready` deltaP `14.1463` edge `0.0246` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `0.2242` n `62` status `ready` deltaP `4.9884` edge `0.0497` maxDD `-2.3368`
- `news_risk_high->metal_1h` score `0.1766` n `62` status `ready` deltaP `6.9828` edge `0.0085` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.1666` n `54` status `ready` deltaP `12.85` edge `0.0153` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0666` n `62` status `ready` deltaP `4.6214` edge `0.0094` maxDD `-0.5338`
- `news_risk_high->fx_1h` score `0.0141` n `62` status `ready` deltaP `3.8246` edge `0.0044` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.0205` n `54` status `ready` deltaP `5.2007` edge `0.0168` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.1` n `54` status `ready` deltaP `6.1544` edge `0.0009` maxDD `-0.6874`
- `market_context_high->fx_24h` score `-0.1802` n `53` status `ready` deltaP `5.3072` edge `0.0387` maxDD `-2.4411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
