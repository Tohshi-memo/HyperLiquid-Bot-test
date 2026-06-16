# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T13:22:38.377411+00:00`
- Price records: `672`
- Market context records: `4095`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10376`

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

- `risk_on_high->unknown_4h` score `144.6495` n `40` status `ready` deltaP `-8.811` edge `12.2945` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6495` n `40` status `ready` deltaP `-8.811` edge `12.2945` maxDD `-10.864`
- `market_context_high->unknown_1h` score `48.1425` n `178` status `ready` deltaP `2.1059` edge `4.1556` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0397` n `144` status `ready` deltaP `-9.2396` edge `3.5511` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.0333` n `175` status `ready` deltaP `-2.311` edge `1.8938` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.8089` n `40` status `ready` deltaP `36.5244` edge `-0.0047` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.8089` n `40` status `ready` deltaP `36.5244` edge `-0.0047` maxDD `-0.0446`
- `market_context_high->equity_1h` score `0.6263` n `178` status `ready` deltaP `5.0983` edge `0.0749` maxDD `-2.2022`
- `risk_on_high->equity_1h` score `0.5095` n `40` status `ready` deltaP `11.3623` edge `0.0058` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.5095` n `40` status `ready` deltaP `11.3623` edge `0.0058` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1642` n `40` status `ready` deltaP `11.4634` edge `0.0037` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1642` n `40` status `ready` deltaP `11.4634` edge `0.0037` maxDD `-0.3925`
- `market_context_high->equity_4h` score `0.1467` n `175` status `ready` deltaP `12.1673` edge `0.0842` maxDD `-6.9137`
- `risk_on_high->fx_1h` score `0.0832` n `40` status `ready` deltaP `4.8503` edge `0.0013` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0832` n `40` status `ready` deltaP `4.8503` edge `0.0013` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0106` n `40` status `ready` deltaP `10.509` edge `-0.0172` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0106` n `40` status `ready` deltaP `10.509` edge `-0.0172` maxDD `-2.3372`
- `market_context_high->index_24h` score `-0.0554` n `144` status `ready` deltaP `14.0381` edge `-0.0982` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `-0.1314` n `40` status `ready` deltaP `15.9451` edge `-0.0507` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.1314` n `40` status `ready` deltaP `15.9451` edge `-0.0507` maxDD `-2.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
