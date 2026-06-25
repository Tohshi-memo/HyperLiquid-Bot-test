# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T12:22:27.038263+00:00`
- Price records: `672`
- Market context records: `4722`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `77.0719` n `144` status `ready` deltaP `14.7622` edge `6.366` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.5633` n `144` status `ready` deltaP `14.6172` edge `0.4872` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.213` n `135` status `ready` deltaP `16.5278` edge `0.2499` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2757` n `144` status `ready` deltaP `2.7071` edge `0.0262` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6359` n `144` status `ready` deltaP `4.9289` edge `-0.0021` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8551` n `144` status `ready` deltaP `9.7391` edge `0.0362` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9066` n `144` status `ready` deltaP `-0.8977` edge `-0.002` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9485` n `144` status `ready` deltaP `3.5569` edge `0.0316` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1138` n `144` status `ready` deltaP `-1.2932` edge `0.0145` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2697` n `144` status `ready` deltaP `-4.8362` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.5918` n `144` status `ready` deltaP `-3.4847` edge `-0.009` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1216` n `144` status `ready` deltaP `-0.341` edge `-0.0692` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.5976` n `144` status `ready` deltaP `-0.3826` edge `-0.0834` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3955` n `135` status `ready` deltaP `17.1065` edge `0.0701` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4365` n `144` status `ready` deltaP `-5.4766` edge `-0.0764` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8117` n `135` status `ready` deltaP `-13.044` edge `-0.018` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-7.969` n `144` status `ready` deltaP `-2.0326` edge `-0.1424` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4841` n `135` status `ready` deltaP `-10.9838` edge `-0.0963` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.7485` n `144` status `ready` deltaP `2.2866` edge `-0.2515` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.5291` n `144` status `ready` deltaP `-1.5074` edge `-0.2498` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
