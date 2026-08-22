# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T05:14:02.943366+00:00`
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

- `market_context_high->unknown_1h` score `1.2119` n `133` status `ready` deltaP `8.9866` edge `0.0638` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.7074` n `133` status `ready` deltaP `21.7002` edge `-0.0418` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1533` n `133` status `ready` deltaP `8.9722` edge `0.0101` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1704` n `133` status `ready` deltaP `1.4306` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.175` n `133` status `ready` deltaP `7.1631` edge `0.0368` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2802` n `133` status `ready` deltaP `1.5803` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3349` n `133` status `ready` deltaP `5.709` edge `-0.0194` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.6152` n `133` status `ready` deltaP `-0.2464` edge `0.0078` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6269` n `133` status `ready` deltaP `-3.6727` edge `0.0007` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6917` n `133` status `ready` deltaP `0.792` edge `0.0096` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-1.0567` n `133` status `ready` deltaP `-0.0292` edge `-0.0077` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.4288` n `105` status `ready` deltaP `-4.2658` edge `0.0927` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.4916` n `133` status `ready` deltaP `-1.5499` edge `-0.0784` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8716` n `133` status `ready` deltaP `-2.7348` edge `0.0588` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4051` n `105` status `ready` deltaP `-6.0516` edge `0.0009` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.6066` n `133` status `ready` deltaP `3.7457` edge `-0.1152` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.2901` n `105` status `ready` deltaP `-6.4633` edge `-0.0567` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.084` n `105` status `ready` deltaP `-20.7143` edge `-0.1829` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5693` n `133` status `ready` deltaP `-1.8017` edge `-0.35` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
