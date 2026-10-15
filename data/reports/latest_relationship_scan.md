# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T08:22:30.835225+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9717`

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

- `risk_on_high->commodity_24h` score `7.9411` n `54` status `ready` deltaP `41.2892` edge `0.3865` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9411` n `54` status `ready` deltaP `41.2892` edge `0.3865` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.7641` n `120` status `ready` deltaP `18.9329` edge `0.6652` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.8593` n `54` status `ready` deltaP `23.007` edge `0.4629` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.8593` n `54` status `ready` deltaP `23.007` edge `0.4629` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.1774` n `120` status `ready` deltaP `20.1728` edge `0.5362` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.7766` n `54` status `ready` deltaP `34.9876` edge `0.4644` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7766` n `54` status `ready` deltaP `34.9876` edge `0.4644` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8063` n `123` status `ready` deltaP `13.3294` edge `0.1681` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.098` n `123` status `ready` deltaP `5.1994` edge `0.1374` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.123` n `120` status `ready` deltaP `11.4431` edge `0.0385` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3297` n `54` status `ready` deltaP `0.9537` edge `0.0236` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3297` n `54` status `ready` deltaP `0.9537` edge `0.0236` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3465` n `54` status `ready` deltaP `4.6574` edge `0.0268` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3465` n `54` status `ready` deltaP `4.6574` edge `0.0268` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3562` n `123` status `ready` deltaP `-0.8204` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.4173` n `123` status `ready` deltaP `6.9106` edge `0.0061` maxDD `-0.9556`
- `market_context_high->commodity_24h` score `-0.4281` n `116` status `ready` deltaP `12.8409` edge `0.148` maxDD `-12.0788`
- `risk_on_high->metal_1h` score `-0.4547` n `54` status `ready` deltaP `1.8519` edge `0.0025` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4547` n `54` status `ready` deltaP `1.8519` edge `0.0025` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
