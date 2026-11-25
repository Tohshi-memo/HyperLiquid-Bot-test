# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T13:37:22.548453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32207.3029` n `45` status `ready` deltaP `2.0159` edge `2683.9379` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21936.5881` n `45` status `ready` deltaP `3.1776` edge `1828.0417` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `972.348` n `31` status `ready` deltaP `2.231` edge `81.0317` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `683.6406` n `31` status `ready` deltaP `4.3962` edge `56.9464` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `555.2231` n `31` status `ready` deltaP `5.7292` edge `46.2304` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.1105` n `31` status `ready` deltaP `49.8264` edge `3.3437` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.2403` n `31` status `ready` deltaP `51.3889` edge `3.0941` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.9722` n `31` status `ready` deltaP `53.9931` edge `2.8044` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8421` n `31` status `ready` deltaP `27.3701` edge `0.8914` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.783` n `31` status `ready` deltaP `41.2355` edge `0.7345` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1655` n `31` status `ready` deltaP `37.682` edge `0.7273` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4533` n `31` status `ready` deltaP `18.9123` edge `0.9712` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.0057` n `31` status `ready` deltaP `50.5208` edge `0.247` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2563` n `31` status `ready` deltaP `44.6629` edge `0.1531` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9966` n `31` status `ready` deltaP `20.7359` edge `0.2135` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.388` n `31` status `ready` deltaP `36.1576` edge `0.0673` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7455` n `31` status `ready` deltaP `11.807` edge `0.3194` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5358` n `45` status `ready` deltaP `31.0027` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4943` n `31` status `ready` deltaP `13.6034` edge `0.2648` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
