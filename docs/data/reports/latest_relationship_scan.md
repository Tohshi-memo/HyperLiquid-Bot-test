# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T18:52:31.073116+00:00`
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

- `risk_on_high->commodity_24h` score `7.7181` n `54` status `ready` deltaP `40.7666` edge `0.3714` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7181` n `54` status `ready` deltaP `40.7666` edge `0.3714` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.6262` n `127` status `ready` deltaP `19.8242` edge `0.5948` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.9741` n `127` status `ready` deltaP `21.1206` edge `0.4892` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.6451` n `54` status `ready` deltaP `22.2448` edge `0.3668` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.6451` n `54` status `ready` deltaP `22.2448` edge `0.3668` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1348` n `54` status `ready` deltaP `33.3108` edge `0.3933` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1348` n `54` status `ready` deltaP `33.3108` edge `0.3933` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6642` n `127` status `ready` deltaP `13.9681` edge `0.152` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0249` n `127` status `ready` deltaP `6.3546` edge `0.1236` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5889` n `127` status `ready` deltaP `15.1515` edge `0.0526` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.0698` n `127` status `ready` deltaP `10.624` edge `0.0103` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2725` n `54` status `ready` deltaP `4.9956` edge `0.0049` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2725` n `54` status `ready` deltaP `4.9956` edge `0.0049` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.3417` n `127` status `ready` deltaP `4.3378` edge `0.0021` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3522` n `54` status `ready` deltaP `-1.1011` edge `0.0006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3522` n `54` status `ready` deltaP `-1.1011` edge `0.0006` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.3805` n `54` status `ready` deltaP `2.301` edge `0.0081` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3805` n `54` status `ready` deltaP `2.301` edge `0.0081` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.4197` n `127` status `ready` deltaP `-0.0201` edge `-0.0019` maxDD `-0.4757`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
