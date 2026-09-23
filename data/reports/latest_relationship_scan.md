# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T10:52:38.495573+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `47.0837` n `46` status `ready` deltaP `7.9268` edge `3.8708` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5102` n `46` status `ready` deltaP `13.7078` edge `2.3834` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.7029` n `46` status `ready` deltaP `12.1453` edge `1.321` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.246` n `46` status `ready` deltaP `10.5903` edge `0.9499` maxDD `0.0`
- `market_context_high->index_24h` score `5.6392` n `46` status `ready` deltaP `20.8258` edge `0.3398` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8166` n `96` status `ready` deltaP `-9.0277` edge `1.1474` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.9553` n `96` status `ready` deltaP `32.6389` edge `0.2299` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.0089` n `103` status `ready` deltaP `14.2316` edge `0.2136` maxDD `-2.619`
- `market_context_high->index_4h` score `2.3254` n `46` status `ready` deltaP `27.1275` edge `0.0263` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.3019` n `103` status `ready` deltaP `9.0487` edge `0.2313` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9465` n `103` status `ready` deltaP `11.511` edge `0.1345` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6787` n `103` status `ready` deltaP `14.505` edge `0.0867` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2531` n `103` status `ready` deltaP `19.4131` edge `0.0386` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.1053` n `96` status `ready` deltaP `27.0833` edge `0.1201` maxDD `-1.7159`
- `market_context_high->equity_4h` score `1.0086` n `46` status `ready` deltaP `7.6816` edge `0.0635` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9335` n `46` status `ready` deltaP `8.1099` edge `0.048` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.7944` n `46` status `ready` deltaP `12.0021` edge `0.0115` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6158` n `103` status `ready` deltaP `14.9032` edge `0.0113` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2244` n `103` status `ready` deltaP `7.9574` edge `0.01` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.1978` n `103` status `ready` deltaP `12.2883` edge `0.0392` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
