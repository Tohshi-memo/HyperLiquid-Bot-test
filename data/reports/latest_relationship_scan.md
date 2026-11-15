# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T08:52:29.822689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9948`

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

- `market_context_high->unknown_24h` score `537.2673` n `66` status `ready` deltaP `2.4263` edge `44.7561` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.393` n `50` status `ready` deltaP `48.8319` edge `3.4445` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1619` n `66` status `ready` deltaP `42.6501` edge `3.05` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.7696` n `66` status `ready` deltaP `57.8121` edge `2.2864` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7652` n `50` status `ready` deltaP `46.3882` edge `2.8519` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3551` n `50` status `ready` deltaP `39.6768` edge `0.8781` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.1083` n `50` status `ready` deltaP `16.9636` edge `1.377` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.528` n `66` status `ready` deltaP `44.9372` edge `0.3369` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.31` n `50` status `ready` deltaP `48.7002` edge `0.2845` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3317` n `50` status `ready` deltaP `40.513` edge `0.2879` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.1137` n `66` status `ready` deltaP `57.6388` edge `0.4887` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.7141` n `50` status `ready` deltaP `23.7378` edge `0.4555` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0983` n `50` status `ready` deltaP `46.2134` edge `0.1544` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0935` n `50` status `ready` deltaP `29.4329` edge `0.3718` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0211` n `50` status `ready` deltaP `21.497` edge `0.2548` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.493` n `50` status `ready` deltaP `32.0` edge `0.1031` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0929` n `66` status `ready` deltaP `12.6306` edge `1.2061` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.857` n `50` status `ready` deltaP `28.1524` edge `0.0854` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3167` n `50` status `ready` deltaP `26.491` edge `0.0419` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3238` n `50` status `ready` deltaP `17.497` edge `0.0238` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
