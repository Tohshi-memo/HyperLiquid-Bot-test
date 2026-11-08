# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T08:52:23.839329+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4760`

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

- `market_context_high->unknown_4h` score `125.2016` n `37` status `ready` deltaP `-4.0911` edge `10.5055` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2676` n `37` status `ready` deltaP `10.5074` edge `0.2482` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1839` n `37` status `ready` deltaP `34.3812` edge `0.0451` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0304` n `37` status `ready` deltaP `26.5079` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.4835` n `45` status `ready` deltaP `7.6389` edge `0.0948` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.7903` n `37` status `ready` deltaP `9.7508` edge `0.0594` maxDD `-3.0172`
- `news_risk_high->fx_4h` score `0.7673` n `45` status `ready` deltaP `13.1199` edge `0.011` maxDD `-0.0954`
- `market_context_high->crypto_alt_1h` score `0.5355` n `37` status `ready` deltaP `11.9963` edge `0.0702` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4098` n `37` status `ready` deltaP `6.9227` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->equity_4h` score `0.3656` n `45` status `ready` deltaP `1.4804` edge `0.1109` maxDD `-4.2454`
- `market_context_high->index_1h` score `0.3093` n `37` status `ready` deltaP `2.0999` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.1889` n `45` status `ready` deltaP `7.649` edge `0.021` maxDD `-0.4888`
- `market_context_high->commodity_1h` score `0.1335` n `37` status `ready` deltaP `9.3179` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0337` n `48` status `ready` deltaP `6.9985` edge `0.003` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `-0.0069` n `37` status `ready` deltaP `3.1395` edge `0.0236` maxDD `-1.633`
- `news_risk_high->fx_1h` score `-0.0433` n `48` status `ready` deltaP `3.0938` edge `0.004` maxDD `-0.0804`
- `market_context_high->metal_1h` score `-0.056` n `37` status `ready` deltaP `1.3514` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.1517` n `48` status `ready` deltaP `-1.0354` edge `0.0424` maxDD `-1.396`
- `news_risk_high->index_24h` score `-0.3052` n `45` status `ready` deltaP `0.8681` edge `0.1219` maxDD `-6.6786`
- `market_context_high->equity_4h` score `-0.637` n `37` status `ready` deltaP `22.8618` edge `0.0939` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
