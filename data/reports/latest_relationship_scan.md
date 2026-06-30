# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T21:37:41.738871+00:00`
- Price records: `672`
- Market context records: `5288`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `23.8578` n `153` status `ready` deltaP `26.9914` edge `1.8172` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5272` n `153` status `ready` deltaP `25.7353` edge `0.8707` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2771` n `178` status `ready` deltaP `16.7718` edge `0.4087` maxDD `-9.46`
- `market_context_high->equity_24h` score `4.1522` n `153` status `ready` deltaP `19.9653` edge `0.7758` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `4.0537` n `178` status `ready` deltaP `16.6279` edge `0.4562` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.0631` n `178` status `ready` deltaP `10.508` edge `0.1824` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.6893` n `178` status `ready` deltaP `14.6496` edge `0.062` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5589` n `153` status `ready` deltaP `13.3068` edge `0.0474` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3521` n `188` status `ready` deltaP `4.2744` edge `0.097` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2599` n `153` status `ready` deltaP `20.8231` edge `0.058` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.1804` n `188` status `ready` deltaP `5.472` edge `0.1031` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.1697` n `188` status `ready` deltaP `8.1253` edge `0.0565` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0569` n `188` status `ready` deltaP `5.2841` edge `0.0104` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2668` n `178` status `ready` deltaP `7.5209` edge `0.0274` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3395` n `188` status `ready` deltaP `1.8633` edge `0.0074` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3774` n `188` status `ready` deltaP `0.1147` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.718` n `178` status `ready` deltaP `1.3754` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3915` n `188` status `ready` deltaP `-2.7265` edge `-0.006` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.7328` n `178` status `ready` deltaP `-3.9018` edge `0.0042` maxDD `-9.3609`
- `market_context_high->crypto_alt_24h` score `-2.9039` n `153` status `ready` deltaP `13.3476` edge `0.3797` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
