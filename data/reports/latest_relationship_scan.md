# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T14:22:28.378767+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3804`

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

- `market_context_high->unknown_1h` score `32207.4937` n `45` status `ready` deltaP `2.3153` edge `2683.9518` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21924.3853` n `45` status `ready` deltaP `3.1776` edge `1827.0248` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `972.5387` n `31` status `ready` deltaP `2.5304` edge `81.0456` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `671.4378` n `31` status `ready` deltaP `4.3962` edge `55.9295` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `519.8579` n `31` status `ready` deltaP `5.7292` edge `43.2833` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.5626` n `31` status `ready` deltaP `50.3472` edge `3.3779` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.5484` n `31` status `ready` deltaP `51.9097` edge `3.1163` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.2107` n `31` status `ready` deltaP `54.5139` edge `2.8208` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8697` n `31` status `ready` deltaP `27.3701` edge `0.8937` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.8382` n `31` status `ready` deltaP `41.2355` edge `0.7391` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1619` n `31` status `ready` deltaP `37.682` edge `0.727` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4565` n `31` status `ready` deltaP `18.9123` edge `0.9716` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.0953` n `31` status `ready` deltaP `51.0417` edge `0.251` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3028` n `31` status `ready` deltaP `45.1837` edge `0.1535` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9846` n `31` status `ready` deltaP `20.7359` edge `0.2125` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3916` n `31` status `ready` deltaP `36.1576` edge `0.0676` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7588` n `31` status `ready` deltaP `11.807` edge `0.3211` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.719` n `31` status `ready` deltaP `31.9925` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.5052` n `31` status `ready` deltaP `13.6034` edge `0.2662` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.4956` n `45` status `ready` deltaP `30.5454` edge `0.0328` maxDD `-0.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
