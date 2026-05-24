# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T15:37:18.505556+00:00`
- Price records: `672`
- Market context records: `1751`
- Flow alert records: `6941`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1601` n `163` status `ready` deltaP `26.9365` edge `0.6597` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9055` n `196` status `ready` deltaP `20.3615` edge `0.533` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3022` n `196` status `ready` deltaP `21.9574` edge `0.4527` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.2567` n `163` status `ready` deltaP `19.0301` edge `0.3507` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.1385` n `163` status `ready` deltaP `15.2726` edge `0.7751` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.9753` n `196` status `ready` deltaP `15.9594` edge `0.251` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.875` n `163` status `ready` deltaP `17.2693` edge `0.6143` maxDD `-33.1875`
- `market_context_high->unknown_4h` score `2.8299` n `196` status `ready` deltaP `12.7271` edge `0.3781` maxDD `-11.1695`
- `market_context_high->index_4h` score `0.8213` n `196` status `ready` deltaP `11.2556` edge `0.1023` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7993` n `196` status `ready` deltaP `7.5706` edge `0.1185` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.6353` n `163` status `ready` deltaP `19.5639` edge `0.7811` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2412` n `196` status `ready` deltaP `4.8974` edge `0.0948` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0682` n `196` status `ready` deltaP `4.9707` edge `0.0534` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1939` n `196` status `ready` deltaP `3.9167` edge `0.0209` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2537` n `196` status `ready` deltaP `12.444` edge `0.1537` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.4801` n `196` status `ready` deltaP `6.3944` edge `0.0294` maxDD `-6.3532`
- `market_context_high->crypto_alt_24h` score `-0.6105` n `163` status `ready` deltaP `20.406` edge `0.994` maxDD `-88.8062`
- `market_context_high->fx_24h` score `-0.6369` n `163` status `ready` deltaP `6.8601` edge `0.0061` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.735` n `196` status `ready` deltaP `-0.11` edge `0.0031` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
