# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T15:52:25.504896+00:00`
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

- `market_context_high->unknown_24h` score `574.6499` n `66` status `ready` deltaP `4.5139` edge `47.8574` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.5294` n `53` status `ready` deltaP `40.6119` edge `3.094` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.7757` n `66` status `ready` deltaP `35.6376` edge `2.8979` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.7854` n `66` status `ready` deltaP `57.7652` edge `1.7047` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.1463` n `53` status `ready` deltaP `42.3906` edge `2.1122` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3062` n `53` status `ready` deltaP `36.2402` edge `0.8136` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2618` n `53` status `ready` deltaP `50.3472` edge `0.2695` maxDD `0.0`
- `market_context_high->index_24h` score `7.1188` n `66` status `ready` deltaP `41.3825` edge `0.3265` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.7608` n `53` status `ready` deltaP `37.6375` edge `0.2595` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2539` n `66` status `ready` deltaP `51.5152` edge `0.4193` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.855` n `53` status `ready` deltaP `45.4815` edge `0.139` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3034` n `53` status `ready` deltaP `20.5908` edge `0.3701` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6691` n `53` status `ready` deltaP `19.5119` edge `0.2387` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.389` n `53` status `ready` deltaP `31.2845` edge `0.0992` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.6193` n `53` status `ready` deltaP `14.4261` edge `0.6902` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.4065` n `53` status `ready` deltaP `26.8033` edge `0.2937` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.3782` n `53` status `ready` deltaP `24.5571` edge `0.0781` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2517` n `53` status `ready` deltaP `26.1891` edge `0.0385` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3747` n `53` status `ready` deltaP `18.3736` edge `0.0222` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.863` n `53` status `ready` deltaP `18.1928` edge `0.0873` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
