# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T05:51:37.612610+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9614`

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

- `market_context_high->crypto_alt_4h` score `8.0581` n `117` status `ready` deltaP `20.1181` edge `0.6818` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.8182` n `54` status `ready` deltaP `40.5923` edge `0.3809` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8182` n `54` status `ready` deltaP `40.5923` edge `0.3809` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.6533` n `54` status `ready` deltaP `22.3973` edge `0.4498` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.6533` n `54` status `ready` deltaP `22.3973` edge `0.4498` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.5843` n `117` status `ready` deltaP `22.0346` edge `0.5577` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8196` n `54` status `ready` deltaP `35.14` edge `0.4689` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8196` n `54` status `ready` deltaP `35.14` edge `0.4689` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7762` n `120` status `ready` deltaP `13.2685` edge `0.166` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0282` n `120` status `ready` deltaP `4.4012` edge `0.1369` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3628` n `117` status `ready` deltaP `13.7652` edge `0.043` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2985` n `54` status `ready` deltaP `1.2531` edge `0.0256` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2985` n `54` status `ready` deltaP `1.2531` edge `0.0256` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3543` n `54` status `ready` deltaP `4.6574` edge `0.0258` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3543` n `54` status `ready` deltaP `4.6574` edge `0.0258` maxDD `-5.8485`
- `market_context_high->metal_1h` score `-0.4009` n `120` status `ready` deltaP `6.9661` edge `0.0071` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4313` n `54` status `ready` deltaP `2.1513` edge `0.0035` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4313` n `54` status `ready` deltaP `2.1513` edge `0.0035` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4693` n `120` status `ready` deltaP `-0.1202` edge `-0.0003` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.4958` n `120` status `ready` deltaP `1.4865` edge `0.0013` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
