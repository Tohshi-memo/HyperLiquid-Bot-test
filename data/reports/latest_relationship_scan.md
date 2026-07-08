# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T06:22:26.411940+00:00`
- Price records: `672`
- Market context records: `6059`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11073`

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

- `news_risk_high->fx_24h` score `8.1222` n `30` status `ready` deltaP `72.7431` edge `0.1919` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3233` n `30` status `ready` deltaP `44.7256` edge `0.0667` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `2.4304` n `30` status `ready` deltaP `27.8819` edge `0.0314` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.3232` n `30` status `ready` deltaP `27.8243` edge `0.022` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.695` n `30` status `ready` deltaP `22.6042` edge `0.0111` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.3081` n `206` status `ready` deltaP `7.8794` edge `0.1482` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.9791` n `30` status `ready` deltaP `11.2375` edge `0.0973` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.344` n `30` status `ready` deltaP `6.0679` edge `0.0498` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0937` n `30` status `ready` deltaP `9.2361` edge `0.0376` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.5091` n `206` status `ready` deltaP `0.6075` edge `-0.0008` maxDD `-0.6538`
- `market_context_high->metal_1h` score `-0.5092` n `206` status `ready` deltaP `2.0827` edge `0.0007` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.5457` n `30` status `ready` deltaP `-0.4092` edge `-0.0306` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7541` n `206` status `ready` deltaP `-2.4315` edge `-0.002` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8386` n `206` status `ready` deltaP `4.7003` edge `0.0379` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8625` n `206` status `ready` deltaP `4.2556` edge `0.0363` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0107` n `206` status `ready` deltaP `1.0434` edge `0.0168` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0314` n `30` status `ready` deltaP `-9.2515` edge `-0.0191` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0697` n `206` status `ready` deltaP `0.6308` edge `0.0195` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.2156` n `206` status `ready` deltaP `2.9615` edge `-0.0023` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2315` n `206` status `ready` deltaP `-4.3408` edge `-0.022` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
