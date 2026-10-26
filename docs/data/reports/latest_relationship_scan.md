# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T01:22:29.922133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5070`

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

- `market_context_high->unknown_4h` score `29.9589` n `113` status `ready` deltaP `-0.7487` edge `2.5351` maxDD `-1.016`
- `market_context_high->fx_24h` score `-0.0662` n `92` status `ready` deltaP `18.4556` edge `0.0257` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0996` n `113` status `ready` deltaP `2.9609` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.101` n `113` status `ready` deltaP `6.5441` edge `0.0078` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.2057` n `92` status `ready` deltaP `17.7385` edge `0.1224` maxDD `-7.3625`
- `market_context_high->crypto_major_24h` score `-0.4054` n `92` status `ready` deltaP `3.9175` edge `0.0495` maxDD `-5.0856`
- `market_context_high->commodity_1h` score `-0.4175` n `113` status `ready` deltaP `0.5657` edge `0.0115` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6238` n `113` status `ready` deltaP `-1.4374` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6263` n `113` status `ready` deltaP `4.7838` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.6638` n `113` status `ready` deltaP `-0.2564` edge `0.0395` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.7988` n `92` status `ready` deltaP `10.9677` edge `-0.0473` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2577` n `113` status `ready` deltaP `3.9955` edge `-0.0298` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0156` n `113` status `ready` deltaP `3.5466` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1514` n `113` status `ready` deltaP `-7.7676` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1152` n `113` status `ready` deltaP `-1.1115` edge `-0.0648` maxDD `-11.3243`
- `market_context_high->commodity_24h` score `-3.6373` n `92` status `ready` deltaP `-11.5187` edge `-0.076` maxDD `-11.4158`
- `market_context_high->equity_1h` score `-3.7828` n `113` status `ready` deltaP `-0.0901` edge `-0.0873` maxDD `-12.1865`
- `market_context_high->equity_24h` score `-7.3031` n `92` status `ready` deltaP `0.3095` edge `-0.41` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-8.5357` n `92` status `ready` deltaP `-7.1332` edge `-0.3115` maxDD `-49.4877`
- `market_context_high->crypto_major_4h` score `-9.9872` n `113` status `ready` deltaP `-12.7428` edge `-0.2475` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
