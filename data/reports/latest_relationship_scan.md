# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T16:22:31.899502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11940`

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

- `market_context_high->unknown_24h` score `298.0363` n `84` status `ready` deltaP `6.4425` edge `24.8075` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `88.9169` n `93` status `ready` deltaP `8.0137` edge `7.4011` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.2231` n `53` status `ready` deltaP `21.0486` edge `2.1989` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.2057` n `84` status `ready` deltaP `18.7799` edge `1.5459` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9459` n `53` status `ready` deltaP `36.8969` edge `1.3539` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.6385` n `53` status `ready` deltaP `33.6487` edge `0.6919` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.5721` n `53` status `ready` deltaP `43.7716` edge `0.3392` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.0872` n `84` status `ready` deltaP `38.3836` edge `1.0623` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0599` n `84` status `ready` deltaP `38.8491` edge `0.2873` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6868` n `53` status `ready` deltaP `44.4145` edge `0.1321` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8221` n `84` status `ready` deltaP `20.926` edge `0.1885` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4137` n `53` status `ready` deltaP `19.129` edge `0.1873` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.1132` n `53` status `ready` deltaP `21.6579` edge `0.2638` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0483` n `53` status `ready` deltaP `26.7114` edge `0.1013` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.0479` n `53` status `ready` deltaP `17.1167` edge `0.2029` maxDD `-3.7082`
- `news_risk_high->metal_1h` score `2.2421` n `53` status `ready` deltaP `26.3388` edge `0.0367` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.853` n `53` status `ready` deltaP `19.2217` edge `0.0699` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.502` n `53` status `ready` deltaP `25.2789` edge `0.1879` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2286` n `53` status `ready` deltaP `16.8766` edge `0.02` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6061` n `53` status `ready` deltaP `18.4922` edge `0.0596` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
