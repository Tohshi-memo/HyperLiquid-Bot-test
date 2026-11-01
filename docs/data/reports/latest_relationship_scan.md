# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T05:52:26.033012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `6436.6499` n `59` status `ready` deltaP `3.3398` edge `536.3727` maxDD `-0.2646`
- `market_context_high->unknown_4h` score `334.2245` n `59` status `ready` deltaP `5.4697` edge `27.8199` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `80.2072` n `108` status `ready` deltaP `-5.1951` edge `6.7472` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `31.4192` n `59` status `ready` deltaP `3.1539` edge `2.6083` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.9833` n `59` status `ready` deltaP `40.6573` edge `1.4316` maxDD `-1.6568`
- `news_risk_high->crypto_alt_24h` score `13.3596` n `98` status `ready` deltaP `31.5476` edge `1.0386` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.595` n `59` status `ready` deltaP `55.5056` edge `0.1932` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.0713` n `108` status `ready` deltaP `19.2073` edge `0.4332` maxDD `-7.4246`
- `market_context_high->crypto_alt_4h` score `4.2583` n `59` status `ready` deltaP `18.7836` edge `0.2911` maxDD `-3.2507`
- `market_context_high->crypto_major_4h` score `4.1883` n `59` status `ready` deltaP `25.5271` edge `0.2314` maxDD `-2.5378`
- `market_context_high->commodity_24h` score `3.5652` n `59` status `ready` deltaP `40.8133` edge `0.2354` maxDD `-2.3666`
- `market_context_high->commodity_4h` score `2.9504` n `59` status `ready` deltaP `28.4053` edge `0.0899` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.8008` n `59` status `ready` deltaP `2.8653` edge `0.2845` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.1559` n `59` status `ready` deltaP `8.4539` edge `0.2877` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.6075` n `59` status `ready` deltaP `-6.7091` edge `0.4026` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6066` n `59` status `ready` deltaP `19.1505` edge `0.0487` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.9344` n `59` status `ready` deltaP `11.7172` edge `0.0246` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7294` n `108` status `ready` deltaP `8.1282` edge `0.102` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.6231` n `59` status `ready` deltaP `-0.9972` edge `0.144` maxDD `-1.5969`
- `market_context_high->fx_1h` score `0.6227` n `59` status `ready` deltaP `14.7544` edge `-0.0001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
