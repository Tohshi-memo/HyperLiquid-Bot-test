# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T21:37:27.597268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0005` n `145` status `ready` deltaP `20.4064` edge `0.0281` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9005` n `177` status `ready` deltaP `12.2107` edge `0.0651` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6266` n `183` status `ready` deltaP `8.6426` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0991` n `177` status `ready` deltaP `6.6772` edge `0.0072` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1286` n `183` status `ready` deltaP `4.2857` edge `0.0001` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.5658` n `145` status `ready` deltaP `-0.3299` edge `0.0828` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6479` n `183` status `ready` deltaP `-4.7642` edge `-0.0034` maxDD `-0.832`
- `market_context_high->index_4h` score `-0.924` n `177` status `ready` deltaP `-4.0125` edge `-0.012` maxDD `-1.3774`
- `market_context_high->metal_24h` score `-0.939` n `145` status `ready` deltaP `2.5482` edge `0.0372` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.0712` n `183` status `ready` deltaP `-3.596` edge `-0.0097` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2494` n `183` status `ready` deltaP `-4.7266` edge `-0.009` maxDD `-2.0884`
- `market_context_high->equity_24h` score `-1.3803` n `145` status `ready` deltaP `-0.1745` edge `0.2383` maxDD `-24.4616`
- `market_context_high->crypto_alt_1h` score `-2.7544` n `183` status `ready` deltaP `-10.1387` edge `-0.0422` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0484` n `177` status `ready` deltaP `-6.4868` edge `-0.0344` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.2666` n `145` status `ready` deltaP `-2.9152` edge `-0.0841` maxDD `-18.8874`
- `market_context_high->equity_4h` score `-3.6989` n `177` status `ready` deltaP `-13.0968` edge `-0.1122` maxDD `-12.9761`
- `market_context_high->crypto_major_1h` score `-3.7448` n `183` status `ready` deltaP `-10.1166` edge `-0.0542` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-6.0374` n `145` status `ready` deltaP `-12.8226` edge `-0.1784` maxDD `-13.8056`
- `market_context_high->crypto_alt_4h` score `-6.4225` n `177` status `ready` deltaP `-13.1416` edge `-0.1439` maxDD `-17.6293`
- `market_context_high->commodity_24h` score `-7.18` n `145` status `ready` deltaP `-2.0343` edge `-0.1148` maxDD `-47.7059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
