# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T17:52:35.622822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `301.6795` n `84` status `ready` deltaP `6.4425` edge `25.1111` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `87.1578` n `94` status `ready` deltaP `8.1053` edge `7.2539` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.7861` n `53` status `ready` deltaP `21.7406` edge `2.2412` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.7687` n `84` status `ready` deltaP `19.4719` edge `1.5882` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.1577` n `53` status `ready` deltaP `37.0699` edge `1.3799` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4601` n `53` status `ready` deltaP `33.039` edge `0.6811` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `7.6068` n `84` status `ready` deltaP `39.4217` edge `1.122` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.5312` n `53` status `ready` deltaP `43.4256` edge `0.3381` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1451` n `84` status `ready` deltaP `38.8491` edge `0.2944` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.7364` n `53` status `ready` deltaP `44.7193` edge `0.1342` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8852` n `84` status `ready` deltaP `21.4451` edge `0.1903` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4769` n `53` status `ready` deltaP `19.6481` edge `0.1891` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.0892` n `53` status `ready` deltaP `21.6579` edge `0.2618` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.0635` n `53` status `ready` deltaP `17.2664` edge `0.2032` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0375` n `53` status `ready` deltaP `26.7114` edge `0.1004` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2625` n `53` status `ready` deltaP `26.4885` edge `0.0374` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.7548` n `53` status `ready` deltaP `18.4595` edge `0.0668` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5913` n `53` status `ready` deltaP `25.7363` edge `0.1963` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1986` n `53` status `ready` deltaP `16.5772` edge `0.0195` maxDD `-0.4103`
- `market_context_high->fx_24h` score `0.5704` n `84` status `ready` deltaP `23.896` edge `0.0482` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
