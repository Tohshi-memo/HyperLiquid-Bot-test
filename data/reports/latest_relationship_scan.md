# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T18:22:38.048635+00:00`
- Price records: `672`
- Market context records: `4748`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7470`

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

- `market_context_high->unknown_1h` score `83.0944` n `136` status `ready` deltaP `13.6184` edge `6.8755` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2716` n `134` status `ready` deltaP `12.4864` edge `0.4771` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.201` n `124` status `ready` deltaP `15.7482` edge `0.2541` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3618` n `134` status `ready` deltaP `7.92` edge `0.0077` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5032` n `134` status `ready` deltaP `6.7005` edge `0.0594` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.5143` n `136` status `ready` deltaP `2.1354` edge `0.0225` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.9241` n `134` status `ready` deltaP `-1.2923` edge `-0.003` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9282` n `136` status `ready` deltaP `-1.3341` edge `-0.0149` maxDD `-5.2828`
- `market_context_high->fx_1h` score `-1.2319` n `136` status `ready` deltaP `-4.6583` edge `-0.0051` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.5082` n `136` status `ready` deltaP `-2.6946` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.5572` n `134` status `ready` deltaP `7.3808` edge `0.0181` maxDD `-9.0989`
- `market_context_high->metal_1h` score `-2.5051` n `136` status `ready` deltaP `-2.8751` edge `-0.069` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5135` n `124` status `ready` deltaP `17.3611` edge `0.0729` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.6401` n `136` status `ready` deltaP `0.0132` edge `-0.0407` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1616` n `136` status `ready` deltaP `0.6252` edge `-0.0664` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.333` n `124` status `ready` deltaP `-14.7794` edge `-0.0206` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.6828` n `134` status `ready` deltaP `1.6768` edge `-0.0442` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.241` n `124` status `ready` deltaP `-11.2736` edge `-0.1079` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.356` n `134` status `ready` deltaP `2.0136` edge `-0.1482` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.4196` n `134` status `ready` deltaP `3.0966` edge `-0.276` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
