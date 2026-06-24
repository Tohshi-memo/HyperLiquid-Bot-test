# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T21:22:28.886194+00:00`
- Price records: `672`
- Market context records: `4660`
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

- `market_context_high->unknown_1h` score `70.4327` n `146` status `ready` deltaP `8.9082` edge `5.8559` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.0537` n `146` status `ready` deltaP `10.6478` edge `0.4712` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.1808` n `146` status `ready` deltaP `8.3001` edge `0.1354` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.43` n `146` status `ready` deltaP `2.7992` edge `0.0251` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5738` n `146` status `ready` deltaP `-2.0999` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6527` n `146` status `ready` deltaP `4.3351` edge `-0.0003` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.744` n `146` status `ready` deltaP `-0.7485` edge `0.0083` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7896` n `146` status `ready` deltaP `0.9919` edge `0.0004` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9416` n `146` status `ready` deltaP `2.3555` edge `0.0405` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2614` n `146` status `ready` deltaP `4.5815` edge `0.0185` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6999` n `146` status `ready` deltaP `-4.2142` edge `-0.0127` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.7881` n `146` status `ready` deltaP `-3.1929` edge `-0.071` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.8232` n `146` status `ready` deltaP `13.0208` edge `0.0617` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.135` n `146` status `ready` deltaP `-0.7485` edge `-0.0942` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.1431` n `146` status `ready` deltaP `-10.0742` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_major_1h` score `-6.3606` n `146` status `ready` deltaP `-4.3454` edge `-0.1258` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3634` n `146` status `ready` deltaP `-6.3951` edge `-0.0335` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.7892` n `146` status `ready` deltaP `0.0` edge `-0.1329` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4674` n `146` status `ready` deltaP `-2.7272` edge `-0.2742` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-10.9502` n `146` status `ready` deltaP `-2.2052` edge `-0.2948` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
