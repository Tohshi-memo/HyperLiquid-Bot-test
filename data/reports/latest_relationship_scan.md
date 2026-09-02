# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T07:37:23.665299+00:00`
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

- `risk_on_high->unknown_4h` score `7.4785` n `107` status `ready` deltaP `19.3056` edge `0.5563` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4785` n `107` status `ready` deltaP `19.3056` edge `0.5563` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.513` n `148` status `ready` deltaP `15.1821` edge `0.4277` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `3.2011` n `107` status `ready` deltaP `20.577` edge `0.546` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `3.2011` n `107` status `ready` deltaP `20.577` edge `0.546` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.8337` n `107` status `ready` deltaP `3.0724` edge `0.19` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8337` n `107` status `ready` deltaP `3.0724` edge `0.19` maxDD `-1.9475`
- `news_risk_high->unknown_1h` score `1.1234` n `59` status `ready` deltaP `0.5379` edge `0.1247` maxDD `-1.1072`
- `market_context_high->equity_24h` score `0.5223` n `148` status `ready` deltaP `16.845` edge `0.4379` maxDD `-24.6594`
- `market_context_high->unknown_1h` score `0.504` n `148` status `ready` deltaP `1.6832` edge `0.0938` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.23` n `59` status `ready` deltaP `11.2495` edge `0.0035` maxDD `-0.7461`
- `news_risk_high->equity_24h` score `0.1761` n `59` status `ready` deltaP `6.5266` edge `0.2194` maxDD `-15.5253`
- `risk_on_high->index_1h` score `0.094` n `107` status `ready` deltaP `7.9439` edge `0.0036` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.094` n `107` status `ready` deltaP `7.9439` edge `0.0036` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0592` n `107` status `ready` deltaP `19.8684` edge `0.0082` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0592` n `107` status `ready` deltaP `19.8684` edge `0.0082` maxDD `-3.6448`
- `risk_on_high->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0585` n `107` status `ready` deltaP `11.3465` edge `0.0031` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.1628` n `107` status `ready` deltaP `7.5676` edge `0.0116` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1628` n `107` status `ready` deltaP `7.5676` edge `0.0116` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
