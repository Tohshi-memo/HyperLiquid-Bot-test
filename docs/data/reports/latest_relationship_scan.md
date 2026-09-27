# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T15:37:27.192597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `745.7436` n `136` status `ready` deltaP `1.2153` edge `62.1372` maxDD `0.0`
- `market_context_high->unknown_1h` score `173.4267` n `38` status `ready` deltaP `10.093` edge `14.3896` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `58.0452` n `34` status `ready` deltaP `30.3921` edge `4.6696` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0798` n `34` status `ready` deltaP `35.4269` edge `2.3852` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.879` n `34` status `ready` deltaP `15.1144` edge `2.3438` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6591` n `34` status `ready` deltaP `33.3435` edge `0.5081` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.537` n `38` status `ready` deltaP `20.0337` edge `0.2988` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4109` n `34` status `ready` deltaP `39.4812` edge `0.1282` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0935` n `38` status `ready` deltaP `25.4092` edge `0.2052` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.3006` n `38` status `ready` deltaP `36.0478` edge `0.0418` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.2218` n `38` status `ready` deltaP `9.8845` edge `0.2097` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.67` n `38` status `ready` deltaP `19.0435` edge `0.0525` maxDD `-1.5564`
- `news_risk_high->index_24h` score `0.9999` n `136` status `ready` deltaP `17.1671` edge `0.0384` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `0.9847` n `38` status `ready` deltaP `10.7627` edge `0.0961` maxDD `-4.8632`
- `market_context_high->index_1h` score `0.9799` n `38` status `ready` deltaP `13.7804` edge `0.0093` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.7584` n `38` status `ready` deltaP `13.733` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.6085` n `38` status `ready` deltaP `10.55` edge `0.0966` maxDD `-5.7799`
- `news_risk_high->metal_24h` score `0.5215` n `136` status `ready` deltaP `15.9518` edge `0.1226` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4311` n `38` status `ready` deltaP `10.5986` edge `0.0225` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
