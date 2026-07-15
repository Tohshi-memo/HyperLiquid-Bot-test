# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T16:37:28.633201+00:00`
- Price records: `672`
- Market context records: `6834`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `0.942` n `176` status `ready` deltaP `-1.5467` edge `0.5063` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1667` n `176` status `ready` deltaP `9.7065` edge `0.136` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3242` n `212` status `ready` deltaP `0.9208` edge `0.0008` maxDD `-0.5468`
- `market_context_high->crypto_major_1h` score `-0.4137` n `212` status `ready` deltaP `4.621` edge `0.0207` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.5087` n `212` status `ready` deltaP `2.4348` edge `0.0178` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.9111` n `212` status `ready` deltaP `-3.1522` edge `-0.0058` maxDD `-2.199`
- `market_context_high->metal_1h` score `-0.9838` n `212` status `ready` deltaP `-6.2677` edge `-0.0104` maxDD `-1.9158`
- `market_context_high->fx_4h` score `-1.1215` n `202` status `ready` deltaP `8.9531` edge `0.0029` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1434` n `212` status `ready` deltaP `-2.9121` edge `-0.0074` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6262` n `212` status `ready` deltaP `-3.542` edge `-0.0218` maxDD `-3.2083`
- `market_context_high->index_4h` score `-2.1619` n `202` status `ready` deltaP `0.6052` edge `-0.0354` maxDD `-10.3308`
- `market_context_high->commodity_4h` score `-2.3171` n `202` status `ready` deltaP `-4.3814` edge `-0.0149` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7059` n `202` status `ready` deltaP `-3.1937` edge `-0.0273` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9069` n `202` status `ready` deltaP `0.3365` edge `-0.0422` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1044` n `202` status `ready` deltaP `0.338` edge `-0.0419` maxDD `-20.6678`
- `market_context_high->equity_1h` score `-3.1163` n `212` status `ready` deltaP `-0.5084` edge `-0.0442` maxDD `-12.6351`
- `market_context_high->unknown_4h` score `-3.206` n `202` status `ready` deltaP `-9.7817` edge `0.0346` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4528` n `176` status `ready` deltaP `-9.7853` edge `-0.0022` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.3149` n `202` status `ready` deltaP `-1.6783` edge `-0.217` maxDD `-49.7697`
- `market_context_high->metal_24h` score `-9.3611` n `176` status `ready` deltaP `-19.7128` edge `-0.2202` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
