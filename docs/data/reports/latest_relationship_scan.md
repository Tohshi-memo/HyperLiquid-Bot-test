# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T14:52:38.820944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11516`

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

- `risk_on_high->unknown_4h` score `7.0742` n `107` status `ready` deltaP `16.8666` edge `0.5389` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.0742` n `107` status `ready` deltaP `16.8666` edge `0.5389` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.4759` n `107` status `ready` deltaP `25.6117` edge `0.7001` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.4759` n `107` status `ready` deltaP `25.6117` edge `0.7001` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.1548` n `147` status `ready` deltaP `12.6006` edge `0.4151` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.4761` n `59` status `ready` deltaP `11.5613` edge `0.376` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.9048` n `147` status `ready` deltaP `21.5809` edge `0.5812` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6534` n `107` status `ready` deltaP `2.4736` edge `0.179` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6534` n `107` status `ready` deltaP `2.4736` edge `0.179` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `1.076` n `66` status `ready` deltaP `2.5586` edge `0.1073` maxDD `-1.1086`
- `market_context_high->unknown_1h` score `0.3235` n `147` status `ready` deltaP `0.827` edge `0.0845` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.3196` n `59` status `ready` deltaP `11.8593` edge `0.0069` maxDD `-0.7461`
- `risk_on_high->crypto_alt_24h` score `0.3054` n `107` status `ready` deltaP `15.5277` edge `0.626` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.3054` n `107` status `ready` deltaP `15.5277` edge `0.626` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.2764` n `59` status `ready` deltaP `15.4485` edge `0.2259` maxDD `-19.4761`
- `risk_on_high->index_4h` score `0.1305` n `107` status `ready` deltaP `21.0879` edge `0.0092` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1305` n `107` status `ready` deltaP `21.0879` edge `0.0092` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0917` n `107` status `ready` deltaP `7.9439` edge `0.0033` maxDD `-0.5605`
- `news_risk_high->index_1h` score `-0.0456` n `66` status `ready` deltaP `4.5455` edge `-0.0008` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
