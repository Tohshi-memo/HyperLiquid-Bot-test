# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T01:22:28.598183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1638.232` n `137` status `ready` deltaP `1.9097` edge `136.5066` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3581` n `137` status `ready` deltaP `28.5711` edge `1.3693` maxDD `-20.7279`
- `news_risk_high->equity_24h` score `8.5662` n `137` status `ready` deltaP `28.8955` edge `0.7561` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.5836` n `137` status `ready` deltaP `24.3816` edge `0.8205` maxDD `-18.7528`
- `news_risk_high->index_24h` score `3.7667` n `137` status `ready` deltaP `34.9795` edge `0.1415` maxDD `-1.5309`
- `news_risk_high->metal_24h` score `3.1487` n `137` status `ready` deltaP `27.5231` edge `0.2435` maxDD `-5.1675`
- `news_risk_high->equity_4h` score `2.8441` n `140` status `ready` deltaP `28.8197` edge `0.205` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.4329` n `140` status `ready` deltaP `13.1707` edge `0.3809` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3529` n `140` status `ready` deltaP `10.231` edge `0.1356` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7494` n `140` status `ready` deltaP `8.1223` edge `0.071` maxDD `-1.6827`
- `news_risk_high->index_1h` score `0.482` n `140` status `ready` deltaP `8.7211` edge `0.0108` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0091` n `140` status `ready` deltaP `8.4103` edge `0.0285` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1514` n `140` status `ready` deltaP `4.1916` edge `0.0809` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5804` n `140` status `ready` deltaP `0.2053` edge `0.0132` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2039` n `140` status `ready` deltaP `-1.4939` edge `0.1271` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.363` n `140` status `ready` deltaP `-8.4539` edge `0.0276` maxDD `-3.3454`
- `news_risk_high->fx_4h` score `-1.4048` n `140` status `ready` deltaP `7.3563` edge `-0.0078` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8573` n `140` status `ready` deltaP `-9.3798` edge `-0.0042` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8779` n `140` status `ready` deltaP `-9.5509` edge `-0.0096` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2892` n `140` status `ready` deltaP `-9.4381` edge `0.0113` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
