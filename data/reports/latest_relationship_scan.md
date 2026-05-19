# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T09:52:17.930700+00:00`
- Price records: `672`
- Market context records: `1208`
- Flow alert records: `5384`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.7029` n `130` status `ready` deltaP `44.0946` edge `1.3778` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.1174` n `130` status `ready` deltaP `21.9979` edge `0.6481` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.8926` n `130` status `ready` deltaP `2.765` edge `0.6776` maxDD `-6.7322`
- `market_context_high->commodity_24h` score `5.464` n `130` status `ready` deltaP `-2.7698` edge `0.6441` maxDD `-8.6239`
- `market_context_high->metal_24h` score `4.3023` n `130` status `ready` deltaP `-3.6085` edge `0.5493` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8191` n `130` status `ready` deltaP `14.5286` edge `0.2044` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.0813` n `130` status `ready` deltaP `17.8766` edge `0.1629` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.7543` n `130` status `ready` deltaP `18.0742` edge `0.3371` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9413` n `130` status `ready` deltaP `10.3565` edge `0.0777` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8932` n `130` status `ready` deltaP `9.9119` edge `0.0622` maxDD `-0.9743`
- `market_context_high->index_1h` score `0.5612` n `130` status `ready` deltaP `8.9636` edge `0.0187` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4532` n `130` status `ready` deltaP `4.4104` edge `0.0458` maxDD `-1.3281`
- `market_context_high->metal_1h` score `-0.1067` n `130` status `ready` deltaP `9.2469` edge `-0.0095` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1394` n `130` status `ready` deltaP `5.0184` edge `0.0005` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.2181` n `130` status `ready` deltaP `5.3635` edge `0.1284` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3885` n `130` status `ready` deltaP `0.2948` edge `0.0325` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3956` n `130` status `ready` deltaP `2.948` edge `0.0062` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.639` n `130` status `ready` deltaP `0.1523` edge `0.2187` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.7803` n `130` status `ready` deltaP `-2.4367` edge `0.0127` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.7963` n `130` status `ready` deltaP `10.3963` edge `-0.0283` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
