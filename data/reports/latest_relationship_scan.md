# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T01:22:31.161717+00:00`
- Price records: `672`
- Market context records: `7728`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.7263` n `132` status `ready` deltaP `19.396` edge `0.3154` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0897` n `133` status `ready` deltaP `13.4573` edge `0.0452` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9968` n `133` status `ready` deltaP `14.6513` edge `0.1572` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6865` n `133` status `ready` deltaP `8.8093` edge `0.1102` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.611` n `133` status `ready` deltaP `8.6466` edge `0.0792` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.4734` n `133` status `ready` deltaP `1.6636` edge `0.2409` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.4107` n `133` status `ready` deltaP `9.245` edge `0.0156` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.17` n `133` status `ready` deltaP `4.1286` edge `0.0299` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.1594` n `132` status `ready` deltaP `15.2545` edge `0.0275` maxDD `-3.0343`
- `market_context_high->metal_24h` score `-0.1417` n `133` status `ready` deltaP `4.7645` edge `0.1655` maxDD `-2.3927`
- `market_context_high->commodity_1h` score `-0.17` n `133` status `ready` deltaP `3.6951` edge `0.0071` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.2385` n `133` status `ready` deltaP `3.7168` edge `0.0147` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2608` n `133` status `ready` deltaP `10.5585` edge `0.042` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `-0.2269` edge `-0.0006` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7896` n `133` status `ready` deltaP `2.1656` edge `0.0201` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.5171` n `133` status `ready` deltaP `0.6808` edge `0.0745` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5751` n `133` status `ready` deltaP `-5.385` edge `-0.0032` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7345` n `132` status `ready` deltaP `5.6858` edge `-0.0241` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1733` n `133` status `ready` deltaP `-1.1244` edge `-0.1146` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5794` n `132` status `ready` deltaP `-18.4537` edge `0.0026` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
