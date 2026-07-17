# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T12:18:55.574409+00:00`
- Price records: `672`
- Market context records: `7027`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11520`

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

- `market_context_high->fx_1h` score `-0.2981` n `217` status `ready` deltaP `1.3928` edge `0.001` maxDD `-0.5465`
- `market_context_high->crypto_alt_1h` score `-0.578` n `217` status `ready` deltaP `1.5101` edge `0.0282` maxDD `-4.5815`
- `market_context_high->fx_4h` score `-0.6336` n `217` status `ready` deltaP `11.2342` edge `0.0073` maxDD `-1.741`
- `market_context_high->metal_1h` score `-0.6763` n `217` status `ready` deltaP `-1.6391` edge `0.001` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7061` n `217` status `ready` deltaP `0.0897` edge `0.0` maxDD `-2.2895`
- `market_context_high->unknown_24h` score `-0.9235` n `204` status `ready` deltaP `-7.0772` edge `0.3838` maxDD `-18.7342`
- `market_context_high->crypto_major_1h` score `-1.0909` n `217` status `ready` deltaP `3.0189` edge `0.0242` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.2187` n `217` status `ready` deltaP `-2.7898` edge `0.0009` maxDD `-3.0421`
- `market_context_high->commodity_1h` score `-1.3488` n `217` status `ready` deltaP `-4.0433` edge `-0.0189` maxDD `-2.3233`
- `market_context_high->commodity_4h` score `-1.4362` n `217` status `ready` deltaP `-4.1763` edge `-0.0371` maxDD `-3.2013`
- `market_context_high->index_4h` score `-1.8595` n `217` status `ready` deltaP `6.7958` edge `-0.0138` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9782` n `217` status `ready` deltaP `5.3256` edge `0.0092` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.1569` n `217` status `ready` deltaP `-6.0146` edge `0.0801` maxDD `-8.913`
- `market_context_high->commodity_24h` score `-2.6368` n `204` status `ready` deltaP `-2.7982` edge `-0.0702` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7301` n `217` status `ready` deltaP `0.9786` edge `0.022` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.9647` n `217` status `ready` deltaP `2.7049` edge `-0.0168` maxDD `-15.1969`
- `market_context_high->crypto_major_4h` score `-3.088` n `217` status `ready` deltaP `2.0632` edge `0.0188` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.8575` n `204` status `ready` deltaP `-3.5131` edge `-0.0134` maxDD `-4.1045`
- `market_context_high->equity_4h` score `-7.2842` n `217` status `ready` deltaP `4.1658` edge `-0.0746` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.5602` n `204` status `ready` deltaP `-11.6524` edge `-0.0554` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
