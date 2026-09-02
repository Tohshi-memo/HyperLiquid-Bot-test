# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T02:22:29.070639+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.4019` n `107` status `ready` deltaP `19.4581` edge `0.5489` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4019` n `107` status `ready` deltaP `19.4581` edge `0.5489` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.9485` n `151` status `ready` deltaP `15.7507` edge `0.4602` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.614` n `107` status `ready` deltaP `3.2221` edge `0.1707` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.614` n `107` status `ready` deltaP `3.2221` edge `0.1707` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.4833` n `151` status `ready` deltaP `2.5846` edge `0.1694` maxDD `-2.042`
- `risk_on_high->equity_24h` score `1.2942` n `107` status `ready` deltaP `16.9312` edge `0.4114` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `1.2942` n `107` status `ready` deltaP `16.9312` edge `0.4114` maxDD `-19.9806`
- `news_risk_high->unknown_1h` score `0.9037` n `59` status `ready` deltaP `0.6876` edge `0.1054` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1549` n `59` status `ready` deltaP `10.6397` edge `0.0013` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1512` n `107` status `ready` deltaP `12.8435` edge `0.005` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1512` n `107` status `ready` deltaP `12.8435` edge `0.005` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0652` n `107` status `ready` deltaP `7.4948` edge `0.0029` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0652` n `107` status `ready` deltaP `7.4948` edge `0.0029` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0333` n `107` status `ready` deltaP `19.5635` edge `0.0069` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0333` n `107` status `ready` deltaP `19.5635` edge `0.0069` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.18` n `107` status `ready` deltaP `7.4179` edge `0.0104` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.18` n `107` status `ready` deltaP `7.4179` edge `0.0104` maxDD `-2.3009`
- `news_risk_high->index_1h` score `-0.2261` n `59` status `ready` deltaP `2.0933` edge `-0.0076` maxDD `-0.8275`
- `risk_on_high->commodity_1h` score `-0.2425` n `107` status `ready` deltaP `2.6275` edge `0.0036` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
