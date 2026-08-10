# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T16:22:25.585181+00:00`
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

- `market_context_high->equity_24h` score `1.1077` n `136` status `ready` deltaP `4.2894` edge `0.3771` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.7344` n `169` status `ready` deltaP `11.0793` edge `0.0588` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7131` n `136` status `ready` deltaP `18.7634` edge `0.0151` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7039` n `176` status `ready` deltaP `9.5332` edge `0.0294` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0837` n `169` status `ready` deltaP `6.7948` edge `0.0077` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1098` n `176` status `ready` deltaP `4.5727` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.2917` n `136` status `ready` deltaP `3.9058` edge `0.1028` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5241` n `176` status `ready` deltaP `-2.5483` edge `-0.0025` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7642` n `176` status `ready` deltaP `-3.8956` edge `-0.0084` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-0.7965` n `136` status `ready` deltaP `1.2119` edge `0.0537` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-0.8562` n `176` status `ready` deltaP `-1.8678` edge `-0.0108` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2325` n `169` status `ready` deltaP `-1.8843` edge `-0.0119` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.7469` n `176` status `ready` deltaP `-10.3565` edge `-0.0466` maxDD `-5.9993`
- `market_context_high->metal_4h` score `-2.0492` n `169` status `ready` deltaP `-7.2197` edge `-0.0382` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2399` n `169` status `ready` deltaP `-11.101` edge `-0.1297` maxDD `-7.9331`
- `market_context_high->crypto_major_24h` score `-3.5062` n `136` status `ready` deltaP `0.576` edge `-0.0466` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-3.8524` n `176` status `ready` deltaP `-11.0676` edge `-0.0643` maxDD `-11.3025`
- `market_context_high->crypto_alt_4h` score `-3.8633` n `169` status `ready` deltaP `-11.5403` edge `-0.1426` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-3.9823` n `136` status `ready` deltaP `-10.8676` edge `-0.1151` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.7437` n `136` status `ready` deltaP `-5.3752` edge `-0.2136` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
