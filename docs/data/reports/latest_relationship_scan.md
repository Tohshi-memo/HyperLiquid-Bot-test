# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T02:07:23.854824+00:00`
- Price records: `672`
- Market context records: `7092`
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

- `market_context_high->fx_4h` score `0.4633` n `163` status `ready` deltaP `17.2948` edge `0.0141` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1648` n `163` status `ready` deltaP `4.2724` edge `0.0029` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3395` n `163` status `ready` deltaP `-0.6796` edge `0.0321` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.4252` n `163` status `ready` deltaP `1.8653` edge `-0.005` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5901` n `163` status `ready` deltaP `3.703` edge `0.0349` maxDD `-7.1523`
- `market_context_high->crypto_alt_1h` score `-0.6396` n `163` status `ready` deltaP `0.7999` edge `0.0278` maxDD `-4.5815`
- `market_context_high->commodity_1h` score `-0.8683` n `163` status `ready` deltaP `-4.5277` edge `-0.0195` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4307` n `163` status `ready` deltaP `-5.6758` edge `-0.0046` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.456` n `163` status `ready` deltaP `-5.7647` edge `-0.0447` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.7618` n `163` status `ready` deltaP `-8.502` edge `-0.009` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0044` n `163` status `ready` deltaP `3.4064` edge `-0.0374` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.2742` n `163` status `ready` deltaP `2.5709` edge `-0.0388` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.8724` n `163` status `ready` deltaP `-5.2935` edge `-0.0732` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-2.9624` n `163` status `ready` deltaP `4.5975` edge `0.018` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1809` n `163` status `ready` deltaP `-1.5562` edge `-0.0189` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.0882` n `163` status `ready` deltaP `-6.071` edge `-0.0175` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.1089` n `163` status `ready` deltaP `-5.3232` edge `-0.0086` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.2845` n `163` status `ready` deltaP `1.9537` edge `-0.1881` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.802` n `163` status `ready` deltaP `-22.938` edge `-0.0659` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.2123` n `163` status `ready` deltaP `-24.2352` edge `-0.1269` maxDD `-43.6711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
