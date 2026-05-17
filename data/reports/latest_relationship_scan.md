# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T09:37:12.415603+00:00`
- Price records: `672`
- Market context records: `999`
- Flow alert records: `4784`
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

- `market_context_high->crypto_major_24h` score `12.9288` n `211` status `ready` deltaP `31.7485` edge `0.9246` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1684` n `211` status `ready` deltaP `10.8554` edge `0.3984` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3678` n `211` status `ready` deltaP `1.6829` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5224` n `211` status `ready` deltaP `2.6322` edge `0.0197` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6395` n `211` status `ready` deltaP `1.106` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.744` n `211` status `ready` deltaP `2.7527` edge `0.005` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7602` n `211` status `ready` deltaP `0.237` edge `0.0006` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.7626` n `211` status `ready` deltaP `2.9045` edge `0.1166` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.2168` n `211` status `ready` deltaP `4.8011` edge `-0.0157` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2713` n `211` status `ready` deltaP `4.6699` edge `0.1234` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5027` n `211` status `ready` deltaP `1.9623` edge `0.0769` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7423` n `211` status `ready` deltaP `-1.5478` edge `0.0174` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8531` n `211` status `ready` deltaP `-0.5626` edge `-0.0379` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0303` n `211` status `ready` deltaP `-0.4384` edge `-0.0223` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9181` n `211` status `ready` deltaP `7.1892` edge `0.0795` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2329` n `211` status `ready` deltaP `-1.6265` edge `0.0582` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3068` n `211` status `ready` deltaP `-1.8385` edge `0.0145` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.6217` n `211` status `ready` deltaP `-2.0081` edge `-0.023` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.5914` n `211` status `ready` deltaP `-4.5819` edge `-0.1624` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.1221` n `211` status `ready` deltaP `2.9388` edge `0.4039` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
