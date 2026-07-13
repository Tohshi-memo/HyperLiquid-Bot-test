# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T01:07:26.223618+00:00`
- Price records: `672`
- Market context records: `6558`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.3637` n `144` status `ready` deltaP `11.7201` edge `0.7822` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8095` n `210` status `ready` deltaP `-4.6806` edge `0.2721` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3803` n `144` status `ready` deltaP `13.4773` edge `0.212` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.1394` n `198` status `ready` deltaP `11.3405` edge `0.024` maxDD `-1.2056`
- `market_context_high->crypto_alt_4h` score `-0.2085` n `198` status `ready` deltaP `8.4335` edge `0.1001` maxDD `-8.9781`
- `market_context_high->fx_1h` score `-0.3386` n `210` status `ready` deltaP `1.1577` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4688` n `210` status `ready` deltaP `6.7479` edge `0.0215` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5135` n `210` status `ready` deltaP `6.4899` edge `0.0222` maxDD `-5.8368`
- `market_context_high->crypto_major_4h` score `-0.5173` n `198` status `ready` deltaP `11.0156` edge `0.0893` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.5619` n `210` status `ready` deltaP `0.0399` edge `-0.004` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6192` n `210` status `ready` deltaP `-1.4286` edge `0.0021` maxDD `-0.7564`
- `market_context_high->equity_4h` score `-0.7462` n `198` status `ready` deltaP `9.3003` edge `0.0457` maxDD `-8.2573`
- `market_context_high->unknown_4h` score `-0.9789` n `198` status `ready` deltaP `-16.4865` edge `0.2689` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.2364` n `210` status `ready` deltaP `1.7822` edge `-0.0039` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2452` n `210` status `ready` deltaP `-3.2777` edge `-0.0012` maxDD `-2.1239`
- `market_context_high->metal_4h` score `-1.3012` n `198` status `ready` deltaP `0.8653` edge `0.0342` maxDD `-2.8763`
- `market_context_high->commodity_4h` score `-1.366` n `198` status `ready` deltaP `-1.9139` edge `-0.0129` maxDD `-5.6246`
- `market_context_high->metal_24h` score `-1.9745` n `144` status `ready` deltaP `5.966` edge `0.0887` maxDD `-5.7746`
- `market_context_high->fx_4h` score `-2.9704` n `198` status `ready` deltaP `-2.7639` edge `-0.0079` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8424` n `144` status `ready` deltaP `-4.7877` edge `-0.0072` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
