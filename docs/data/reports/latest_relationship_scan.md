# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T19:22:32.558860+00:00`
- Price records: `672`
- Market context records: `4752`
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

- `market_context_high->unknown_1h` score `81.3575` n `139` status `ready` deltaP `13.3428` edge `6.7326` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.9285` n `136` status `ready` deltaP `13.0022` edge `0.5284` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.225` n `124` status `ready` deltaP `15.7482` edge `0.2561` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4191` n `136` status `ready` deltaP `6.9225` edge `0.007` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4686` n `139` status `ready` deltaP `2.6924` edge `0.0226` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5955` n `136` status `ready` deltaP `5.8554` edge `0.0532` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9132` n `136` status `ready` deltaP `-1.1119` edge `-0.0028` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9468` n `139` status `ready` deltaP `-1.6779` edge `-0.015` maxDD `-5.2828`
- `market_context_high->fx_1h` score `-1.1988` n `139` status `ready` deltaP `-4.2896` edge `-0.0048` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.4914` n `139` status `ready` deltaP `-2.4846` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.5124` n `136` status `ready` deltaP `7.5502` edge `0.0207` maxDD `-9.0989`
- `market_context_high->metal_1h` score `-2.4696` n `139` status `ready` deltaP `-2.5223` edge `-0.0668` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.6128` n `124` status `ready` deltaP `16.6667` edge `0.0648` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7671` n `139` status `ready` deltaP `-0.9004` edge `-0.0509` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.2676` n `139` status `ready` deltaP `-0.2725` edge `-0.074` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.4042` n `124` status `ready` deltaP `-15.4738` edge `-0.0219` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.7335` n `136` status `ready` deltaP `0.9415` edge `-0.0458` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.371` n `124` status `ready` deltaP `-11.968` edge `-0.1141` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.3016` n `136` status `ready` deltaP `2.161` edge `-0.1422` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.3652` n `136` status `ready` deltaP `3.4074` edge `-0.2711` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
