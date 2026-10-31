# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T08:07:25.739722+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_24h` score `1702.5795` n `130` status `ready` deltaP `-5.2644` edge `141.9597` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `108.5226` n `98` status `ready` deltaP `-5.6427` edge `9.1098` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `35.8705` n `130` status `ready` deltaP `2.0849` edge `2.9886` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.7477` n `130` status `ready` deltaP `21.7629` edge `0.8596` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `6.0645` n `95` status `ready` deltaP `20.9258` edge `0.4722` maxDD `-5.8399`
- `market_context_high->index_24h` score `4.2632` n `130` status `ready` deltaP `40.422` edge `0.1041` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9236` n `98` status `ready` deltaP `8.2457` edge `0.1049` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.8236` n `130` status `ready` deltaP `12.3952` edge `0.0152` maxDD `-0.3362`
- `market_context_high->metal_4h` score `0.3796` n `130` status `ready` deltaP `15.6402` edge `0.0322` maxDD `-1.6911`
- `market_context_high->commodity_4h` score `0.3265` n `130` status `ready` deltaP `13.9634` edge `0.056` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.3132` n `130` status `ready` deltaP `5.0645` edge `0.0799` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.2033` n `130` status `ready` deltaP `8.4615` edge `0.0633` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0098` n `130` status `ready` deltaP `2.3218` edge `0.1417` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.052` n `130` status `ready` deltaP `4.5071` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2168` n `130` status `ready` deltaP `2.6946` edge `0.0154` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.4242` n `130` status `ready` deltaP `5.2804` edge `0.1751` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.4707` n `130` status `ready` deltaP `0.3119` edge `-0.0027` maxDD `-0.4445`
- `market_context_high->index_1h` score `-0.6429` n `130` status `ready` deltaP `0.1912` edge `0.001` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8235` n `130` status `ready` deltaP `3.1437` edge `0.051` maxDD `-7.536`
- `news_risk_high->index_1h` score `-0.8682` n `98` status `ready` deltaP `1.7139` edge `-0.0038` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
