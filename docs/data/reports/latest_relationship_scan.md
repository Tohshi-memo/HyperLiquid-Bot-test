# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T09:52:14.813807+00:00`
- Price records: `672`
- Market context records: `1000`
- Flow alert records: `4787`
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

- `market_context_high->crypto_major_24h` score `12.9438` n `211` status `ready` deltaP `31.8009` edge `0.9255` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1758` n `211` status `ready` deltaP `10.8725` edge `0.3989` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3756` n `211` status `ready` deltaP `1.5332` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5068` n `211` status `ready` deltaP `2.7819` edge `0.02` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6395` n `211` status `ready` deltaP `1.106` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7452` n `211` status `ready` deltaP `2.7527` edge `0.0049` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7649` n `211` status `ready` deltaP `0.1614` edge `0.0005` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.7851` n `211` status `ready` deltaP `2.7877` edge `0.1155` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.2168` n `211` status `ready` deltaP `4.8011` edge `-0.0157` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2878` n `211` status `ready` deltaP `4.7035` edge `0.1218` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.4995` n `211` status `ready` deltaP `2.0019` edge `0.0769` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.739` n `211` status `ready` deltaP `-1.5071` edge `0.0174` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8446` n `211` status `ready` deltaP `-0.4129` edge `-0.0378` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0291` n `211` status `ready` deltaP `-0.4384` edge `-0.0222` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9088` n `211` status `ready` deltaP `7.2596` edge `0.0798` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.243` n `211` status `ready` deltaP `-1.6928` edge `0.0578` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2968` n `211` status `ready` deltaP `-1.7882` edge `0.015` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.6266` n `211` status `ready` deltaP `-2.0879` edge `-0.0231` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.5882` n `211` status `ready` deltaP `-4.5193` edge `-0.1624` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.093` n `211` status `ready` deltaP `3.0035` edge `0.4072` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
