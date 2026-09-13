# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T05:37:29.411809+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12629`

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

- `market_context_high->unknown_24h` score `18150.2732` n `56` status `ready` deltaP `13.2689` edge `1512.4395` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.079` n `82` status `ready` deltaP `-4.502` edge `31.6621` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.7837` n `82` status `ready` deltaP `31.8851` edge `1.3182` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.7733` n `82` status `ready` deltaP `38.1098` edge `1.3741` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.911` n `56` status `ready` deltaP `49.1319` edge `0.5817` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.8061` n `56` status `ready` deltaP `20.3869` edge `0.764` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.6946` n `82` status `ready` deltaP `18.6441` edge `0.6116` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2718` n `82` status `ready` deltaP `44.0421` edge `0.2467` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7254` n `82` status `ready` deltaP `25.4404` edge `0.2696` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2906` n `56` status `ready` deltaP `42.1875` edge `0.0763` maxDD `0.0`
- `market_context_high->index_24h` score `4.1127` n `56` status `ready` deltaP `43.8244` edge `0.0898` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.5451` n `56` status `ready` deltaP `9.3254` edge `0.1088` maxDD `-2.4203`
- `risk_on_high->crypto_alt_4h` score `0.2624` n `58` status `ready` deltaP `9.735` edge `0.1362` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2624` n `58` status `ready` deltaP `9.735` edge `0.1362` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.2608` n `82` status `ready` deltaP `10.061` edge `0.0292` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1119` n `65` status `ready` deltaP `3.3141` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1119` n `65` status `ready` deltaP `3.3141` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1627` n `125` status `ready` deltaP `2.9449` edge `-0.0016` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
