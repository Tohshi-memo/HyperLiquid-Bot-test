# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T12:52:27.459589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `382.6248` n `74` status `ready` deltaP `5.8042` edge `31.8608` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7078` n `53` status `ready` deltaP `31.9314` edge `2.5834` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.1515` n `74` status `ready` deltaP `27.5713` edge `2.0588` maxDD `-8.7317`
- `market_context_high->crypto_alt_24h` score `18.6866` n `74` status `ready` deltaP `51.9285` edge `1.4625` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2432` n `53` status `ready` deltaP `42.3906` edge `1.74` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.3054` n `53` status `ready` deltaP `34.4109` edge `0.7424` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.037` n `74` status `ready` deltaP `38.1757` edge `0.3298` maxDD `-3.4976`
- `news_risk_high->commodity_24h` score `5.7651` n `53` status `ready` deltaP `36.9792` edge `0.2339` maxDD `0.0`
- `market_context_high->index_24h` score `4.7979` n `74` status `ready` deltaP `25.4363` edge `0.2394` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.595` n `53` status `ready` deltaP `43.9571` edge `0.1275` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0838` n `53` status `ready` deltaP `23.575` edge `0.2135` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.3214` n `53` status `ready` deltaP `17.7155` edge `0.2217` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.0209` n `53` status `ready` deltaP `18.914` edge `0.2744` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0199` n `53` status `ready` deltaP `27.9309` edge `0.0908` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.9395` n `53` status `ready` deltaP `19.1136` edge `0.7` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1056` n `53` status `ready` deltaP `24.8418` edge `0.0353` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.921` n `53` status `ready` deltaP `19.8315` edge `0.0715` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8436` n `53` status `ready` deltaP `26.1936` edge `0.2256` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `15.9784` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5909` n `53` status `ready` deltaP `16.6958` edge `0.0624` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
