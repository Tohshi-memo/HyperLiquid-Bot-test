# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T05:22:25.303630+00:00`
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

- `market_context_high->unknown_1h` score `1.5707` n `133` status `ready` deltaP `8.9866` edge `0.0937` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6736` n `133` status `ready` deltaP `21.5478` edge `-0.0436` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1454` n `133` status `ready` deltaP `8.8197` edge `0.0101` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->equity_1h` score `-0.168` n `133` status `ready` deltaP `7.1631` edge `0.0377` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1704` n `133` status `ready` deltaP `1.4306` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2794` n `133` status `ready` deltaP `1.5803` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3325` n `133` status `ready` deltaP `5.709` edge `-0.0191` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.6263` n `133` status `ready` deltaP `-0.3989` edge `0.0074` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6269` n `133` status `ready` deltaP `-3.6727` edge `0.0007` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6909` n `133` status `ready` deltaP `0.792` edge `0.0097` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.9403` n `133` status `ready` deltaP `0.1205` edge `0.001` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4409` n `133` status `ready` deltaP `-1.5499` edge `-0.0719` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.4487` n `105` status `ready` deltaP `-4.4395` edge `0.0922` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.8646` n `133` status `ready` deltaP `-2.7348` edge `0.0597` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4202` n `105` status `ready` deltaP `-6.2252` edge `0.0008` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.5464` n `133` status `ready` deltaP `3.8981` edge `-0.1112` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.2795` n `105` status `ready` deltaP `-6.2897` edge `-0.0565` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0847` n `105` status `ready` deltaP `-20.7143` edge `-0.183` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5513` n `133` status `ready` deltaP `-1.8017` edge `-0.3485` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
