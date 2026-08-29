# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T04:22:24.532897+00:00`
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

- `news_risk_high->unknown_24h` score `57.6724` n `50` status `ready` deltaP `20.4506` edge `4.6697` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.1963` n `50` status `ready` deltaP `46.6066` edge `2.5831` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `10.0749` n `50` status `ready` deltaP `28.0208` edge `0.7021` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `7.7047` n `75` status `ready` deltaP `14.4512` edge `0.5809` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.2871` n `50` status `ready` deltaP `30.1005` edge `0.4994` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.9812` n `120` status `ready` deltaP `13.7839` edge `0.5631` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.5294` n `50` status `ready` deltaP `43.4073` edge `0.0923` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.3466` n `120` status `ready` deltaP `28.7406` edge `0.1892` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4922` n `50` status `ready` deltaP `26.9948` edge `0.0428` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4062` n `120` status `ready` deltaP `18.6179` edge `0.1171` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.3764` n `80` status `ready` deltaP `5.0749` edge `0.1999` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `1.4866` n `75` status `ready` deltaP `33.4695` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9503` n `120` status `ready` deltaP `9.2416` edge `0.0626` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6393` n `80` status `ready` deltaP `12.994` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.447` n `80` status `ready` deltaP `12.6497` edge `0.005` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1075` n `120` status `ready` deltaP `10.1016` edge `0.0106` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.332` n `120` status `ready` deltaP `4.6607` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3645` n `80` status `ready` deltaP `0.756` edge `-0.0081` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4807` n `120` status `ready` deltaP `13.6382` edge `0.2141` maxDD `-20.9394`
- `news_risk_high->equity_1h` score `-0.5422` n `80` status `ready` deltaP `9.0569` edge `-0.0365` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
