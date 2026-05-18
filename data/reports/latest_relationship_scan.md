# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T16:37:22.443554+00:00`
- Price records: `672`
- Market context records: `1135`
- Flow alert records: `5170`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8739`

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

- `market_context_high->crypto_major_24h` score `19.3229` n `151` status `ready` deltaP `41.9368` edge `1.4078` maxDD `-5.5043`
- `market_context_high->crypto_alt_24h` score `9.0153` n `151` status `ready` deltaP `18.2936` edge `0.7912` maxDD `-12.2838`
- `market_context_high->equity_24h` score `7.2204` n `151` status `ready` deltaP `17.7727` edge `0.5518` maxDD `-4.8203`
- `market_context_high->index_24h` score `5.6525` n `151` status `ready` deltaP `16.3838` edge `0.4035` maxDD `-2.668`
- `market_context_high->metal_24h` score `5.5768` n `151` status `ready` deltaP `-1.7477` edge `0.6431` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.9922` n `168` status `ready` deltaP `10.6417` edge `0.1614` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8812` n `168` status `ready` deltaP `7.9849` edge `0.0885` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4666` n `168` status `ready` deltaP `7.1963` edge `0.0226` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.406` n `168` status `ready` deltaP `3.1793` edge `0.0504` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1528` n `168` status `ready` deltaP `8.7616` edge `0.1533` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1244` n `168` status `ready` deltaP `8.1658` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0802` n `168` status `ready` deltaP `6.9825` edge `0.0367` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2352` n `168` status `ready` deltaP `6.8007` edge `-0.0039` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2634` n `168` status `ready` deltaP `2.9441` edge `0.0427` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7279` n `168` status `ready` deltaP `0.7839` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7871` n `168` status `ready` deltaP `-2.3738` edge `-0.0043` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.9549` n `168` status `ready` deltaP `5.996` edge `0.1341` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4428` n `168` status `ready` deltaP `6.3952` edge `-0.0508` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1823` n `168` status `ready` deltaP `-11.883` edge `-0.012` maxDD `-13.0076`
- `market_context_high->unknown_24h` score `-3.3681` n `151` status `ready` deltaP `2.6387` edge `-0.0253` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
