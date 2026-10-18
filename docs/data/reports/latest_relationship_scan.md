# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T05:37:40.291919+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10534`

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

- `risk_on_high->commodity_24h` score `3.8163` n `64` status `ready` deltaP `23.7478` edge `0.2174` maxDD `-1.282`
- `risk_on_and_context->commodity_24h` score `3.8163` n `64` status `ready` deltaP `23.7478` edge `0.2174` maxDD `-1.282`
- `market_context_high->commodity_24h` score `2.1221` n `116` status `ready` deltaP `15.2349` edge `0.164` maxDD `-3.4314`
- `market_context_high->crypto_major_4h` score `1.6751` n `154` status `ready` deltaP `15.9962` edge `0.3734` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6206` n `154` status `ready` deltaP `5.1462` edge `0.1063` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1825` n `154` status `ready` deltaP `7.7397` edge `0.1218` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1325` n `91` status `ready` deltaP `12.9992` edge `0.1784` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1325` n `91` status `ready` deltaP `12.9992` edge `0.1784` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0629` n `91` status `ready` deltaP `4.1052` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0629` n `91` status `ready` deltaP `4.1052` edge `0.0058` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1691` n `154` status `ready` deltaP `7.2521` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3865` n `154` status `ready` deltaP `6.8901` edge `0.0088` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4632` n `91` status `ready` deltaP `9.1081` edge `0.0303` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4632` n `91` status `ready` deltaP `9.1081` edge `0.0303` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.5897` n `154` status `ready` deltaP `9.8573` edge `0.0391` maxDD `-7.3168`
- `market_context_high->metal_4h` score `-0.5977` n `154` status `ready` deltaP `6.1035` edge `0.0432` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
