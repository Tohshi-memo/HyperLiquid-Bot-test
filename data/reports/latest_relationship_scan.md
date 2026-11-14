# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T14:37:31.588362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `574.0355` n `66` status `ready` deltaP `4.5139` edge `47.8062` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.3652` n `53` status `ready` deltaP `39.7439` edge `3.0861` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.6115` n `66` status `ready` deltaP `34.7696` edge `2.89` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.3942` n `66` status `ready` deltaP `57.7652` edge `1.6721` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.8109` n `53` status `ready` deltaP `42.3906` edge `2.0692` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2034` n `53` status `ready` deltaP `35.6304` edge `0.8091` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.1623` n `53` status `ready` deltaP `49.4792` edge `0.267` maxDD `0.0`
- `market_context_high->index_24h` score `7.085` n `66` status `ready` deltaP `41.0353` edge `0.326` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.727` n `53` status `ready` deltaP `37.2903` edge `0.259` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2321` n `66` status `ready` deltaP `51.5152` edge `0.4165` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8442` n `53` status `ready` deltaP `45.4815` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.103` n `53` status `ready` deltaP `20.5908` edge `0.3534` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6631` n `53` status `ready` deltaP `19.5119` edge `0.2382` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3208` n `53` status `ready` deltaP `30.5223` edge `0.0986` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.3651` n `53` status `ready` deltaP `14.4261` edge `0.6576` maxDD `-29.0448`
- `news_risk_high->index_4h` score `2.3113` n `53` status `ready` deltaP `23.7949` edge `0.0776` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.2534` n `53` status `ready` deltaP `26.4985` edge `0.2761` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.2457` n `53` status `ready` deltaP `26.1891` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3125` n `53` status `ready` deltaP `17.6251` edge `0.022` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8404` n `53` status `ready` deltaP `18.1928` edge `0.0844` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
