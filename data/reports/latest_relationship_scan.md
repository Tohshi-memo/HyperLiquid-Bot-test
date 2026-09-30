# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T13:22:32.212542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_4h` score `318.6897` n `46` status `ready` deltaP `8.2317` edge `26.5026` maxDD `0.0`
- `market_context_high->unknown_1h` score `311.1231` n `50` status `ready` deltaP `7.8802` edge `25.8793` maxDD `-0.0597`
- `news_risk_high->crypto_alt_24h` score `15.8275` n `135` status `ready` deltaP `26.2963` edge `1.1646` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `6.9894` n `46` status `ready` deltaP `17.8486` edge `0.5338` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.6871` n `135` status `ready` deltaP `24.9074` edge `0.6261` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.1368` n `135` status `ready` deltaP `23.4723` edge `0.6703` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.8949` n `46` status `ready` deltaP `13.6201` edge `0.3631` maxDD `-7.6792`
- `market_context_high->fx_4h` score `3.4202` n `46` status `ready` deltaP `38.3219` edge `0.0426` maxDD `-0.0449`
- `news_risk_high->index_24h` score `3.3254` n `135` status `ready` deltaP `31.0995` edge `0.1176` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.0885` n `50` status `ready` deltaP `15.9461` edge `0.1961` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8692` n `135` status `ready` deltaP `22.7546` edge `0.2148` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.7598` n `50` status `ready` deltaP `13.6048` edge `0.2056` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.4461` n `135` status `ready` deltaP `27.1894` edge `0.1827` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4496` n `50` status `ready` deltaP `20.3413` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7844` n `135` status `ready` deltaP `9.1018` edge `0.067` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.6616` n `135` status `ready` deltaP `7.6048` edge `0.0955` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4286` n `135` status `ready` deltaP `8.2191` edge `0.0097` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.2047` n `135` status `ready` deltaP `7.7586` edge `0.2313` maxDD `-15.9436`
- `market_context_high->equity_1h` score `-0.0047` n `50` status `ready` deltaP `1.1018` edge `0.0571` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0625` n `50` status `ready` deltaP `8.2994` edge `-0.0087` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
