# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T15:37:34.511020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `32.4241` n `51` status `ready` deltaP `22.1711` edge `2.5585` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `5.4731` n `51` status `ready` deltaP `30.3206` edge `0.2911` maxDD `-1.3053`
- `market_context_high->commodity_24h` score `5.4532` n `51` status `ready` deltaP `30.913` edge `0.3327` maxDD `-5.0817`
- `market_context_high->unknown_4h` score `5.1873` n `89` status `ready` deltaP `-0.1319` edge `0.5327` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0787` n `89` status `ready` deltaP `14.4628` edge `0.0781` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2229` n `89` status `ready` deltaP `15.8965` edge `0.0086` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.198` n `89` status `ready` deltaP `5.3556` edge `0.0224` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.501` n `89` status `ready` deltaP `1.016` edge `-0.0176` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5504` n `89` status `ready` deltaP `-1.682` edge `-0.0099` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6295` n `89` status `ready` deltaP `4.1193` edge `0.0153` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8108` n `89` status `ready` deltaP `4.7907` edge `0.0031` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.0607` n `89` status `ready` deltaP `-1.8351` edge `-0.0051` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-1.4324` n `51` status `ready` deltaP `-2.3387` edge `0.0168` maxDD `-4.3126`
- `market_context_high->equity_1h` score `-1.7013` n `89` status `ready` deltaP `4.5381` edge `-0.0948` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8788` n `89` status `ready` deltaP `-10.2785` edge `-0.0469` maxDD `-4.7021`
- `market_context_high->metal_24h` score `-2.409` n `51` status `ready` deltaP `-20.5065` edge `-0.0553` maxDD `-2.6802`
- `market_context_high->unknown_1h` score `-3.4158` n `89` status `ready` deltaP `2.661` edge `-0.2577` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4845` n `89` status `ready` deltaP `-12.3966` edge `-0.0704` maxDD `-7.6533`
- `market_context_high->index_24h` score `-4.7261` n `51` status `ready` deltaP `-24.7243` edge `-0.2216` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
