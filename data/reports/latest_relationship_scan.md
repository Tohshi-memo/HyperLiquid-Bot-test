# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T14:37:28.415580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->fx_4h` score `0.1258` n `115` status `ready` deltaP `8.5034` edge `0.0097` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1109` n `127` status `ready` deltaP `9.582` edge `0.0032` maxDD `-0.8955`
- `market_context_high->fx_1h` score `-0.0958` n `127` status `ready` deltaP `2.8667` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1324` n `127` status `ready` deltaP `6.4772` edge `0.0362` maxDD `-4.375`
- `market_context_high->metal_1h` score `-0.2986` n `127` status `ready` deltaP `0.9206` edge `-0.0048` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.3932` n `115` status `ready` deltaP `4.2696` edge `-0.0213` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.4626` n `115` status `ready` deltaP `3.6705` edge `0.012` maxDD `-1.9958`
- `market_context_high->commodity_24h` score `-0.4902` n `105` status `ready` deltaP `4.2411` edge `0.1142` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5289` n `127` status `ready` deltaP `9.1117` edge `-0.0821` maxDD `-0.4843`
- `market_context_high->equity_4h` score `-0.5822` n `115` status `ready` deltaP `1.8757` edge `0.0972` maxDD `-10.0811`
- `market_context_high->commodity_4h` score `-0.6803` n `115` status `ready` deltaP `-1.7828` edge `0.0097` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6971` n `127` status `ready` deltaP `-4.9625` edge `0.0003` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.8174` n `127` status `ready` deltaP `-0.0377` edge `0.0123` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.2818` n `127` status `ready` deltaP `-2.1064` edge `-0.0478` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.2169` n `115` status `ready` deltaP `1.0128` edge `-0.0645` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.9415` n `105` status `ready` deltaP `-11.7808` edge `-0.0056` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.201` n `105` status `ready` deltaP `-5.7689` edge `-0.0499` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3962` n `115` status `ready` deltaP `-1.5681` edge `-0.2538` maxDD `-3.1677`
- `market_context_high->unknown_4h` score `-4.5325` n `115` status `ready` deltaP `19.6514` edge `-0.4648` maxDD `-0.5133`
- `market_context_high->metal_24h` score `-4.5359` n `105` status `ready` deltaP `-16.8949` edge `-0.1381` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
