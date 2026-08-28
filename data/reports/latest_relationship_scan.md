# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T17:52:25.111843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.1573` n `50` status `ready` deltaP `13.1716` edge `4.4253` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5045` n `50` status `ready` deltaP `43.8336` edge `2.4606` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.9462` n `56` status `ready` deltaP `23.2796` edge `0.7712` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.7487` n `50` status `ready` deltaP `30.1005` edge `0.3712` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.4381` n `50` status `ready` deltaP `22.9948` edge `0.3492` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3266` n `50` status `ready` deltaP `43.4073` edge `0.0754` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0918` n `56` status `ready` deltaP `47.5827` edge `0.0328` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.466` n `120` status `ready` deltaP `6.5049` edge `0.3187` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.349` n `66` status `ready` deltaP `11.967` edge `0.235` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.1438` n `120` status `ready` deltaP `28.7406` edge `0.1723` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.5124` n `120` status `ready` deltaP `18.1606` edge `0.129` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3722` n `50` status `ready` deltaP `26.9948` edge `0.0328` maxDD `-0.2064`
- `market_context_high->unknown_1h` score `0.9827` n `120` status `ready` deltaP `9.3913` edge `0.0643` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9704` n `56` status `ready` deltaP `20.2091` edge `0.066` maxDD `-2.105`
- `news_risk_high->fx_1h` score `0.9008` n `66` status `ready` deltaP `14.834` edge `0.0063` maxDD `-0.0769`
- `news_risk_high->metal_4h` score `0.7918` n `56` status `ready` deltaP `14.46` edge `0.0227` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5887` n `66` status `ready` deltaP `14.9837` edge `0.0076` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1437` n `56` status `ready` deltaP `7.5566` edge `0.0015` maxDD `-0.1919`
- `market_context_high->metal_4h` score `0.0027` n `120` status `ready` deltaP `13.1504` edge `0.0044` maxDD `-3.3377`
- `news_risk_high->metal_1h` score `-0.358` n `66` status `ready` deltaP `3.4794` edge `-0.0195` maxDD `-1.9673`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
