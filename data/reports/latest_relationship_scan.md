# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T06:52:16.739065+00:00`
- Price records: `672`
- Market context records: `1093`
- Flow alert records: `5052`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.5435` n `151` status `ready` deltaP `35.9372` edge `1.1854` maxDD `-3.3749`
- `market_context_high->equity_24h` score `5.9445` n `151` status `ready` deltaP `15.4556` edge `0.442` maxDD `-3.6396`
- `market_context_high->crypto_alt_24h` score `5.7425` n `151` status `ready` deltaP `12.336` edge `0.5197` maxDD `-9.5387`
- `market_context_high->metal_24h` score `5.0528` n `151` status `ready` deltaP `-3.1678` edge `0.6089` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.7355` n `151` status `ready` deltaP `15.1089` edge `0.3247` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0723` n `164` status `ready` deltaP `11.4329` edge `0.1628` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0895` n `164` status `ready` deltaP `9.2987` edge `0.0971` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.6185` n `164` status `ready` deltaP `9.7561` edge `0.1551` maxDD `-6.4882`
- `market_context_high->index_1h` score `0.6039` n `169` status `ready` deltaP `8.5524` edge `0.025` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4578` n `169` status `ready` deltaP `3.5122` edge `0.0525` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1086` n `169` status `ready` deltaP `7.9527` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1068` n `169` status `ready` deltaP `7.3752` edge `0.0363` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.1002` n `169` status `ready` deltaP `7.4682` edge `0.0029` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.294` n `169` status `ready` deltaP `2.7416` edge `0.0415` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6189` n `164` status `ready` deltaP `2.7439` edge `0.002` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.741` n `169` status `ready` deltaP `-1.6077` edge `-0.0035` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.8326` n `164` status `ready` deltaP `6.0975` edge `0.1404` maxDD `-13.0347`
- `market_context_high->unknown_4h` score `-2.3113` n `164` status `ready` deltaP `9.7561` edge `-0.136` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-2.3549` n `164` status `ready` deltaP `7.1646` edge `-0.0486` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.0586` n `164` status `ready` deltaP `-10.0609` edge `-0.0083` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
