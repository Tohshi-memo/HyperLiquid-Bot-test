# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T04:28:14.979594+00:00`
- Price records: `672`
- Market context records: `8267`
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

- `news_risk_high->unknown_24h` score `7314.8978` n `46` status `ready` deltaP `39.0625` edge `609.3144` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2071` n `54` status `ready` deltaP `26.3832` edge `0.4844` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.2729` n `54` status `ready` deltaP `22.5771` edge `0.1531` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7343` n `54` status `ready` deltaP `22.8771` edge `0.0944` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1754` n `54` status `ready` deltaP `10.6313` edge `0.2774` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9754` n `54` status `ready` deltaP `15.3027` edge `0.106` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7277` n `54` status `ready` deltaP `11.2054` edge `0.109` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3902` n `54` status `ready` deltaP `16.6215` edge `0.2066` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.129` n `54` status `ready` deltaP `10.1965` edge `0.0729` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5538` n `54` status `ready` deltaP `7.6514` edge `0.024` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2249` n `54` status `ready` deltaP `8.045` edge `0.0033` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0305` n `54` status `ready` deltaP `3.7037` edge `0.0131` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4144` n `54` status `ready` deltaP `5.3748` edge `0.0068` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1995` n `54` status `ready` deltaP `-9.2593` edge `-0.043` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.3282` n `46` status `ready` deltaP `-19.2557` edge `-0.0443` maxDD `-4.3746`
- `news_risk_high->metal_24h` score `-5.8006` n `46` status `ready` deltaP `-20.8787` edge `-0.0761` maxDD `-10.4475`
- `news_risk_high->commodity_4h` score `-9.0367` n `54` status `ready` deltaP `-32.7913` edge `-0.2037` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.939` n `46` status `ready` deltaP `-25.0679` edge `-0.3409` maxDD `-25.6187`
- `news_risk_high->commodity_24h` score `-12.9612` n `46` status `ready` deltaP `-14.4852` edge `-0.3998` maxDD `-33.0322`
- `news_risk_high->equity_24h` score `-34.9398` n `46` status `ready` deltaP `-24.1998` edge `-1.1705` maxDD `-113.052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
