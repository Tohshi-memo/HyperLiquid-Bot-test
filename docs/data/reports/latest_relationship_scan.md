# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T07:52:27.357060+00:00`
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

- `market_context_high->unknown_1h` score `1.4004` n `133` status `ready` deltaP `8.2381` edge `0.0845` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5245` n `133` status `ready` deltaP `20.3283` edge `-0.0479` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1704` n `133` status `ready` deltaP `1.4306` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1773` n `133` status `ready` deltaP `7.0134` edge `0.0375` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.2392` n `133` status `ready` deltaP `7.2334` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2794` n `133` status `ready` deltaP `1.5803` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.6394` n `133` status `ready` deltaP `-3.6727` edge `-0.0009` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6624` n `133` status `ready` deltaP `1.2494` edge `0.0103` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7131` n `133` status `ready` deltaP `-1.6184` edge `0.0044` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8946` n `133` status `ready` deltaP `-0.4783` edge `0.0088` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4728` n `133` status `ready` deltaP `-2.4481` edge `-0.07` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5879` n `105` status `ready` deltaP `-5.6547` edge `0.0887` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.771` n `133` status `ready` deltaP `-1.8201` edge `0.0656` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.0547` n `133` status `ready` deltaP `4.6603` edge `-0.0753` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5687` n `105` status `ready` deltaP `-7.9613` edge `0.0` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1729` n `105` status `ready` deltaP `-4.5536` edge `-0.0544` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0373` n `105` status `ready` deltaP `-19.8462` edge `-0.1827` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.4603` n `133` status `ready` deltaP `-1.9542` edge `-0.3399` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
