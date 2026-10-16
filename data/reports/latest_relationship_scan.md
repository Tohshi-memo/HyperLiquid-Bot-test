# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T19:52:26.695501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7180`

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

- `market_context_high->crypto_alt_4h` score `7.8393` n `127` status `ready` deltaP `20.434` edge `0.6085` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.624` n `54` status `ready` deltaP `40.0697` edge `0.3682` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.624` n `54` status `ready` deltaP `40.0697` edge `0.3682` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.0937` n `127` status `ready` deltaP `21.7303` edge `0.4951` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.8583` n `54` status `ready` deltaP `22.8546` edge `0.3805` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.8583` n `54` status `ready` deltaP `22.8546` edge `0.3805` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.2125` n `54` status `ready` deltaP `33.9205` edge `0.3992` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2125` n `54` status `ready` deltaP `33.9205` edge `0.3992` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6677` n `127` status `ready` deltaP `14.1178` edge `0.1513` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0069` n `127` status `ready` deltaP `6.2049` edge `0.1231` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5985` n `127` status `ready` deltaP `15.1515` edge `0.0534` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.0854` n `127` status `ready` deltaP `10.4743` edge `0.01` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2826` n `54` status `ready` deltaP `4.8459` edge `0.0046` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2826` n `54` status `ready` deltaP `4.8459` edge `0.0046` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3323` n `127` status `ready` deltaP `4.488` edge `0.0023` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3428` n `54` status `ready` deltaP `-0.9509` edge `0.0008` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3428` n `54` status `ready` deltaP `-0.9509` edge `0.0008` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.3922` n `54` status `ready` deltaP `2.1513` edge `0.0076` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3922` n `54` status `ready` deltaP `2.1513` edge `0.0076` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4354` n `127` status `ready` deltaP `-0.3204` edge `-0.0019` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
