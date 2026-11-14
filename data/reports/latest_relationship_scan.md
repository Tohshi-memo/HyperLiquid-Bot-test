# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T18:37:24.477850+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `576.2987` n `66` status `ready` deltaP `4.5139` edge `47.9948` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.987` n `53` status `ready` deltaP `42.5217` edge `3.1194` maxDD `-3.6503`
- `market_context_high->equity_24h` score `36.2333` n `66` status `ready` deltaP `37.5474` edge `2.9233` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `24.9026` n `66` status `ready` deltaP `57.7652` edge `1.7978` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `18.0517` n `53` status `ready` deltaP `42.9114` edge `2.2248` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.5415` n `53` status `ready` deltaP `37.3072` edge `0.8261` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3993` n `53` status `ready` deltaP `51.7361` edge `0.2717` maxDD `0.0`
- `market_context_high->index_24h` score `7.132` n `66` status `ready` deltaP `41.3825` edge `0.3276` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.774` n `53` status `ready` deltaP `37.6375` edge `0.2606` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2953` n `66` status `ready` deltaP `51.5152` edge `0.4246` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9275` n `53` status `ready` deltaP `45.9388` edge `0.142` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.8332` n `53` status `ready` deltaP `21.0481` edge `0.4112` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.7782` n `53` status `ready` deltaP `20.4101` edge `0.2418` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5447` n `53` status `ready` deltaP `32.9614` edge `0.101` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.3455` n `53` status `ready` deltaP `14.4261` edge `0.7833` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.7587` n `53` status `ready` deltaP `27.2607` edge `0.3358` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4914` n `53` status `ready` deltaP `25.7766` edge `0.0794` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2673` n `53` status `ready` deltaP `26.3388` edge `0.0388` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4143` n `53` status `ready` deltaP `18.8227` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9963` n `53` status `ready` deltaP `19.2407` edge `0.0974` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
