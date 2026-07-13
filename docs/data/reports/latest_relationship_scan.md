# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T09:52:28.078790+00:00`
- Price records: `672`
- Market context records: `6591`
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

- `market_context_high->unknown_24h` score `4.2707` n `159` status `ready` deltaP `6.0481` edge `0.6456` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0088` n `210` status `ready` deltaP `-5.4291` edge `0.2937` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.8329` n `159` status `ready` deltaP `11.0144` edge `0.1828` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3106` n `210` status `ready` deltaP `1.6068` edge `0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4898` n `210` status `ready` deltaP `6.1491` edge `0.0228` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.502` n `210` status `ready` deltaP `0.7884` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5717` n `210` status `ready` deltaP `-0.6801` edge `0.0032` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6653` n `210` status `ready` deltaP `4.2444` edge `0.0177` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9144` n `210` status `ready` deltaP `9.142` edge `0.0098` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.222` n `210` status `ready` deltaP `1.6325` edge `-0.0017` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2365` n `210` status `ready` deltaP `-0.5168` edge `-0.0056` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.401` n `210` status `ready` deltaP `-4.7747` edge `-0.0042` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6657` n `210` status `ready` deltaP `1.4489` edge `-0.002` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7471` n `210` status `ready` deltaP `-17.5232` edge `0.2118` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9035` n `210` status `ready` deltaP `6.3618` edge `0.045` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1902` n `210` status `ready` deltaP `-1.8061` edge `0.0173` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2039` n `210` status `ready` deltaP `3.4088` edge `0.0349` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-3.7368` n `159` status `ready` deltaP `2.0954` edge `0.0685` maxDD `-8.843`
- `market_context_high->fx_24h` score `-3.7563` n `159` status `ready` deltaP `-4.1222` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7687` n `210` status `ready` deltaP `7.3534` edge `-0.0195` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
