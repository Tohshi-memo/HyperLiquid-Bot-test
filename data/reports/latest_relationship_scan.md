# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T07:22:29.624170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12880`

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

- `market_context_high->unknown_24h` score `18102.9867` n `56` status `ready` deltaP `13.4425` edge `1508.4978` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.2095` n `82` status `ready` deltaP `-5.1008` edge `31.5103` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.6973` n `82` status `ready` deltaP `31.8851` edge `1.311` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.6548` n `82` status `ready` deltaP `37.589` edge `1.3677` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.0097` n `56` status `ready` deltaP `46.7758` edge `0.5512` maxDD `-1.645`
- `market_context_high->crypto_alt_24h` score `9.9213` n `56` status `ready` deltaP `20.3869` edge `0.7736` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.961` n `82` status `ready` deltaP `19.8594` edge `0.6257` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.3779` n `82` status `ready` deltaP `45.0838` edge `0.2486` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5982` n `82` status `ready` deltaP `24.2251` edge `0.2671` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2954` n `56` status `ready` deltaP `42.1875` edge `0.0767` maxDD `0.0`
- `market_context_high->index_24h` score `4.0449` n `56` status `ready` deltaP `43.0804` edge `0.0866` maxDD `-0.2717`
- `market_context_high->metal_24h` score `0.82` n `56` status `ready` deltaP `11.6815` edge `0.1147` maxDD `-1.9958`
- `news_risk_high->index_4h` score `0.3225` n `82` status `ready` deltaP `11.128` edge `0.03` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.2266` n `65` status `ready` deltaP `9.5427` edge `0.1329` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.2266` n `65` status `ready` deltaP `9.5427` edge `0.1329` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1712` n `65` status `ready` deltaP `5.4514` edge `0.0035` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1712` n `65` status `ready` deltaP `5.4514` edge `0.0035` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.149` n `65` status `ready` deltaP `2.865` edge `0.0015` maxDD `-0.3081`
- `risk_on_high->commodity_1h` score `-0.2677` n `65` status `ready` deltaP `0.5528` edge `-0.0021` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
