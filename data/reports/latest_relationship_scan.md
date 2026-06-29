# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T10:37:31.691056+00:00`
- Price records: `672`
- Market context records: `5136`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `29.0998` n `63` status `ready` deltaP `29.3155` edge `2.2638` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `7.3713` n `132` status `ready` deltaP `9.5582` edge `0.6147` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3585` n `120` status `ready` deltaP `20.2845` edge `0.5802` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.046` n `120` status `ready` deltaP `14.8069` edge `0.4817` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.586` n `120` status `ready` deltaP `12.6118` edge `0.444` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.5842` n `63` status `ready` deltaP `20.2381` edge `0.154` maxDD `-4.1987`
- `market_context_high->crypto_alt_1h` score `0.8516` n `132` status `ready` deltaP `6.0334` edge `0.1269` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.8074` n `132` status `ready` deltaP `8.4195` edge `0.1357` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.8035` n `120` status `ready` deltaP `8.3435` edge `0.1752` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.6789` n `132` status `ready` deltaP `7.5576` edge `0.0655` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.0312` n `63` status `ready` deltaP `0.9424` edge `0.1973` maxDD `-11.4122`
- `market_context_high->index_1h` score `-0.0177` n `132` status `ready` deltaP `5.1443` edge `0.0146` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1146` n `132` status `ready` deltaP `4.1825` edge `0.014` maxDD `-1.8592`
- `market_context_high->index_4h` score `-0.4576` n `120` status `ready` deltaP `5.6402` edge `0.036` maxDD `-2.9391`
- `market_context_high->crypto_alt_24h` score `-0.5117` n `63` status `ready` deltaP `15.4513` edge `0.5327` maxDD `-50.438`
- `market_context_high->commodity_1h` score `-0.5269` n `132` status `ready` deltaP `1.3473` edge `0.0004` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5697` n `120` status `ready` deltaP `2.3984` edge `0.052` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6463` n `132` status `ready` deltaP `-2.5903` edge `-0.0015` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-1.0042` n `120` status `ready` deltaP `-3.2622` edge `0.0003` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.1103` n `63` status `ready` deltaP `0.6449` edge `-0.0053` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
