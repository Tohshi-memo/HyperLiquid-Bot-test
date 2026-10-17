# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T20:52:26.576395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9652`

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

- `risk_on_high->commodity_24h` score `7.0224` n `54` status `ready` deltaP `38.8502` edge `0.3262` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0224` n `54` status `ready` deltaP `38.8502` edge `0.3262` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.1287` n `174` status `ready` deltaP `12.8417` edge `0.3378` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.5275` n `90` status `ready` deltaP `15.9451` edge `0.1983` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5275` n `90` status `ready` deltaP `15.9451` edge `0.1983` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4616` n `175` status `ready` deltaP `5.1839` edge `0.0928` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1085` n `175` status `ready` deltaP `8.1505` edge `0.1047` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0308` n `91` status `ready` deltaP `5.3064` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0308` n `91` status `ready` deltaP `5.3064` edge `0.0056` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1956` n `175` status `ready` deltaP `6.713` edge `0.005` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2648` n `91` status `ready` deltaP `1.0478` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2648` n `91` status `ready` deltaP `1.0478` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3008` n `175` status `ready` deltaP `6.0419` edge `0.0081` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3751` n `175` status `ready` deltaP `10.1664` edge `0.0381` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.4403` n `91` status `ready` deltaP `9.8588` edge `0.0272` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4403` n `91` status `ready` deltaP `9.8588` edge `0.0272` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.472` n `91` status `ready` deltaP `1.2946` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.472` n `91` status `ready` deltaP `1.2946` edge `0.004` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5718` n `174` status `ready` deltaP `6.1922` edge `0.0406` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.6919` n `91` status `ready` deltaP `0.3487` edge `0.0009` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
