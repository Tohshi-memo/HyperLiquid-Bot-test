# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T19:52:30.631834+00:00`
- Price records: `672`
- Market context records: `8018`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11816`

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

- `market_context_high->equity_24h` score `15.9758` n `88` status `ready` deltaP `25.26` edge `1.2971` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8368` n `88` status `ready` deltaP `35.8752` edge `0.4139` maxDD `0.0`
- `market_context_high->equity_4h` score `6.2531` n `101` status `ready` deltaP `24.4917` edge `0.4471` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.7624` n `88` status `ready` deltaP `23.0837` edge `0.2126` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.5221` n `101` status `ready` deltaP `22.8913` edge `0.1198` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4543` n `101` status `ready` deltaP `25.6371` edge `0.0696` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9792` n `88` status `ready` deltaP `11.6039` edge `0.1546` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6778` n `101` status `ready` deltaP `13.9755` edge `0.1284` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3608` n `88` status `ready` deltaP `25.7366` edge `0.0367` maxDD `-2.5901`
- `market_context_high->index_1h` score `0.8501` n `101` status `ready` deltaP `13.8836` edge `0.0213` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6384` n `101` status `ready` deltaP `9.2903` edge `0.0291` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6012` n `101` status `ready` deltaP `11.478` edge `0.0416` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5492` n `101` status `ready` deltaP `8.8762` edge `0.1584` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.5151` n `101` status `ready` deltaP `5.6015` edge `0.1173` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0354` n `101` status `ready` deltaP `1.9342` edge `0.0349` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.304` n `101` status `ready` deltaP `-0.4713` edge `0.0009` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3996` n `101` status `ready` deltaP `5.6649` edge `0.0037` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5989` n `101` status `ready` deltaP `-1.3592` edge `-0.0054` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2184` n `101` status `ready` deltaP `0.0406` edge `-0.0063` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8967` n `101` status `ready` deltaP `7.2419` edge `-0.164` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
