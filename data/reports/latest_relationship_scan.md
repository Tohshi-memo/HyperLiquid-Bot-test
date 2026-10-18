# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T13:37:26.104914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.3064` n `131` status `ready` deltaP `20.0322` edge `0.1438` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.8269` n `90` status `ready` deltaP `20.5071` edge `0.0953` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8269` n `90` status `ready` deltaP `20.5071` edge `0.0953` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.816` n `137` status `ready` deltaP `16.4968` edge `0.3818` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.8786` n `137` status `ready` deltaP `6.6163` edge `0.118` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.3499` n `91` status `ready` deltaP `14.5236` edge `0.1961` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3499` n `91` status `ready` deltaP `14.5236` edge `0.1961` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.008` n `91` status `ready` deltaP `5.0061` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.008` n `91` status `ready` deltaP `5.0061` edge `0.0057` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0189` n `137` status `ready` deltaP `4.9685` edge `0.1153` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.4123` n `137` status `ready` deltaP `3.8081` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4284` n `91` status `ready` deltaP `9.5585` edge `0.0302` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4284` n `91` status `ready` deltaP `9.5585` edge `0.0302` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.4383` n `137` status `ready` deltaP `5.1906` edge `0.0037` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6586` n `137` status `ready` deltaP `5.0583` edge `0.0451` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.7123` n `137` status `ready` deltaP `-0.8155` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
