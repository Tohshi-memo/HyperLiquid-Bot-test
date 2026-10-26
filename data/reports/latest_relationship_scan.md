# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T08:22:35.149330+00:00`
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

- `market_context_high->unknown_4h` score `17.7089` n `126` status `ready` deltaP `-2.6737` edge `1.5271` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6045` n `113` status `ready` deltaP `28.4445` edge `0.1549` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1522` n `113` status `ready` deltaP `21.8765` edge `0.0309` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0723` n `126` status `ready` deltaP `8.6358` edge `0.0083` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.003` n `136` status `ready` deltaP `5.1603` edge `0.0018` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3245` n `136` status `ready` deltaP `1.5939` edge `0.0124` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3357` n `136` status `ready` deltaP `5.5125` edge `-0.0006` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.4435` n `126` status `ready` deltaP `2.9012` edge `0.0467` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.572` n `113` status `ready` deltaP `11.1296` edge `-0.0193` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.6788` n `136` status `ready` deltaP `-2.4789` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2567` n `126` status `ready` deltaP `3.99` edge `-0.0167` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.4639` n `136` status `ready` deltaP `0.5988` edge `-0.0336` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2856` n `126` status `ready` deltaP `-10.3489` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-3.8336` n `136` status `ready` deltaP `-2.0034` edge `-0.0775` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-4.0014` n `136` status `ready` deltaP `-3.4343` edge `-0.0621` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.8027` n `113` status `ready` deltaP `-2.0726` edge `-0.1162` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.1323` n `126` status `ready` deltaP `-8.7616` edge `-0.2238` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5383` n `113` status `ready` deltaP `-18.9927` edge `-0.1527` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.0071` n `113` status `ready` deltaP `-4.7275` edge `-0.3093` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9077` n `126` status `ready` deltaP `-8.856` edge `-0.3568` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
