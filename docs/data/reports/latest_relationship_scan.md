# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T18:07:51.509080+00:00`
- Price records: `672`
- Market context records: `4645`
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

- `market_context_high->unknown_1h` score `70.1651` n `146` status `ready` deltaP `9.0579` edge `5.8326` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.0665` n `146` status `ready` deltaP `10.3429` edge `0.4743` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.0997` n `146` status `ready` deltaP `6.2167` edge `0.0592` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3701` n `146` status `ready` deltaP `2.9489` edge `0.0291` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5824` n `146` status `ready` deltaP `-2.2496` edge `-0.0042` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6925` n `146` status `ready` deltaP `-0.7485` edge `0.0149` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.7168` n `146` status `ready` deltaP `2.2114` edge `0.0016` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7628` n `146` status `ready` deltaP `3.2681` edge `-0.0073` maxDD `-5.9823`
- `market_context_high->equity_4h` score `-1.132` n `146` status `ready` deltaP `1.2884` edge `0.0232` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.1564` n `146` status `ready` deltaP `5.1912` edge `0.0279` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6759` n `146` status `ready` deltaP `-4.0645` edge `-0.0117` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8933` n `146` status `ready` deltaP `-3.7917` edge `-0.0805` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.0068` n `146` status `ready` deltaP `-8.6853` edge `-0.0081` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.1446` n `146` status `ready` deltaP `-1.0479` edge `-0.093` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.1709` n `146` status `ready` deltaP `11.2847` edge `0.0443` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.387` n `146` status `ready` deltaP `-4.4951` edge `-0.127` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.6024` n `146` status `ready` deltaP `-6.7423` edge `-0.0511` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.1561` n `146` status `ready` deltaP `-1.2195` edge `-0.1718` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.8012` n `146` status `ready` deltaP `-4.5565` edge `-0.3048` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.2787` n `146` status `ready` deltaP `-3.2723` edge `-0.3298` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
