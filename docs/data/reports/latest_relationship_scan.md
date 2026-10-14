# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T07:07:29.910552+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.5469` n `117` status `ready` deltaP `16.7644` edge `0.5787` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.2836` n `54` status `ready` deltaP `32.0` edge `0.3103` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2836` n `54` status `ready` deltaP `32.0` edge `0.3103` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0528` n `117` status `ready` deltaP `21.12` edge `0.5195` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.1358` n `54` status `ready` deltaP `19.0436` edge `0.3458` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1358` n `54` status `ready` deltaP `19.0436` edge `0.3458` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.6696` n `117` status `ready` deltaP `-2.7048` edge `0.4718` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4741` n `54` status `ready` deltaP `34.2254` edge `0.4307` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4741` n `54` status `ready` deltaP `34.2254` edge `0.4307` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7554` n `117` status `ready` deltaP `14.0156` edge `0.1596` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3531` n `117` status `ready` deltaP `7.4582` edge `0.1436` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0886` n `117` status `ready` deltaP `12.3932` edge `0.0293` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2769` n `54` status `ready` deltaP `2.8998` edge `0.0174` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2769` n `54` status `ready` deltaP `2.8998` edge `0.0174` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3672` n `117` status `ready` deltaP `0.797` edge `0.0021` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4165` n `117` status `ready` deltaP `6.9656` edge `0.0058` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4851` n `54` status `ready` deltaP `1.5525` edge `0.0006` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4851` n `54` status `ready` deltaP `1.5525` edge `0.0006` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5922` n `54` status `ready` deltaP `3.7592` edge `0.0016` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5922` n `54` status `ready` deltaP `3.7592` edge `0.0016` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
