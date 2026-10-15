# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T06:22:25.867375+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `market_context_high->crypto_alt_4h` score `8.1845` n `117` status `ready` deltaP `20.4229` edge `0.6903` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.8641` n `54` status `ready` deltaP `40.9408` edge `0.3824` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8641` n `54` status `ready` deltaP `40.9408` edge `0.3824` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.7797` n `54` status `ready` deltaP `22.7021` edge `0.4583` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.7797` n `54` status `ready` deltaP `22.7021` edge `0.4583` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.6531` n `117` status `ready` deltaP `22.3395` edge `0.5614` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8643` n `54` status `ready` deltaP `35.4449` edge `0.4726` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8643` n `54` status `ready` deltaP `35.4449` edge `0.4726` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8086` n `120` status `ready` deltaP `13.4182` edge `0.1677` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0534` n `120` status `ready` deltaP `4.5509` edge `0.138` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3592` n `117` status `ready` deltaP `13.7652` edge `0.0427` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2822` n `54` status `ready` deltaP `1.4028` edge `0.0267` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2822` n `54` status `ready` deltaP `1.4028` edge `0.0267` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3333` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3333` n `54` status `ready` deltaP `4.8071` edge `0.0275` maxDD `-5.8485`
- `market_context_high->metal_1h` score `-0.4033` n `120` status `ready` deltaP `6.9661` edge `0.0069` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4329` n `54` status `ready` deltaP `2.1513` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4329` n `54` status `ready` deltaP `2.1513` edge `0.0033` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4561` n `120` status `ready` deltaP `0.03` edge `-0.0002` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `-0.4782` n `116` status `ready` deltaP `12.4925` edge `0.1439` maxDD `-12.0788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
