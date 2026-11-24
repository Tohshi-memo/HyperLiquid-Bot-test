# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T12:37:30.446475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4320`

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

- `market_context_high->unknown_1h` score `32326.9491` n `45` status `ready` deltaP `1.5668` edge `2693.9114` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22154.4498` n `45` status `ready` deltaP `2.5678` edge `1846.2009` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1117.4197` n `31` status `ready` deltaP `1.7819` edge `93.124` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `919.0967` n `31` status `ready` deltaP `3.7864` edge `76.5718` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.138` n `31` status `ready` deltaP `49.3056` edge `2.6828` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.629` n `31` status `ready` deltaP `40.9722` edge `2.6126` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.29` n `31` status `ready` deltaP `46.875` edge `2.295` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.2245` n `31` status `ready` deltaP `41.4091` edge `0.6868` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.022` n `31` status `ready` deltaP `24.1689` edge `0.8444` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3449` n `31` status `ready` deltaP `32.499` edge `0.6103` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.8646` n `31` status `ready` deltaP `15.4062` edge `0.9191` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.6987` n `31` status `ready` deltaP `56.4684` edge `0.1946` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.1274` n `31` status `ready` deltaP `38.3681` edge `0.1715` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5167` n `31` status `ready` deltaP `18.7898` edge `0.1865` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9509` n `45` status `ready` deltaP `35.5759` edge `0.0372` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8988` n `31` status `ready` deltaP `31.7369` edge `0.056` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6122` n `31` status `ready` deltaP `11.6573` edge `0.3033` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5704` n `31` status `ready` deltaP `30.4955` edge `0.0194` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.287` n `31` status `ready` deltaP `11.5076` edge `0.2522` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6193` n `31` status `ready` deltaP `30.7803` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
