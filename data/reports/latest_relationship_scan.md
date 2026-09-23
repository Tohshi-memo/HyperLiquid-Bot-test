# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T23:22:30.199219+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_1h` score `72.1099` n `47` status `ready` deltaP `10.116` edge `5.9488` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.8927` n `46` status `ready` deltaP `21.6939` edge `2.7787` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.2248` n `46` status `ready` deltaP `19.0897` edge `1.5682` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `18.5593` n `46` status `ready` deltaP `16.6667` edge `1.4355` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.2365` n `97` status `ready` deltaP `-1.7934` edge `1.4675` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.8105` n `46` status `ready` deltaP `28.1175` edge `0.3888` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.8358` n `103` status `ready` deltaP `14.2316` edge `0.4079` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `4.6686` n `97` status `ready` deltaP `-3.9519` edge `0.9035` maxDD `-32.7147`
- `news_risk_high->crypto_major_4h` score `4.591` n `103` status `ready` deltaP `17.4328` edge `0.3241` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.5713` n `103` status `ready` deltaP `13.4571` edge `0.1736` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.5275` n `97` status `ready` deltaP `24.7369` edge `0.1636` maxDD `-2.431`
- `market_context_high->index_4h` score `2.4308` n `47` status `ready` deltaP `28.691` edge `0.0267` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0169` n `103` status `ready` deltaP `15.7026` edge `0.1069` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.6309` n `46` status `ready` deltaP `22.0939` edge `0.012` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.5588` n `103` status `ready` deltaP `22.9192` edge `0.0407` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3187` n `47` status `ready` deltaP `10.5896` edge `0.0811` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7546` n `47` status `ready` deltaP `12.3646` edge `0.0083` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.7221` n `97` status `ready` deltaP `18.1718` edge `0.0632` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.611` n `103` status `ready` deltaP `15.0529` edge `0.0099` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
