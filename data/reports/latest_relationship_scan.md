# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T00:07:28.570839+00:00`
- Price records: `672`
- Market context records: `8038`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `17.1881` n `83` status `ready` deltaP `27.525` edge `1.3491` maxDD `-5.0208`
- `market_context_high->metal_24h` score `8.0036` n `83` status `ready` deltaP `35.8752` edge `0.4278` maxDD `0.0`
- `market_context_high->equity_4h` score `6.715` n `96` status `ready` deltaP `26.1687` edge `0.4687` maxDD `-4.6862`
- `market_context_high->commodity_24h` score `3.8892` n `83` status `ready` deltaP `27.5334` edge `0.256` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.5895` n `96` status `ready` deltaP `26.9817` edge `0.0719` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5556` n `96` status `ready` deltaP `22.8912` edge `0.1226` maxDD `-0.979`
- `market_context_high->index_24h` score `1.9078` n `83` status `ready` deltaP `10.171` edge `0.1582` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6842` n `96` status `ready` deltaP `13.8161` edge `0.13` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.5401` n `83` status `ready` deltaP `25.8023` edge `0.0398` maxDD `-1.6778`
- `market_context_high->index_1h` score `0.8261` n `96` status `ready` deltaP `13.6727` edge `0.0207` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.769` n `96` status `ready` deltaP `10.6974` edge `0.0306` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.491` n `96` status `ready` deltaP `10.7098` edge `0.0326` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.4409` n `96` status `ready` deltaP `8.8415` edge `0.1496` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.4135` n `96` status `ready` deltaP `5.4116` edge `0.1101` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0995` n `96` status `ready` deltaP `0.5988` edge `0.0265` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.2893` n `96` status `ready` deltaP `4.878` edge `0.0035` maxDD `-0.8104`
- `market_context_high->commodity_1h` score `-0.5923` n `96` status `ready` deltaP `-1.5032` edge `-0.0036` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.5927` n `96` status `ready` deltaP `-1.9149` edge `0.0001` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-1.1159` n `96` status `ready` deltaP `1.3973` edge `-0.0022` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.821` n `96` status `ready` deltaP `7.4538` edge `-0.1591` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
