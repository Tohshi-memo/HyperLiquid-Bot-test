# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T20:52:25.639104+00:00`
- Price records: `672`
- Market context records: `6217`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.151` n `32` status `ready` deltaP `42.2194` edge `0.8292` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5318` n `32` status `ready` deltaP `56.4626` edge `0.1679` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1123` n `32` status `ready` deltaP `43.064` edge `0.0602` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.461` n `32` status `ready` deltaP `15.625` edge `0.2893` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.874` n `192` status `ready` deltaP `1.6623` edge `0.2459` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4093` n `32` status `ready` deltaP `14.4274` edge `0.1312` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.125` n `32` status `ready` deltaP `20.4294` edge `-0.0219` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7655` n `32` status `ready` deltaP `10.1235` edge `0.0768` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3751` n `192` status `ready` deltaP `-2.1469` edge `0.2988` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0439` n `192` status `ready` deltaP `19.8023` edge `0.1192` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.237` n `32` status `ready` deltaP `8.801` edge `-0.0019` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5703` n `192` status `ready` deltaP `-0.7485` edge `0.0021` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6954` n `192` status `ready` deltaP `2.9091` edge `0.0102` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7823` n `32` status `ready` deltaP `-3.4431` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8628` n `192` status `ready` deltaP `1.7652` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.8903` n `192` status `ready` deltaP `4.5316` edge `0.0324` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8982` n `192` status `ready` deltaP `4.3943` edge `0.0308` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1141` n `192` status `ready` deltaP `-2.863` edge `-0.0122` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
