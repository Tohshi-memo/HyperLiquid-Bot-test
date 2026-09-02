# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T13:22:25.149920+00:00`
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

- `risk_on_high->unknown_4h` score `7.2484` n `107` status `ready` deltaP `17.6288` edge `0.5483` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2484` n `107` status `ready` deltaP `17.6288` edge `0.5483` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3303` n `147` status `ready` deltaP `13.3628` edge `0.4246` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `5.1585` n `107` status `ready` deltaP `24.57` edge `0.6825` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `5.1585` n `107` status `ready` deltaP `24.57` edge `0.6825` maxDD `-19.9806`
- `news_risk_high->equity_24h` score `2.1336` n `59` status `ready` deltaP `10.5196` edge `0.3559` maxDD `-15.5253`
- `risk_on_high->unknown_1h` score `1.7281` n `107` status `ready` deltaP `2.773` edge `0.1832` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7281` n `107` status `ready` deltaP `2.773` edge `0.1832` maxDD `-1.9475`
- `market_context_high->equity_24h` score `1.6878` n `147` status `ready` deltaP `20.5392` edge `0.5627` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.0182` n `65` status `ready` deltaP `2.2985` edge `0.1042` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.3994` n `147` status `ready` deltaP `1.1264` edge `0.0888` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2784` n `59` status `ready` deltaP `11.5544` edge `0.0055` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1398` n `107` status `ready` deltaP `21.0879` edge `0.0104` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->crypto_alt_24h` score `0.0164` n `107` status `ready` deltaP `14.486` edge `0.5959` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.0164` n `107` status `ready` deltaP `14.486` edge `0.5959` maxDD `-42.8959`
- `risk_on_high->metal_1h` score `-0.0108` n `107` status `ready` deltaP `10.2986` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0108` n `107` status `ready` deltaP `10.2986` edge `0.0012` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
