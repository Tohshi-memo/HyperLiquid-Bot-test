# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T05:22:36.088997+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12605`

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

- `market_context_high->unknown_24h` score `17619.1474` n `57` status `ready` deltaP `13.3315` edge `1468.1786` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.0766` n `82` status `ready` deltaP `-4.502` edge `31.6619` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.804` n `82` status `ready` deltaP `38.2834` edge `1.3755` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.8029` n `82` status `ready` deltaP `31.8851` edge `1.3198` maxDD `-2.2369`
- `market_context_high->equity_24h` score `10.8851` n `57` status `ready` deltaP `48.9583` edge `0.5807` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.8354` n `57` status `ready` deltaP `20.8881` edge `0.7631` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.6591` n `82` status `ready` deltaP `18.4705` edge `0.6098` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2567` n `82` status `ready` deltaP `43.8685` edge `0.2466` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7429` n `82` status `ready` deltaP `25.614` edge `0.2699` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.275` n `57` status `ready` deltaP `42.1875` edge `0.075` maxDD `0.0`
- `market_context_high->index_24h` score `4.1118` n `57` status `ready` deltaP `43.9327` edge `0.089` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.4401` n `57` status `ready` deltaP `8.4338` edge `0.1071` maxDD `-2.5519`
- `news_risk_high->index_4h` score `0.2521` n `82` status `ready` deltaP `9.9085` edge `0.0291` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.2287` n `57` status `ready` deltaP `9.1918` edge `0.1355` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2287` n `57` status `ready` deltaP `9.1918` edge `0.1355` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1639` n `125` status `ready` deltaP `2.9449` edge `-0.0017` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
