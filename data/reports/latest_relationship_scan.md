# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T20:52:28.226787+00:00`
- Price records: `672`
- Market context records: `6017`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11126`

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

- `news_risk_high->fx_24h` score `7.6681` n `30` status `ready` deltaP `69.2708` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2163` n `30` status `ready` deltaP `43.6585` edge `0.0649` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.4384` n `30` status `ready` deltaP `29.2014` edge `0.1124` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1809` n `211` status `ready` deltaP `7.8365` edge `0.1547` maxDD `-4.0158`
- `market_context_high->equity_24h` score `0.9953` n `185` status `ready` deltaP `27.6802` edge `0.4882` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8122` n `30` status `ready` deltaP `10.1896` edge `0.0829` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1912` n `30` status `ready` deltaP `5.1697` edge `0.0362` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1351` n `30` status `ready` deltaP `9.2361` edge `0.0429` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3517` n `211` status `ready` deltaP `4.3023` edge `0.0061` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4234` n `30` status `ready` deltaP `1.2375` edge `-0.0259` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.6293` n `211` status `ready` deltaP `0.9848` edge `0.0256` maxDD `-4.3608`
- `market_context_high->fx_1h` score `-0.6661` n `211` status `ready` deltaP `-0.5853` edge `-0.0014` maxDD `-0.6829`
- `market_context_high->commodity_1h` score `-0.6935` n `211` status `ready` deltaP `-1.6339` edge `-0.0005` maxDD `-0.7117`
- `market_context_high->index_24h` score `-0.8595` n `185` status `ready` deltaP `4.0109` edge `0.0644` maxDD `-8.1067`
- `market_context_high->crypto_alt_1h` score `-1.0313` n `211` status `ready` deltaP `3.0054` edge `0.023` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.0371` n `211` status `ready` deltaP `3.2544` edge `0.0221` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0524` n `30` status `ready` deltaP `-9.7006` edge `-0.0188` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0608` n `211` status `ready` deltaP `-2.08` edge `-0.01` maxDD `-2.9703`
- `market_context_high->index_4h` score `-1.0763` n `211` status `ready` deltaP `1.5728` edge `0.0157` maxDD `-2.8004`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
