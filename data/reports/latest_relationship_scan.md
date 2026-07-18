# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T00:07:26.863993+00:00`
- Price records: `672`
- Market context records: `7083`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7371` n `170` status `ready` deltaP `17.6883` edge `0.0135` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0615` n `170` status `ready` deltaP `0.4702` edge `0.0476` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1305` n `170` status `ready` deltaP `4.7164` edge `0.0028` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4105` n `170` status `ready` deltaP `0.7062` edge `0.0291` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4431` n `170` status `ready` deltaP `1.4318` edge `-0.0044` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6497` n `170` status `ready` deltaP `2.7809` edge `0.0334` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8935` n `170` status `ready` deltaP `-4.9084` edge `-0.0202` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4319` n `170` status `ready` deltaP `-5.7661` edge `-0.0041` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5568` n `170` status `ready` deltaP `-7.4032` edge `-0.0467` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9541` n `170` status `ready` deltaP `3.7742` edge `-0.0334` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1342` n `170` status `ready` deltaP `4.7686` edge `-0.0355` maxDD `-12.2591`
- `market_context_high->unknown_4h` score `-2.2324` n `170` status `ready` deltaP `-7.7386` edge `0.029` maxDD `-4.742`
- `market_context_high->commodity_24h` score `-2.6008` n `170` status `ready` deltaP `-3.8031` edge `-0.0605` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-3.0121` n `170` status `ready` deltaP `3.7034` edge `0.0176` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0608` n `170` status `ready` deltaP `-0.6115` edge `-0.0098` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.8372` n `170` status `ready` deltaP `-2.3171` edge `-0.006` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.8828` n `170` status `ready` deltaP `-3.848` edge `-0.0152` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-5.3434` n `170` status `ready` deltaP `-20.3064` edge `-0.035` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-8.0795` n `170` status `ready` deltaP `3.3304` edge `-0.171` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4158` n `170` status `ready` deltaP `-23.1495` edge `-0.1164` maxDD `-44.1138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
