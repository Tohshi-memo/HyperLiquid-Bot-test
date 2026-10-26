# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T13:52:36.988093+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8376`

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

- `market_context_high->unknown_4h` score `15.4646` n `146` status `ready` deltaP `0.023` edge `1.3221` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5607` n `113` status `ready` deltaP `28.0973` edge `0.1516` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.1365` n `146` status `ready` deltaP `9.4387` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1095` n `151` status `ready` deltaP `6.4411` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `-0.0086` n `113` status `ready` deltaP `19.0987` edge `0.0288` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2347` n `151` status `ready` deltaP `6.9586` edge `0.0027` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3403` n `151` status `ready` deltaP `1.6963` edge `0.0104` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4096` n `113` status `ready` deltaP `11.4768` edge `-0.0008` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.4709` n `146` status `ready` deltaP `6.1581` edge `0.0426` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.565` n `151` status `ready` deltaP `-0.9071` edge `-0.0012` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.058` n `146` status `ready` deltaP `6.0245` edge `-0.0048` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.1563` n `151` status `ready` deltaP `2.4041` edge `-0.0062` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.8541` n `146` status `ready` deltaP `-4.9449` edge `-0.0173` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2094` n `151` status `ready` deltaP `-0.8615` edge `-0.0489` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.2885` n `151` status `ready` deltaP `-2.2267` edge `-0.0301` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.36` n `113` status `ready` deltaP `-1.899` edge `-0.0606` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.9556` n `146` status `ready` deltaP `-2.6625` edge `-0.1136` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0606` n `113` status `ready` deltaP `-2.4705` edge `-0.203` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4587` n `113` status `ready` deltaP `-18.6455` edge `-0.1448` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.6795` n `146` status `ready` deltaP `-4.4082` edge `-0.229` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
