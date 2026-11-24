# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T15:37:27.445405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4278`

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

- `market_context_high->unknown_1h` score `32276.7567` n `45` status `ready` deltaP `1.5668` edge `2689.7287` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22111.5774` n `45` status `ready` deltaP `2.5678` edge `1842.6282` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1067.2273` n `31` status `ready` deltaP `1.7819` edge `88.9413` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `876.2243` n `31` status `ready` deltaP `3.7864` edge `72.9991` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.9828` n `31` status `ready` deltaP `49.3056` edge `2.7532` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.9348` n `31` status `ready` deltaP `40.625` edge `2.6404` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.1372` n `31` status `ready` deltaP `46.875` edge `2.3656` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.0882` n `31` status `ready` deltaP `41.2355` edge `0.6766` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9272` n `31` status `ready` deltaP `24.1689` edge `0.8365` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1961` n `31` status `ready` deltaP `32.499` edge `0.5979` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.7162` n `31` status `ready` deltaP `15.1013` edge `0.9021` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.4781` n `31` status `ready` deltaP `54.3851` edge `0.1901` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.1334` n `31` status `ready` deltaP `38.3681` edge `0.172` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3836` n `31` status `ready` deltaP `18.4904` edge `0.1774` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9413` n `45` status `ready` deltaP `35.5759` edge `0.0364` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8806` n `31` status `ready` deltaP `31.5844` edge `0.0555` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5732` n `31` status `ready` deltaP `11.5076` edge `0.2993` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5189` n `31` status `ready` deltaP `30.0464` edge `0.0181` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.245` n `31` status `ready` deltaP `11.2082` edge `0.2488` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6256` n `31` status `ready` deltaP `30.7803` edge `0.0311` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
