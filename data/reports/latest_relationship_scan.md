# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T13:52:29.707247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `205.9273` n `88` status `ready` deltaP `-21.512` edge `26.8127` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.6393` n `88` status `ready` deltaP `41.3037` edge `0.367` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.3587` n `125` status `ready` deltaP `13.1598` edge `0.0726` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0915` n `125` status `ready` deltaP `2.0563` edge `0.0198` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1635` n `125` status `ready` deltaP `0.8539` edge `0.0015` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.367` n `125` status `ready` deltaP `3.5976` edge `0.0059` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5113` n `125` status `ready` deltaP `1.8036` edge `-0.006` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8092` n `125` status `ready` deltaP `-7.2862` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9639` n `125` status `ready` deltaP `7.0659` edge `-0.0133` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.5299` n `88` status `ready` deltaP `-9.0594` edge `0.025` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6456` n `125` status `ready` deltaP `-9.2838` edge `-0.0451` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.7382` n `88` status `ready` deltaP `-6.834` edge `0.0739` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9831` n `125` status `ready` deltaP `-1.5461` edge `-0.021` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-1.9905` n `125` status `ready` deltaP `-4.5497` edge `-0.0302` maxDD `-5.4277`
- `market_context_high->index_24h` score `-2.0145` n `88` status `ready` deltaP `-5.3662` edge `-0.0685` maxDD `-2.3194`
- `market_context_high->index_4h` score `-2.1763` n `125` status `ready` deltaP `-13.5476` edge `-0.0098` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5686` n `125` status `ready` deltaP `-0.1707` edge `-0.0605` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6589` n `88` status `ready` deltaP `-3.6142` edge `0.0125` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.2084` n `125` status `ready` deltaP `-0.4467` edge `-0.552` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-8.1039` n `125` status `ready` deltaP `-11.7524` edge `-0.1091` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
