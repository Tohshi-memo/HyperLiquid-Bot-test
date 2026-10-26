# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T10:22:29.058867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `18.0416` n `132` status `ready` deltaP `-1.5752` edge `1.5475` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5944` n `113` status `ready` deltaP `28.4445` edge `0.1536` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1182` n `144` status `ready` deltaP `6.5494` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0714` n `113` status `ready` deltaP `20.4876` edge `0.0298` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0318` n `132` status `ready` deltaP `8.1902` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.2308` n `144` status `ready` deltaP `7.2147` edge `0.0015` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2868` n `144` status `ready` deltaP `2.1249` edge `0.012` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5182` n `113` status `ready` deltaP `11.1296` edge `-0.0124` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5856` n `132` status `ready` deltaP `4.0789` edge `0.0469` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.587` n `144` status `ready` deltaP `-1.0895` edge `-0.0028` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2557` n `132` status `ready` deltaP `3.5292` edge `-0.0135` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.2648` n `144` status `ready` deltaP `2.4784` edge `-0.0206` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2572` n `132` status `ready` deltaP `-10.2965` edge `-0.0333` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3064` n `144` status `ready` deltaP `-0.9273` edge `-0.0609` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4189` n `144` status `ready` deltaP `-2.4534` edge `-0.0453` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6935` n `113` status `ready` deltaP `-2.0726` edge `-0.1022` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.876` n `132` status `ready` deltaP `-7.1185` edge `-0.2019` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4911` n `113` status `ready` deltaP `-18.8191` edge `-0.1478` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.6601` n `113` status `ready` deltaP `-3.8594` edge `-0.2706` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-13.4402` n `132` status `ready` deltaP `-8.7675` edge `-0.3354` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
