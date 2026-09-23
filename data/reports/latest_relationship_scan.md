# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T23:07:36.952757+00:00`
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

- `market_context_high->unknown_1h` score `72.1243` n `47` status `ready` deltaP `10.116` edge `5.95` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.7588` n `46` status `ready` deltaP `21.5203` edge `2.7687` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.1378` n `46` status `ready` deltaP `18.9161` edge `1.5621` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `18.363` n `46` status `ready` deltaP `16.4931` edge `1.4203` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.1027` n `97` status `ready` deltaP `-1.967` edge `1.4575` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.7822` n `46` status `ready` deltaP `27.9439` edge `0.3876` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.8056` n `103` status `ready` deltaP `14.0792` edge `0.4064` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5838` n `103` status `ready` deltaP `17.4328` edge `0.3235` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `4.4724` n `97` status `ready` deltaP `-4.1255` edge `0.8883` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.557` n `97` status `ready` deltaP `24.9105` edge `0.1649` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.5426` n `103` status `ready` deltaP `13.3074` edge `0.1722` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4296` n `47` status `ready` deltaP `28.691` edge `0.0266` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9965` n `103` status `ready` deltaP `15.5529` edge `0.1062` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.5882` n `46` status `ready` deltaP `21.9203` edge `0.0096` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.5454` n `103` status `ready` deltaP `22.7667` edge `0.0406` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3005` n `47` status `ready` deltaP `10.4372` edge `0.0806` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1086` n `97` status `ready` deltaP `27.6221` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7403` n `47` status `ready` deltaP `12.2149` edge `0.0081` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.6943` n `97` status `ready` deltaP `17.9982` edge `0.0608` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.5966` n `103` status `ready` deltaP `14.9032` edge `0.0097` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
