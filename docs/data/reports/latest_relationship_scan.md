# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T22:22:33.134271+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4053`

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

- `market_context_high->unknown_24h` score `1490.9898` n `98` status `ready` deltaP `3.4722` edge `124.226` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.6014` n `98` status `ready` deltaP `47.0592` edge `2.0135` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6971` n `98` status `ready` deltaP `33.1208` edge `1.8758` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4937` n `98` status `ready` deltaP `-0.666` edge `0.0013` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7525` n `98` status `ready` deltaP `-1.1044` edge `0.1919` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8577` n `98` status `ready` deltaP `16.0501` edge `0.144` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.052` n `98` status `ready` deltaP `-5.0196` edge `-0.0027` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2515` n `98` status `ready` deltaP `-2.5571` edge `0.0069` maxDD `-7.6911`
- `market_context_high->crypto_major_4h` score `-1.3161` n `98` status `ready` deltaP `-3.2977` edge `0.2115` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.3197` n `98` status `ready` deltaP `-8.148` edge `-0.001` maxDD `-0.3721`
- `market_context_high->metal_4h` score `-1.3848` n `98` status `ready` deltaP `5.5221` edge `-0.0215` maxDD `-6.1238`
- `market_context_high->crypto_major_1h` score `-2.2938` n `98` status `ready` deltaP `-2.4349` edge `0.0118` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9119` n `98` status `ready` deltaP `-12.1982` edge `-0.027` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.963` n `98` status `ready` deltaP `-15.9721` edge `-0.0357` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.5214` n `98` status `ready` deltaP `-1.387` edge `-0.0656` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.612` n `98` status `ready` deltaP `-25.4542` edge `-0.0104` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.6311` n `98` status `ready` deltaP `-17.7721` edge `-0.0032` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8317` n `98` status `ready` deltaP `-27.7159` edge `-0.1218` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.636` n `98` status `ready` deltaP `-10.8666` edge `-0.105` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.5288` n `98` status `ready` deltaP `-18.8496` edge `-0.3163` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
