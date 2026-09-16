# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T20:22:29.712608+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11235`

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

- `news_risk_high->unknown_4h` score `369.4188` n `83` status `ready` deltaP `-20.9007` edge `31.0137` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.7378` n `83` status `ready` deltaP `42.3444` edge `1.4171` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.2312` n `83` status `ready` deltaP `35.105` edge `1.4014` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.5633` n `83` status `ready` deltaP `44.3378` edge `1.0121` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.1098` n `83` status `ready` deltaP `49.7678` edge `0.2783` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.3785` n `52` status `ready` deltaP `38.5417` edge `0.2746` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3785` n `52` status `ready` deltaP `38.5417` edge `0.2746` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.3422` n `83` status `ready` deltaP `32.6849` edge `0.2727` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `5.0794` n `149` status `ready` deltaP `31.8303` edge `0.2636` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.419` n `52` status `ready` deltaP `29.9484` edge `0.0369` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.419` n `52` status `ready` deltaP `29.9484` edge `0.0369` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4132` n `52` status `ready` deltaP `32.1047` edge `-0.0087` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4132` n `52` status `ready` deltaP `32.1047` edge `-0.0087` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.3187` n `149` status `ready` deltaP `26.4507` edge `0.0587` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2783` n `149` status `ready` deltaP `29.3298` edge `0.0159` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9444` n `149` status `ready` deltaP `14.5642` edge `0.0193` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3967` n `83` status `ready` deltaP `12.1933` edge `0.0324` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1879` n `52` status `ready` deltaP `6.8632` edge `0.0089` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
