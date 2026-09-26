# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T23:35:03.983458+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3894.3156` n `90` status `ready` deltaP `1.2153` edge `324.5182` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4287` n `45` status `ready` deltaP `10.2029` edge `5.8057` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.7531` n `45` status `ready` deltaP `26.25` edge `4.0062` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.1413` n `45` status `ready` deltaP `36.1459` edge `2.0522` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.9051` n `45` status `ready` deltaP `14.9653` edge `2.1803` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.5085` n `45` status `ready` deltaP `31.1111` edge `0.4271` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6549` n `45` status `ready` deltaP `31.7709` edge `0.1166` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.297` n `45` status `ready` deltaP `37.0833` edge `0.0346` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8784` n `45` status `ready` deltaP `18.0861` edge `0.1611` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.6069` n `90` status `ready` deltaP `20.0` edge `0.0576` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.2192` n `90` status `ready` deltaP `27.3264` edge `0.1389` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1685` n `45` status `ready` deltaP `13.0739` edge `0.0505` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `1.123` n `45` status `ready` deltaP `9.0684` edge `0.0999` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.088` n `45` status `ready` deltaP `8.3533` edge `0.1084` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.8194` n `45` status `ready` deltaP `7.2798` edge `0.1102` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.6432` n `45` status `ready` deltaP `10.8516` edge `0.0091` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.2198` n `45` status `ready` deltaP `4.9102` edge `0.0745` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1966` n `45` status `ready` deltaP `8.1237` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1766` n `45` status `ready` deltaP `5.3027` edge `0.011` maxDD `-0.1976`
- `news_risk_high->equity_4h` score `-0.0679` n `139` status `ready` deltaP `16.6312` edge `0.0444` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
