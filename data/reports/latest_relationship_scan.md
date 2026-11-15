# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T06:22:26.529911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9714`

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

- `market_context_high->unknown_24h` score `546.6897` n `66` status `ready` deltaP `2.4263` edge `45.5413` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.3346` n `51` status `ready` deltaP `47.1064` edge `3.3678` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.0899` n `66` status `ready` deltaP `42.6501` edge `3.044` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.1972` n `66` status `ready` deltaP `57.8121` edge `2.2387` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.9294` n `51` status `ready` deltaP `45.2509` edge `2.7588` maxDD `-7.3315`
- `news_risk_high->equity_4h` score `12.0144` n `51` status `ready` deltaP `38.4636` edge `0.8578` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.5117` n `66` status `ready` deltaP `44.7639` edge `0.3367` maxDD `-0.0653`
- `news_risk_high->crypto_alt_24h` score `7.3896` n `51` status `ready` deltaP `16.1009` edge `1.2906` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `7.3476` n `51` status `ready` deltaP `49.74` edge `0.2807` maxDD `0.0`
- `news_risk_high->index_24h` score `6.255` n `51` status `ready` deltaP `40.575` edge `0.2811` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.9222` n `66` status `ready` deltaP `55.9057` edge `0.4757` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.3157` n `51` status `ready` deltaP `22.1237` edge `0.4376` maxDD `-9.036`
- `news_risk_high->metal_4h` score `5.0269` n `51` status `ready` deltaP `45.6352` edge `0.1523` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7606` n `51` status `ready` deltaP `28.3105` edge `0.3583` maxDD `-9.6921`
- `news_risk_high->equity_1h` score `3.7902` n `51` status `ready` deltaP `19.5257` edge `0.2487` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4728` n `51` status `ready` deltaP `31.9724` edge `0.1016` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `2.7821` n `66` status `ready` deltaP `12.6306` edge `1.1802` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.6003` n `51` status `ready` deltaP `25.9379` edge `0.0831` maxDD `-0.813`
- `news_risk_high->metal_1h` score `2.3343` n `51` status `ready` deltaP `26.7406` edge `0.0417` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3101` n `51` status `ready` deltaP `17.4152` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
