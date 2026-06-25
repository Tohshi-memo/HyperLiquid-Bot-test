# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T18:52:34.278350+00:00`
- Price records: `672`
- Market context records: `4750`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `82.1363` n `138` status `ready` deltaP `13.523` edge `6.7963` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.9356` n `135` status `ready` deltaP `12.7462` edge `0.5307` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.213` n `124` status `ready` deltaP `15.7482` edge `0.2551` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3942` n `135` status `ready` deltaP `7.3419` edge `0.0074` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.449` n `138` status `ready` deltaP `2.892` edge `0.0229` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5519` n `135` status `ready` deltaP `6.2748` edge `0.056` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9177` n `135` status `ready` deltaP `-1.1992` edge `-0.0028` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9182` n `138` status `ready` deltaP `-1.3234` edge `-0.0137` maxDD `-5.2828`
- `market_context_high->index_1h` score `-0.9488` n `138` status `ready` deltaP `-2.1197` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->fx_1h` score `-1.175` n `138` status `ready` deltaP `-3.9768` edge `-0.0049` maxDD `-0.9869`
- `market_context_high->commodity_4h` score `-1.5262` n `135` status `ready` deltaP `7.4684` edge `0.0201` maxDD `-9.0989`
- `market_context_high->metal_1h` score `-2.4892` n `138` status `ready` deltaP `-2.7792` edge `-0.0676` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5619` n `124` status `ready` deltaP `17.0139` edge `0.069` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7115` n `138` status `ready` deltaP `-0.5511` edge `-0.0461` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2177` n `138` status `ready` deltaP `0.0716` edge `-0.0699` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.368` n `124` status `ready` deltaP `-15.1266` edge `-0.0212` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.7098` n `135` status `ready` deltaP `1.3064` edge `-0.0452` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.3048` n `124` status `ready` deltaP `-11.6208` edge `-0.1109` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.3357` n `135` status `ready` deltaP `2.0901` edge `-0.1461` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.3958` n `135` status `ready` deltaP `3.1786` edge `-0.2735` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
