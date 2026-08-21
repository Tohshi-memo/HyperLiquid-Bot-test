# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T21:22:30.645740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.2383` n `133` status `ready` deltaP `8.6872` edge `0.068` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2564` n `133` status `ready` deltaP `21.8526` edge `-0.0804` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.2145` n `133` status `ready` deltaP `11.3547` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1574` n `133` status `ready` deltaP `9.1246` edge `0.0096` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1004` n `133` status `ready` deltaP `2.7779` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2155` n `133` status `ready` deltaP `6.5643` edge `0.0356` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3254` n `133` status `ready` deltaP `0.8318` edge `-0.0054` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4369` n `133` status `ready` deltaP `4.0321` edge `-0.0213` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5673` n `133` status `ready` deltaP `3.0786` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6185` n `133` status `ready` deltaP `-0.3989` edge `0.0084` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6776` n `133` status `ready` deltaP `-4.5709` edge `0.0002` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.686` n `133` status `ready` deltaP `0.7193` edge `0.0182` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-0.9783` n `105` status `ready` deltaP `0.0744` edge `0.1013` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.2467` n `133` status `ready` deltaP `-1.5499` edge `-0.047` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3164` n `133` status `ready` deltaP `3.8981` edge `-0.0087` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.813` n `133` status `ready` deltaP `-1.6677` edge `0.0592` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4969` n `105` status `ready` deltaP `-7.0933` edge `0.0002` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9615` n `133` status `ready` deltaP `-0.1249` edge `-0.2272` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2871` n `105` status `ready` deltaP `-6.8105` edge `-0.054` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.8207` n `105` status `ready` deltaP `-18.4574` edge `-0.1642` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
