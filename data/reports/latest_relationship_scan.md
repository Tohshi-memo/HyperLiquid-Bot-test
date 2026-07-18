# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T02:52:29.202581+00:00`
- Price records: `672`
- Market context records: `7095`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.4407` n `160` status `ready` deltaP `16.875` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1204` n `160` status `ready` deltaP `4.7979` edge `0.0031` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.2548` n `160` status `ready` deltaP `-0.2807` edge `0.0365` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.4021` n `160` status `ready` deltaP `1.003` edge `0.0282` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4294` n `160` status `ready` deltaP `1.8151` edge `-0.0052` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.567` n `160` status `ready` deltaP `3.8024` edge `0.0372` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.842` n `160` status `ready` deltaP `-4.0681` edge `-0.0192` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.4021` n `160` status `ready` deltaP `-4.8933` edge `-0.0436` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.4128` n `160` status `ready` deltaP `-5.4379` edge `-0.0047` maxDD `-2.1427`
- `market_context_high->unknown_4h` score `-1.6914` n `160` status `ready` deltaP `-7.9268` edge `-0.0038` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0377` n `160` status `ready` deltaP `3.0651` edge `-0.0394` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3387` n `160` status `ready` deltaP `1.5701` edge `-0.0404` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-2.9597` n `160` status `ready` deltaP `4.6799` edge `0.0178` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.0047` n `160` status `ready` deltaP `-5.9722` edge `-0.0797` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.1586` n `160` status `ready` deltaP `-1.0213` edge `-0.0196` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.1788` n `160` status `ready` deltaP `-7.0833` edge `-0.0183` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.2292` n `160` status `ready` deltaP `-6.6921` edge `-0.0095` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.3771` n `160` status `ready` deltaP `1.4024` edge `-0.1963` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8005` n `160` status `ready` deltaP `-23.1597` edge `-0.0643` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.1206` n `160` status `ready` deltaP `-24.6181` edge `-0.132` maxDD `-43.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
