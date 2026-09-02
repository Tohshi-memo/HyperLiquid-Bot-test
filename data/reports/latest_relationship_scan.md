# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T12:07:24.021741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.2992` n `107` status `ready` deltaP `17.9337` edge `0.5505` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2992` n `107` status `ready` deltaP `17.9337` edge `0.5505` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3337` n `148` status `ready` deltaP `13.8102` edge `0.4219` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `4.8155` n `107` status `ready` deltaP `23.702` edge `0.6597` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `4.8155` n `107` status `ready` deltaP `23.702` edge `0.6597` maxDD `-19.9806`
- `news_risk_high->equity_24h` score `1.7905` n `59` status `ready` deltaP `9.6516` edge `0.3331` maxDD `-15.5253`
- `risk_on_high->unknown_1h` score `1.7605` n `107` status `ready` deltaP `2.9227` edge `0.1849` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7605` n `107` status `ready` deltaP `2.9227` edge `0.1849` maxDD `-1.9475`
- `market_context_high->equity_24h` score `1.5716` n `148` status `ready` deltaP `19.97` edge `0.5516` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1046` n `60` status `ready` deltaP `1.038` edge `0.1198` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.4308` n `148` status `ready` deltaP `1.5335` edge `0.0887` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2736` n `59` status `ready` deltaP `11.5544` edge `0.0051` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.1181` n `107` status `ready` deltaP `8.393` edge `0.0037` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1181` n `107` status `ready` deltaP `8.393` edge `0.0037` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0352` n `107` status `ready` deltaP `11.0471` edge `0.0021` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0352` n `107` status `ready` deltaP `11.0471` edge `0.0021` maxDD `-1.699`
- `market_context_high->commodity_1h` score `-0.107` n `148` status `ready` deltaP `7.1492` edge `0.0084` maxDD `-1.5315`
- `news_risk_high->index_1h` score `-0.1102` n `60` status `ready` deltaP `3.7824` edge `-0.004` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
