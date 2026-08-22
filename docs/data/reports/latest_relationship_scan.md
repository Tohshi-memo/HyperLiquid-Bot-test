# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T21:07:27.085012+00:00`
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

- `market_context_high->unknown_1h` score `1.5843` n `146` status `ready` deltaP `6.6669` edge `0.1103` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.7799` n `146` status `ready` deltaP `18.466` edge `-0.0142` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0952` n `146` status `ready` deltaP `7.9874` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `0.0127` n `146` status `ready` deltaP `7.5342` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.165` n `146` status `ready` deltaP `1.5647` edge `0.0043` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2806` n `146` status `ready` deltaP `8.2818` edge `-0.017` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3264` n `146` status `ready` deltaP `4.9258` edge `0.0323` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3566` n `146` status `ready` deltaP `0.1723` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5414` n `146` status `ready` deltaP `3.4268` edge `0.0113` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8692` n `146` status `ready` deltaP `-3.9759` edge `0.0001` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0997` n `146` status `ready` deltaP `-8.0244` edge `-0.0025` maxDD `-1.1328`
- `market_context_high->fx_24h` score `-1.1614` n `130` status `ready` deltaP `0.3178` edge `0.0099` maxDD `-2.2066`
- `market_context_high->crypto_alt_1h` score `-1.6626` n `146` status `ready` deltaP `-3.117` edge `-0.0429` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.7021` n `146` status `ready` deltaP `-0.7642` edge `0.0685` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1227` n `130` status `ready` deltaP `-5.1255` edge `0.0406` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-2.4449` n `146` status `ready` deltaP `-6.6504` edge `-0.1214` maxDD `-7.8171`
- `market_context_high->crypto_alt_4h` score `-2.5006` n `146` status `ready` deltaP `3.0196` edge `-0.0817` maxDD `-7.0785`
- `market_context_high->index_24h` score `-4.3791` n `130` status `ready` deltaP `-6.4049` edge `-0.038` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3823` n `130` status `ready` deltaP `-23.3921` edge `-0.2033` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.8198` n `146` status `ready` deltaP `-0.4782` edge `-0.3488` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
