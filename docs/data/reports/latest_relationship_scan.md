# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T16:07:31.005346+00:00`
- Price records: `672`
- Market context records: `2881`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `8.454` n `142` status `ready` deltaP `7.7367` edge `1.0446` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.8616` n `142` status `ready` deltaP `9.7197` edge `0.3868` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.7157` n `142` status `ready` deltaP `9.0815` edge `0.5328` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.2712` n `142` status `ready` deltaP `11.1062` edge `0.2133` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6992` n `142` status `ready` deltaP `15.5516` edge `0.3473` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.7534` n `142` status `ready` deltaP `6.0331` edge `0.1279` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7328` n `142` status `ready` deltaP `15.435` edge `0.0752` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.008` n `142` status `ready` deltaP `4.6471` edge `0.0174` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0134` n `142` status `ready` deltaP `4.4805` edge `0.0421` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.125` n `142` status `ready` deltaP `4.4014` edge `0.0982` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.6105` n `142` status `ready` deltaP `14.4903` edge `0.2866` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.6194` n `142` status `ready` deltaP `-0.8813` edge `0.0018` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6652` n `142` status `ready` deltaP `-2.0346` edge `0.0025` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6707` n `142` status `ready` deltaP `-0.3163` edge `0.0007` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.6866` n `142` status `ready` deltaP `4.7968` edge `0.056` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.754` n `142` status `ready` deltaP `-1.8512` edge `0.0328` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.7798` n `142` status `ready` deltaP `4.8242` edge `0.0548` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1269` n `142` status `ready` deltaP `3.6671` edge `0.0231` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2905` n `142` status `ready` deltaP `-5.1249` edge `0.0045` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3771` n `142` status `ready` deltaP `-1.8852` edge `-0.015` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
