# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T01:37:27.436510+00:00`
- Price records: `672`
- Market context records: `7090`
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

- `market_context_high->fx_4h` score `0.7235` n `165` status `ready` deltaP `17.4584` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1447` n `165` status `ready` deltaP `4.5382` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3297` n `165` status `ready` deltaP `-0.3321` edge `0.0306` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.4383` n `165` status `ready` deltaP `1.5995` edge `-0.0049` maxDD `-2.2895`
- `market_context_high->crypto_alt_1h` score `-0.6172` n `165` status `ready` deltaP `1.0806` edge `0.0278` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.6222` n `165` status `ready` deltaP `3.3406` edge `0.0332` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8887` n `165` status `ready` deltaP `-4.8158` edge `-0.0202` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4675` n `165` status `ready` deltaP `-6.1368` edge `-0.0046` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4903` n `165` status `ready` deltaP `-6.274` edge `-0.0457` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.8314` n `165` status `ready` deltaP `-8.8738` edge `-0.0122` maxDD `-4.742`
- `market_context_high->equity_1h` score `-2.0155` n `165` status `ready` deltaP `3.1183` edge `-0.0369` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.232` n `165` status `ready` deltaP `3.2178` edge `-0.0377` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.7881` n `165` status `ready` deltaP `-4.8548` edge `-0.0691` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-3.0027` n `165` status `ready` deltaP `3.9431` edge `0.0172` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1942` n `165` status `ready` deltaP `-1.9466` edge `-0.018` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.0275` n `165` status `ready` deltaP `-5.4166` edge `-0.0168` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.0309` n `165` status `ready` deltaP `-4.4383` edge `-0.008` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.2354` n `165` status `ready` deltaP `2.1618` edge `-0.1832` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.7837` n `165` status `ready` deltaP `-22.7841` edge `-0.0654` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.2804` n `165` status `ready` deltaP `-23.9773` edge `-0.1238` maxDD `-43.8444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
