# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T09:07:20.933999+00:00`
- Price records: `672`
- Market context records: `3058`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.6969` n `96` status `ready` deltaP `13.0209` edge `2.4455` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.9545` n `96` status `ready` deltaP `45.4861` edge `0.8837` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.3957` n `96` status `ready` deltaP `24.132` edge `1.0019` maxDD `-1.7175`
- `market_context_high->index_24h` score `10.4288` n `96` status `ready` deltaP `26.0417` edge `0.8085` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.3891` n `96` status `ready` deltaP `25.1736` edge `1.4393` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.499` n `130` status `ready` deltaP `17.1248` edge `0.1588` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1679` n `133` status `ready` deltaP `0.9849` edge `0.0217` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3966` n `130` status `ready` deltaP `2.0379` edge `0.0587` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5379` n `133` status `ready` deltaP `3.227` edge `0.0158` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6131` n `133` status `ready` deltaP `-5.9453` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6928` n `133` status `ready` deltaP `4.7308` edge `0.0926` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.767` n `96` status `ready` deltaP `0.1736` edge `-0.0123` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-0.8474` n `133` status `ready` deltaP `1.8831` edge `0.0242` maxDD `-8.6319`
- `market_context_high->unknown_1h` score `-1.0259` n `133` status `ready` deltaP `3.5534` edge `-0.0361` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0333` n `133` status `ready` deltaP `3.3632` edge `0.0714` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1724` n `130` status `ready` deltaP `-9.1065` edge `-0.0054` maxDD `-1.0693`
- `market_context_high->metal_1h` score `-1.2121` n `133` status `ready` deltaP `-2.2028` edge `-0.0039` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.224` n `130` status `ready` deltaP `10.8865` edge `0.0614` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.829` n `130` status `ready` deltaP `18.5085` edge `0.3184` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.1692` n `130` status `ready` deltaP `8.9188` edge `0.0467` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
