# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T03:52:30.521678+00:00`
- Price records: `672`
- Market context records: `6246`
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

- `news_risk_high->crypto_alt_24h` score `14.2496` n `32` status `ready` deltaP `42.302` edge `0.9202` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1019` n `32` status `ready` deltaP `51.9591` edge `0.1621` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1791` n `32` status `ready` deltaP `43.6738` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.2945` n `32` status `ready` deltaP `15.7102` edge `0.3956` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3116` n `32` status `ready` deltaP `27.8443` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2267` n `192` status `ready` deltaP `2.4108` edge `0.2703` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `2.1843` n `32` status `ready` deltaP `25.0905` edge `0.0353` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8568` n `192` status `ready` deltaP `0.4446` edge `0.405` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3548` n `32` status `ready` deltaP `14.128` edge `0.1262` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7834` n `32` status `ready` deltaP `10.5726` edge `0.0761` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0918` n `192` status `ready` deltaP `19.9008` edge `0.1124` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1684` n `32` status `ready` deltaP `8.8905` edge `0.0063` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3143` n `192` status `ready` deltaP `0.761` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.493` n `192` status `ready` deltaP `4.281` edge `0.027` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.557` n `192` status `ready` deltaP `2.8201` edge `0.0265` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6685` n `192` status `ready` deltaP `-1.9461` edge `0.0019` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7636` n `32` status `ready` deltaP `-3.4431` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.834` n `192` status `ready` deltaP `1.7652` edge `-0.0014` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8803` n `192` status `ready` deltaP `4.8434` edge `0.0301` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9449` n `192` status `ready` deltaP `4.2322` edge `0.0274` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
