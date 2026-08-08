# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T02:52:32.296733+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `6.9318` n `81` status `ready` deltaP `4.2052` edge `0.8556` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.6565` n `81` status `ready` deltaP `11.4005` edge `0.2863` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.7839` n `103` status `ready` deltaP `17.1826` edge `0.1014` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.7186` n `81` status `ready` deltaP `33.6034` edge `0.0663` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.3329` n `81` status `ready` deltaP `8.7577` edge `0.204` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1794` n `103` status `ready` deltaP `13.6329` edge `0.0417` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3094` n `103` status `ready` deltaP `5.0957` edge `0.0231` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.5118` n `103` status `ready` deltaP `1.9054` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5139` n `103` status `ready` deltaP `-3.6335` edge `-0.0069` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6163` n `103` status `ready` deltaP `-3.5608` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6255` n `103` status `ready` deltaP `-1.2713` edge `-0.0112` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.9309` n `103` status `ready` deltaP `0.4129` edge `-0.005` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0248` n `103` status `ready` deltaP `-2.6107` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.7516` n `103` status `ready` deltaP `-8.9326` edge `-0.0235` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.8399` n `103` status `ready` deltaP `3.0458` edge `-0.0399` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.0642` n `81` status `ready` deltaP `10.5131` edge `-0.0853` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.2156` n `103` status `ready` deltaP `-5.7889` edge `-0.0464` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5871` n `81` status `ready` deltaP `-21.4313` edge `-0.1727` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7189` n `103` status `ready` deltaP `-7.6827` edge `-0.0935` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1997` n `103` status `ready` deltaP `-9.6806` edge `-0.1963` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
