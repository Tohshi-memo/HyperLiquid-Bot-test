# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T04:52:27.391837+00:00`
- Price records: `672`
- Market context records: `6357`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->crypto_alt_24h` score `14.9678` n `32` status `ready` deltaP `41.3194` edge `0.9866` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2202` n `32` status `ready` deltaP `51.5625` edge `0.1746` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4647` n `32` status `ready` deltaP `17.7083` edge `0.5323` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7801` n `32` status `ready` deltaP `32.8125` edge `0.1168` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.362` n `32` status `ready` deltaP `28.4431` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5037` n `32` status `ready` deltaP `14.7268` edge `0.1413` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9034` n `32` status `ready` deltaP `11.4708` edge `0.0855` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7284` n `202` status `ready` deltaP `14.693` edge `0.0424` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0392` n `202` status `ready` deltaP `7.305` edge `0.0222` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `-0.0598` n `214` status `ready` deltaP `-7.6305` edge `0.1467` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3843` n `214` status `ready` deltaP `3.8838` edge `0.0026` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5461` n `129` status `ready` deltaP `-4.2757` edge `0.1449` maxDD `-6.2457`
- `market_context_high->index_1h` score `-0.5898` n `214` status `ready` deltaP `-1.0297` edge `0.0032` maxDD `-0.7564`
- `market_context_high->metal_24h` score `-0.649` n `129` status `ready` deltaP `14.7367` edge `0.0754` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.7027` n `32` status `ready` deltaP `0.5208` edge `-0.0064` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7275` n `32` status `ready` deltaP `5.4828` edge `-0.0627` maxDD `-0.7581`
- `market_context_high->fx_1h` score `-0.7642` n `214` status `ready` deltaP `-1.2298` edge `-0.0021` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.773` n `32` status `ready` deltaP `-3.5928` edge `-0.0254` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.9215` n `202` status `ready` deltaP `-12.7565` edge `0.2243` maxDD `-11.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
