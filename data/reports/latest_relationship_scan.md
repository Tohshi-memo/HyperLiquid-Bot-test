# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T10:07:28.813248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.0718` n `50` status `ready` deltaP `10.8743` edge `30.4384` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2912` n `50` status `ready` deltaP `12.0244` edge `24.4441` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.9975` n `50` status `ready` deltaP `26.8596` edge `1.0744` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `10.382` n `50` status `ready` deltaP `34.513` edge `0.7767` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.3325` n `70` status `ready` deltaP `38.7997` edge `0.6227` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.131` n `69` status `ready` deltaP `28.8499` edge `0.7004` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7969` n `70` status `ready` deltaP `29.6782` edge `0.5863` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4506` n `50` status `ready` deltaP `18.2283` edge `0.5697` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.309` n `50` status `ready` deltaP `18.2496` edge `0.533` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.3015` n `69` status `ready` deltaP `32.9139` edge `0.1549` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.985` n `70` status `ready` deltaP `28.8824` edge `0.2008` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3633` n `50` status `ready` deltaP `15.4012` edge `0.2439` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.0964` n `70` status `ready` deltaP `15.4149` edge `0.1908` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `3.0109` n `50` status `ready` deltaP `13.7006` edge `0.2046` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9872` n `50` status `ready` deltaP `33.5129` edge `0.039` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9187` n `70` status `ready` deltaP `32.2548` edge `0.0544` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.2729` n `70` status `ready` deltaP `19.1977` edge `0.103` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.6587` n `70` status `ready` deltaP `6.5441` edge `0.1465` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4615` n `50` status `ready` deltaP `20.491` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.443` n `70` status `ready` deltaP `13.5501` edge `0.0661` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
