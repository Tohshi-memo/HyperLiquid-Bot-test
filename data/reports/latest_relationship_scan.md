# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T18:42:08.438181+00:00`
- Price records: `672`
- Market context records: `6528`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7866`

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

- `news_risk_high->crypto_alt_24h` score `13.3495` n `32` status `ready` deltaP `36.211` edge `0.8858` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5657` n `32` status `ready` deltaP `54.2461` edge `0.1855` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2539` n `144` status `ready` deltaP `11.8934` edge `0.7719` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8722` n `32` status `ready` deltaP `20.911` edge `0.5632` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6865` n `38` status `ready` deltaP `39.0164` edge `0.0517` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.3838` n `188` status `ready` deltaP `-5.437` edge `0.325` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.086` n `32` status `ready` deltaP `22.6766` edge `0.0432` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.764` n `38` status `ready` deltaP `22.1636` edge `0.0173` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.667` n `144` status `ready` deltaP `14.6905` edge `0.2278` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6873` n `177` status `ready` deltaP `14.3715` edge `0.0291` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.6065` n `38` status `ready` deltaP `5.4995` edge `0.0948` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4674` n `177` status `ready` deltaP `11.3133` edge `0.1189` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1124` n `38` status `ready` deltaP `2.0328` edge `0.0518` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2627` n `32` status `ready` deltaP `7.3765` edge `0.0043` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3808` n `177` status `ready` deltaP `9.4744` edge `0.0579` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.3976` n `177` status `ready` deltaP `12.8377` edge `0.0925` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.4497` n `188` status `ready` deltaP `1.7932` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.4617` n `188` status `ready` deltaP `-1.0447` edge `-0.0015` maxDD `-0.7249`
- `market_context_high->unknown_4h` score `-0.545` n `177` status `ready` deltaP `-20.1823` edge `0.3297` maxDD `-10.5788`
- `market_context_high->crypto_major_1h` score `-0.5664` n `188` status `ready` deltaP `6.1154` edge `0.0132` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
