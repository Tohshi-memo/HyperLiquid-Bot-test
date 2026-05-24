# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T09:22:13.007097+00:00`
- Price records: `672`
- Market context records: `1721`
- Flow alert records: `6862`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.6368` n `142` status `ready` deltaP `25.4496` edge `0.626` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.1592` n `142` status `ready` deltaP `17.206` edge `0.9306` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `6.0115` n `196` status `ready` deltaP `21.581` edge `0.5337` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4958` n `196` status `ready` deltaP `23.1769` edge `0.4607` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.905` n `142` status `ready` deltaP `17.1085` edge `0.3342` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0317` n `196` status `ready` deltaP `13.7941` edge `0.3878` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0105` n `196` status `ready` deltaP `16.2643` edge `0.2519` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5758` n `142` status `ready` deltaP `15.8487` edge `0.5155` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7285` n `196` status `ready` deltaP `7.4209` edge `0.1136` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5324` n `196` status `ready` deltaP `8.6642` edge `0.0955` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1765` n `196` status `ready` deltaP `4.7477` edge `0.0904` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.0396` n `142` status `ready` deltaP `22.9519` edge `1.0312` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0191` n `196` status `ready` deltaP `4.6713` edge `0.0513` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.329` n `196` status `ready` deltaP `11.9867` edge `0.1471` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4371` n `196` status `ready` deltaP `1.3718` edge `0.0176` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6646` n `196` status `ready` deltaP `-3.1162` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7947` n `142` status `ready` deltaP `4.7371` edge `0.0071` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.8321` n `142` status `ready` deltaP `21.2852` edge `0.61` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.5432` n `196` status `ready` deltaP `1.5367` edge `0.0081` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
