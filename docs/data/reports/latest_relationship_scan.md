# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T17:37:26.394216+00:00`
- Price records: `672`
- Market context records: `4745`
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

- `market_context_high->unknown_1h` score `83.1351` n `136` status `ready` deltaP `13.9178` edge `6.8769` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2145` n `133` status `ready` deltaP `12.2227` edge `0.4741` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.1698` n `124` status `ready` deltaP `15.7482` edge `0.2515` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.3531` n `133` status `ready` deltaP `8.0575` edge `0.0079` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4664` n `136` status `ready` deltaP `2.5845` edge `0.0235` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.4766` n `133` status `ready` deltaP `6.838` edge `0.0619` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.9157` n `136` status `ready` deltaP `-1.1844` edge `-0.0143` maxDD `-5.2828`
- `market_context_high->fx_4h` score `-0.9308` n `133` status `ready` deltaP `-1.3914` edge `-0.0032` maxDD `-1.882`
- `market_context_high->fx_1h` score `-1.2331` n `136` status `ready` deltaP `-4.6583` edge `-0.0052` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.5082` n `136` status `ready` deltaP `-2.6946` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.5671` n `133` status `ready` deltaP `7.2872` edge `0.0179` maxDD `-9.0989`
- `market_context_high->commodity_24h` score `-2.4372` n `124` status `ready` deltaP `17.8819` edge `0.0792` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.5137` n `136` status `ready` deltaP `-3.0248` edge `-0.0691` maxDD `-15.3067`
- `market_context_high->crypto_alt_1h` score `-2.6151` n `136` status `ready` deltaP `0.1629` edge `-0.0385` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1141` n `136` status `ready` deltaP `0.9246` edge `-0.0623` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.2817` n `124` status `ready` deltaP `-14.2585` edge `-0.0198` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.6715` n `133` status `ready` deltaP `1.7582` edge `-0.0433` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.1454` n `124` status `ready` deltaP `-10.7527` edge `-0.1034` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.3485` n `133` status `ready` deltaP `2.0837` edge `-0.1477` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.4381` n `133` status `ready` deltaP `3.1611` edge `-0.2788` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
