# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T00:37:38.692459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.0655` n `50` status `ready` deltaP `10.4251` edge `30.2742` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.2061` n `50` status `ready` deltaP `10.3659` edge `24.2814` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.4587` n `70` status `ready` deltaP `35.4464` edge `1.1033` maxDD `-2.1107`
- `market_context_high->crypto_alt_24h` score `10.7859` n `50` status `ready` deltaP `20.875` edge `0.93` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.5282` n `70` status `ready` deltaP `33.7351` edge `0.6176` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9939` n `50` status `ready` deltaP `31.6528` edge `0.6801` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.6815` n `50` status `ready` deltaP `18.6098` edge `0.5864` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.2684` n `107` status `ready` deltaP `29.0418` edge `0.5465` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.1029` n `50` status `ready` deltaP `16.7988` edge `0.5255` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `3.36` n `70` status `ready` deltaP `9.6528` edge `0.5601` maxDD `-9.1614`
- `market_context_high->crypto_alt_1h` score `3.2338` n `50` status `ready` deltaP `14.8024` edge `0.2371` maxDD `-3.6376`
- `news_risk_high->equity_4h` score `3.1062` n `107` status `ready` deltaP `26.013` edge `0.1467` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0073` n `50` status `ready` deltaP `13.4012` edge `0.2063` maxDD `-2.2692`
- `news_risk_high->crypto_major_4h` score `2.8612` n `107` status `ready` deltaP `20.7033` edge `0.3822` maxDD `-7.2722`
- `market_context_high->fx_4h` score `2.8287` n `50` status `ready` deltaP `31.622` edge `0.0384` maxDD `-0.0791`
- `news_risk_high->index_24h` score `1.6164` n `70` status `ready` deltaP `19.2361` edge `0.0515` maxDD `-0.2696`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3039` n `70` status `ready` deltaP `13.3978` edge `0.2038` maxDD `-2.0759`
- `news_risk_high->crypto_alt_1h` score `1.2993` n `107` status `ready` deltaP `5.8117` edge `0.1256` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2749` n `50` status `ready` deltaP `6.0208` edge `0.3095` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
