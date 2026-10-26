# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T06:52:31.779167+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `21.3979` n `120` status `ready` deltaP `-2.8659` edge `1.8358` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6068` n `113` status `ready` deltaP `28.4445` edge `0.1552` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.2126` n `113` status `ready` deltaP `22.9182` edge `0.0317` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.0501` n `130` status `ready` deltaP `5.684` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0253` n `120` status `ready` deltaP `8.0488` edge `0.0083` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3286` n `130` status `ready` deltaP `-0.2787` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3815` n `130` status `ready` deltaP `4.8111` edge `-0.0018` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.599` n `120` status `ready` deltaP `0.5996` edge `0.0421` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.646` n `130` status `ready` deltaP `-1.8793` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6792` n `113` status `ready` deltaP `10.0879` edge `-0.0261` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.1979` n `120` status `ready` deltaP `4.9695` edge `-0.0157` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3407` n `130` status `ready` deltaP `2.158` edge `-0.0282` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1767` n `120` status `ready` deltaP `-8.4045` edge `-0.0356` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3748` n `130` status `ready` deltaP `-0.2326` edge `-0.0743` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4576` n `130` status `ready` deltaP `-1.8333` edge `-0.0544` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-5.0402` n `113` status `ready` deltaP `-3.1142` edge `-0.1397` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.3479` n `120` status `ready` deltaP `-10.8232` edge `-0.2377` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5711` n `113` status `ready` deltaP `-18.9927` edge `-0.1569` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.3748` n `113` status `ready` deltaP `-5.7691` edge `-0.3495` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9535` n `120` status `ready` deltaP `-8.313` edge `-0.3663` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
