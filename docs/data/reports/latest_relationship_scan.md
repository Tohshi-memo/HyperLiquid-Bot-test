# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T14:37:38.507099+00:00`
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

- `market_context_high->unknown_1h` score `32288.6355` n `45` status `ready` deltaP `1.5668` edge `2690.7186` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22113.3786` n `45` status `ready` deltaP `2.5678` edge `1842.7783` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1079.1061` n `31` status `ready` deltaP `1.7819` edge `89.9312` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `878.0255` n `31` status `ready` deltaP `3.7864` edge `73.1492` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.54` n `31` status `ready` deltaP `49.3056` edge `2.7163` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.5722` n `31` status `ready` deltaP `40.2778` edge `2.6125` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.7148` n `31` status `ready` deltaP `46.875` edge `2.3304` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.1038` n `31` status `ready` deltaP `41.2355` edge `0.6779` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.95` n `31` status `ready` deltaP `24.1689` edge `0.8384` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.1925` n `31` status `ready` deltaP `32.499` edge `0.5976` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.7436` n `31` status `ready` deltaP `15.2537` edge `0.9046` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.5588` n `31` status `ready` deltaP `55.0795` edge `0.1922` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.0654` n `31` status `ready` deltaP `37.8472` edge `0.1698` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4304` n `31` status `ready` deltaP `18.6401` edge `0.1803` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9437` n `45` status `ready` deltaP `35.5759` edge `0.0366` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8952` n `31` status `ready` deltaP `31.7369` edge `0.0557` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6098` n `31` status `ready` deltaP `11.6573` edge `0.303` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5404` n `31` status `ready` deltaP `30.1961` edge `0.0189` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2761` n `31` status `ready` deltaP `11.3579` edge `0.2518` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6217` n `31` status `ready` deltaP `30.7803` edge `0.0306` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
