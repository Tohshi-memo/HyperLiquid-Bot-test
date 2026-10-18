# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T00:37:25.614619+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.1074` n `54` status `ready` deltaP `39.3728` edge `0.3298` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1074` n `54` status `ready` deltaP `39.3728` edge `0.3298` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.0216` n `174` status `ready` deltaP `12.5368` edge `0.342` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.4124` n `174` status `ready` deltaP `4.1486` edge `0.0956` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.3752` n `91` status `ready` deltaP `14.9809` edge `0.1963` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3752` n `91` status `ready` deltaP `14.9809` edge `0.1963` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.0847` n `174` status `ready` deltaP `7.4179` edge `0.1076` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.026` n `91` status `ready` deltaP `5.1562` edge `0.0062` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.026` n `91` status `ready` deltaP `5.1562` edge `0.0062` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1835` n `174` status `ready` deltaP `6.8551` edge `0.0056` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3128` n `174` status `ready` deltaP `5.766` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4212` n `91` status `ready` deltaP `9.4084` edge `0.0318` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4212` n `91` status `ready` deltaP `9.4084` edge `0.0318` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5229` n `174` status `ready` deltaP `7.2943` edge `0.0415` maxDD `-1.6961`
- `market_context_high->equity_1h` score `-0.5357` n `174` status `ready` deltaP `10.0083` edge `0.0426` maxDD `-7.3168`
- `risk_on_high->crypto_major_1h` score `-0.7456` n `91` status `ready` deltaP `-0.9986` edge `0.003` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
