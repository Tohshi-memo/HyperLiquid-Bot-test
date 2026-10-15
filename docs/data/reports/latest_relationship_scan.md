# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T00:37:31.251421+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9422`

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

- `market_context_high->crypto_alt_4h` score `7.3211` n `117` status `ready` deltaP `19.051` edge `0.6275` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.2087` n `54` status `ready` deltaP `36.9338` edge `0.3545` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.2087` n `54` status `ready` deltaP `36.9338` edge `0.3545` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3402` n `117` status `ready` deltaP `21.5773` edge `0.5404` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.9164` n `54` status `ready` deltaP `21.3302` edge `0.3955` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.9164` n `54` status `ready` deltaP `21.3302` edge `0.3955` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6609` n `54` status `ready` deltaP `34.6827` edge `0.4516` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6609` n `54` status `ready` deltaP `34.6827` edge `0.4516` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8875` n `117` status `ready` deltaP `14.315` edge `0.1683` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2359` n `117` status `ready` deltaP `5.5121` edge `0.1468` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5288` n `117` status `ready` deltaP `14.9847` edge `0.0487` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2967` n `117` status `ready` deltaP `8.1632` edge `0.0078` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3419` n `117` status `ready` deltaP `1.2474` edge `0.0012` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3531` n `54` status `ready` deltaP `0.9537` edge `0.0206` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3531` n `54` status `ready` deltaP `0.9537` edge `0.0206` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.4072` n `54` status `ready` deltaP `2.7501` edge `0.0026` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4072` n `54` status `ready` deltaP `2.7501` edge `0.0026` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4373` n `54` status `ready` deltaP `2.5915` edge `0.0312` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4373` n `54` status `ready` deltaP `2.5915` edge `0.0312` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.4704` n `117` status `ready` deltaP `1.975` edge `0.0013` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
