# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T06:52:28.738019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10438`

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

- `risk_on_high->commodity_24h` score `2.701` n `69` status `ready` deltaP `18.9087` edge `0.1788` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.701` n `69` status `ready` deltaP `18.9087` edge `0.1788` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `2.2961` n `116` status `ready` deltaP `15.9227` edge `0.1717` maxDD `-1.9206`
- `market_context_high->crypto_major_4h` score `1.8903` n `149` status `ready` deltaP `17.0506` edge `0.3843` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6901` n `149` status `ready` deltaP `5.6997` edge `0.1084` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.1539` n `91` status `ready` deltaP `13.3041` edge `0.1791` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1539` n `91` status `ready` deltaP `13.3041` edge `0.1791` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.1281` n `149` status `ready` deltaP `6.6853` edge `0.1161` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.355` n `149` status `ready` deltaP `6.1118` edge `0.0045` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4392` n `91` status `ready` deltaP `9.4084` edge `0.0303` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4392` n `91` status `ready` deltaP `9.4084` edge `0.0303` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.4648` n `149` status `ready` deltaP `5.9418` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.6644` n `149` status `ready` deltaP `9.1945` edge `0.0373` maxDD `-7.3168`
- `market_context_high->metal_4h` score `-0.7202` n `149` status `ready` deltaP `4.5128` edge `0.0436` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
