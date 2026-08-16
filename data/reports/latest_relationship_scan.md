# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T13:41:03.781739+00:00`
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

- `market_context_high->unknown_24h` score `205.1582` n `88` status `ready` deltaP `-21.512` edge `26.7141` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.6249` n `88` status `ready` deltaP `41.3037` edge `0.3658` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4163` n `124` status `ready` deltaP `13.7146` edge `0.0737` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0915` n `125` status `ready` deltaP `2.0563` edge `0.0198` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.3393` n `124` status `ready` deltaP `3.929` edge `0.006` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5191` n `125` status `ready` deltaP `1.6539` edge `-0.006` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8092` n `125` status `ready` deltaP `-7.2862` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9478` n `124` status `ready` deltaP `7.3908` edge `-0.0134` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.5428` n `88` status `ready` deltaP `-9.233` edge `0.0245` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6456` n `125` status `ready` deltaP `-9.2838` edge `-0.0451` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.7261` n `88` status `ready` deltaP `-6.6603` edge `0.0743` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9843` n `125` status `ready` deltaP `-1.5461` edge `-0.0211` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-1.9953` n `125` status `ready` deltaP `-4.5497` edge `-0.0306` maxDD `-5.4277`
- `market_context_high->index_24h` score `-2.0047` n `88` status `ready` deltaP `-5.1926` edge `-0.0684` maxDD `-2.3194`
- `market_context_high->index_4h` score `-2.1582` n `124` status `ready` deltaP `-13.3065` edge `-0.0099` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5678` n `124` status `ready` deltaP `0.0639` edge `-0.062` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6467` n `88` status `ready` deltaP `-3.4406` edge `0.0129` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.194` n `125` status `ready` deltaP `-0.297` edge `-0.5518` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-8.176` n `124` status `ready` deltaP `-12.2492` edge `-0.1118` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
