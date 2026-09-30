# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T11:52:28.434828+00:00`
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

- `market_context_high->unknown_1h` score `401.8258` n `51` status `ready` deltaP `7.9194` edge `33.4376` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `332.4201` n `41` status `ready` deltaP `8.2317` edge `27.6468` maxDD `0.0`
- `news_risk_high->unknown_24h` score `205.5088` n `135` status `ready` deltaP `1.9097` edge `17.113` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3859` n `135` status `ready` deltaP `26.9907` edge `1.2065` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.0127` n `135` status `ready` deltaP `25.6019` edge `0.6486` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.5529` n `135` status `ready` deltaP `23.9931` edge `0.7015` maxDD `-15.8971`
- `market_context_high->crypto_major_4h` score `4.0089` n `41` status `ready` deltaP `12.3476` edge `0.3221` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4338` n `135` status `ready` deltaP `31.794` edge `0.122` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.2487` n `41` status `ready` deltaP `36.433` edge `0.0409` maxDD `-0.0449`
- `news_risk_high->metal_24h` score `2.995` n `135` status `ready` deltaP `23.6227` edge `0.2195` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.5957` n `135` status `ready` deltaP `27.7992` edge `0.1911` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.3693` n `51` status `ready` deltaP `15.1403` edge `0.1575` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.1209` n `51` status `ready` deltaP `13.2089` edge `0.155` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.467` n `51` status `ready` deltaP `20.5589` edge `0.0116` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `0.9159` n `135` status `ready` deltaP `8.503` edge `0.1107` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.9127` n `135` status `ready` deltaP `9.7006` edge `0.0737` maxDD `-1.6514`
- `news_risk_high->crypto_alt_4h` score `0.8479` n `135` status `ready` deltaP `8.6732` edge `0.2788` maxDD `-15.9436`
- `market_context_high->crypto_alt_4h` score `0.8133` n `41` status `ready` deltaP `8.3841` edge `0.1777` maxDD `-7.6792`
- `news_risk_high->index_1h` score `0.4933` n `135` status `ready` deltaP `8.8179` edge `0.0111` maxDD `-0.302`
- `market_context_high->commodity_1h` score `-0.0096` n `51` status `ready` deltaP `9.1229` edge `-0.0074` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
