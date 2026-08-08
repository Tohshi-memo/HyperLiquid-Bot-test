# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T07:52:24.820521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.114` n `81` status `ready` deltaP `1.9483` edge `0.8025` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5941` n `81` status `ready` deltaP `11.4005` edge `0.2811` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7225` n `81` status `ready` deltaP `33.6034` edge `0.0668` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.5833` n `103` status `ready` deltaP `15.2009` edge `0.0979` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1352` n `81` status `ready` deltaP `7.0216` edge `0.1991` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.0836` n `103` status `ready` deltaP `12.585` edge `0.0407` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2663` n `103` status `ready` deltaP `5.5448` edge `0.0237` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4711` n `103` status `ready` deltaP `-2.885` edge `-0.0064` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5118` n `103` status `ready` deltaP `1.9054` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5368` n `103` status `ready` deltaP `0.253` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6327` n `103` status `ready` deltaP `-3.8602` edge `-0.0058` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9175` n `103` status `ready` deltaP `0.5653` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0652` n `103` status `ready` deltaP `-3.3729` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.6879` n `103` status `ready` deltaP `4.5702` edge `-0.0374` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.7456` n `103` status `ready` deltaP `-9.0823` edge `-0.022` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.242` n `103` status `ready` deltaP `-5.9386` edge `-0.0476` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6316` n `81` status `ready` deltaP `7.0409` edge `-0.1349` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6951` n `103` status `ready` deltaP `-7.8351` edge `-0.0905` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7916` n `81` status `ready` deltaP `-22.9938` edge `-0.1885` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.3152` n `103` status `ready` deltaP `-9.9855` edge `-0.2039` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
