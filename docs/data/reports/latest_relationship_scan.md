# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T13:52:24.206985+00:00`
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

- `risk_on_high->unknown_4h` score `7.19` n `107` status `ready` deltaP `17.3239` edge `0.5455` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.19` n `107` status `ready` deltaP `17.3239` edge `0.5455` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `5.2706` n `147` status `ready` deltaP `13.0579` edge `0.4217` maxDD `-2.563`
- `risk_on_high->equity_24h` score `5.2512` n `107` status `ready` deltaP `24.9173` edge `0.686` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.2512` n `107` status `ready` deltaP `24.9173` edge `0.686` maxDD `-19.828`
- `news_risk_high->equity_24h` score `2.2513` n `59` status `ready` deltaP `10.8669` edge `0.3619` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.7587` n `147` status `ready` deltaP `20.8865` edge `0.5671` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.7169` n `107` status `ready` deltaP `2.773` edge `0.1823` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.7169` n `107` status `ready` deltaP `2.773` edge `0.1823` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.006` n `65` status `ready` deltaP `2.2985` edge `0.1032` maxDD `-1.1086`
- `market_context_high->unknown_1h` score `0.387` n `147` status `ready` deltaP `1.1264` edge `0.0878` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.2966` n `59` status `ready` deltaP `11.7068` edge `0.006` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.1383` n `107` status `ready` deltaP `21.0879` edge `0.0102` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1383` n `107` status `ready` deltaP `21.0879` edge `0.0102` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `risk_on_high->crypto_alt_24h` score `0.0922` n `107` status `ready` deltaP `14.8332` edge `0.6033` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.0922` n `107` status `ready` deltaP `14.8332` edge `0.6033` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.0632` n `59` status `ready` deltaP `14.754` edge `0.2032` maxDD `-19.4761`
- `risk_on_high->metal_1h` score `-0.0357` n `107` status `ready` deltaP `9.9992` edge `0.0` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
