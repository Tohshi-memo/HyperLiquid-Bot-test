# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T09:22:29.608420+00:00`
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

- `market_context_high->unknown_4h` score `18.0711` n `130` status `ready` deltaP `-2.1365` edge `1.5537` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6006` n `113` status `ready` deltaP `28.4445` edge `0.1544` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.131` n `130` status `ready` deltaP `9.3691` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_24h` score `0.113` n `113` status `ready` deltaP `21.1821` edge `0.0305` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.1124` n `140` status `ready` deltaP `6.4628` edge `0.0021` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.2844` n `140` status `ready` deltaP `6.3345` edge `0.0005` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4063` n `140` status `ready` deltaP `0.7956` edge `0.0109` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5447` n `113` status `ready` deltaP `11.1296` edge `-0.0158` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5825` n `130` status `ready` deltaP `4.0126` edge `0.0476` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6145` n `140` status `ready` deltaP `-1.5441` edge `-0.0033` maxDD `-1.2155`
- `market_context_high->crypto_major_1h` score `-1.3069` n `140` status `ready` deltaP `1.728` edge `-0.021` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.319` n `130` status `ready` deltaP `2.7017` edge `-0.0161` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.3265` n `130` status `ready` deltaP `-11.2406` edge `-0.0359` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3776` n `140` status `ready` deltaP `-1.2917` edge `-0.0676` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3832` n `140` status `ready` deltaP `-2.3525` edge `-0.0414` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7395` n `113` status `ready` deltaP `-2.0726` edge `-0.1081` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.0165` n `130` status `ready` deltaP `-8.0042` edge `-0.214` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5012` n `113` status `ready` deltaP `-18.8191` edge `-0.1491` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.8095` n `113` status `ready` deltaP `-4.033` edge `-0.2886` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-13.6859` n `130` status `ready` deltaP `-9.7232` edge `-0.3495` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
