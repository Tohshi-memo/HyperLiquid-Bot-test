# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T14:07:36.824098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.8177` n `148` status `ready` deltaP `6.4898` edge `0.0476` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5233` n `143` status `ready` deltaP `18.4835` edge `-0.0357` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.104` n `143` status `ready` deltaP `8.0686` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0323` n `148` status `ready` deltaP `6.6839` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0588` n `148` status `ready` deltaP `3.5321` edge `0.0048` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2322` n `143` status `ready` deltaP `7.3235` edge `-0.017` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3216` n `148` status `ready` deltaP `0.8294` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3533` n `148` status `ready` deltaP `4.4384` edge `0.0321` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4935` n `143` status `ready` deltaP `4.3035` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.824` n `143` status `ready` deltaP `-3.2118` edge `0.0008` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0757` n `148` status `ready` deltaP `-8.0272` edge `-0.0028` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.6313` n `129` status `ready` deltaP `2.047` edge `0.0114` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7485` n `143` status `ready` deltaP `-1.7578` edge `0.0682` maxDD `-16.1188`
- `market_context_high->commodity_24h` score `-2.1694` n `129` status `ready` deltaP `-5.7534` edge `0.0409` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.2982` n `143` status `ready` deltaP `4.0498` edge `-0.0717` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.4612` n `148` status `ready` deltaP `-2.2981` edge `-0.0403` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5364` n `148` status `ready` deltaP `-5.1586` edge `-0.1144` maxDD `-7.6729`
- `market_context_high->index_24h` score `-4.5488` n `129` status `ready` deltaP `-9.2498` edge `-0.0415` maxDD `-21.0679`
- `market_context_high->metal_24h` score `-5.5356` n `129` status `ready` deltaP `-25.6057` edge `-0.2082` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.579` n `143` status `ready` deltaP `-0.6929` edge `-0.3273` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
