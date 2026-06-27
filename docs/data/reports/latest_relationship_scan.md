# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T20:52:32.353881+00:00`
- Price records: `672`
- Market context records: `4971`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.3813` n `100` status `ready` deltaP `6.7545` edge `1.4535` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.7848` n `90` status `ready` deltaP `29.5223` edge `0.92` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4987` n `90` status `ready` deltaP `21.4363` edge `0.6044` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1426` n `90` status `ready` deltaP `21.9817` edge `0.5839` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9233` n `87` status `ready` deltaP `27.6102` edge `0.3438` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7433` n `90` status `ready` deltaP `13.6382` edge `0.1925` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5827` n `90` status `ready` deltaP `12.2629` edge `0.1247` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8946` n `90` status `ready` deltaP `11.2839` edge `0.0455` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.5568` n `100` status `ready` deltaP `8.1497` edge `0.0744` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.4919` n `100` status `ready` deltaP `5.6407` edge `0.1293` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4011` n `100` status `ready` deltaP `7.5988` edge `0.103` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0442` n `100` status `ready` deltaP `2.9401` edge `0.0347` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3781` n `100` status `ready` deltaP `2.1018` edge `0.013` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4083` n `100` status `ready` deltaP `0.994` edge `0.007` maxDD `-1.278`
- `market_context_high->fx_4h` score `-1.1633` n `90` status `ready` deltaP `-7.3205` edge `-0.0033` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.165` n `87` status `ready` deltaP `-0.6645` edge `-0.0101` maxDD `-2.2711`
- `market_context_high->commodity_4h` score `-1.1858` n `90` status `ready` deltaP `5.3117` edge `-0.0097` maxDD `-4.9624`
- `market_context_high->fx_1h` score `-1.4951` n `100` status `ready` deltaP `-9.1078` edge `-0.0039` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-4.4563` n `87` status `ready` deltaP `17.2234` edge `0.0247` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.0014` n `87` status `ready` deltaP `-8.8602` edge `0.0211` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
