# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T05:37:27.165422+00:00`
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

- `market_context_high->unknown_1h` score `1.5371` n `133` status `ready` deltaP `8.8369` edge `0.0919` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6566` n `133` status `ready` deltaP `21.3953` edge `-0.044` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1446` n `133` status `ready` deltaP `8.8197` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1626` n `133` status `ready` deltaP `1.5803` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.1641` n `133` status `ready` deltaP `7.1631` edge `0.0382` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2779` n `133` status `ready` deltaP `1.5803` edge `-0.0043` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3238` n `133` status `ready` deltaP `5.8614` edge `-0.019` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6277` n `133` status `ready` deltaP `-3.6727` edge `0.0006` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6373` n `133` status `ready` deltaP `-0.5513` edge `0.007` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6909` n `133` status `ready` deltaP `0.792` edge `0.0097` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.8503` n `133` status `ready` deltaP `0.1205` edge `0.0085` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3933` n `133` status `ready` deltaP `-1.5499` edge `-0.0658` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.4685` n `105` status `ready` deltaP `-4.6131` edge `0.0917` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.8607` n `133` status `ready` deltaP `-2.7348` edge `0.0602` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4365` n `105` status `ready` deltaP `-6.3988` edge `0.0006` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.5224` n `133` status `ready` deltaP `3.8981` edge `-0.1092` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.2697` n `105` status `ready` deltaP `-6.1161` edge `-0.0564` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0863` n `105` status `ready` deltaP `-20.7143` edge `-0.1832` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5561` n `133` status `ready` deltaP `-1.8017` edge `-0.3489` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
