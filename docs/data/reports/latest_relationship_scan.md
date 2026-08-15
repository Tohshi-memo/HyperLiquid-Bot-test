# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T22:52:26.346481+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `125.5723` n `109` status `ready` deltaP `-27.3353` edge `16.5496` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.7452` n `32` status `ready` deltaP `-37.5704` edge `4.6518` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7452` n `32` status `ready` deltaP `-37.5704` edge `4.6518` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9779` n `36` status `ready` deltaP `26.6609` edge `0.9417` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6981` n `36` status `ready` deltaP `39.4817` edge `0.3783` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.6773` n `109` status `ready` deltaP `37.3332` edge `0.3133` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.5766` n `32` status `ready` deltaP `39.1681` edge `0.2036` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5766` n `32` status `ready` deltaP `39.1681` edge `0.2036` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0298` n `32` status `ready` deltaP `27.6809` edge `0.4477` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0298` n `32` status `ready` deltaP `27.6809` edge `0.4477` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.8239` n `36` status `ready` deltaP `32.409` edge `0.1026` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.939` n `32` status `ready` deltaP `21.1128` edge `0.1224` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.939` n `32` status `ready` deltaP `21.1128` edge `0.1224` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2643` n `109` status `ready` deltaP `20.9695` edge `0.096` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.029` n `36` status `ready` deltaP `23.4248` edge `0.0261` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.8113` n `36` status `ready` deltaP `9.032` edge `0.1226` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.412` n `32` status `ready` deltaP `15.1572` edge `0.0399` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.412` n `32` status `ready` deltaP `15.1572` edge `0.0399` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7895` n `32` status `ready` deltaP `15.2026` edge `0.1778` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7895` n `32` status `ready` deltaP `15.2026` edge `0.1778` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
