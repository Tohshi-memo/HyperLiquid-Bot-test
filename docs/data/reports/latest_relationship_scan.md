# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T09:07:15.148490+00:00`
- Price records: `672`
- Market context records: `997`
- Flow alert records: `4778`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `12.9001` n `211` status `ready` deltaP `31.6444` edge `0.9229` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1561` n `211` status `ready` deltaP `10.8213` edge `0.3976` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3522` n `211` status `ready` deltaP `1.9823` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5236` n `211` status `ready` deltaP `2.6322` edge `0.0196` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6395` n `211` status `ready` deltaP `1.106` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7176` n `211` status `ready` deltaP `3.137` edge `0.1188` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.744` n `211` status `ready` deltaP `2.7527` edge `0.005` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7524` n `211` status `ready` deltaP `0.3876` edge `0.0006` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2175` n `211` status `ready` deltaP `4.8011` edge `-0.0158` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2395` n `211` status `ready` deltaP `4.6031` edge `0.1265` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5078` n `211` status `ready` deltaP `1.8836` edge `0.077` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7463` n `211` status `ready` deltaP `-1.6288` edge `0.0176` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8718` n `211` status `ready` deltaP `-0.862` edge `-0.0383` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0483` n `211` status `ready` deltaP `-0.5881` edge `-0.0228` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9377` n `211` status `ready` deltaP `7.049` edge `0.0788` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2548` n `211` status `ready` deltaP `-1.7958` edge `0.0575` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3256` n `211` status `ready` deltaP `-1.9386` edge `0.0136` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.6103` n `211` status `ready` deltaP `-1.8493` edge `-0.0226` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.5979` n `211` status `ready` deltaP `-4.7065` edge `-0.1624` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.1818` n `211` status `ready` deltaP `2.8101` edge `0.3971` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
