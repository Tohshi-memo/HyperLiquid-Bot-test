# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T18:07:36.661182+00:00`
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

- `news_risk_high->unknown_24h` score `54.2144` n `50` status `ready` deltaP `13.3449` edge `4.4289` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.6035` n `50` status `ready` deltaP `44.0069` edge `2.4677` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.9244` n `56` status `ready` deltaP `23.1272` edge `0.7704` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.7775` n `50` status `ready` deltaP `30.1005` edge `0.3736` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.5779` n `50` status `ready` deltaP `23.1681` edge `0.3597` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.329` n `50` status `ready` deltaP `43.4073` edge `0.0756` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0918` n `56` status `ready` deltaP `47.5827` edge `0.0328` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5231` n `120` status `ready` deltaP `6.6782` edge `0.3223` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1462` n `120` status `ready` deltaP `28.7406` edge `0.1725` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1235` n `67` status `ready` deltaP `10.8589` edge `0.2236` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.4906` n `120` status `ready` deltaP `18.0082` edge `0.1282` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3722` n `50` status `ready` deltaP `26.9948` edge `0.0328` maxDD `-0.2064`
- `market_context_high->unknown_1h` score `0.9863` n `120` status `ready` deltaP `9.3913` edge `0.0646` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.979` n `56` status `ready` deltaP `20.2091` edge `0.0671` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7991` n `56` status `ready` deltaP `14.46` edge `0.0233` maxDD `-0.249`
- `news_risk_high->fx_1h` score `0.7841` n `67` status `ready` deltaP `14.0339` edge `0.0062` maxDD `-0.0868`
- `news_risk_high->commodity_1h` score `0.5369` n `67` status `ready` deltaP `14.1836` edge `0.0063` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1449` n `56` status `ready` deltaP `7.5566` edge `0.0016` maxDD `-0.1919`
- `market_context_high->metal_4h` score `0.0074` n `120` status `ready` deltaP `13.1504` edge `0.005` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3951` n `67` status `ready` deltaP `0.2882` edge `-0.0094` maxDD `-0.787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
