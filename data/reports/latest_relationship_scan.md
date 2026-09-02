# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T08:07:27.656755+00:00`
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

- `risk_on_high->unknown_4h` score `7.4615` n `107` status `ready` deltaP `19.1532` edge `0.5559` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4615` n `107` status `ready` deltaP `19.1532` edge `0.5559` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.496` n `148` status `ready` deltaP `15.0297` edge `0.4273` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `3.3752` n `107` status `ready` deltaP `20.9242` edge `0.5582` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `3.3752` n `107` status `ready` deltaP `20.9242` edge `0.5582` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8121` n `107` status `ready` deltaP `2.9227` edge `0.1892` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8121` n `107` status `ready` deltaP `2.9227` edge `0.1892` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.1018` n `59` status `ready` deltaP `0.3882` edge `0.1239` maxDD `-1.1072`
- `market_context_high->equity_24h` score `0.6355` n `148` status `ready` deltaP `17.1922` edge `0.4501` maxDD `-24.6594`
- `market_context_high->unknown_1h` score `0.4824` n `148` status `ready` deltaP `1.5335` edge `0.093` maxDD `-2.042`
- `news_risk_high->equity_24h` score `0.3503` n `59` status `ready` deltaP `6.8738` edge `0.2316` maxDD `-15.5253`
- `news_risk_high->fx_4h` score `0.2336` n `59` status `ready` deltaP `11.2495` edge `0.0038` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0854` n `107` status `ready` deltaP `7.7942` edge `0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0854` n `107` status `ready` deltaP `7.7942` edge `0.0035` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1737` n `107` status `ready` deltaP `7.4179` edge `0.0112` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1737` n `107` status `ready` deltaP `7.4179` edge `0.0112` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
