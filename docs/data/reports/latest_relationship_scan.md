# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T19:52:26.688179+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `1.2036` n `133` status `ready` deltaP `8.3878` edge `0.0671` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.2073` n `133` status `ready` deltaP `10.0392` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1826` n `133` status `ready` deltaP `10.7559` edge `0.0048` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `-0.0314` n `133` status `ready` deltaP `21.0904` edge `-0.0993` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1159` n `133` status `ready` deltaP `2.4785` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2163` n `133` status `ready` deltaP `6.5643` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3519` n `133` status `ready` deltaP `0.3827` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4859` n `133` status `ready` deltaP `3.27` edge `-0.0225` maxDD `-1.5942`
- `market_context_high->crypto_alt_1h` score `-0.5816` n `133` status `ready` deltaP `0.869` edge `0.0259` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.5942` n `133` status `ready` deltaP `2.6213` edge `0.0099` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6675` n `133` status `ready` deltaP `-1.1611` edge `0.0072` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6768` n `133` status `ready` deltaP `-4.5709` edge `0.0003` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.9211` n `105` status `ready` deltaP `0.5953` edge `0.1026` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1625` n `133` status `ready` deltaP `-0.9511` edge `-0.0402` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3988` n `133` status `ready` deltaP `3.2884` edge `-0.0115` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8486` n `133` status `ready` deltaP `-2.2774` edge `0.0587` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.5934` n `105` status `ready` deltaP `-8.1349` edge `-0.0009` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.9907` n `133` status `ready` deltaP `-0.4298` edge `-0.2276` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2613` n `105` status `ready` deltaP `-6.4633` edge `-0.053` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7817` n `105` status `ready` deltaP `-18.4574` edge `-0.1592` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
