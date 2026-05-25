# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T11:52:15.353316+00:00`
- Price records: `672`
- Market context records: `1839`
- Flow alert records: `7194`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.8888` n `196` status `ready` deltaP `22.9249` edge `0.5357` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.4494` n `178` status `ready` deltaP `25.5072` edge `0.61` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.3255` n `196` status `ready` deltaP `26.1044` edge `0.4777` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3711` n `196` status `ready` deltaP `17.2132` edge `0.4519` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.3655` n `178` status `ready` deltaP `17.1739` edge `0.2888` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.799` n `196` status `ready` deltaP `16.0652` edge `0.2356` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7051` n `178` status `ready` deltaP `14.56` edge `0.6604` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.6117` n `178` status `ready` deltaP `14.1522` edge `0.5298` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.7929` n `196` status `ready` deltaP `12.0707` edge `0.0945` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3884` n `198` status `ready` deltaP `5.5919` edge `0.0937` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2877` n `178` status `ready` deltaP `19.5537` edge `0.7522` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2199` n `198` status `ready` deltaP `5.61` edge `0.0923` maxDD `-4.9097`
- `market_context_high->fx_24h` score `-0.0485` n `178` status `ready` deltaP `12.1294` edge `0.02` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1085` n `198` status `ready` deltaP `4.2053` edge `0.0423` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5025` n `198` status `ready` deltaP `3.2723` edge `0.0315` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.535` n `196` status `ready` deltaP `13.2` edge `0.1366` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5897` n `198` status `ready` deltaP `5.5178` edge `0.0212` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6382` n `198` status `ready` deltaP `-0.2268` edge `0.0115` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7354` n `198` status `ready` deltaP `-4.5092` edge `-0.001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0624` n `196` status `ready` deltaP `-5.8922` edge `-0.0081` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
