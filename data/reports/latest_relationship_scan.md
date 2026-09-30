# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T14:07:35.071426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7268`

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

- `market_context_high->unknown_1h` score `308.6955` n `50` status `ready` deltaP `7.8802` edge `25.677` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `288.8637` n `49` status `ready` deltaP `8.2317` edge `24.0171` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.6732` n `135` status `ready` deltaP `26.1227` edge `1.1529` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0369` n `49` status `ready` deltaP `19.3878` edge `0.5275` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.5669` n `135` status `ready` deltaP `24.5602` edge `0.6184` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.018` n `135` status `ready` deltaP `23.4723` edge `0.6604` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.8214` n `49` status `ready` deltaP `15.0262` edge `0.3476` maxDD `-7.6792`
- `news_risk_high->index_24h` score `3.2598` n `135` status `ready` deltaP `30.5787` edge `0.1156` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.169` n `49` status `ready` deltaP `35.5712` edge `0.04` maxDD `-0.0449`
- `market_context_high->crypto_major_1h` score `3.0357` n `50` status `ready` deltaP `15.9461` edge `0.1917` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8083` n `135` status `ready` deltaP `22.2338` edge `0.2132` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.6734` n `50` status `ready` deltaP `13.6048` edge `0.1984` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3807` n `135` status `ready` deltaP `26.7321` edge `0.1803` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4376` n `50` status `ready` deltaP `20.1916` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8012` n `135` status `ready` deltaP `9.2515` edge `0.0674` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.5752` n `135` status `ready` deltaP `7.6048` edge `0.0883` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4131` n `135` status `ready` deltaP `8.0694` edge `0.0094` maxDD `-0.302`
- `market_context_high->equity_1h` score `0.0062` n `50` status `ready` deltaP `1.2515` edge `0.0575` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `-0.0466` n `135` status `ready` deltaP `7.3013` edge `0.2134` maxDD `-15.9436`
- `market_context_high->commodity_1h` score `-0.0633` n `50` status `ready` deltaP `8.2994` edge `-0.0088` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
