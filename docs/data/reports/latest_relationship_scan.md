# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T11:37:28.045842+00:00`
- Price records: `672`
- Market context records: `6599`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.5547` n `165` status `ready` deltaP `4.0275` edge `0.5994` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0376` n `210` status `ready` deltaP `-5.1297` edge `0.2941` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.5753` n `165` status `ready` deltaP `9.4894` edge `0.1715` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3098` n `210` status `ready` deltaP `1.6068` edge `0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4664` n `210` status `ready` deltaP `6.4485` edge `0.0238` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5537` n `210` status `ready` deltaP `-0.3807` edge `0.0035` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5666` n `210` status `ready` deltaP `-0.1098` edge `-0.0036` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6754` n `210` status `ready` deltaP `4.0947` edge `0.0174` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9293` n `210` status `ready` deltaP `8.9896` edge `0.0089` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.2215` n `210` status `ready` deltaP `-0.3644` edge `-0.0047` maxDD `-5.6246`
- `market_context_high->equity_1h` score `-1.2232` n `210` status `ready` deltaP `1.6325` edge `-0.0018` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.3363` n `210` status `ready` deltaP `-4.1759` edge `-0.0028` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6436` n `210` status `ready` deltaP `1.7537` edge `-0.0012` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7507` n `210` status `ready` deltaP `-17.5232` edge `0.2115` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9074` n `210` status `ready` deltaP `6.3618` edge `0.0445` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.2015` n `210` status `ready` deltaP `3.5613` edge `0.0342` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2074` n `210` status `ready` deltaP `-1.9585` edge `0.0161` maxDD `-5.2172`
- `market_context_high->fx_24h` score `-3.8229` n `165` status `ready` deltaP `-5.4178` edge `-0.0005` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.4446` n `165` status `ready` deltaP `0.6375` edge `0.0605` maxDD `-10.1439`
- `market_context_high->equity_4h` score `-4.8992` n `210` status `ready` deltaP `6.5912` edge `-0.0253` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
