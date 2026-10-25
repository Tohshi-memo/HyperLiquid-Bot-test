# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T11:52:32.156508+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `39.2931` n `113` status `ready` deltaP `-0.2914` edge `3.3099` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.5869` n `113` status `ready` deltaP `4.0207` edge `0.321` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.7946` n `53` status `ready` deltaP `17.3807` edge `0.0769` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0487` n `113` status `ready` deltaP `8.221` edge `0.0091` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0575` n `113` status `ready` deltaP `3.7094` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5469` n `113` status `ready` deltaP `-0.6319` edge `0.0087` maxDD `-1.0053`
- `market_context_high->crypto_major_24h` score `-0.5639` n `53` status `ready` deltaP `0.2031` edge `0.0289` maxDD `-4.5369`
- `market_context_high->metal_1h` score `-0.6347` n `113` status `ready` deltaP `4.6341` edge `-0.0046` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6347` n `113` status `ready` deltaP `-1.5871` edge `-0.0056` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9154` n `113` status `ready` deltaP `-3.61` edge `0.0296` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3729` n `113` status `ready` deltaP `2.0494` edge `-0.0316` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8466` n `113` status `ready` deltaP `5.2234` edge `-0.0177` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1601` n `113` status `ready` deltaP `-7.92` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->fx_24h` score `-2.1877` n `53` status `ready` deltaP `-4.812` edge `0.007` maxDD `-1.2451`
- `market_context_high->crypto_alt_1h` score `-3.109` n `113` status `ready` deltaP `-2.1594` edge `-0.0573` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.5788` n `53` status `ready` deltaP `-10.4265` edge `0.0028` maxDD `-7.1882`
- `market_context_high->crypto_alt_24h` score `-3.7811` n `53` status `ready` deltaP `4.5663` edge `-0.0499` maxDD `-30.8906`
- `market_context_high->equity_1h` score `-3.8068` n `113` status `ready` deltaP `-0.0901` edge `-0.0893` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.0724` n `53` status `ready` deltaP `-9.0802` edge `-0.1506` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-10.0316` n `113` status `ready` deltaP `-12.7428` edge `-0.2512` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
