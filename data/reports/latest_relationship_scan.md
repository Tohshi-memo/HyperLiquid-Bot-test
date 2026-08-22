# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T07:37:27.096444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.4232` n `133` status `ready` deltaP `8.3878` edge `0.0854` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5439` n `133` status `ready` deltaP `20.4807` edge `-0.0473` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1782` n `133` status `ready` deltaP `1.2809` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1859` n `133` status `ready` deltaP `6.8637` edge `0.0374` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.2487` n `133` status `ready` deltaP `7.0809` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2794` n `133` status `ready` deltaP `1.5803` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.6472` n `133` status `ready` deltaP `-3.8224` edge `-0.0009` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6632` n `133` status `ready` deltaP `1.2494` edge `0.0102` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7139` n `133` status `ready` deltaP `-1.6184` edge `0.0043` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.9174` n `133` status `ready` deltaP `-0.628` edge `0.0079` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4665` n `133` status `ready` deltaP `-2.2984` edge `-0.0702` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5879` n `105` status `ready` deltaP `-5.6547` edge `0.0887` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.7749` n `133` status `ready` deltaP `-1.8201` edge `0.0651` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.1437` n `133` status `ready` deltaP `4.5079` edge `-0.0817` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5536` n `105` status `ready` deltaP `-7.7877` edge `0.0001` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1842` n `105` status `ready` deltaP `-4.7272` edge `-0.0547` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0478` n `105` status `ready` deltaP `-20.0199` edge `-0.1829` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5011` n `133` status `ready` deltaP `-1.9542` edge `-0.3433` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
