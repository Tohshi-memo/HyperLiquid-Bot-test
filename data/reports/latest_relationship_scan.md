# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T00:37:23.649191+00:00`
- Price records: `672`
- Market context records: `3021`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `21.4896` n `99` status `ready` deltaP `9.5959` edge `2.1185` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5621` n `99` status `ready` deltaP `42.3769` edge `0.7884` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `12.5028` n `99` status `ready` deltaP `21.37` edge `0.9459` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.9015` n `99` status `ready` deltaP `20.2494` edge `1.025` maxDD `-18.3486`
- `market_context_high->index_24h` score `6.7706` n `99` status `ready` deltaP `19.839` edge `0.5575` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5447` n `112` status `ready` deltaP `18.6411` edge `0.1525` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6059` n `112` status `ready` deltaP `14.068` edge `0.1748` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.4557` n `112` status `ready` deltaP `24.4991` edge `0.4499` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.1859` n `112` status `ready` deltaP `16.7247` edge `0.1021` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.0223` n `124` status `ready` deltaP `2.4773` edge `0.0276` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3617` n `124` status `ready` deltaP `3.6073` edge `0.0392` maxDD `-5.7692`
- `market_context_high->fx_1h` score `-0.4805` n `124` status `ready` deltaP `-3.8246` edge `0.0005` maxDD `-0.2615`
- `market_context_high->index_1h` score `-0.5404` n `124` status `ready` deltaP `4.6311` edge `0.0255` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.6172` n `124` status `ready` deltaP `6.244` edge `0.0922` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8095` n `124` status `ready` deltaP `4.2641` edge `-0.0228` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-0.9294` n `112` status `ready` deltaP `-0.8275` edge `0.0334` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.0807` n `124` status `ready` deltaP `4.0999` edge `0.0604` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.225` n `124` status `ready` deltaP `-2.9168` edge `-0.0058` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.5666` n `112` status `ready` deltaP `-7.6002` edge `-0.0009` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.7239` n `99` status `ready` deltaP `-4.7506` edge `-0.0248` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
