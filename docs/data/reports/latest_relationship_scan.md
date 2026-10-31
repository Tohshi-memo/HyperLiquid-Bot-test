# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T01:22:27.990513+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1585.1739` n `134` status `ready` deltaP `-6.0894` edge `132.1814` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `144.7604` n `95` status `ready` deltaP `-3.0602` edge `12.1124` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4662` n `134` status `ready` deltaP `0.4163` edge `3.3827` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.7524` n `83` status `ready` deltaP `24.2121` edge `0.5507` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.9667` n `134` status `ready` deltaP `18.2214` edge `0.7348` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.8412` n `134` status `ready` deltaP `36.8263` edge `0.0929` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4842` n `95` status `ready` deltaP `11.1881` edge `0.132` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4438` n `134` status `ready` deltaP `15.3099` edge `0.0568` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3618` n `134` status `ready` deltaP `10.4545` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3264` n `134` status `ready` deltaP `14.9163` edge `0.032` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1683` n `134` status `ready` deltaP `4.033` edge `0.0747` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0119` n `134` status `ready` deltaP `2.0864` edge `0.143` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1079` n `134` status `ready` deltaP `6.7164` edge `0.049` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1439` n `134` status `ready` deltaP `3.4409` edge `0.0165` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4634` n `134` status `ready` deltaP `0.4414` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6913` n `134` status `ready` deltaP `3.9257` edge `0.1499` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.8407` n `95` status `ready` deltaP `2.0422` edge `-0.0037` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.8809` n `134` status `ready` deltaP `-2.6946` edge `0.0004` maxDD `-1.1344`
- `news_risk_high->commodity_1h` score `-0.9428` n `95` status `ready` deltaP `-8.358` edge `0.0005` maxDD `-1.9193`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
