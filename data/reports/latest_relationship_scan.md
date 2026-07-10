# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T02:07:30.638107+00:00`
- Price records: `672`
- Market context records: `6239`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `14.015` n `32` status `ready` deltaP `42.2194` edge `0.9012` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1969` n `32` status `ready` deltaP `52.8912` edge `0.1638` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1865` n `32` status `ready` deltaP `43.8262` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.1279` n `32` status `ready` deltaP `15.625` edge `0.3748` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3092` n `32` status `ready` deltaP `27.8443` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2591` n `192` status `ready` deltaP `2.4108` edge `0.273` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.9496` n `32` status `ready` deltaP `24.0009` edge `0.023` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8712` n `192` status `ready` deltaP `0.4446` edge `0.4062` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3626` n `32` status `ready` deltaP `14.2777` edge `0.1262` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7693` n `32` status `ready` deltaP `10.5726` edge `0.0743` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0681` n `192` status `ready` deltaP `19.8023` edge `0.1161` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1761` n `32` status `ready` deltaP `8.801` edge `0.0059` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3159` n `192` status `ready` deltaP `0.761` edge `-0.001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5226` n `192` status `ready` deltaP `4.281` edge `0.0232` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6709` n `192` status `ready` deltaP `-1.9461` edge `0.0017` maxDD `-0.5708`
- `market_context_high->equity_4h` score `-0.7218` n `192` status `ready` deltaP `2.5152` edge `0.0148` maxDD `-2.671`
- `news_risk_high->metal_1h` score `-0.7901` n `32` status `ready` deltaP `-3.5928` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8748` n `192` status `ready` deltaP `1.6155` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8944` n `192` status `ready` deltaP `4.8434` edge `0.0283` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9371` n `192` status `ready` deltaP `4.3819` edge `0.0274` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
