# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T09:22:17.363081+00:00`
- Price records: `672`
- Market context records: `998`
- Flow alert records: `4781`
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

- `market_context_high->crypto_major_24h` score `12.9139` n `211` status `ready` deltaP `31.6964` edge `0.9237` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1611` n `211` status `ready` deltaP `10.8383` edge `0.3979` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.36` n `211` status `ready` deltaP `1.8326` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5368` n `211` status `ready` deltaP `2.4825` edge `0.0195` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6395` n `211` status `ready` deltaP `1.106` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7389` n `211` status `ready` deltaP `3.0209` edge `0.1178` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.744` n `211` status `ready` deltaP `2.7527` edge `0.005` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7563` n `211` status `ready` deltaP `0.3124` edge `0.0006` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2175` n `211` status `ready` deltaP `4.8011` edge `-0.0158` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.256` n `211` status `ready` deltaP `4.6364` edge `0.1249` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5058` n `211` status `ready` deltaP `1.9229` edge `0.0769` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7443` n `211` status `ready` deltaP `-1.5883` edge `0.0175` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8625` n `211` status `ready` deltaP `-0.7123` edge `-0.0381` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0459` n `211` status `ready` deltaP `-0.5881` edge `-0.0226` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9285` n `211` status `ready` deltaP `7.119` edge `0.0791` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2408` n `211` status `ready` deltaP `-1.7113` edge `0.0581` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3168` n `211` status `ready` deltaP `-1.8886` edge `0.014` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.616` n `211` status `ready` deltaP `-1.9286` edge `-0.0228` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.5947` n `211` status `ready` deltaP `-4.6443` edge `-0.1624` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.1527` n `211` status `ready` deltaP `2.8744` edge `0.4004` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
