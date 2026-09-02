# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T13:37:31.908213+00:00`
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

- `risk_on_high->unknown_4h` score `7.2262` n `107` status `ready` deltaP `17.4764` edge `0.5475` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.2262` n `107` status `ready` deltaP `17.4764` edge `0.5475` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `5.3068` n `147` status `ready` deltaP `13.2104` edge `0.4237` maxDD `-2.563`
- `risk_on_high->equity_24h` score `5.1893` n `107` status `ready` deltaP `24.7437` edge `0.682` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.1893` n `107` status `ready` deltaP `24.7437` edge `0.682` maxDD `-19.828`
- `news_risk_high->equity_24h` score `2.1894` n `59` status `ready` deltaP `10.6933` edge `0.3579` maxDD `-15.4056`
- `risk_on_high->unknown_1h` score `1.7445` n `107` status `ready` deltaP `2.9227` edge `0.1836` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.7445` n `107` status `ready` deltaP `2.9227` edge `0.1836` maxDD `-1.95`
- `market_context_high->equity_24h` score `1.7184` n `147` status `ready` deltaP `20.7129` edge `0.5631` maxDD `-24.4698`
- `news_risk_high->unknown_1h` score `1.0336` n `65` status `ready` deltaP `2.4482` edge `0.1045` maxDD `-1.1086`
- `market_context_high->unknown_1h` score `0.4146` n `147` status `ready` deltaP `1.2761` edge `0.0891` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.2942` n `59` status `ready` deltaP `11.7068` edge `0.0058` maxDD `-0.7461`
- `risk_on_high->index_4h` score `0.139` n `107` status `ready` deltaP `21.0879` edge `0.0103` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.139` n `107` status `ready` deltaP `21.0879` edge `0.0103` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0925` n `107` status `ready` deltaP `7.9439` edge `0.0034` maxDD `-0.5605`
- `risk_on_high->crypto_alt_24h` score `0.0567` n `107` status `ready` deltaP `14.6596` edge `0.5999` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.0567` n `107` status `ready` deltaP `14.6596` edge `0.5999` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.0277` n `59` status `ready` deltaP `14.5804` edge `0.1998` maxDD `-19.4761`
- `risk_on_high->metal_1h` score `-0.0224` n `107` status `ready` deltaP `10.1489` edge `0.0007` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
