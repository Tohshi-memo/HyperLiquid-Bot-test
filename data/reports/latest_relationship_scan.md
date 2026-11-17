# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T18:37:36.330883+00:00`
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

- `market_context_high->unknown_24h` score `1492.8985` n `98` status `ready` deltaP `3.4662` edge `124.3851` maxDD `0.0`
- `news_risk_high->equity_24h` score `61.1022` n `43` status `ready` deltaP `68.0222` edge `4.709` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.078` n `43` status `ready` deltaP `55.0305` edge `1.3063` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `18.5107` n `43` status `ready` deltaP `36.0002` edge `2.2475` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.0996` n `98` status `ready` deltaP `45.3737` edge `1.9604` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.2974` n `98` status `ready` deltaP `31.4346` edge `1.8358` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.5756` n `43` status `ready` deltaP `59.3567` edge `0.4326` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.6293` n `43` status `ready` deltaP `20.0677` edge `1.4231` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `8.3168` n `43` status `ready` deltaP `34.0613` edge `0.5427` maxDD `-4.137`
- `news_risk_high->commodity_24h` score `8.3125` n `43` status `ready` deltaP `54.766` edge `0.3276` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.4782` n `43` status `ready` deltaP `27.2369` edge `0.4843` maxDD `-1.7491`
- `news_risk_high->metal_4h` score `6.6436` n `43` status `ready` deltaP `54.9915` edge `0.1915` maxDD `-0.0246`
- `news_risk_high->equity_1h` score `5.6381` n `43` status `ready` deltaP `26.8138` edge `0.3129` maxDD `-0.4122`
- `news_risk_high->index_4h` score `4.4228` n `43` status `ready` deltaP `38.677` edge `0.1332` maxDD `-0.1319`
- `news_risk_high->crypto_major_1h` score `3.6051` n `43` status `ready` deltaP `21.4141` edge `0.1928` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `3.0921` n `43` status `ready` deltaP `20.2862` edge `0.1751` maxDD `-2.5469`
- `news_risk_high->commodity_4h` score `2.9166` n `43` status `ready` deltaP `30.8991` edge `0.0624` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.6593` n `43` status `ready` deltaP `28.3909` edge `0.0541` maxDD `-0.0743`
- `news_risk_high->index_1h` score `1.9137` n `43` status `ready` deltaP `22.462` edge `0.0315` maxDD `-0.0751`
- `news_risk_high->metal_24h` score `0.2436` n `43` status `ready` deltaP `12.4824` edge `0.1653` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
