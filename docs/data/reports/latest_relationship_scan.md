# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T10:22:29.531219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9244`

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

- `risk_on_high->commodity_24h` score `7.9375` n `54` status `ready` deltaP `41.2892` edge `0.3862` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9375` n `54` status `ready` deltaP `41.2892` edge `0.3862` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.6667` n `123` status `ready` deltaP `18.75` edge `0.6583` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.6229` n `54` status `ready` deltaP `22.0924` edge `0.4493` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.6229` n `54` status `ready` deltaP `22.0924` edge `0.4493` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.0481` n `123` status `ready` deltaP `20.0712` edge `0.5261` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.5894` n `54` status `ready` deltaP `34.073` edge `0.4465` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5894` n `54` status `ready` deltaP `34.073` edge `0.4465` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8362` n `123` status `ready` deltaP `13.6288` edge `0.1686` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1076` n `123` status `ready` deltaP `5.3491` edge `0.1372` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1235` n `123` status `ready` deltaP `11.1788` edge `0.0403` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3235` n `54` status `ready` deltaP `1.1034` edge `0.0234` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3235` n `54` status `ready` deltaP `1.1034` edge `0.0234` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.327` n `54` status `ready` deltaP `4.9568` edge `0.0273` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.327` n `54` status `ready` deltaP `4.9568` edge `0.0273` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3398` n `123` status `ready` deltaP `-0.5201` edge `-0.0017` maxDD `-0.4047`
- `market_context_high->commodity_24h` score `-0.4304` n `116` status `ready` deltaP `12.8409` edge `0.1477` maxDD `-12.0788`
- `market_context_high->index_1h` score `-0.4999` n `123` status `ready` deltaP `1.4832` edge `0.0008` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5167` n `123` status `ready` deltaP `5.8627` edge `0.0048` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5193` n `54` status `ready` deltaP `0.804` edge `0.0012` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
