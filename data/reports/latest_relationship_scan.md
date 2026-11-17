# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T18:07:44.161392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1494.4784` n `98` status `ready` deltaP `3.4602` edge `124.5168` maxDD `0.0`
- `news_risk_high->equity_24h` score `61.5872` n `44` status `ready` deltaP `68.0245` edge `4.7494` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `19.911` n `44` status `ready` deltaP `54.878` edge `1.2934` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.7377` n `44` status `ready` deltaP `36.4973` edge `2.2733` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.993` n `98` status `ready` deltaP `45.078` edge `1.9487` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.2017` n `98` status `ready` deltaP `31.1384` edge `1.8255` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.6093` n `44` status `ready` deltaP `59.374` edge `0.4353` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.9365` n `44` status `ready` deltaP `20.9343` edge `1.4567` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.3817` n `44` status `ready` deltaP `54.6713` edge `0.334` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3022` n `44` status `ready` deltaP `34.2849` edge `0.54` maxDD `-4.137`
- `news_risk_high->crypto_major_4h` score `7.6648` n `44` status `ready` deltaP `27.6191` edge `0.4973` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6139` n `44` status `ready` deltaP `54.7395` edge `0.1907` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.3779` n `44` status `ready` deltaP `25.2722` edge `0.3022` maxDD `-0.4683`
- `news_risk_high->index_4h` score `4.4089` n `44` status `ready` deltaP `38.7888` edge `0.1313` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.6625` n `44` status `ready` deltaP `21.9515` edge `0.194` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.1321` n `44` status `ready` deltaP `21.0261` edge `0.1735` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.9606` n `44` status `ready` deltaP `31.3748` edge `0.0629` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.6776` n `44` status `ready` deltaP `28.7697` edge `0.0531` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.7635` n `44` status `ready` deltaP `20.8764` edge `0.0297` maxDD `-0.0869`
- `news_risk_high->metal_24h` score `0.3774` n `44` status `ready` deltaP `13.9746` edge `0.1725` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
