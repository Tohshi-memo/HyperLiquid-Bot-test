# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T10:07:35.525967+00:00`
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

- `market_context_high->unknown_4h` score `18.5666` n `131` status `ready` deltaP `-1.7024` edge `1.5921` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5959` n `113` status `ready` deltaP `28.4445` edge `0.1538` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1496` n `143` status `ready` deltaP `6.9428` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.082` n `113` status `ready` deltaP `20.6612` edge `0.03` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0689` n `131` status `ready` deltaP `8.6239` edge `0.0081` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.2415` n `143` status `ready` deltaP `7.0391` edge `0.0013` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3152` n `143` status `ready` deltaP `1.7996` edge `0.0118` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5252` n `113` status `ready` deltaP `11.1296` edge `-0.0133` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.5678` n `143` status `ready` deltaP `-0.7496` edge `-0.0026` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.5991` n `131` status `ready` deltaP `3.8959` edge `0.047` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.2656` n `143` status `ready` deltaP `2.2979` edge `-0.0195` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.2864` n `131` status `ready` deltaP `3.1186` edge `-0.0147` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.2885` n `131` status `ready` deltaP `-10.765` edge `-0.0342` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2887` n `143` status `ready` deltaP `-0.602` edge `-0.0608` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3845` n `143` status `ready` deltaP `-2.1524` edge `-0.0429` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.706` n `113` status `ready` deltaP `-2.0726` edge `-0.1038` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.9355` n `131` status `ready` deltaP `-7.558` edge `-0.2066` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.4934` n `113` status `ready` deltaP `-18.8191` edge `-0.1481` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.7073` n `113` status `ready` deltaP `-4.033` edge `-0.2755` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.8014` n `131` status `ready` deltaP `-9.2417` edge `-0.3406` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
