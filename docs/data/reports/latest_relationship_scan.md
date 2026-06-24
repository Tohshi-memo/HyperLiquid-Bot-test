# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T19:37:29.057513+00:00`
- Price records: `672`
- Market context records: `4652`
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

- `market_context_high->unknown_1h` score `70.2574` n `146` status `ready` deltaP `9.2076` edge `5.8393` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.3963` n `146` status `ready` deltaP `11.1051` edge `0.4967` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.6372` n `146` status `ready` deltaP `7.0848` edge `0.0982` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3737` n `146` status `ready` deltaP `3.2483` edge `0.0268` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5535` n `146` status `ready` deltaP `-1.8005` edge `-0.0035` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6029` n `146` status `ready` deltaP `-0.1497` edge `0.0224` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.6637` n `146` status `ready` deltaP `4.1827` edge `-0.0007` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7429` n `146` status `ready` deltaP `1.7541` edge `0.0013` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9097` n `146` status `ready` deltaP `2.203` edge `0.0456` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2302` n `146` status `ready` deltaP `4.5815` edge `0.0225` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6184` n `146` status `ready` deltaP `-3.6154` edge `-0.0099` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7702` n `146` status `ready` deltaP `-3.0432` edge `-0.0697` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.0278` n `146` status `ready` deltaP `-8.8589` edge `-0.0087` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.0546` n `146` status `ready` deltaP `-0.8982` edge `-0.0865` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.0548` n `146` status `ready` deltaP `11.8056` edge `0.0505` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.2694` n `146` status `ready` deltaP `-4.3454` edge `-0.1182` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.4294` n `146` status `ready` deltaP `-6.3951` edge `-0.039` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.8059` n `146` status `ready` deltaP `-0.3049` edge `-0.133` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5844` n `146` status `ready` deltaP `-3.6418` edge `-0.2831` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.9347` n `146` status `ready` deltaP `-2.3576` edge `-0.2918` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
