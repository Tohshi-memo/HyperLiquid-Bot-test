# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T09:52:31.423521+00:00`
- Price records: `672`
- Market context records: `6272`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11084`

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

- `news_risk_high->crypto_alt_24h` score `15.1225` n `32` status `ready` deltaP `43.058` edge `0.9879` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9285` n `32` status `ready` deltaP `50.346` edge `0.1584` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2061` n `32` status `ready` deltaP `44.1311` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9903` n `32` status `ready` deltaP `16.4901` edge `0.4796` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4708` n `32` status `ready` deltaP `25.5515` edge `0.0561` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2961` n `32` status `ready` deltaP `27.6946` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8732` n `202` status `ready` deltaP `1.9669` edge `0.2438` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3174` n `32` status `ready` deltaP `13.5292` edge `0.1254` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2725` n `192` status `ready` deltaP `-1.3847` edge `0.3685` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7896` n `32` status `ready` deltaP `10.5726` edge `0.0769` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0105` n `192` status `ready` deltaP `5.564` edge `0.0555` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1652` n `32` status `ready` deltaP `9.1912` edge `0.0047` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3175` n `202` status `ready` deltaP `0.7144` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3657` n `192` status `ready` deltaP `16.8235` edge `0.0978` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4385` n `192` status `ready` deltaP `5.0432` edge `0.0289` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5859` n `202` status `ready` deltaP `-0.7944` edge `0.0025` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.671` n `32` status `ready` deltaP `-1.9461` edge `-0.0233` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7306` n `202` status `ready` deltaP `6.6431` edge `0.0373` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8433` n `202` status `ready` deltaP `4.8349` edge `0.0364` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.8657` n `202` status `ready` deltaP `1.5192` edge `-0.0024` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
