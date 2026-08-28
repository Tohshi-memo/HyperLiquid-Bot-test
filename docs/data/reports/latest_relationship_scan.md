# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T17:07:25.176778+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `54.0593` n `50` status `ready` deltaP `12.6516` edge `4.4206` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.2025` n `50` status `ready` deltaP `43.3137` edge `2.4389` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.1951` n `56` status `ready` deltaP `23.7369` edge `0.7889` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.6455` n `50` status `ready` deltaP `30.1005` edge `0.3626` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.0101` n `50` status `ready` deltaP `22.4749` edge `0.317` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.323` n `50` status `ready` deltaP `43.4073` edge `0.0751` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0528` n `56` status `ready` deltaP `47.1254` edge `0.0326` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.4931` n `63` status `ready` deltaP `12.3278` edge `0.2446` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.368` n `120` status `ready` deltaP `5.9849` edge `0.314` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1402` n `120` status `ready` deltaP `28.7406` edge `0.172` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7614` n `120` status `ready` deltaP `18.6179` edge `0.1467` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3662` n `50` status `ready` deltaP `26.9948` edge `0.0323` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.2733` n `63` status `ready` deltaP `17.4152` edge `0.0071` maxDD `-0.034`
- `market_context_high->unknown_1h` score `1.0019` n `120` status `ready` deltaP `9.3913` edge `0.0659` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9157` n `56` status `ready` deltaP `20.0566` edge `0.06` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7547` n `56` status `ready` deltaP `14.46` edge `0.0196` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4869` n `63` status `ready` deltaP `13.2521` edge `0.0061` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1365` n `56` status `ready` deltaP `7.5566` edge `0.0009` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.0215` n `120` status `ready` deltaP `13.1504` edge `0.0013` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3645` n `63` status `ready` deltaP `0.8246` edge `-0.0097` maxDD `-0.7353`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
