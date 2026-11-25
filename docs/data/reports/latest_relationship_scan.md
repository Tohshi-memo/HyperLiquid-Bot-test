# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T11:07:30.708063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3972`

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

- `market_context_high->unknown_1h` score `32223.0889` n `45` status `ready` deltaP `2.3153` edge `2685.2514` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21962.9653` n `45` status `ready` deltaP `3.1776` edge `1830.2398` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `988.1339` n `31` status `ready` deltaP `2.5304` edge `82.3452` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `710.0178` n `31` status `ready` deltaP `4.3962` edge `59.1445` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `658.3427` n `31` status `ready` deltaP `5.7292` edge `54.8237` maxDD `0.0`
- `news_risk_high->equity_24h` score `42.714` n `31` status `ready` deltaP `48.0903` edge `3.2389` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.4639` n `31` status `ready` deltaP `50.1736` edge `3.0375` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.3264` n `31` status `ready` deltaP `52.4306` edge `2.761` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8541` n `31` status `ready` deltaP `27.3701` edge `0.8924` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.6043` n `31` status `ready` deltaP `41.2355` edge `0.7196` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2747` n `31` status `ready` deltaP `37.682` edge `0.7364` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5703` n `31` status `ready` deltaP `18.9123` edge `0.9862` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.712` n `31` status `ready` deltaP `48.7847` edge `0.2341` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1356` n `31` status `ready` deltaP `43.274` edge `0.1523` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0206` n `31` status `ready` deltaP `20.7359` edge `0.2155` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3832` n `31` status `ready` deltaP `36.1576` edge `0.0669` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7487` n `31` status `ready` deltaP `11.807` edge `0.3198` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.6418` n `45` status `ready` deltaP `32.2222` edge `0.0338` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4444` n `31` status `ready` deltaP `13.1543` edge `0.2614` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
