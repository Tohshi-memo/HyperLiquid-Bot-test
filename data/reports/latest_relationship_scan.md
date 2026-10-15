# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T08:07:27.358310+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9711`

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

- `risk_on_high->commodity_24h` score `7.9387` n `54` status `ready` deltaP `41.2892` edge `0.3863` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9387` n `54` status `ready` deltaP `41.2892` edge `0.3863` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.7665` n `120` status `ready` deltaP `18.9329` edge `0.6654` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.8617` n `54` status `ready` deltaP `23.007` edge `0.4631` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.8617` n `54` status `ready` deltaP `23.007` edge `0.4631` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.2124` n `120` status `ready` deltaP `20.3252` edge `0.5381` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.7993` n `54` status `ready` deltaP `35.14` edge `0.4663` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7993` n `54` status `ready` deltaP `35.14` edge `0.4663` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8267` n `123` status `ready` deltaP `13.4791` edge `0.1688` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1196` n `123` status `ready` deltaP `5.3491` edge `0.1382` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1388` n `120` status `ready` deltaP `11.5955` edge `0.0388` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3157` n `54` status `ready` deltaP `1.1034` edge `0.0244` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3157` n `54` status `ready` deltaP `1.1034` edge `0.0244` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3333` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3333` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3562` n `123` status `ready` deltaP `-0.8204` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.4161` n `123` status `ready` deltaP `6.9106` edge `0.0062` maxDD `-0.9556`
- `market_context_high->commodity_24h` score `-0.4296` n `116` status `ready` deltaP `12.8409` edge `0.1478` maxDD `-12.0788`
- `risk_on_high->metal_1h` score `-0.4539` n `54` status `ready` deltaP `1.8519` edge `0.0026` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4539` n `54` status `ready` deltaP `1.8519` edge `0.0026` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
