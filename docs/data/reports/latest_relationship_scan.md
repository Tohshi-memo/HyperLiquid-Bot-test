# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T15:07:27.909987+00:00`
- Price records: `672`
- Market context records: `4632`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.014` n `146` status `ready` deltaP `8.3094` edge `5.825` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4127` n `146` status `ready` deltaP `9.5807` edge `0.4249` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3125` n `146` status `ready` deltaP `3.398` edge `0.0309` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5567` n `146` status `ready` deltaP `-1.8005` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7515` n `146` status `ready` deltaP `1.7541` edge `0.0002` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8344` n `146` status `ready` deltaP `-2.0958` edge `0.0057` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9133` n `146` status `ready` deltaP `1.4388` edge `-0.0144` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.9865` n `146` status `ready` deltaP `5.9534` edge `0.0446` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.2947` n `145` status `ready` deltaP `5.3616` edge `-0.0513` maxDD `-4.7201`
- `market_context_high->equity_4h` score `-1.6171` n `146` status `ready` deltaP `-0.5409` edge `-0.0268` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7263` n `146` status `ready` deltaP `-4.5136` edge `-0.0129` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.965` n `146` status `ready` deltaP `-4.5402` edge `-0.0847` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.9419` n `145` status `ready` deltaP `11.6295` edge `0.0493` maxDD `-30.0922`
- `market_context_high->fx_24h` score `-5.0389` n `145` status `ready` deltaP `-9.0266` edge `-0.0085` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5883` n `146` status `ready` deltaP `-2.3952` edge `-0.121` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7888` n `146` status `ready` deltaP `-5.9921` edge `-0.1505` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.0342` n `145` status `ready` deltaP `-7.9694` edge `-0.0789` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.0928` n `146` status `ready` deltaP `-3.0488` edge `-0.2797` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1802` n `146` status `ready` deltaP `-6.3857` edge `-0.3412` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.2396` n `146` status `ready` deltaP `-5.1015` edge `-0.4408` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
