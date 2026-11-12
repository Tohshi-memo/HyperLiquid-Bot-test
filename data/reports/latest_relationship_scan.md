# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T06:37:23.946263+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11530`

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

- `market_context_high->unknown_24h` score `186.8929` n `88` status `ready` deltaP `5.6858` edge `15.5506` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.2342` n `88` status `ready` deltaP `7.2201` edge `7.3495` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `31.0811` n `52` status `ready` deltaP `23.9486` edge `2.4916` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.8493` n `88` status `ready` deltaP `16.5185` edge `1.4498` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.9639` n `52` status `ready` deltaP `37.9491` edge `1.6056` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2951` n `53` status `ready` deltaP `33.9536` edge `0.8271` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6899` n `52` status `ready` deltaP `40.1384` edge `0.2899` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.4612` n `88` status `ready` deltaP `34.9638` edge `0.9765` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8513` n `88` status `ready` deltaP `35.0071` edge `0.2262` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2491` n `53` status `ready` deltaP `40.9084` edge `0.119` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1377` n `52` status `ready` deltaP `21.0074` edge `0.2308` maxDD `-0.4168`
- `news_risk_high->crypto_major_4h` score `3.9936` n `53` status `ready` deltaP `21.353` edge `0.3392` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5514` n `53` status `ready` deltaP `18.464` edge `0.2441` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.0058` n `88` status `ready` deltaP `16.9864` edge `0.1835` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7508` n `53` status `ready` deltaP `24.8821` edge `0.0887` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2173` n `53` status `ready` deltaP `25.2789` edge `0.2796` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1524` n `53` status `ready` deltaP `20.5937` edge `0.0857` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0768` n `53` status `ready` deltaP `24.8418` edge `0.0329` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3017` n `53` status `ready` deltaP `17.176` edge `0.0241` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.78` n `53` status `ready` deltaP `19.2407` edge `0.0769` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
