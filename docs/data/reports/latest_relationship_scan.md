# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T21:52:27.365660+00:00`
- Price records: `672`
- Market context records: `7072`
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

- `market_context_high->fx_4h` score `0.7005` n `179` status `ready` deltaP `17.3968` edge `0.0124` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1268` n `179` status `ready` deltaP `0.8087` edge `0.0399` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1718` n `179` status `ready` deltaP `4.2301` edge `0.0026` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3528` n `179` status `ready` deltaP `1.4259` edge `0.0317` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6112` n `179` status `ready` deltaP `3.551` edge `0.0332` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.6892` n `179` status `ready` deltaP `-0.8455` edge `-0.0041` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-0.8023` n `179` status `ready` deltaP `-5.2519` edge `0.1316` maxDD `-4.742`
- `market_context_high->commodity_1h` score `-0.8619` n `179` status `ready` deltaP `-4.3906` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3614` n `179` status `ready` deltaP `-4.9753` edge `-0.0035` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6737` n `179` status `ready` deltaP `-7.851` edge `-0.0462` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8926` n `179` status `ready` deltaP `4.2518` edge `-0.0287` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2517` n `179` status `ready` deltaP `2.3138` edge `-0.0342` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4712` n `179` status `ready` deltaP `-2.8282` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9874` n `179` status `ready` deltaP `-0.0238` edge `-0.0043` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0956` n `179` status `ready` deltaP `2.4126` edge `0.0155` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6494` n `179` status `ready` deltaP `-1.2453` edge `-0.0131` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.692` n `179` status `ready` deltaP `-0.7273` edge `-0.0045` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.4279` n `179` status `ready` deltaP `-16.8897` edge `0.0596` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.936` n `179` status `ready` deltaP `3.9898` edge `-0.157` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.675` n `179` status `ready` deltaP `-22.1155` edge `-0.1039` maxDD `-44.3931`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
