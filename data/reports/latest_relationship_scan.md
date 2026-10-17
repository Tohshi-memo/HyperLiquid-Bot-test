# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T20:07:30.134235+00:00`
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

- `risk_on_high->commodity_24h` score `7.0032` n `54` status `ready` deltaP `38.8502` edge `0.3246` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0032` n `54` status `ready` deltaP `38.8502` edge `0.3246` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.2073` n `174` status `ready` deltaP `13.299` edge `0.3413` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.5786` n `90` status `ready` deltaP `16.4024` edge `0.2018` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5786` n `90` status `ready` deltaP `16.4024` edge `0.2018` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4664` n `175` status `ready` deltaP `5.1839` edge `0.0932` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0702` n `175` status `ready` deltaP `7.8511` edge `0.1035` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0056` n `91` status `ready` deltaP `5.0061` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0056` n `91` status `ready` deltaP `5.0061` edge `0.0055` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.212` n `175` status `ready` deltaP `6.4127` edge `0.0049` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.257` n `91` status `ready` deltaP `1.1979` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.257` n `91` status `ready` deltaP `1.1979` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3172` n `175` status `ready` deltaP `5.7425` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.4008` n `175` status `ready` deltaP `9.716` edge `0.0378` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.48` n `91` status `ready` deltaP `9.4084` edge `0.0269` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.48` n `91` status `ready` deltaP `9.4084` edge `0.0269` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4883` n `91` status `ready` deltaP `0.9952` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4883` n `91` status `ready` deltaP `0.9952` edge `0.0039` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5718` n `174` status `ready` deltaP `6.1922` edge `0.0406` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.6888` n `91` status `ready` deltaP `0.3487` edge `0.0013` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
