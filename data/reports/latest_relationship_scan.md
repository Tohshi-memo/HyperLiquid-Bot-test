# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T16:52:28.803830+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11686`

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

- `market_context_high->unknown_24h` score `299.7463` n `84` status `ready` deltaP `6.4425` edge `24.95` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `89.1725` n `93` status `ready` deltaP `8.0137` edge `7.4224` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.3594` n `53` status `ready` deltaP `21.2216` edge `2.2091` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.342` n `84` status `ready` deltaP `18.9529` edge `1.5561` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9997` n `53` status `ready` deltaP `36.8969` edge `1.3608` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.5445` n `53` status `ready` deltaP `33.3438` edge `0.6861` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.5757` n `53` status `ready` deltaP `43.7716` edge `0.3395` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.2448` n `84` status `ready` deltaP `38.7296` edge `1.0802` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0875` n `84` status `ready` deltaP `38.8491` edge `0.2896` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6964` n `53` status `ready` deltaP `44.4145` edge `0.1329` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8233` n `84` status `ready` deltaP `20.926` edge `0.1886` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.4149` n `53` status `ready` deltaP `19.129` edge `0.1874` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.1012` n `53` status `ready` deltaP `21.6579` edge `0.2628` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0411` n `53` status `ready` deltaP `26.7114` edge `0.1007` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.0287` n `53` status `ready` deltaP `17.1167` edge `0.2013` maxDD `-3.7082`
- `news_risk_high->metal_1h` score `2.2409` n `53` status `ready` deltaP `26.3388` edge `0.0366` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.813` n `53` status `ready` deltaP `18.9168` edge `0.0686` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.517` n `53` status `ready` deltaP `25.4314` edge `0.1888` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1998` n `53` status `ready` deltaP `16.5772` edge `0.0196` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.5913` n `53` status `ready` deltaP `18.3425` edge `0.0587` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
