# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T01:22:31.984529+00:00`
- Price records: `672`
- Market context records: `4677`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `77.1074` n `137` status `ready` deltaP `11.5018` edge `6.3907` maxDD `-1.674`
- `market_context_high->unknown_4h` score `4.8251` n `137` status `ready` deltaP `10.0855` edge `0.4559` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.5043` n `137` status `ready` deltaP `9.4193` edge `0.1549` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5371` n `137` status `ready` deltaP `1.5057` edge `0.0248` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.8349` n `137` status `ready` deltaP `2.9152` edge `-0.0142` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.866` n `137` status `ready` deltaP `-0.3884` edge `-0.0002` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8808` n `137` status `ready` deltaP `-3.0038` edge `0.0058` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.9896` n `137` status `ready` deltaP `-3.3601` edge `-0.0046` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2798` n `137` status `ready` deltaP `4.5865` edge `0.0161` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3949` n `137` status `ready` deltaP `0.2681` edge `-0.0037` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7618` n `137` status `ready` deltaP `-4.9499` edge `-0.0134` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8052` n `137` status `ready` deltaP `-3.772` edge `-0.0777` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6394` n `137` status `ready` deltaP `-10.4927` edge `-0.0108` maxDD `-5.4691`
- `market_context_high->commodity_24h` score `-5.0869` n `137` status `ready` deltaP `12.5139` edge `0.0431` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6226` n `137` status `ready` deltaP `-3.0038` edge `-0.1198` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7866` n `137` status `ready` deltaP `-5.905` edge `-0.1509` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.1638` n `137` status `ready` deltaP `-9.8148` edge `-0.0774` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6293` n `137` status `ready` deltaP `-3.2847` edge `-0.2187` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.3104` n `137` status `ready` deltaP `-2.232` edge `-0.2918` maxDD `-64.6236`
- `market_context_high->crypto_major_4h` score `-11.7175` n `137` status `ready` deltaP `-4.5599` edge `-0.3787` maxDD `-82.1179`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
