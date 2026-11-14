# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T14:07:23.070550+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `573.7979` n `66` status `ready` deltaP `4.5139` edge `47.7864` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.2114` n `53` status `ready` deltaP `39.3967` edge `3.0756` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.4577` n `66` status `ready` deltaP `34.4224` edge `2.8795` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.219` n `66` status `ready` deltaP `57.7652` edge `1.6575` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.6612` n `53` status `ready` deltaP `42.3906` edge `2.05` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1902` n `53` status `ready` deltaP `35.6304` edge `0.808` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.1214` n `53` status `ready` deltaP `49.1319` edge `0.2659` maxDD `0.0`
- `market_context_high->index_24h` score `7.0477` n `66` status `ready` deltaP `40.6881` edge `0.3252` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.6897` n `53` status `ready` deltaP `36.9431` edge `0.2582` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2243` n `66` status `ready` deltaP `51.5152` edge `0.4155` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.843` n `53` status `ready` deltaP `45.4815` edge `0.138` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0346` n `53` status `ready` deltaP `20.5908` edge `0.3477` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6547` n `53` status `ready` deltaP `19.5119` edge `0.2375` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2928` n `53` status `ready` deltaP `30.2175` edge `0.0983` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2845` n `53` status `ready` deltaP `23.49` edge `0.0774` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `2.2512` n `53` status `ready` deltaP `14.4261` edge `0.643` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.2326` n `53` status `ready` deltaP `26.0394` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.2074` n `53` status `ready` deltaP `26.4985` edge `0.2702` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2993` n `53` status `ready` deltaP `17.4754` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8037` n `53` status `ready` deltaP `18.1928` edge `0.0797` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
