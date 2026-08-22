# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T05:52:22.207380+00:00`
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

- `market_context_high->unknown_1h` score `1.4903` n `133` status `ready` deltaP `8.6872` edge `0.089` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.6372` n `133` status `ready` deltaP `21.2429` edge `-0.0446` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1367` n `133` status `ready` deltaP `8.6673` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1289` n `133` status `ready` deltaP `9.708` edge `0.0049` maxDD `-0.9144`
- `market_context_high->equity_1h` score `-0.1602` n `133` status `ready` deltaP `7.1631` edge `0.0387` maxDD `-5.2257`
- `market_context_high->fx_1h` score `-0.1704` n `133` status `ready` deltaP `1.4306` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2779` n `133` status `ready` deltaP `1.5803` edge `-0.0043` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3144` n `133` status `ready` deltaP `6.0139` edge `-0.0188` maxDD `-1.5942`
- `market_context_high->commodity_1h` score `-0.6285` n `133` status `ready` deltaP `-3.6727` edge `0.0005` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6491` n `133` status `ready` deltaP `-0.7038` edge `0.0065` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6822` n `133` status `ready` deltaP `0.9445` edge `0.0098` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-0.7603` n `133` status `ready` deltaP `0.1205` edge `0.016` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3496` n `133` status `ready` deltaP `-1.5499` edge `-0.0602` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.4884` n `105` status `ready` deltaP `-4.7867` edge `0.0912` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.8568` n `133` status `ready` deltaP `-2.7348` edge `0.0607` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.4516` n `105` status `ready` deltaP `-6.5724` edge `0.0005` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-2.508` n `133` status `ready` deltaP `3.8981` edge `-0.108` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.2599` n `105` status `ready` deltaP `-5.9425` edge `-0.0563` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-5.0871` n `105` status `ready` deltaP `-20.7143` edge `-0.1833` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5899` n `133` status `ready` deltaP `-1.9542` edge `-0.3507` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
