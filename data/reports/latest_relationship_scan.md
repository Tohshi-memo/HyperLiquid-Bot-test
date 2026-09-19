# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T06:37:32.612568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8452`

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

- `news_risk_high->crypto_major_24h` score `58.3622` n `63` status `ready` deltaP `35.4911` edge `4.7161` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `51.818` n `63` status `ready` deltaP `38.5913` edge `4.1988` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0245` n `149` status `ready` deltaP `-1.8354` edge `3.0376` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.2556` n `63` status `ready` deltaP `47.5694` edge `0.7875` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9031` n `52` status `ready` deltaP `-9.076` edge `0.9083` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9031` n `52` status `ready` deltaP `-9.076` edge `0.9083` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2592` n `52` status `ready` deltaP `44.9653` edge `0.3885` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2592` n `52` status `ready` deltaP `44.9653` edge `0.3885` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.3082` n `79` status `ready` deltaP `24.0931` edge `0.561` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.9601` n `149` status `ready` deltaP `38.2539` edge `0.3775` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.9813` n `79` status `ready` deltaP `20.859` edge `0.3935` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `3.907` n `63` status `ready` deltaP `33.2837` edge `0.1254` maxDD `-0.403`
- `news_risk_high->crypto_alt_1h` score `3.3477` n `81` status `ready` deltaP `17.4503` edge `0.2092` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6425` n `81` status `ready` deltaP `20.2188` edge `0.1377` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5346` n `52` status `ready` deltaP `30.2533` edge `0.0445` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5346` n `52` status `ready` deltaP `30.2533` edge `0.0445` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4343` n `149` status `ready` deltaP `26.7556` edge `0.0663` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.3433` n `79` status `ready` deltaP `15.0336` edge `0.0336` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.1215` n `63` status `ready` deltaP `6.3988` edge `0.055` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.039` n `149` status `ready` deltaP `15.4624` edge `0.0212` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
