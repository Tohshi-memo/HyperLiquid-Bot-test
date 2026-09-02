# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T07:52:34.477586+00:00`
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

- `risk_on_high->unknown_4h` score `7.4773` n `107` status `ready` deltaP `19.3056` edge `0.5562` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4773` n `107` status `ready` deltaP `19.3056` edge `0.5562` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.5118` n `148` status `ready` deltaP `15.1821` edge `0.4276` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `3.2906` n `107` status `ready` deltaP `20.7506` edge `0.5523` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `3.2906` n `107` status `ready` deltaP `20.7506` edge `0.5523` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8301` n `107` status `ready` deltaP `3.0724` edge `0.1897` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8301` n `107` status `ready` deltaP `3.0724` edge `0.1897` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.1198` n `59` status `ready` deltaP `0.5379` edge `0.1244` maxDD `-1.1072`
- `market_context_high->equity_24h` score `0.5804` n `148` status `ready` deltaP `17.0186` edge `0.4442` maxDD `-24.6594`
- `market_context_high->unknown_1h` score `0.5004` n `148` status `ready` deltaP `1.6832` edge `0.0935` maxDD `-2.042`
- `news_risk_high->equity_24h` score `0.2656` n `59` status `ready` deltaP `6.7002` edge `0.2257` maxDD `-15.5253`
- `news_risk_high->fx_4h` score `0.2324` n `59` status `ready` deltaP `11.2495` edge `0.0037` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0854` n `107` status `ready` deltaP `7.7942` edge `0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0854` n `107` status `ready` deltaP `7.7942` edge `0.0035` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_high->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0585` n `107` status `ready` deltaP `19.8684` edge `0.0081` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1745` n `107` status `ready` deltaP `7.4179` edge `0.0111` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1745` n `107` status `ready` deltaP `7.4179` edge `0.0111` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
