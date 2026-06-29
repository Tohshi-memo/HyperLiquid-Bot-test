# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T17:15:19.700780+00:00`
- Price records: `672`
- Market context records: `5164`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `29.6435` n `64` status `ready` deltaP `33.1597` edge `2.2682` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `5.9116` n `140` status `ready` deltaP `20.0174` edge `0.4614` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `4.6319` n `64` status `ready` deltaP `19.4444` edge `0.8029` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.6276` n `140` status `ready` deltaP `14.6777` edge `0.4477` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `4.4478` n `64` status `ready` deltaP `17.5347` edge `0.8195` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `3.8881` n `140` status `ready` deltaP `13.554` edge `0.4629` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.8181` n `149` status `ready` deltaP `9.9486` edge `0.316` maxDD `-2.7986`
- `market_context_high->commodity_24h` score `1.1175` n `64` status `ready` deltaP `19.2708` edge `0.1492` maxDD `-5.7522`
- `market_context_high->crypto_major_1h` score `0.8212` n `149` status `ready` deltaP `8.0376` edge `0.1394` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7746` n `149` status `ready` deltaP `5.2656` edge `0.1256` maxDD `-5.0257`
- `market_context_high->metal_24h` score `0.7267` n `64` status `ready` deltaP `0.3472` edge `0.2337` maxDD `-6.0945`
- `market_context_high->equity_4h` score `0.5717` n `140` status `ready` deltaP `8.2665` edge `0.1564` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3043` n `149` status `ready` deltaP `7.7231` edge `0.0704` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.037` n `149` status `ready` deltaP `5.0386` edge `0.0137` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.096` n `149` status `ready` deltaP `4.8266` edge `0.0147` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.196` n `149` status `ready` deltaP `2.9428` edge `0.0005` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4147` n `140` status `ready` deltaP `4.4207` edge `0.0291` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4696` n `140` status `ready` deltaP `5.3223` edge `0.0077` maxDD `-1.6047`
- `market_context_high->fx_24h` score `-0.5151` n `64` status `ready` deltaP `6.0764` edge `0.0061` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.5503` n `149` status `ready` deltaP `1.3061` edge `0.0016` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
