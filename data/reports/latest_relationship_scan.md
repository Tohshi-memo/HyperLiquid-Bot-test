# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T12:52:29.827511+00:00`
- Price records: `672`
- Market context records: `6604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.4726` n `168` status `ready` deltaP `3.0318` edge `0.5791` maxDD `-14.1276`
- `market_context_high->unknown_1h` score `2.0663` n `208` status `ready` deltaP `-5.4612` edge `0.2987` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.4428` n `168` status `ready` deltaP `8.7638` edge `0.1653` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2935` n `208` status `ready` deltaP `1.9058` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4296` n `208` status `ready` deltaP `6.8574` edge `0.0258` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5279` n `208` status `ready` deltaP `0.0864` edge `0.0037` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5688` n `208` status `ready` deltaP `-0.0777` edge `-0.0041` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6599` n `208` status `ready` deltaP `4.3039` edge `0.018` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9248` n `208` status `ready` deltaP `9.076` edge `0.0089` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1522` n `208` status `ready` deltaP `2.1361` edge `0.0001` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2006` n `208` status `ready` deltaP `0.0235` edge `-0.0046` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3306` n `208` status `ready` deltaP `-4.2175` edge `-0.0026` maxDD `-2.0797`
- `market_context_high->fx_4h` score `-1.6284` n `208` status `ready` deltaP `2.0169` edge `-0.001` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.6335` n `208` status `ready` deltaP `-17.378` edge `0.2203` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8198` n `208` status `ready` deltaP `6.9066` edge `0.0521` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1615` n `208` status `ready` deltaP `3.9399` edge `0.0368` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1849` n `208` status `ready` deltaP `-1.7354` edge `0.0175` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1856` n `208` status `ready` deltaP `6.6605` edge `-0.0259` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-3.7775` n `168` status `ready` deltaP `-6.078` edge `-0.0004` maxDD `-9.1367`
- `market_context_high->metal_24h` score `-4.8695` n `168` status `ready` deltaP `-0.0227` edge `0.0574` maxDD `-10.7102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
