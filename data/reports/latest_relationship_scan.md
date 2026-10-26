# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T09:07:31.761746+00:00`
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

- `market_context_high->unknown_4h` score `18.6174` n `129` status `ready` deltaP `-2.2677` edge `1.6001` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6014` n `113` status `ready` deltaP `28.4445` edge `0.1545` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1228` n `113` status `ready` deltaP `21.3557` edge `0.0306` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.1157` n `129` status `ready` deltaP `9.1936` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0869` n `139` status `ready` deltaP `6.1442` edge `0.0021` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.2734` n `139` status `ready` deltaP `6.5599` edge `0.0004` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3787` n `139` status `ready` deltaP `1.021` edge `0.0117` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5509` n `113` status `ready` deltaP `11.1296` edge `-0.0166` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5932` n `129` status `ready` deltaP `3.8193` edge `0.048` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6317` n `139` status `ready` deltaP `-1.7695` edge `-0.004` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.3109` n `129` status `ready` deltaP `2.901` edge `-0.0164` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3493` n `139` status `ready` deltaP `1.3785` edge `-0.0241` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.3239` n `129` status `ready` deltaP `-11.1009` edge `-0.0365` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4315` n `139` status `ready` deltaP `-1.6823` edge `-0.0719` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.745` n `139` status `ready` deltaP `-2.6139` edge `-0.0462` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7528` n `113` status `ready` deltaP `-2.0726` edge `-0.1098` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.0642` n `129` status `ready` deltaP `-8.4574` edge `-0.2171` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.509` n `113` status `ready` deltaP `-18.8191` edge `-0.1501` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.8544` n `113` status `ready` deltaP `-4.2066` edge `-0.2932` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9115` n `129` status `ready` deltaP `-9.5895` edge `-0.3524` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
