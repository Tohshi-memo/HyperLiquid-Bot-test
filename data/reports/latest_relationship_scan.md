# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T07:07:26.519159+00:00`
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

- `risk_on_high->unknown_4h` score `7.4955` n `107` status `ready` deltaP `19.4581` edge `0.5567` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4955` n `107` status `ready` deltaP `19.4581` edge `0.5567` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.53` n `148` status `ready` deltaP `15.3346` edge `0.4281` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `3.0197` n `107` status `ready` deltaP `20.2298` edge `0.5332` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `3.0197` n `107` status `ready` deltaP `20.2298` edge `0.5332` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.848` n `107` status `ready` deltaP `3.2221` edge `0.1902` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.848` n `107` status `ready` deltaP `3.2221` edge `0.1902` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.1377` n `59` status `ready` deltaP `0.6876` edge `0.1249` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.5183` n `148` status `ready` deltaP `1.8329` edge `0.094` maxDD `-2.042`
- `market_context_high->equity_24h` score `0.4044` n `148` status `ready` deltaP `16.4978` edge `0.4251` maxDD `-24.6594`
- `news_risk_high->fx_4h` score `0.2276` n `59` status `ready` deltaP `11.2495` edge `0.0033` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1034` n `107` status `ready` deltaP `8.0936` edge `0.0038` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1034` n `107` status `ready` deltaP `8.0936` edge `0.0038` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.068` n `107` status `ready` deltaP `20.0208` edge `0.0083` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.068` n `107` status `ready` deltaP `20.0208` edge `0.0083` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0671` n `107` status `ready` deltaP `11.4962` edge `0.0032` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0671` n `107` status `ready` deltaP `11.4962` edge `0.0032` maxDD `-1.699`
- `news_risk_high->equity_24h` score `-0.0052` n `59` status `ready` deltaP `6.1794` edge `0.2066` maxDD `-15.5253`
- `risk_on_high->equity_1h` score `-0.1504` n `107` status `ready` deltaP `7.7173` edge `0.0122` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1504` n `107` status `ready` deltaP `7.7173` edge `0.0122` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
