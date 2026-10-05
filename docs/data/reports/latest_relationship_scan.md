# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T19:08:45.199257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8176`

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

- `market_context_high->crypto_major_24h` score `10.7188` n `78` status `ready` deltaP `29.0331` edge `0.7133` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5494` n `65` status `ready` deltaP `33.4662` edge `0.593` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0046` n `65` status `ready` deltaP `20.5488` edge `0.4978` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4691` n `78` status `ready` deltaP `26.0283` edge `0.3442` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.2745` n `65` status `ready` deltaP `22.9167` edge `0.1201` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.2057` n `65` status `ready` deltaP `9.8184` edge `0.2117` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.7263` n `65` status `ready` deltaP `30.3893` edge `0.0508` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4989` n `65` status `ready` deltaP `9.7167` edge `0.179` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.44` n `117` status `ready` deltaP `12.9534` edge `0.2134` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2063` n `65` status `ready` deltaP `18.5952` edge `0.1209` maxDD `-2.881`
- `news_risk_high->index_1h` score `1.9129` n `65` status `ready` deltaP `23.8208` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8402` n `65` status `ready` deltaP `17.554` edge `0.0779` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.647` n `117` status `ready` deltaP `27.8873` edge `0.027` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1673` n `65` status `ready` deltaP `3.6711` edge `0.1247` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.1373` n `117` status `ready` deltaP `15.6869` edge `0.0602` maxDD `-1.6002`
- `market_context_high->fx_1h` score `1.0462` n `117` status `ready` deltaP `16.2854` edge `0.007` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7677` n `78` status `ready` deltaP `25.0534` edge `0.0689` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7405` n `117` status `ready` deltaP `12.2051` edge `0.02` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.6048` n `78` status `ready` deltaP `13.4081` edge `-0.0329` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3381` n `65` status `ready` deltaP `24.9119` edge `0.0804` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
