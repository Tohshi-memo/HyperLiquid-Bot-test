# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T10:22:19.991655+00:00`
- Price records: `672`
- Market context records: `2552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.6435` n `149` status `ready` deltaP `24.4036` edge `0.5755` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.5478` n `118` status `ready` deltaP `19.4768` edge `0.3653` maxDD `-1.626`
- `market_context_high->crypto_major_24h` score `4.9897` n `118` status `ready` deltaP `12.1704` edge `0.6` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.9459` n `149` status `ready` deltaP `17.4486` edge `0.3935` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9009` n `149` status `ready` deltaP `10.7669` edge `0.1916` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.2348` n `118` status `ready` deltaP `18.9972` edge `0.0346` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.1977` n `149` status `ready` deltaP `9.7265` edge `0.1537` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.8382` n `118` status `ready` deltaP `7.6536` edge `0.1169` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6514` n `149` status `ready` deltaP `7.9351` edge `0.1208` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1823` n `118` status `ready` deltaP `-0.9592` edge `0.6702` maxDD `-39.2351`
- `market_context_high->index_4h` score `-0.082` n `149` status `ready` deltaP `6.2274` edge `0.0358` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1765` n `149` status `ready` deltaP `2.8654` edge `0.0352` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.2017` n `149` status `ready` deltaP `3.2995` edge `0.0106` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.462` n `149` status `ready` deltaP `0.862` edge `0.0098` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.5405` n `149` status `ready` deltaP `0.635` edge `0.0042` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.5554` n `149` status `ready` deltaP `4.058` edge `0.0145` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7205` n `118` status `ready` deltaP `1.6037` edge `0.0046` maxDD `-1.946`
- `market_context_high->equity_1h` score `-0.8213` n `149` status `ready` deltaP `-0.4481` edge `0.0184` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8492` n `149` status `ready` deltaP `3.6872` edge `0.0434` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.9073` n `149` status `ready` deltaP `-0.3059` edge `0.0124` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
