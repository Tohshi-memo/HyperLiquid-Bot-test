# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T19:52:37.641445+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9717`

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

- `market_context_high->unknown_1h` score `85.8031` n `47` status `ready` deltaP `10.116` edge `7.0899` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `44.9333` n `47` status `ready` deltaP `30.4226` edge `3.5809` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.9212` n `47` status `ready` deltaP `24.782` edge `2.3662` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.8842` n `47` status `ready` deltaP `31.117` edge `1.9018` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8334` n `47` status `ready` deltaP `34.7628` edge `0.434` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9634` n `47` status `ready` deltaP `33.8431` edge `0.1285` maxDD `-0.2401`
- `news_risk_high->unknown_1h` score `3.8286` n `111` status `ready` deltaP `-4.5476` edge `0.3738` maxDD `-0.9543`
- `news_risk_high->crypto_alt_1h` score `3.4735` n `111` status `ready` deltaP `16.6937` edge `0.2272` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9303` n `47` status `ready` deltaP `33.569` edge `0.0358` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.7438` n `111` status `ready` deltaP `17.8886` edge `0.1529` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.5321` n `106` status `ready` deltaP `8.8558` edge `0.3971` maxDD `-15.9436`
- `news_risk_high->crypto_major_4h` score `2.5073` n `106` status `ready` deltaP `16.4692` edge `0.3123` maxDD `-13.719`
- `market_context_high->equity_4h` score `2.3975` n `47` status `ready` deltaP `17.1445` edge `0.1273` maxDD `-1.3444`
- `news_risk_high->crypto_major_24h` score `2.3185` n `83` status `ready` deltaP `-2.9534` edge `1.2212` maxDD `-63.6743`
- `news_risk_high->commodity_24h` score `1.9966` n `83` status `ready` deltaP `21.5006` edge `0.0912` maxDD `-1.7857`
- `news_risk_high->fx_4h` score `1.7139` n `106` status `ready` deltaP `24.6031` edge `0.0424` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.6028` n `111` status `ready` deltaP `20.2622` edge `0.027` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9858` n `47` status `ready` deltaP `14.9095` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9354` n `47` status `ready` deltaP `11.6161` edge `0.0408` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8536` n `83` status `ready` deltaP `23.2304` edge `0.0994` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
