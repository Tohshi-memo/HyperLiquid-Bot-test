# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T20:52:25.273014+00:00`
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

- `news_risk_high->unknown_24h` score `55.0305` n `50` status `ready` deltaP `15.2513` edge `4.4842` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.8336` n `50` status `ready` deltaP `45.9133` edge `2.5575` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.072` n `66` status `ready` deltaP `20.9581` edge `0.7178` maxDD `-0.4551`
- `news_risk_high->crypto_major_24h` score `7.45` n `50` status `ready` deltaP `25.0745` edge `0.503` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.2035` n `50` status `ready` deltaP `30.1005` edge `0.4091` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.3866` n `50` status `ready` deltaP `43.4073` edge `0.0804` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `4.3392` n `120` status `ready` deltaP `8.5846` edge `0.3776` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `3.5101` n `71` status `ready` deltaP `9.5556` edge `0.2645` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2038` n `120` status `ready` deltaP `28.7406` edge `0.1773` maxDD `-3.1535`
- `news_risk_high->fx_4h` score `2.6369` n `66` status `ready` deltaP `35.3335` edge `0.025` maxDD `-0.2652`
- `news_risk_high->index_24h` score `2.3962` n `50` status `ready` deltaP `26.9948` edge `0.0348` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2737` n `120` status `ready` deltaP `17.246` edge `0.1152` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9227` n `120` status `ready` deltaP `9.3913` edge `0.0593` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.583` n `71` status `ready` deltaP `12.2101` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3743` n `71` status `ready` deltaP `11.4616` edge `0.0036` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0729` n `120` status `ready` deltaP `13.1504` edge `0.0134` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.4036` n `120` status `ready` deltaP `3.3134` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4678` n `71` status `ready` deltaP `-1.031` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->index_4h` score `-0.6594` n `66` status `ready` deltaP `-0.1524` edge `-0.0207` maxDD `-1.6927`
- `news_risk_high->metal_1h` score `-0.6596` n `71` status `ready` deltaP `-0.1054` edge `-0.0263` maxDD `-2.605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
