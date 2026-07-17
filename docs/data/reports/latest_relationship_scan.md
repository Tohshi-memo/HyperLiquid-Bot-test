# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T23:22:32.374514+00:00`
- Price records: `672`
- Market context records: `7079`
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

- `market_context_high->fx_4h` score `0.7503` n `173` status `ready` deltaP `17.8838` edge `0.0133` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0432` n `173` status `ready` deltaP `0.9086` edge `0.0462` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.0644` n `173` status `ready` deltaP `5.5121` edge `0.003` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.409` n `173` status `ready` deltaP `0.6758` edge `0.0295` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4832` n `173` status `ready` deltaP `0.6464` edge `-0.0043` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6262` n `173` status `ready` deltaP `3.1584` edge `0.0339` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.9062` n `173` status `ready` deltaP `-5.1668` edge `-0.0201` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3538` n `173` status `ready` deltaP `-4.8346` edge `-0.0038` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.581` n `173` status `ready` deltaP `-7.8537` edge `-0.0468` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.6661` n `173` status `ready` deltaP `-6.8703` edge `0.0704` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9144` n `173` status `ready` deltaP `4.2227` edge `-0.0313` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1743` n `173` status `ready` deltaP `3.922` edge `-0.035` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.5227` n `173` status `ready` deltaP `-3.2012` edge `-0.058` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0171` n `173` status `ready` deltaP `-0.2511` edge `-0.0066` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0692` n `173` status `ready` deltaP `2.7853` edge `0.0164` maxDD `-24.6094`
- `market_context_high->metal_4h` score `-3.7329` n `173` status `ready` deltaP `-1.1032` edge `-0.0054` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.8014` n `173` status `ready` deltaP `-2.9504` edge `-0.0144` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-5.0053` n `173` status `ready` deltaP `-18.8885` edge `-0.0011` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.998` n `173` status `ready` deltaP `3.9537` edge `-0.1647` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4914` n `173` status `ready` deltaP `-22.7511` edge `-0.112` maxDD `-44.1823`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
