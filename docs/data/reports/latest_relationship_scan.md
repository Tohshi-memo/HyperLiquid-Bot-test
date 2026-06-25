# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T11:52:33.838839+00:00`
- Price records: `672`
- Market context records: `4720`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7430`

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

- `market_context_high->unknown_1h` score `77.0551` n `144` status `ready` deltaP `14.6125` edge `6.3656` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.3673` n `144` status `ready` deltaP `14.3123` edge `0.4729` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.1679` n `135` status `ready` deltaP `16.3542` edge `0.2473` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2796` n `144` status `ready` deltaP `2.7071` edge `0.0257` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6508` n `144` status `ready` deltaP `4.7765` edge `-0.003` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8755` n `144` status `ready` deltaP `9.5867` edge `0.0346` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.9232` n `144` status `ready` deltaP `-1.2026` edge `-0.0021` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9925` n `144` status `ready` deltaP `3.2521` edge `0.028` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1282` n `144` status `ready` deltaP `-1.4429` edge `0.0143` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2816` n `144` status `ready` deltaP `-4.9859` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6241` n `144` status `ready` deltaP `-3.7841` edge `-0.0097` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1192` n `144` status `ready` deltaP `-0.341` edge `-0.0689` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.614` n `144` status `ready` deltaP `-0.5323` edge `-0.0845` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.3883` n `135` status `ready` deltaP `17.1065` edge `0.0707` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4222` n `144` status `ready` deltaP `-5.3269` edge `-0.0762` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8081` n `135` status `ready` deltaP `-13.044` edge `-0.0177` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-7.9878` n `144` status `ready` deltaP `-2.0326` edge `-0.1448` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.4347` n `135` status `ready` deltaP `-10.6366` edge `-0.0945` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.717` n `144` status `ready` deltaP `2.5915` edge `-0.2495` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.5987` n `144` status `ready` deltaP `-1.8123` edge `-0.2567` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
