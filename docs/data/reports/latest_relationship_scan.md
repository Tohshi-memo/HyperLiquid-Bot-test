# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T13:52:26.036662+00:00`
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

- `market_context_high->unknown_24h` score `573.6947` n `66` status `ready` deltaP `4.5139` edge `47.7778` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.1243` n `53` status `ready` deltaP `39.2231` edge `3.0695` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.3706` n `66` status `ready` deltaP `34.2488` edge `2.8734` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.135` n `66` status `ready` deltaP `57.7652` edge `1.6505` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.5788` n `53` status `ready` deltaP `42.217` edge `2.0406` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1866` n `53` status `ready` deltaP `35.6304` edge `0.8077` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.1015` n `53` status `ready` deltaP `48.9583` edge `0.2654` maxDD `0.0`
- `market_context_high->index_24h` score `7.0278` n `66` status `ready` deltaP `40.5145` edge `0.3247` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.6698` n `53` status `ready` deltaP `36.7695` edge `0.2577` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2204` n `66` status `ready` deltaP `51.5152` edge `0.415` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.843` n `53` status `ready` deltaP `45.4815` edge `0.138` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0142` n `53` status `ready` deltaP `20.5908` edge `0.346` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6403` n `53` status `ready` deltaP `19.3622` edge `0.2373` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2782` n `53` status `ready` deltaP `30.065` edge `0.0981` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2711` n `53` status `ready` deltaP `23.3376` edge `0.0773` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2194` n `53` status `ready` deltaP `25.8897` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.1966` n `53` status `ready` deltaP `14.4261` edge `0.636` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.1902` n `53` status `ready` deltaP `26.4985` edge `0.268` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2873` n `53` status `ready` deltaP `17.3257` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7874` n `53` status `ready` deltaP `18.0431` edge `0.0786` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
