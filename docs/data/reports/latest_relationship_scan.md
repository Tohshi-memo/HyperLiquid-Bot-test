# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T14:22:29.558273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5252`

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

- `market_context_high->unknown_4h` score `37.3069` n `113` status `ready` deltaP `-0.4439` edge `3.1454` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.1133` n `62` status `ready` deltaP `7.9413` edge `0.0474` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0207` n `113` status `ready` deltaP `7.9161` edge `0.0088` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0661` n `113` status `ready` deltaP `3.5597` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5182` n `113` status `ready` deltaP `-0.3325` edge `0.0091` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.662` n `113` status `ready` deltaP `-2.0362` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6635` n `113` status `ready` deltaP `4.3347` edge `-0.005` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.8798` n `113` status `ready` deltaP `-3.0003` edge `0.0301` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.3012` n `62` status `ready` deltaP `-5.606` edge `-0.0269` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3683` n `113` status `ready` deltaP `2.4985` edge `-0.034` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5142` n `62` status `ready` deltaP `3.1418` edge `0.0101` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.888` n `113` status `ready` deltaP `4.7661` edge `-0.0181` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1232` n `62` status `ready` deltaP `-1.9321` edge `-0.1311` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1854` n `113` status `ready` deltaP `-8.3774` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1175` n `113` status `ready` deltaP `-1.7103` edge `-0.061` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7585` n `62` status `ready` deltaP `-10.1367` edge `0.0214` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8655` n `113` status `ready` deltaP `-0.3895` edge `-0.0922` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.3244` n `62` status `ready` deltaP `-3.1026` edge `-0.2727` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9836` n `113` status `ready` deltaP `-12.7428` edge `-0.2472` maxDD `-32.9851`
- `market_context_high->unknown_1h` score `-11.7862` n `113` status `ready` deltaP `3.7213` edge `-0.9581` maxDD `-1.5781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
