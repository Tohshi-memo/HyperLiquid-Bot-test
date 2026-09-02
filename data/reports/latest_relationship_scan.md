# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T13:07:31.539888+00:00`
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

- `risk_on_high->unknown_4h` score `7.2496` n `107` status `ready` deltaP `17.6288` edge `0.5484` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2496` n `107` status `ready` deltaP `17.6288` edge `0.5484` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.3315` n `147` status `ready` deltaP `13.3628` edge `0.4247` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `5.087` n `107` status `ready` deltaP `24.3964` edge `0.6777` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `5.087` n `107` status `ready` deltaP `24.3964` edge `0.6777` maxDD `-19.9806`
- `news_risk_high->equity_24h` score `2.0621` n `59` status `ready` deltaP `10.346` edge `0.3511` maxDD `-15.5253`
- `risk_on_high->unknown_1h` score `1.7281` n `107` status `ready` deltaP `2.773` edge `0.1832` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7281` n `107` status `ready` deltaP `2.773` edge `0.1832` maxDD `-1.9475`
- `market_context_high->equity_24h` score `1.6413` n `147` status `ready` deltaP `20.3656` edge `0.5579` maxDD `-24.6594`
- `news_risk_high->unknown_1h` score `1.1834` n `64` status `ready` deltaP `3.2841` edge `0.1114` maxDD `-1.1072`
- `market_context_high->unknown_1h` score `0.3994` n `147` status `ready` deltaP `1.1264` edge `0.0888` maxDD `-2.042`
- `news_risk_high->fx_4h` score `0.2772` n `59` status `ready` deltaP `11.5544` edge `0.0054` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.1406` n `107` status `ready` deltaP `21.0879` edge `0.0105` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1406` n `107` status `ready` deltaP `21.0879` edge `0.0105` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `-0.0006` n `107` status `ready` deltaP `10.4483` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0006` n `107` status `ready` deltaP `10.4483` edge `0.0015` maxDD `-1.699`
- `risk_on_high->crypto_alt_24h` score `-0.023` n `107` status `ready` deltaP `14.3124` edge `0.592` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `-0.023` n `107` status `ready` deltaP `14.3124` edge `0.592` maxDD `-42.8959`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
