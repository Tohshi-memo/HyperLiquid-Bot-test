# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T11:37:29.599237+00:00`
- Price records: `672`
- Market context records: `7135`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.7723` n `139` status `ready` deltaP `17.8584` edge `0.0153` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1326` n `151` status `ready` deltaP `4.6903` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.431` n `151` status `ready` deltaP `-2.6986` edge `0.0421` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6166` n `151` status `ready` deltaP `-0.1814` edge `0.0252` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6401` n `151` status `ready` deltaP `3.6424` edge `0.0347` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.694` n `151` status `ready` deltaP `-1.5743` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7128` n `151` status `ready` deltaP `1.8103` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3404` n `151` status `ready` deltaP `-4.5128` edge `-0.0053` maxDD `-2.1049`
- `market_context_high->commodity_4h` score `-2.1985` n `139` status `ready` deltaP `-5.7565` edge `-0.0413` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2054` n `139` status `ready` deltaP `-5.2115` edge `0.0197` maxDD `-5.1658`
- `market_context_high->crypto_major_4h` score `-3.3588` n `139` status `ready` deltaP `0.5736` edge `-0.0054` maxDD `-24.6569`
- `market_context_high->equity_1h` score `-3.504` n `151` status `ready` deltaP `-0.0674` edge `-0.0458` maxDD `-14.9936`
- `market_context_high->index_4h` score `-4.0419` n `139` status `ready` deltaP `-2.3283` edge `-0.0514` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.3078` n `139` status `ready` deltaP `-7.7229` edge `-0.0126` maxDD `-5.2585`
- `market_context_high->commodity_24h` score `-4.4243` n `134` status `ready` deltaP `-13.1271` edge `-0.1503` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9442` n `134` status `ready` deltaP `-15.5861` edge `-0.0254` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.4392` n `139` status `ready` deltaP `-3.4195` edge `-0.0419` maxDD `-23.0856`
- `market_context_high->unknown_24h` score `-10.05` n `134` status `ready` deltaP `-32.2088` edge `-0.1081` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.9235` n `139` status `ready` deltaP `-1.5902` edge `-0.2577` maxDD `-64.3595`
- `market_context_high->metal_24h` score `-14.4459` n `134` status `ready` deltaP `-29.2392` edge `-0.1851` maxDD `-40.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
