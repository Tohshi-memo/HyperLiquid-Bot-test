# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T11:37:27.934521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7269`

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

- `market_context_high->unknown_24h` score `2130.1793` n `117` status `ready` deltaP `-6.7174` edge `177.6027` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `98.6382` n `98` status `ready` deltaP `-5.493` edge `8.2851` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `52.325` n `117` status `ready` deltaP `1.4866` edge `4.3638` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.4795` n `40` status `ready` deltaP `46.0417` edge `1.1548` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.2507` n `117` status `ready` deltaP `25.8814` edge `0.9574` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.0628` n `98` status `ready` deltaP `18.4856` edge `0.4373` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.5616` n `117` status `ready` deltaP `41.8269` edge `0.1196` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8756` n `98` status `ready` deltaP `7.7966` edge `0.1039` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.7393` n `117` status `ready` deltaP `18.2784` edge `0.0349` maxDD `-1.2916`
- `market_context_high->metal_1h` score `0.6231` n `117` status `ready` deltaP `13.8902` edge `0.0163` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.4232` n `117` status `ready` deltaP `5.4494` edge `0.0865` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3344` n `117` status `ready` deltaP `8.5253` edge `0.0738` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.2708` n `117` status `ready` deltaP `3.5413` edge `0.1542` maxDD `-4.7801`
- `market_context_high->commodity_4h` score `-0.0071` n `117` status `ready` deltaP `10.5861` edge `0.0504` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.0354` n `117` status `ready` deltaP `4.7636` edge `-0.0009` maxDD `-0.1655`
- `market_context_high->metal_24h` score `-0.0645` n `117` status `ready` deltaP `10.3232` edge `0.1876` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.3258` n `117` status `ready` deltaP `2.7192` edge `-0.0019` maxDD `-0.3062`
- `market_context_high->index_1h` score `-0.4391` n `117` status `ready` deltaP `2.6486` edge `0.0016` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4513` n `117` status `ready` deltaP `0.0025` edge `0.0138` maxDD `-0.4475`
- `market_context_high->crypto_alt_1h` score `-0.8277` n `117` status `ready` deltaP `2.2672` edge `0.0563` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
