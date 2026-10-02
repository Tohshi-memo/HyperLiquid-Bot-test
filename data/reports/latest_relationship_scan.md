# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T19:56:45.429682+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4940`

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

- `market_context_high->unknown_1h` score `365.6878` n `50` status `ready` deltaP `10.8743` edge `30.4064` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.9613` n `50` status `ready` deltaP `10.3659` edge `24.261` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1701` n `73` status `ready` deltaP `41.0103` edge `1.095` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.8447` n `50` status `ready` deltaP `17.75` edge `0.8724` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0162` n `50` status `ready` deltaP `31.8264` edge `0.6808` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.7715` n `73` status `ready` deltaP `31.1905` edge `0.5715` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.5073` n `50` status `ready` deltaP `18.4573` edge `0.5729` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.7295` n `50` status `ready` deltaP `16.6463` edge `0.4954` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.5505` n `116` status `ready` deltaP `22.5084` edge `0.4469` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.4016` n `50` status `ready` deltaP `15.5509` edge `0.2461` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1787` n `50` status `ready` deltaP `14.7485` edge `0.2116` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7385` n `50` status `ready` deltaP `30.5549` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5107` n `116` status `ready` deltaP `22.0984` edge `0.1315` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.528` n `50` status `ready` deltaP `7.4097` edge `0.3327` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5254` n `73` status `ready` deltaP `5.9908` edge `0.471` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4591` n `50` status `ready` deltaP `20.491` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_4h` score `1.4491` n `116` status `ready` deltaP `15.1125` edge `0.316` maxDD `-10.477`
- `news_risk_high->metal_24h` score `1.3551` n `73` status `ready` deltaP `13.009` edge `0.2144` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.2542` n `116` status `ready` deltaP `6.4475` edge `0.1176` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8464` n `50` status `ready` deltaP `18.0764` edge `0.0898` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
