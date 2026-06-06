# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T22:22:25.279381+00:00`
- Price records: `672`
- Market context records: `3118`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

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

- `market_context_high->commodity_24h` score `14.6642` n `96` status `ready` deltaP `46.7014` edge `0.9535` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.7226` n `96` status `ready` deltaP `11.1111` edge `2.366` maxDD `-56.0513`
- `market_context_high->unknown_24h` score `12.5985` n `96` status `ready` deltaP `21.7014` edge `0.954` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.241` n `96` status `ready` deltaP `31.9445` edge `0.8959` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.281` n `96` status `ready` deltaP `13.3681` edge `1.3211` maxDD `-48.3203`
- `market_context_high->commodity_4h` score `2.9944` n `122` status `ready` deltaP `18.2452` edge `0.1737` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0326` n `134` status `ready` deltaP `2.6812` edge `0.0271` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.415` n `134` status `ready` deltaP `4.9312` edge `0.0202` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5458` n `96` status `ready` deltaP `4.1667` edge `-0.0005` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7491` n `134` status `ready` deltaP `3.4386` edge `0.094` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.039` n `134` status `ready` deltaP `0.7463` edge `0.0104` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1298` n `134` status `ready` deltaP `-10.7427` edge `-0.0057` maxDD `-0.736`
- `market_context_high->fx_4h` score `-1.3836` n `122` status `ready` deltaP `-13.1722` edge `-0.0052` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3841` n `122` status `ready` deltaP `10.1784` edge `0.0456` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.0848` n `134` status `ready` deltaP `-0.4268` edge `0.0554` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.189` n `134` status `ready` deltaP `-5.3624` edge `-0.0073` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.2164` n `122` status `ready` deltaP `3.1662` edge `-0.001` maxDD `-14.051`
- `market_context_high->unknown_1h` score `-2.77` n `134` status `ready` deltaP `3.2711` edge `-0.05` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.858` n `122` status `ready` deltaP `12.5949` edge `0.2259` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.968` n `122` status `ready` deltaP `6.6523` edge `-0.0225` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
