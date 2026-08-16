# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T12:07:25.913026+00:00`
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

- `market_context_high->unknown_24h` score `200.5164` n `88` status `ready` deltaP `-21.512` edge `26.119` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5481` n `88` status `ready` deltaP `41.3037` edge `0.3594` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.7728` n `118` status `ready` deltaP `17.2412` edge `0.0799` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0783` n `125` status `ready` deltaP `2.206` edge `0.0199` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.098` n `118` status `ready` deltaP `6.0898` edge `0.0073` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.544` n `125` status `ready` deltaP `1.2048` edge `-0.0062` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8099` n `125` status `ready` deltaP `-7.2862` edge `-0.0031` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-1.0292` n `118` status `ready` deltaP `6.0356` edge `-0.0148` maxDD `-4.5909`
- `market_context_high->index_4h` score `-1.3164` n `118` status `ready` deltaP `-11.7197` edge `-0.0094` maxDD `-0.8328`
- `market_context_high->fx_24h` score `-1.6149` n `88` status `ready` deltaP `-10.2747` edge `0.0222` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-1.6563` n `88` status `ready` deltaP `-5.6187` edge `0.0763` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-1.6915` n `125` status `ready` deltaP `-10.0323` edge `-0.046` maxDD `-4.9849`
- `market_context_high->index_24h` score `-1.9745` n `88` status `ready` deltaP `-4.6717` edge `-0.068` maxDD `-2.3194`
- `market_context_high->crypto_alt_1h` score `-2.0131` n `125` status `ready` deltaP `-1.6958` edge `-0.0225` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.0205` n `125` status `ready` deltaP `-4.6994` edge `-0.0317` maxDD `-5.4277`
- `market_context_high->crypto_major_4h` score `-2.2917` n `118` status `ready` deltaP `1.6097` edge `-0.0688` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6447` n `88` status `ready` deltaP `-3.267` edge `0.012` maxDD `-35.189`
- `market_context_high->equity_4h` score `-5.4013` n `118` status `ready` deltaP `-29.1443` edge `-0.1936` maxDD `-15.3661`
- `market_context_high->unknown_1h` score `-7.2192` n `125` status `ready` deltaP `-0.5964` edge `-0.5519` maxDD `-1.3246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
