# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T02:22:28.001113+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.306` n `103` status `ready` deltaP `4.5729` edge `0.551` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6359` n `103` status `ready` deltaP `13.2535` edge `0.1889` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4284` n `123` status `ready` deltaP `14.3293` edge `0.0908` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8862` n `135` status `ready` deltaP `10.8827` edge `0.0356` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8482` n `103` status `ready` deltaP `22.0958` edge `0.0481` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4955` n `103` status `ready` deltaP `9.1002` edge `0.156` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3615` n `135` status `ready` deltaP `3.483` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.4574` n `123` status `ready` deltaP `6.0467` edge `-0.0031` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.5858` n `123` status `ready` deltaP `-0.2541` edge `-0.0129` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6724` n `135` status `ready` deltaP `-4.4433` edge `-0.007` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.8695` n `135` status `ready` deltaP `-3.9942` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.95` n `135` status `ready` deltaP `-0.061` edge `0.0041` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0305` n `123` status `ready` deltaP `-2.1342` edge `-0.017` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1519` n `135` status `ready` deltaP `-12.1424` edge `-0.0342` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3868` n `123` status `ready` deltaP `0.559` edge `-0.0689` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1538` n `135` status `ready` deltaP `-10.4724` edge `-0.0657` maxDD `-6.8504`
- `market_context_high->crypto_major_24h` score `-3.6079` n `103` status `ready` deltaP `6.2197` edge `-0.0927` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4866` n `103` status `ready` deltaP `-12.4461` edge `-0.1466` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.6301` n `123` status `ready` deltaP `-12.4492` edge `-0.1372` maxDD `-6.585`
- `market_context_high->unknown_1h` score `-8.2975` n `135` status `ready` deltaP `-4.9723` edge `-0.6136` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
