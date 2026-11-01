# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T17:07:29.171741+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6601`

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

- `market_context_high->unknown_24h` score `7170.7387` n `55` status `ready` deltaP `1.3889` edge `597.5523` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.1638` n `55` status `ready` deltaP `6.2611` edge `31.6429` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `72.2282` n `55` status `ready` deltaP `4.2107` edge `6.002` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.094` n `55` status `ready` deltaP `42.7999` edge `1.4961` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1892` n `94` status `ready` deltaP `30.9619` edge `1.0283` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.6336` n `55` status `ready` deltaP `53.8194` edge `0.194` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3026` n `55` status `ready` deltaP `44.4003` edge `0.2603` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1786` n `55` status `ready` deltaP `24.5122` edge `0.3809` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.7095` n `55` status `ready` deltaP `31.5023` edge `0.2994` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5225` n `55` status `ready` deltaP `6.3525` edge `0.3214` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3272` n `55` status `ready` deltaP `31.2195` edge `0.0942` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.9855` n `122` status `ready` deltaP `12.545` edge `0.3038` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.3786` n `55` status `ready` deltaP `10.3378` edge `0.3037` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.8833` n `55` status `ready` deltaP `-4.2992` edge `0.4219` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6762` n `55` status `ready` deltaP `19.5704` edge `0.0517` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5644` n `55` status `ready` deltaP `3.3261` edge `0.1607` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.5034` n `55` status `ready` deltaP `4.6734` edge `0.1612` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4899` n `55` status `ready` deltaP `8.7806` edge `0.1266` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.9882` n `55` status `ready` deltaP `12.2237` edge `0.0257` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5467` n `55` status `ready` deltaP `13.337` edge `-0.0004` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
