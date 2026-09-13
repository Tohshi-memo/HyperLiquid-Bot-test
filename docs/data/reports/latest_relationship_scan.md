# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T06:52:31.535825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12697`

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

- `market_context_high->unknown_24h` score `19233.9857` n `54` status `ready` deltaP `13.3102` edge `1602.7486` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.2251` n `82` status `ready` deltaP `-4.9511` edge `31.5106` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.7033` n `82` status `ready` deltaP `31.8851` edge `1.3115` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.662` n `82` status `ready` deltaP `37.589` edge `1.3683` maxDD `-9.098`
- `market_context_high->equity_24h` score `11.0788` n `54` status `ready` deltaP `50.0` edge `0.5899` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.7335` n `54` status `ready` deltaP `19.3287` edge `0.765` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.8804` n `82` status `ready` deltaP `19.5122` edge `0.6213` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.3418` n `82` status `ready` deltaP `44.7366` edge `0.2479` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6332` n `82` status `ready` deltaP `24.5724` edge `0.2677` maxDD `-0.6334`
- `market_context_high->index_24h` score `4.3537` n `54` status `ready` deltaP `45.7755` edge `0.0927` maxDD `-0.1382`
- `market_context_high->commodity_24h` score `4.3014` n `54` status `ready` deltaP `42.1875` edge `0.0772` maxDD `0.0`
- `market_context_high->metal_24h` score `0.7646` n `54` status `ready` deltaP `10.7061` edge `0.1141` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.3324` n `63` status `ready` deltaP `11.1426` edge `0.1358` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.3324` n `63` status `ready` deltaP `11.1426` edge `0.1358` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.3051` n `82` status `ready` deltaP `10.8231` edge `0.0298` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.146` n `65` status `ready` deltaP `5.152` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.2333` n `128` status `ready` deltaP `2.0631` edge `-0.0016` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
