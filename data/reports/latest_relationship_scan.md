# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T19:07:31.032574+00:00`
- Price records: `672`
- Market context records: `4649`
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

- `market_context_high->unknown_1h` score `70.2107` n `146` status `ready` deltaP `9.0579` edge `5.8364` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `5.3181` n `146` status `ready` deltaP `10.9526` edge `0.4912` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `0.4798` n `146` status `ready` deltaP `6.7376` edge `0.0874` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4157` n `146` status `ready` deltaP `2.9489` edge `0.0253` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5621` n `146` status `ready` deltaP `-1.9502` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6341` n `146` status `ready` deltaP `-0.4491` edge `0.0204` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.6936` n `146` status `ready` deltaP `3.8778` edge `-0.0025` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.7263` n `146` status `ready` deltaP `2.059` edge `0.0014` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9755` n `146` status `ready` deltaP `1.8982` edge `0.0392` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2302` n `146` status `ready` deltaP `4.5815` edge `0.0225` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6316` n `146` status `ready` deltaP `-3.7651` edge `-0.01` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8099` n `146` status `ready` deltaP `-3.3426` edge `-0.0728` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.0104` n `146` status `ready` deltaP `-8.6853` edge `-0.0084` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.0822` n `146` status `ready` deltaP `-1.0479` edge `-0.0878` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.1294` n `146` status `ready` deltaP `11.4583` edge `0.0466` maxDD `-30.7016`
- `market_context_high->crypto_major_1h` score `-6.303` n `146` status `ready` deltaP `-4.4951` edge `-0.12` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.4853` n `146` status `ready` deltaP `-6.5687` edge `-0.0425` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.8911` n `146` status `ready` deltaP `-0.6098` edge `-0.1419` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.6509` n `146` status `ready` deltaP `-3.9467` edge `-0.2896` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.0145` n `146` status `ready` deltaP `-2.6625` edge `-0.3` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
