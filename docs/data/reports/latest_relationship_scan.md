# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T09:07:13.790202+00:00`
- Price records: `672`
- Market context records: `959`
- Flow alert records: `2689`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.8847` n `156` status `ready` deltaP `33.2532` edge `1.0521` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.9426` n `156` status `ready` deltaP `9.7222` edge `0.6804` maxDD `0.0`
- `market_context_high->equity_24h` score `1.1825` n `156` status `ready` deltaP `1.9231` edge `0.3462` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.4418` n `156` status `ready` deltaP `0.454` edge `0.2333` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.3586` n `204` status `ready` deltaP `2.04` edge `0.0373` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3749` n `204` status `ready` deltaP `1.3503` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.542` n `204` status `ready` deltaP `2.1604` edge `0.0173` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7255` n `204` status `ready` deltaP `2.8942` edge `0.0056` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-1.0345` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->equity_4h` score `-1.2183` n `192` status `ready` deltaP `2.6677` edge `0.0959` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.3497` n `204` status `ready` deltaP `-2.9412` edge `-0.0157` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.5035` n `192` status `ready` deltaP `-0.0635` edge `0.0274` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.5894` n `204` status `ready` deltaP `6.4283` edge `-0.003` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.834` n `204` status `ready` deltaP `1.9109` edge `-0.0216` maxDD `-8.1842`
- `market_context_high->metal_1h` score `-1.8962` n `204` status `ready` deltaP `-2.5155` edge `-0.0304` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-2.4363` n `192` status `ready` deltaP `-0.7749` edge `0.0814` maxDD `-13.0076`
- `market_context_high->crypto_major_4h` score `-2.4509` n `192` status `ready` deltaP `8.9939` edge `0.1064` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-3.2796` n `192` status `ready` deltaP `-2.2485` edge `0.0195` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.3516` n `192` status `ready` deltaP `6.2881` edge `-0.1334` maxDD `-8.3588`
- `market_context_high->unknown_24h` score `-4.1355` n `156` status `ready` deltaP `6.4637` edge `-0.0227` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
