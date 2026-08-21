# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T16:37:26.548302+00:00`
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

- `market_context_high->unknown_1h` score `0.2532` n `133` status `ready` deltaP `8.0884` edge `-0.0101` maxDD `-0.4843`
- `market_context_high->index_1h` score `0.1483` n `133` status `ready` deltaP `10.1571` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.0175` n `123` status `ready` deltaP `6.5548` edge `0.0088` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.0926` n `133` status `ready` deltaP `2.9276` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2334` n `133` status `ready` deltaP `6.4146` edge `0.0343` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3262` n `133` status `ready` deltaP `0.8318` edge `-0.0055` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.5903` n `123` status `ready` deltaP `1.7276` edge `-0.0256` maxDD `-1.5942`
- `market_context_high->commodity_24h` score `-0.6565` n `105` status `ready` deltaP `2.8522` edge `0.1096` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-0.662` n `133` status `ready` deltaP `0.5696` edge `0.0212` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.6628` n `133` status `ready` deltaP `-4.2715` edge `0.0001` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6991` n `123` status `ready` deltaP `0.5081` edge `0.0085` maxDD `-2.4544`
- `market_context_high->commodity_4h` score `-0.7014` n `123` status `ready` deltaP `-1.8293` edge `0.0073` maxDD `-2.4692`
- `market_context_high->unknown_4h` score `-0.9176` n `123` status `ready` deltaP `20.7825` edge `-0.1711` maxDD `-0.5133`
- `market_context_high->crypto_major_1h` score `-1.1726` n `133` status `ready` deltaP `-0.9511` edge `-0.0415` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.3712` n `123` status `ready` deltaP `3.0488` edge `-0.0076` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.3907` n `123` status `ready` deltaP `-1.626` edge `0.0656` maxDD `-13.9778`
- `market_context_high->fx_24h` score `-2.8064` n `105` status `ready` deltaP `-10.3919` edge `-0.0036` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-3.839` n `123` status `ready` deltaP `0.1017` edge `-0.2185` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2472` n `105` status `ready` deltaP `-6.4633` edge `-0.0512` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.6403` n `105` status `ready` deltaP `-17.7629` edge `-0.1457` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
