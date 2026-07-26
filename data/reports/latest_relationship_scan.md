# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T17:22:29.565365+00:00`
- Price records: `672`
- Market context records: `8007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11822`

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

- `market_context_high->equity_24h` score `15.9144` n `90` status `ready` deltaP `25.9028` edge `1.2877` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.7746` n `90` status `ready` deltaP `35.9375` edge `0.4083` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1738` n `103` status `ready` deltaP `24.445` edge `0.4408` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5881` n `103` status `ready` deltaP `23.9715` edge `0.1181` maxDD `-0.979`
- `market_context_high->index_4h` score `2.434` n `103` status `ready` deltaP `25.4884` edge `0.0689` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.3356` n `90` status `ready` deltaP `21.3541` edge `0.1969` maxDD `-6.2367`
- `market_context_high->index_24h` score `2.0688` n `90` status `ready` deltaP `12.6042` edge `0.1554` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6407` n `103` status `ready` deltaP `13.8422` edge `0.1262` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3146` n `90` status `ready` deltaP `26.3195` edge `0.0369` maxDD `-2.8915`
- `market_context_high->index_1h` score `0.8865` n `103` status `ready` deltaP `14.3684` edge `0.0211` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7091` n `103` status `ready` deltaP `10.1898` edge `0.029` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6625` n `103` status `ready` deltaP `9.9618` edge `0.1606` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6037` n `103` status `ready` deltaP `6.4394` edge `0.1191` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5466` n `103` status `ready` deltaP `10.7886` edge `0.0392` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0407` n `103` status `ready` deltaP `0.9345` edge `0.0318` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2328` n `103` status `ready` deltaP `0.8662` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3703` n `103` status `ready` deltaP `5.9407` edge `0.0043` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5287` n `103` status `ready` deltaP `-0.1904` edge `-0.0042` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1955` n `103` status `ready` deltaP `0.1969` edge `-0.0044` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8801` n `103` status `ready` deltaP `7.4356` edge `-0.1639` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
