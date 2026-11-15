# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T02:22:28.548583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9372`

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

- `market_context_high->unknown_24h` score `561.66` n `66` status `ready` deltaP `2.4306` edge `46.7888` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.1978` n `53` status `ready` deltaP `44.9522` edge `3.2041` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.4442` n `66` status `ready` deltaP `39.9779` edge `3.008` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `28.9346` n `66` status `ready` deltaP `57.7652` edge `2.1338` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.8952` n `53` status `ready` deltaP `43.0851` edge `2.5882` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8667` n `53` status `ready` deltaP `39.1365` edge `0.841` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2618` n `53` status `ready` deltaP `50.3472` edge `0.2695` maxDD `0.0`
- `market_context_high->index_24h` score `7.2476` n `66` status `ready` deltaP `42.077` edge `0.3326` maxDD `-0.0653`
- `news_risk_high->crypto_major_4h` score `6.1036` n `53` status `ready` deltaP `22.5725` edge `0.5069` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `5.9663` n `53` status `ready` deltaP `14.4261` edge `1.1193` maxDD `-29.0448`
- `news_risk_high->index_24h` score `5.8896` n `53` status `ready` deltaP `38.332` edge `0.2656` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.5899` n `66` status `ready` deltaP `53.2513` edge `0.4508` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0651` n `53` status `ready` deltaP `46.5486` edge `0.1494` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8034` n `53` status `ready` deltaP `20.4101` edge `0.2439` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.416` n `53` status `ready` deltaP `31.7419` edge `0.0984` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.3447` n `53` status `ready` deltaP `27.5655` edge `0.4089` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.484` n `53` status `ready` deltaP `25.6241` edge `0.0798` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2554` n `53` status `ready` deltaP `25.8897` edge `0.0408` maxDD `-0.3692`
- `market_context_high->crypto_major_24h` score `2.1469` n `66` status `ready` deltaP `12.6105` edge `1.1274` maxDD `-76.2717`
- `news_risk_high->index_1h` score `1.3903` n `53` status `ready` deltaP `18.5233` edge `0.0225` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
