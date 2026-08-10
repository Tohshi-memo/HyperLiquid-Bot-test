# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T16:07:36.381250+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->equity_24h` score `0.9811` n `136` status `ready` deltaP `4.1161` edge `0.3677` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.7562` n `169` status `ready` deltaP `11.2317` edge `0.0596` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7158` n `176` status `ready` deltaP `9.6829` edge `0.0294` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7155` n `136` status `ready` deltaP `18.7634` edge `0.0153` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.0691` n `169` status `ready` deltaP `6.9473` edge `0.0079` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1098` n `176` status `ready` deltaP `4.5727` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.3151` n `136` status `ready` deltaP `3.7325` edge `0.102` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5164` n `176` status `ready` deltaP `-2.3986` edge `-0.0025` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7533` n `176` status `ready` deltaP `-3.7459` edge `-0.008` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-0.7989` n `136` status `ready` deltaP `1.2119` edge `0.0535` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-0.8468` n `176` status `ready` deltaP `-1.7181` edge `-0.0106` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2325` n `169` status `ready` deltaP `-1.8843` edge `-0.0119` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.7376` n `176` status `ready` deltaP `-10.2068` edge `-0.0464` maxDD `-5.9993`
- `market_context_high->metal_4h` score `-2.0343` n `169` status `ready` deltaP `-7.0673` edge `-0.0373` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2642` n `169` status `ready` deltaP `-11.2535` edge `-0.1318` maxDD `-7.9331`
- `market_context_high->crypto_major_24h` score `-3.5741` n `136` status `ready` deltaP `0.4027` edge `-0.0511` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.8536` n `176` status `ready` deltaP `-11.0676` edge `-0.0644` maxDD `-11.3025`
- `market_context_high->crypto_alt_4h` score `-3.8883` n `169` status `ready` deltaP `-11.6927` edge `-0.1448` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.0285` n `136` status `ready` deltaP `-11.0409` edge `-0.1178` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.7336` n `136` status `ready` deltaP `-5.3752` edge `-0.2123` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
