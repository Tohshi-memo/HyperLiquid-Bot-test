# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T03:22:28.071911+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32367.851` n `45` status `ready` deltaP `2.1656` edge `2697.3159` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22228.1074` n `45` status `ready` deltaP `2.8727` edge `1852.337` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1158.3216` n `31` status `ready` deltaP `2.3807` edge `96.5285` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `992.7543` n `31` status `ready` deltaP `4.0913` edge `82.7079` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.5936` n `31` status `ready` deltaP `42.5347` edge `2.7659` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.9471` n `31` status `ready` deltaP `45.8333` edge `2.6067` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7872` n `31` status `ready` deltaP `45.6597` edge `2.2612` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.8436` n `31` status `ready` deltaP `42.2771` edge `0.7326` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.7244` n `31` status `ready` deltaP `24.1689` edge `0.8196` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6635` n `31` status `ready` deltaP `30.8222` edge `0.5647` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.6407` n `31` status `ready` deltaP `14.3391` edge `0.8975` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.6339` n `31` status `ready` deltaP `56.4684` edge `0.1892` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.6095` n `31` status `ready` deltaP `40.1042` edge `0.2001` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.3224` n `31` status `ready` deltaP `18.3407` edge `0.1733` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1966` n `45` status `ready` deltaP `38.1673` edge `0.0404` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.774` n `31` status `ready` deltaP `30.8222` edge `0.0517` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5888` n `31` status `ready` deltaP `11.3579` edge `0.3023` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5009` n `31` status `ready` deltaP `29.8967` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.192` n `31` status `ready` deltaP `10.6094` edge `0.246` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6022` n `31` status `ready` deltaP `30.6306` edge `0.0291` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
