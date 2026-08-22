# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T20:52:25.443920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.5182` n `147` status `ready` deltaP `6.2009` edge `0.1079` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.7897` n `147` status `ready` deltaP `18.5592` edge `-0.014` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.081` n `147` status `ready` deltaP `7.7298` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `0.0192` n `147` status `ready` deltaP `7.6734` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1488` n `147` status `ready` deltaP `1.8769` edge `0.0043` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.3061` n `147` status `ready` deltaP `7.9777` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3116` n `147` status `ready` deltaP `5.21` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3471` n `147` status `ready` deltaP `0.3534` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5316` n `147` status `ready` deltaP `3.6005` edge `0.0114` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8842` n `147` status `ready` deltaP `-4.2196` edge `-0.0002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1078` n `147` status `ready` deltaP `-8.1775` edge `-0.0025` maxDD `-1.134`
- `market_context_high->fx_24h` score `-1.167` n `131` status `ready` deltaP `0.1802` edge `0.0101` maxDD `-2.2066`
- `market_context_high->crypto_alt_1h` score `-1.665` n `147` status `ready` deltaP `-2.9685` edge `-0.0442` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.7116` n `147` status `ready` deltaP `-0.9613` edge `0.0686` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1205` n `131` status `ready` deltaP `-4.873` edge `0.0391` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-2.4407` n `147` status `ready` deltaP `-6.4646` edge `-0.1221` maxDD `-7.8171`
- `market_context_high->crypto_alt_4h` score `-2.5995` n `147` status `ready` deltaP `2.549` edge `-0.0868` maxDD `-7.0785`
- `market_context_high->index_24h` score `-4.354` n `131` status `ready` deltaP `-6.1029` edge `-0.0368` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3681` n `131` status `ready` deltaP `-23.1195` edge `-0.2033` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.8675` n `147` status `ready` deltaP `-0.7591` edge `-0.3509` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
