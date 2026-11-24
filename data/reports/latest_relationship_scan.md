# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T14:52:31.880521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4284`

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

- `market_context_high->unknown_1h` score `32284.2999` n `45` status `ready` deltaP `1.5668` edge `2690.3573` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22113.3762` n `45` status `ready` deltaP `2.5678` edge `1842.7781` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1074.7705` n `31` status `ready` deltaP `1.7819` edge `89.5699` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `878.0231` n `31` status `ready` deltaP `3.7864` edge `73.149` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.6252` n `31` status `ready` deltaP `49.3056` edge `2.7234` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.5926` n `31` status `ready` deltaP `40.2778` edge `2.6142` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.8` n `31` status `ready` deltaP `46.875` edge `2.3375` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0942` n `31` status `ready` deltaP `41.2355` edge `0.6771` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.926` n `31` status `ready` deltaP `24.1689` edge `0.8364` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1527` n `31` status `ready` deltaP `32.3466` edge `0.5953` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.7162` n `31` status `ready` deltaP `15.1013` edge `0.9021` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.5389` n `31` status `ready` deltaP `54.9059` edge `0.1917` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.0654` n `31` status `ready` deltaP `37.8472` edge `0.1698` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.368` n `31` status `ready` deltaP `18.4904` edge `0.1761` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9437` n `45` status `ready` deltaP `35.5759` edge `0.0366` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8794` n `31` status `ready` deltaP `31.5844` edge `0.0554` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5732` n `31` status `ready` deltaP `11.5076` edge `0.2993` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5225` n `31` status `ready` deltaP `30.0464` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2395` n `31` status `ready` deltaP `11.2082` edge `0.2481` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6116` n `31` status `ready` deltaP `30.6306` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
