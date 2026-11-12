# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T16:07:28.796599+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11930`

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

- `market_context_high->unknown_24h` score `298.0171` n `84` status `ready` deltaP `6.4425` edge `24.8059` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `88.8257` n `93` status `ready` deltaP `8.0137` edge `7.3935` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.1919` n `53` status `ready` deltaP `21.0486` edge `2.1963` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.1745` n `84` status `ready` deltaP `18.7799` edge `1.5433` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9365` n `53` status `ready` deltaP `36.8969` edge `1.3527` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.7203` n `53` status `ready` deltaP `33.8012` edge `0.6977` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.5511` n `53` status `ready` deltaP `43.5986` edge `0.3386` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.0321` n `84` status `ready` deltaP `38.2106` edge `1.0564` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0491` n `84` status `ready` deltaP `38.8491` edge `0.2864` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6832` n `53` status `ready` deltaP `44.4145` edge `0.1318` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8245` n `84` status `ready` deltaP `20.926` edge `0.1887` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4161` n `53` status `ready` deltaP `19.129` edge `0.1875` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.1535` n `53` status `ready` deltaP `17.2664` edge `0.2107` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1468` n `53` status `ready` deltaP `21.6579` edge `0.2666` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0519` n `53` status `ready` deltaP `26.7114` edge `0.1016` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2625` n `53` status `ready` deltaP `26.4885` edge `0.0374` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8748` n `53` status `ready` deltaP `19.3741` edge `0.0707` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.5341` n `53` status `ready` deltaP `25.4314` edge `0.191` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.249` n `53` status `ready` deltaP `17.0263` edge `0.0207` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6435` n `53` status `ready` deltaP `18.6419` edge `0.0634` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
