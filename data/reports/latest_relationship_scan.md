# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T05:07:28.736308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12607`

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

- `market_context_high->unknown_24h` score `17107.6007` n `58` status `ready` deltaP `13.392` edge `1425.5493` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.3982` n `82` status `ready` deltaP `-4.502` edge `31.6887` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.8323` n `82` status `ready` deltaP `38.457` edge `1.3767` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.8245` n `82` status `ready` deltaP `31.8851` edge `1.3216` maxDD `-2.2369`
- `market_context_high->equity_24h` score `10.864` n `58` status `ready` deltaP `48.7847` edge `0.5801` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.8933` n `58` status `ready` deltaP `21.3721` edge `0.7647` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.6248` n `82` status `ready` deltaP `18.2969` edge `0.6081` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2404` n `82` status `ready` deltaP `43.6949` edge `0.2464` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7604` n `82` status `ready` deltaP `25.7876` edge `0.2702` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2534` n `58` status `ready` deltaP `42.1875` edge `0.0732` maxDD `0.0`
- `market_context_high->index_24h` score `4.1076` n `58` status `ready` deltaP `44.0314` edge `0.088` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3261` n `58` status `ready` deltaP `7.579` edge `0.1046` maxDD `-2.7324`
- `news_risk_high->index_4h` score `0.2434` n `82` status `ready` deltaP `9.7561` edge `0.029` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.1905` n `56` status `ready` deltaP `8.6237` edge `0.1344` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1905` n `56` status `ready` deltaP `8.6237` edge `0.1344` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.122` n `65` status `ready` deltaP `4.8526` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1065` n `125` status `ready` deltaP `2.9449` edge `-0.0017` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
