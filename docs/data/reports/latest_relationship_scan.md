# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T20:22:25.259374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6813`

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

- `market_context_high->unknown_24h` score `7380.2347` n `55` status `ready` deltaP `1.3889` edge `615.0103` maxDD `0.0`
- `market_context_high->unknown_4h` score `369.0806` n `55` status `ready` deltaP `7.1757` edge `30.7132` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `52.3394` n `55` status `ready` deltaP `4.2107` edge `4.3446` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.202` n `55` status `ready` deltaP `42.7999` edge `1.5051` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2492` n `94` status `ready` deltaP `30.9619` edge `1.0333` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.4122` n `55` status `ready` deltaP `51.5625` edge `0.1906` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.2422` n `55` status `ready` deltaP `24.5122` edge `0.3862` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `6.0886` n `55` status `ready` deltaP `42.4906` edge `0.2552` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.6937` n `55` status `ready` deltaP `31.3498` edge `0.2991` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5213` n `55` status `ready` deltaP `6.3525` edge `0.3213` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.2754` n `55` status `ready` deltaP `31.0671` edge `0.0909` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5643` n `126` status `ready` deltaP `10.3852` edge `0.2831` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4287` n `55` status `ready` deltaP `10.685` edge `0.3078` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9223` n `55` status `ready` deltaP `-4.2992` edge `0.4269` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7626` n `55` status `ready` deltaP `20.485` edge `0.0528` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6555` n `55` status `ready` deltaP `4.2243` edge `0.1623` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.5103` n `55` status `ready` deltaP `8.7806` edge `0.1283` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.5094` n `55` status `ready` deltaP `4.374` edge `0.1637` maxDD `-2.3659`
- `market_context_high->metal_1h` score `1.0025` n `55` status `ready` deltaP `12.3734` edge `0.0259` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5638` n `55` status `ready` deltaP `13.6364` edge `-0.0002` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
