# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T14:52:27.044943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11814`

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

- `market_context_high->unknown_24h` score `209.761` n `88` status `ready` deltaP `-21.512` edge `27.3042` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.7077` n `88` status `ready` deltaP `41.3037` edge `0.3727` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.3575` n `125` status `ready` deltaP `13.1598` edge `0.0725` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0915` n `125` status `ready` deltaP `2.0563` edge `0.0198` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1324` n `125` status `ready` deltaP `1.4527` edge `0.0015` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.3158` n `125` status `ready` deltaP `4.2073` edge `0.0061` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5268` n `125` status `ready` deltaP `1.5042` edge `-0.006` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7936` n `125` status `ready` deltaP `-6.9868` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9386` n `125` status `ready` deltaP `7.5232` edge `-0.0131` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.479` n `88` status `ready` deltaP `-8.3649` edge `0.0269` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6456` n `125` status `ready` deltaP `-9.2838` edge `-0.0451` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.7884` n `88` status `ready` deltaP `-7.5284` edge `0.0721` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9652` n `125` status `ready` deltaP `-1.3964` edge `-0.0205` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-1.9726` n `125` status `ready` deltaP `-4.4` edge `-0.0297` maxDD `-5.4277`
- `market_context_high->index_24h` score `-2.0447` n `88` status `ready` deltaP `-5.887` edge `-0.0689` maxDD `-2.3194`
- `market_context_high->index_4h` score `-2.1629` n `125` status `ready` deltaP `-13.3951` edge `-0.0097` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5554` n `125` status `ready` deltaP `-0.1707` edge `-0.0594` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.7332` n `88` status `ready` deltaP `-4.3087` edge `0.0076` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1785` n `125` status `ready` deltaP `-0.1473` edge `-0.5515` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-8.0571` n `125` status `ready` deltaP `-11.7524` edge `-0.1052` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
