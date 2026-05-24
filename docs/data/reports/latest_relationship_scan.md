# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T14:52:13.552424+00:00`
- Price records: `672`
- Market context records: `1747`
- Flow alert records: `6932`
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

- `market_context_high->metal_24h` score `7.1749` n `160` status `ready` deltaP `26.6259` edge `0.663` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8575` n `196` status `ready` deltaP `20.3615` edge `0.529` maxDD `-9.1295`
- `market_context_high->index_24h` score `4.3643` n `160` status `ready` deltaP `19.2049` edge `0.3585` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `4.3044` n `160` status `ready` deltaP `15.3661` edge `0.7883` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.1925` n `196` status `ready` deltaP `21.5001` edge `0.4466` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `2.9191` n `196` status `ready` deltaP `13.0319` edge `0.3835` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.9177` n `160` status `ready` deltaP `17.3982` edge `0.617` maxDD `-33.1875`
- `market_context_high->equity_4h` score `2.9172` n `196` status `ready` deltaP `15.5021` edge `0.2492` maxDD `-5.0894`
- `market_context_high->crypto_alt_1h` score `0.7993` n `196` status `ready` deltaP `7.5706` edge `0.1185` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.7631` n `196` status `ready` deltaP `10.7983` edge `0.1005` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.7015` n `160` status `ready` deltaP `19.7617` edge `0.7853` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.234` n `196` status `ready` deltaP `4.8974` edge `0.0942` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0503` n `196` status `ready` deltaP `4.821` edge `0.0529` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.1783` n `160` status `ready` deltaP `20.7073` edge `1.028` maxDD `-88.8062`
- `market_context_high->index_1h` score `-0.2407` n `196` status `ready` deltaP `3.4676` edge `0.02` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2724` n `196` status `ready` deltaP `12.444` edge `0.1513` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.491` n `196` status `ready` deltaP `6.2447` edge `0.029` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.6568` n `160` status `ready` deltaP `6.5955` edge `0.0062` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->unknown_1h` score `-1.6774` n `196` status `ready` deltaP `0.3391` edge `0.0049` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
