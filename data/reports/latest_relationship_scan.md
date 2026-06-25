# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T04:52:28.916398+00:00`
- Price records: `672`
- Market context records: `4691`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9744`

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

- `market_context_high->unknown_1h` score `78.7142` n `135` status `ready` deltaP `12.1757` edge `6.5201` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2072` n `135` status `ready` deltaP `10.9169` edge `0.4822` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1118` n `135` status `ready` deltaP `11.4931` edge `0.1917` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5674` n `135` status `ready` deltaP `1.3074` edge `0.0236` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7796` n `135` status `ready` deltaP `3.7692` edge `-0.0128` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8796` n `135` status `ready` deltaP `-3.0417` edge `0.0062` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9449` n `135` status `ready` deltaP `-1.6351` edge `-0.002` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0478` n `135` status `ready` deltaP `-4.043` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.2521` n `135` status `ready` deltaP `1.3946` edge `0.0071` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2565` n `135` status `ready` deltaP `5.2462` edge `0.0147` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.8079` n `135` status `ready` deltaP `-5.5866` edge `-0.013` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8676` n `135` status `ready` deltaP `-4.4766` edge `-0.081` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7316` n `135` status `ready` deltaP `-12.5232` edge `-0.0148` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.8248` n `135` status `ready` deltaP `14.1551` edge `0.054` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5628` n `135` status `ready` deltaP `-2.301` edge `-0.1195` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7083` n `135` status `ready` deltaP `-5.1065` edge `-0.1497` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3879` n `135` status `ready` deltaP `-10.6366` edge `-0.0906` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6368` n `135` status `ready` deltaP `-3.1595` edge `-0.2205` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.162` n `135` status `ready` deltaP `-0.7012` edge `-0.2846` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6329` n `135` status `ready` deltaP `-3.5953` edge `-0.3774` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
