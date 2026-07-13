# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T10:22:30.501529+00:00`
- Price records: `672`
- Market context records: `6593`
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

- `market_context_high->unknown_24h` score `4.053` n `161` status `ready` deltaP `5.5021` edge `0.6311` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0232` n `210` status `ready` deltaP `-5.2794` edge `0.2939` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7298` n `161` status `ready` deltaP `10.4614` edge `0.1779` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2934` n `210` status `ready` deltaP `1.9062` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4656` n `210` status `ready` deltaP `6.4485` edge `0.0239` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.523` n `210` status `ready` deltaP `0.489` edge `-0.002` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5631` n `210` status `ready` deltaP `-0.5304` edge `0.0033` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6536` n `210` status `ready` deltaP `4.3941` edge `0.0182` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9167` n `210` status `ready` deltaP `9.142` edge `0.0095` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2076` n `210` status `ready` deltaP `1.7822` edge `-0.0015` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2333` n `210` status `ready` deltaP `-0.5168` edge `-0.0052` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3722` n `210` status `ready` deltaP `-4.4753` edge `-0.0038` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6547` n `210` status `ready` deltaP `1.6013` edge `-0.0016` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7629` n `210` status `ready` deltaP `-17.6756` edge `0.2115` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9051` n `210` status `ready` deltaP `6.3618` edge `0.0448` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1948` n `210` status `ready` deltaP `-1.8061` edge `0.0167` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2071` n `210` status `ready` deltaP `3.4088` edge `0.0345` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.7721` n `161` status `ready` deltaP `-4.4261` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-3.9628` n `161` status `ready` deltaP `1.6188` edge `0.0661` maxDD `-9.2368`
- `market_context_high->equity_4h` score `-4.7807` n `210` status `ready` deltaP `7.3534` edge `-0.0205` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
