# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T19:07:27.168139+00:00`
- Price records: `672`
- Market context records: `4751`
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

- `market_context_high->unknown_1h` score `81.3155` n `139` status `ready` deltaP `13.1931` edge `6.7301` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.9297` n `136` status `ready` deltaP `13.0022` edge `0.5285` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2202` n `124` status `ready` deltaP `15.7482` edge `0.2557` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.4175` n `136` status `ready` deltaP `6.9225` edge `0.0072` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4698` n `139` status `ready` deltaP `2.6924` edge `0.0225` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5924` n `136` status `ready` deltaP `5.8554` edge `0.0536` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9044` n `136` status `ready` deltaP `-0.9595` edge `-0.0027` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9499` n `139` status `ready` deltaP `-1.6779` edge `-0.0154` maxDD `-5.2828`
- `market_context_high->fx_1h` score `-1.1988` n `139` status `ready` deltaP `-4.2896` edge `-0.0048` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.4926` n `139` status `ready` deltaP `-2.4846` edge `-0.0074` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.4966` n `136` status `ready` deltaP `7.7026` edge `0.021` maxDD `-9.0989`
- `market_context_high->metal_1h` score `-2.4696` n `139` status `ready` deltaP `-2.5223` edge `-0.0668` maxDD `-15.3067`
- `market_context_high->commodity_24h` score `-2.5874` n `124` status `ready` deltaP `16.8403` edge `0.0669` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.7648` n `139` status `ready` deltaP `-0.9004` edge `-0.0506` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.266` n `139` status `ready` deltaP `-0.2725` edge `-0.0738` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.3855` n `124` status `ready` deltaP `-15.3002` edge `-0.0215` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.7288` n `136` status `ready` deltaP `0.9415` edge `-0.0452` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.3379` n `124` status `ready` deltaP `-11.7944` edge `-0.1125` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.2812` n `136` status `ready` deltaP `2.3135` edge `-0.1406` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.3613` n `136` status `ready` deltaP `3.4074` edge `-0.2706` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
