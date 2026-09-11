# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T22:52:32.009577+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11335`

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

- `news_risk_high->unknown_1h` score `448.8201` n `77` status `ready` deltaP `-3.8183` edge `37.4693` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.6127` n `91` status `ready` deltaP `43.1166` edge `1.7866` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.6127` n `91` status `ready` deltaP `43.1166` edge `1.7866` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.0265` n `36` status `ready` deltaP `50.1736` edge `1.5911` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.7032` n `151` status `ready` deltaP `38.0151` edge `1.6379` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `12.4797` n `36` status `ready` deltaP `18.0555` edge `0.9684` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `10.0289` n `36` status `ready` deltaP `31.4236` edge `0.6361` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4119` n `91` status `ready` deltaP `36.9792` edge `0.5378` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4119` n `91` status `ready` deltaP `36.9792` edge `0.5378` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1227` n `151` status `ready` deltaP `36.9792` edge `0.5137` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7272` n `91` status `ready` deltaP `42.8605` edge `0.4787` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7272` n `91` status `ready` deltaP `42.8605` edge `0.4787` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.9629` n `36` status `ready` deltaP `51.0417` edge `0.3233` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.737` n `91` status `ready` deltaP `25.021` edge `1.2319` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.737` n `91` status `ready` deltaP `25.021` edge `1.2319` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.6521` n `36` status `ready` deltaP `49.3055` edge `0.3183` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7003` n `91` status `ready` deltaP `31.7442` edge `0.4326` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7003` n `91` status `ready` deltaP `31.7442` edge `0.4326` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3668` n `91` status `ready` deltaP `51.5644` edge `0.1077` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3668` n `91` status `ready` deltaP `51.5644` edge `0.1077` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
