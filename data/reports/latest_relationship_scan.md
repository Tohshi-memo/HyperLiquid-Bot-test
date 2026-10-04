# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T06:37:26.039554+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `265.185` n `56` status `ready` deltaP `7.1864` edge `22.0652` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `205.0523` n `68` status `ready` deltaP `1.3121` edge `17.1204` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.5655` n `46` status `ready` deltaP `32.4279` edge `1.1249` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.2624` n `46` status `ready` deltaP `38.8704` edge `0.9113` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.3376` n `59` status `ready` deltaP `29.2688` edge `0.7597` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.1012` n `65` status `ready` deltaP `40.1736` edge `0.6776` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5674` n `65` status `ready` deltaP `24.6646` edge `0.6006` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1463` n `56` status `ready` deltaP `19.2945` edge `0.4539` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.8339` n `59` status `ready` deltaP `32.9289` edge `0.1833` maxDD `0.0`
- `market_context_high->equity_24h` score `4.3635` n `46` status `ready` deltaP `9.9615` edge `0.3969` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9361` n `65` status `ready` deltaP `27.1318` edge `0.2084` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.2563` n `56` status `ready` deltaP `17.8789` edge `0.4272` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1684` n `65` status `ready` deltaP `34.5052` edge `0.0602` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9831` n `65` status `ready` deltaP `13.1598` edge `0.1964` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.5807` n `68` status `ready` deltaP `16.1236` edge `0.1526` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1213` n `65` status `ready` deltaP `26.0663` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0526` n `68` status `ready` deltaP `11.1131` edge `0.1716` maxDD `-3.6376`
- `market_context_high->fx_4h` score `2.0526` n `56` status `ready` deltaP `24.6516` edge `0.0341` maxDD `-0.1916`
- `news_risk_high->crypto_alt_1h` score `1.5367` n `65` status `ready` deltaP `4.8687` edge `0.1475` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
