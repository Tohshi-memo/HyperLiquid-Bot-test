# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T19:22:28.299306+00:00`
- Price records: `672`
- Market context records: `4651`
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

- `market_context_high->unknown_1h` score `70.2622` n `146` status `ready` deltaP `9.2076` edge `5.8397` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.3795` n `146` status `ready` deltaP `11.1051` edge `0.4953` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.5549` n `146` status `ready` deltaP `6.9112` edge `0.0925` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3989` n `146` status `ready` deltaP `3.0986` edge `0.0257` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5621` n `146` status `ready` deltaP `-1.9502` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6138` n `146` status `ready` deltaP `-0.2994` edge `0.022` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.6763` n `146` status `ready` deltaP `4.0303` edge `-0.0013` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7342` n `146` status `ready` deltaP `1.9066` edge `0.0014` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9379` n `146` status `ready` deltaP `2.0506` edge `0.043` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2428` n `146` status `ready` deltaP `4.429` edge `0.0219` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6148` n `146` status `ready` deltaP `-3.6154` edge `-0.0096` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7889` n `146` status `ready` deltaP `-3.1929` edge `-0.0711` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.0254` n `146` status `ready` deltaP `-8.8589` edge `-0.0085` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.0486` n `146` status `ready` deltaP `-0.8982` edge `-0.086` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.0987` n `146` status `ready` deltaP `11.6319` edge `0.048` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.2634` n `146` status `ready` deltaP `-4.3454` edge `-0.1177` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.4462` n `146` status `ready` deltaP `-6.3951` edge `-0.0404` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.838` n `146` status `ready` deltaP `-0.4573` edge `-0.1361` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.6149` n `146` status `ready` deltaP `-3.7943` edge `-0.286` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.9614` n `146` status `ready` deltaP `-2.5101` edge `-0.2942` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
