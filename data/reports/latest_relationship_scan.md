# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T03:37:29.333596+00:00`
- Price records: `672`
- Market context records: `8263`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7314.8078` n `46` status `ready` deltaP `39.0625` edge `609.3069` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1003` n `54` status `ready` deltaP `26.3832` edge `0.4755` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.2021` n `54` status `ready` deltaP `22.4274` edge `0.1482` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7079` n `54` status `ready` deltaP `22.8771` edge `0.0922` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1856` n `54` status `ready` deltaP `10.6313` edge `0.2787` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8926` n `54` status `ready` deltaP `15.0033` edge `0.1011` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6701` n `54` status `ready` deltaP `10.906` edge `0.1062` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3442` n `54` status `ready` deltaP `16.6215` edge `0.2007` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.135` n `54` status `ready` deltaP `10.1965` edge `0.0734` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5334` n `54` status `ready` deltaP `7.5017` edge `0.0233` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2164` n `54` status `ready` deltaP `7.8953` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0329` n `54` status `ready` deltaP `3.7037` edge `0.0129` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4159` n `54` status `ready` deltaP `5.3748` edge `0.0066` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1851` n `54` status `ready` deltaP `-9.1096` edge `-0.0428` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.3282` n `46` status `ready` deltaP `-19.2557` edge `-0.0443` maxDD `-4.3746`
- `news_risk_high->metal_24h` score `-5.8054` n `46` status `ready` deltaP `-20.8787` edge `-0.0765` maxDD `-10.4475`
- `news_risk_high->commodity_4h` score `-9.0451` n `54` status `ready` deltaP `-32.7913` edge `-0.2044` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.9678` n `46` status `ready` deltaP `-25.0679` edge `-0.3433` maxDD `-25.6187`
- `news_risk_high->commodity_24h` score `-13.0569` n `46` status `ready` deltaP `-15.0061` edge `-0.4043` maxDD `-33.0322`
- `news_risk_high->equity_24h` score `-35.0958` n `46` status `ready` deltaP `-24.1998` edge `-1.1835` maxDD `-113.052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
