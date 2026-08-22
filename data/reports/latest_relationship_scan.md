# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T10:22:24.575750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.1004` n `140` status `ready` deltaP `7.2627` edge `0.066` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3925` n `133` status `ready` deltaP `19.4136` edge `-0.0528` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0353` n `140` status `ready` deltaP `7.9384` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0757` n `140` status `ready` deltaP `3.2378` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2434` n `140` status `ready` deltaP `2.2583` edge `-0.0044` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2559` n `133` status `ready` deltaP `6.9285` edge `-0.0174` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.2912` n `140` status `ready` deltaP `5.2438` edge `0.0347` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5944` n `133` status `ready` deltaP `2.4689` edge `0.0109` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6759` n `133` status `ready` deltaP `-1.0086` edge `0.0051` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7572` n `140` status `ready` deltaP `-5.8169` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5895` n `133` status `ready` deltaP `5.2701` edge `-0.0406` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6913` n `133` status `ready` deltaP `-0.753` edge `0.0687` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.712` n `114` status `ready` deltaP `-4.8063` edge `0.0727` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.0423` n `140` status `ready` deltaP `-1.8734` edge `-0.0272` maxDD `-6.4399`
- `market_context_high->fx_24h` score `-2.1688` n `114` status `ready` deltaP `-3.6823` edge `0.0048` maxDD `-2.2121`
- `market_context_high->crypto_major_1h` score `-3.1246` n `140` status `ready` deltaP `-4.0291` edge `-0.1023` maxDD `-6.4975`
- `market_context_high->index_24h` score `-4.3232` n `114` status `ready` deltaP `-6.6521` edge `-0.0488` maxDD `-19.5554`
- `market_context_high->crypto_major_4h` score `-5.0753` n `133` status `ready` deltaP `-1.192` edge `-0.3129` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.2658` n `114` status `ready` deltaP `-22.3958` edge `-0.195` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
