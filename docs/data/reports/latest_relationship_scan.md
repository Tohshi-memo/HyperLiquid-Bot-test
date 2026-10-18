# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T06:37:28.171086+00:00`
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

- `risk_on_high->commodity_24h` score `2.7571` n `68` status `ready` deltaP `18.7846` edge `0.1843` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.7571` n `68` status `ready` deltaP `18.7846` edge `0.1843` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `2.1812` n `116` status `ready` deltaP `15.2349` edge `0.1697` maxDD `-2.1597`
- `market_context_high->crypto_major_4h` score `1.8206` n `150` status `ready` deltaP `16.6301` edge `0.3813` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6632` n `150` status `ready` deltaP `5.4691` edge `0.1077` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1612` n `150` status `ready` deltaP `6.994` edge `0.1168` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1539` n `91` status `ready` deltaP `13.3041` edge `0.1791` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1539` n `91` status `ready` deltaP `13.3041` edge `0.1791` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3289` n `150` status `ready` deltaP `6.4384` edge `0.0045` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4368` n `91` status `ready` deltaP `9.4084` edge `0.0305` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4368` n `91` status `ready` deltaP `9.4084` edge `0.0305` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.4514` n `150` status `ready` deltaP `6.1098` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.6307` n `150` status `ready` deltaP `9.5256` edge `0.0379` maxDD `-7.3168`
- `market_context_high->metal_4h` score `-0.6953` n `150` status `ready` deltaP `4.8394` edge `0.0435` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
