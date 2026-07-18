# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T01:52:23.813653+00:00`
- Price records: `672`
- Market context records: `7091`
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

- `market_context_high->fx_4h` score `0.4669` n `164` status `ready` deltaP `17.3781` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.154` n `164` status `ready` deltaP `4.407` edge `0.0029` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3326` n `164` status `ready` deltaP `-0.5039` edge `0.0315` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.4314` n `164` status `ready` deltaP `1.7307` edge `-0.0049` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6082` n `164` status `ready` deltaP `3.5198` edge `0.0338` maxDD `-7.1523`
- `market_context_high->crypto_alt_1h` score `-0.6271` n `164` status `ready` deltaP `0.942` edge `0.0279` maxDD `-4.5815`
- `market_context_high->commodity_1h` score `-0.8782` n `164` status `ready` deltaP `-4.6736` edge `-0.0198` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4492` n `164` status `ready` deltaP `-5.9077` edge `-0.0046` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4693` n `164` status `ready` deltaP `-5.9451` edge `-0.0452` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.7925` n `164` status `ready` deltaP `-8.689` edge `-0.0107` maxDD `-4.5613`
- `market_context_high->equity_1h` score `-2.0104` n `164` status `ready` deltaP `3.2605` edge `-0.0372` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2534` n `164` status `ready` deltaP `2.8963` edge `-0.0383` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.8284` n `164` status `ready` deltaP `-5.0728` edge `-0.071` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-2.9827` n `164` status `ready` deltaP `4.2683` edge `0.0176` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1912` n `164` status `ready` deltaP `-1.8293` edge `-0.0184` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.0583` n `164` status `ready` deltaP `-5.7418` edge `-0.0172` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.0709` n `164` status `ready` deltaP `-4.8781` edge `-0.0084` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.2722` n `164` status `ready` deltaP `1.8293` edge `-0.1857` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.7923` n `164` status `ready` deltaP `-22.8616` edge `-0.0656` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.2473` n `164` status `ready` deltaP `-24.1065` edge `-0.1254` maxDD `-43.7599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
