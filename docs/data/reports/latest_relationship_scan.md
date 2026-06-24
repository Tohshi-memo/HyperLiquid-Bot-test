# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T18:37:40.804911+00:00`
- Price records: `672`
- Market context records: `4647`
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

- `market_context_high->unknown_1h` score `70.1627` n `146` status `ready` deltaP `9.0579` edge `5.8324` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.2037` n `146` status `ready` deltaP `10.6478` edge `0.4837` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.3596` n `146` status `ready` deltaP `6.3904` edge `0.0797` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.418` n `146` status `ready` deltaP `2.7992` edge `0.0261` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.573` n `146` status `ready` deltaP `-2.0999` edge `-0.004` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6777` n `146` status `ready` deltaP `-0.7485` edge `0.0168` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7255` n `146` status `ready` deltaP `2.059` edge `0.0015` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7282` n `146` status `ready` deltaP `3.5729` edge `-0.0049` maxDD `-5.9823`
- `market_context_high->equity_4h` score `-1.0616` n `146` status `ready` deltaP `1.5933` edge `0.0302` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1972` n `146` status `ready` deltaP `4.8864` edge `0.0247` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6675` n `146` status `ready` deltaP `-4.0645` edge `-0.011` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8606` n `146` status `ready` deltaP `-3.4923` edge `-0.0783` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.0092` n `146` status `ready` deltaP `-8.6853` edge `-0.0083` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.111` n `146` status `ready` deltaP `-1.0479` edge `-0.0902` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.1673` n `146` status `ready` deltaP `11.2847` edge `0.0446` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.3414` n `146` status `ready` deltaP `-4.4951` edge `-0.1232` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.552` n `146` status `ready` deltaP `-6.7423` edge `-0.0469` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.0162` n `146` status `ready` deltaP `-0.9146` edge `-0.1559` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.7221` n `146` status `ready` deltaP `-4.2516` edge `-0.2967` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.1388` n `146` status `ready` deltaP `-2.9674` edge `-0.3139` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
