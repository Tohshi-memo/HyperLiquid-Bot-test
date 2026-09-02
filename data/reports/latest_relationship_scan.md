# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T11:07:28.409549+00:00`
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

- `risk_on_high->unknown_4h` score `7.3598` n `107` status `ready` deltaP `18.391` edge `0.5525` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3598` n `107` status `ready` deltaP `18.391` edge `0.5525` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3942` n `148` status `ready` deltaP `14.2675` edge `0.4239` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.4839` n `107` status `ready` deltaP `23.0075` edge `0.6367` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.4839` n `107` status `ready` deltaP `23.0075` edge `0.6367` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.848` n `107` status `ready` deltaP `3.5215` edge `0.1882` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.848` n `107` status `ready` deltaP `3.5215` edge `0.1882` maxDD `-1.9475`
- `news_risk_high->equity_24h` score `1.459` n `59` status `ready` deltaP `8.9571` edge `0.3101` maxDD `-15.5253`
- `market_context_high->equity_24h` score `1.3561` n `148` status `ready` deltaP `19.2755` edge `0.5286` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1377` n `59` status `ready` deltaP `0.987` edge `0.1229` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.5183` n `148` status `ready` deltaP `2.1323` edge `0.092` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2566` n `59` status `ready` deltaP `11.4019` edge `0.0047` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.1306` n `107` status `ready` deltaP `8.5427` edge `0.0043` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1306` n `107` status `ready` deltaP `8.5427` edge `0.0043` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.1114` n `107` status `ready` deltaP `20.6306` edge `0.0098` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1114` n `107` status `ready` deltaP `20.6306` edge `0.0098` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0617` n `107` status `ready` deltaP `11.3465` edge `0.0035` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0617` n `107` status `ready` deltaP `11.3465` edge `0.0035` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.0787` n `107` status `ready` deltaP `8.4658` edge `0.0164` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.0787` n `107` status `ready` deltaP `8.4658` edge `0.0164` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
