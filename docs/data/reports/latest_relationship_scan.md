# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T13:22:30.201842+00:00`
- Price records: `672`
- Market context records: `6607`
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

- `market_context_high->unknown_24h` score `3.7179` n `168` status `ready` deltaP `3.0318` edge `0.5808` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.0968` n `206` status `ready` deltaP `-5.8296` edge `0.3037` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.3165` n `168` status `ready` deltaP `7.9193` edge `0.1604` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2775` n `206` status `ready` deltaP `2.2135` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4434` n `206` status `ready` deltaP `6.7554` edge `0.0247` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5364` n `206` status `ready` deltaP `0.4404` edge `-0.0034` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5552` n `206` status `ready` deltaP `-0.4084` edge `0.0035` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6828` n `206` status `ready` deltaP `4.1785` edge `0.0159` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9011` n `206` status `ready` deltaP `9.5164` edge `0.009` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1696` n `206` status `ready` deltaP `1.9781` edge `-0.0003` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2082` n `206` status `ready` deltaP `-0.0637` edge `-0.005` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3577` n `206` status `ready` deltaP `-4.4373` edge `-0.0034` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.5136` n `206` status `ready` deltaP `-17.3795` edge `0.2303` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6405` n `206` status `ready` deltaP `1.813` edge `-0.0012` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6942` n `206` status `ready` deltaP `7.4621` edge `0.0645` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0787` n `206` status `ready` deltaP `4.4814` edge `0.0438` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.158` n `206` status `ready` deltaP `-1.3527` edge `0.0184` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1351` n `206` status `ready` deltaP `7.1972` edge `-0.023` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.2612` n `168` status `ready` deltaP `-0.0227` edge `0.058` maxDD `-11.0759`
- `market_context_high->fx_24h` score `-3.6951` n `168` status `ready` deltaP `-6.078` edge `-0.0002` maxDD `-8.9737`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
