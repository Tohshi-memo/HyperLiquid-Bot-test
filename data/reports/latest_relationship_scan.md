# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T15:22:31.525497+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11990`

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

- `market_context_high->unknown_24h` score `293.3563` n `84` status `ready` deltaP `6.4425` edge `24.4175` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `97.2495` n `90` status `ready` deltaP `7.727` edge `8.0974` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.1463` n `53` status `ready` deltaP `21.0486` edge `2.1925` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.1289` n `84` status `ready` deltaP `18.7799` edge `1.5395` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9545` n `53` status `ready` deltaP `36.8969` edge `1.355` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.97` n `53` status `ready` deltaP `33.9536` edge `0.7175` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.4748` n `53` status `ready` deltaP `43.0796` edge `0.3357` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.9276` n `84` status `ready` deltaP `38.2106` edge `1.043` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0179` n `84` status `ready` deltaP `38.8491` edge `0.2838` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6736` n `53` status `ready` deltaP `44.4145` edge `0.131` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8401` n `84` status `ready` deltaP `20.926` edge `0.19` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4317` n `53` status `ready` deltaP `19.129` edge `0.1888` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.4234` n `53` status `ready` deltaP `17.5658` edge `0.2312` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.298` n `53` status `ready` deltaP `21.6579` edge `0.2792` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0507` n `53` status `ready` deltaP `26.7114` edge `0.1015` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2841` n `53` status `ready` deltaP `26.6382` edge `0.0382` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9486` n `53` status `ready` deltaP `19.8315` edge `0.0738` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6308` n `53` status `ready` deltaP `25.4314` edge `0.2034` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2981` n `53` status `ready` deltaP `17.3257` edge `0.0228` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7659` n `53` status `ready` deltaP `18.9413` edge `0.0771` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
