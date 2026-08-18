# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T01:37:27.991770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `9.7402` n `31` status `ready` deltaP `5.6693` edge `0.7974` maxDD `-0.5477`
- `risk_on_and_context->unknown_1h` score `9.7402` n `31` status `ready` deltaP `5.6693` edge `0.7974` maxDD `-0.5477`
- `market_context_high->crypto_major_24h` score `5.1344` n `73` status `ready` deltaP `18.0836` edge `0.4281` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.4784` n `73` status `ready` deltaP `16.9844` edge `0.0933` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.6725` n `31` status `ready` deltaP `21.602` edge `0.0081` maxDD `-0.0192`
- `risk_on_and_context->fx_4h` score `1.6725` n `31` status `ready` deltaP `21.602` edge `0.0081` maxDD `-0.0192`
- `market_context_high->index_24h` score `1.0514` n `73` status `ready` deltaP `17.6942` edge `-0.026` maxDD `-0.0141`
- `risk_on_high->commodity_4h` score `0.5906` n `31` status `ready` deltaP `7.9366` edge `0.0857` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.5906` n `31` status `ready` deltaP `7.9366` edge `0.0857` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.5682` n `31` status `ready` deltaP `9.2621` edge `0.0074` maxDD `-0.0771`
- `risk_on_and_context->fx_1h` score `0.5682` n `31` status `ready` deltaP `9.2621` edge `0.0074` maxDD `-0.0771`
- `market_context_high->commodity_4h` score `0.5671` n `113` status `ready` deltaP `12.133` edge `0.0514` maxDD `-2.4692`
- `risk_on_high->index_1h` score `0.4375` n `31` status `ready` deltaP `10.706` edge `0.0026` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.4375` n `31` status `ready` deltaP `10.706` edge `0.0026` maxDD `-0.3343`
- `risk_on_high->crypto_major_1h` score `0.349` n `31` status `ready` deltaP `6.5675` edge `0.0159` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.349` n `31` status `ready` deltaP `6.5675` edge `0.0159` maxDD `-1.1144`
- `market_context_high->commodity_24h` score `0.2495` n `73` status `ready` deltaP `12.6469` edge `0.1198` maxDD `-4.666`
- `market_context_high->index_1h` score `0.1363` n `113` status `ready` deltaP `7.5659` edge `0.0029` maxDD `-0.3584`
- `risk_on_high->equity_1h` score `0.0672` n `31` status `ready` deltaP `8.6923` edge `0.002` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.0672` n `31` status `ready` deltaP `8.6923` edge `0.002` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
