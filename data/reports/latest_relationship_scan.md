# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T09:07:31.661241+00:00`
- Price records: `672`
- Market context records: `4401`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `127.9171` n `46` status `ready` deltaP `1.3057` edge `10.8329` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `127.9171` n `46` status `ready` deltaP `1.3057` edge `10.8329` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.8653` n `227` status `ready` deltaP `2.6492` edge `2.7874` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `12.371` n `218` status `ready` deltaP `5.2347` edge `1.539` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.1783` n `46` status `ready` deltaP `34.1066` edge `0.0422` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1783` n `46` status `ready` deltaP `34.1066` edge `0.0422` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9851` n `44` status `ready` deltaP `-15.3567` edge `0.5465` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9851` n `44` status `ready` deltaP `-15.3567` edge `0.5465` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3277` n `46` status `ready` deltaP `19.3398` edge `0.1316` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3277` n `46` status `ready` deltaP `19.3398` edge `0.1316` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7253` n `44` status `ready` deltaP `20.4861` edge `0.0072` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7253` n `44` status `ready` deltaP `20.4861` edge `0.0072` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4886` n `44` status `ready` deltaP `23.4375` edge `-0.0322` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.4886` n `44` status `ready` deltaP `23.4375` edge `-0.0322` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.811` n `49` status `ready` deltaP `12.801` edge `0.0212` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.811` n `49` status `ready` deltaP `12.801` edge `0.0212` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3659` n `46` status `ready` deltaP `6.6411` edge `0.0362` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3659` n `46` status `ready` deltaP `6.6411` edge `0.0362` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.2285` n `49` status `ready` deltaP `5.8505` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2285` n `49` status `ready` deltaP `5.8505` edge `0.003` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
