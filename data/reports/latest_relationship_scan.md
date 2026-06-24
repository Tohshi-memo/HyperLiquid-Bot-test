# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T13:37:34.600194+00:00`
- Price records: `672`
- Market context records: `4626`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `70.0008` n `146` status `ready` deltaP `8.1597` edge `5.8249` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.3971` n `146` status `ready` deltaP `9.5807` edge `0.4236` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3137` n `146` status `ready` deltaP `3.398` edge `0.0308` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5652` n `146` status `ready` deltaP `-1.9502` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7713` n `146` status `ready` deltaP `1.4492` edge `-0.0003` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.85` n `146` status `ready` deltaP `-1.7964` edge `0.0017` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9054` n `146` status `ready` deltaP `1.5912` edge `-0.0144` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0511` n `146` status `ready` deltaP `5.1912` edge `0.0414` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.6539` n `144` status `ready` deltaP `4.8611` edge `-0.0779` maxDD `-4.7201`
- `market_context_high->index_1h` score `-1.6999` n `146` status `ready` deltaP `-4.2142` edge `-0.0127` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7353` n `146` status `ready` deltaP `-0.9982` edge `-0.0389` maxDD `-8.8203`
- `market_context_high->metal_1h` score `-2.951` n `146` status `ready` deltaP `-4.3905` edge `-0.0839` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6793` n `144` status `ready` deltaP `11.9791` edge `0.0551` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.1621` n `144` status `ready` deltaP `-10.4166` edge `-0.0095` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.586` n `146` status `ready` deltaP `-2.2455` edge `-0.1218` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8308` n `146` status `ready` deltaP `-5.9921` edge `-0.154` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.2783` n `144` status `ready` deltaP `-8.6806` edge `-0.0945` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2236` n `146` status `ready` deltaP `-3.6585` edge `-0.2924` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2799` n `146` status `ready` deltaP `-7.1479` edge `-0.3489` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3852` n `146` status `ready` deltaP `-5.7113` edge `-0.4554` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
