# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T08:52:18.529930+00:00`
- Price records: `672`
- Market context records: `996`
- Flow alert records: `4775`
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

- `market_context_high->crypto_major_24h` score `12.8828` n `211` status `ready` deltaP `31.5925` edge `0.9218` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1451` n `211` status `ready` deltaP `10.8043` edge `0.3968` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3444` n `211` status `ready` deltaP `2.132` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5248` n `211` status `ready` deltaP `2.6322` edge `0.0195` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6263` n `211` status `ready` deltaP `1.2557` edge `0.0163` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7096` n `211` status `ready` deltaP `3.1023` edge `0.1197` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.744` n `211` status `ready` deltaP `2.7527` edge `0.005` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7563` n `211` status `ready` deltaP `0.3122` edge `0.0006` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.2253` n `211` status `ready` deltaP `4.5698` edge `0.1279` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2269` n `211` status `ready` deltaP `4.6514` edge `-0.016` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.5097` n `211` status `ready` deltaP `1.8444` edge `0.0771` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7484` n `211` status `ready` deltaP `-1.6691` edge `0.0177` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8811` n `211` status `ready` deltaP `-1.0117` edge `-0.0385` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0651` n `211` status `ready` deltaP `-0.7378` edge `-0.0232` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9481` n `211` status `ready` deltaP `6.9793` edge `0.0784` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.2687` n `211` status `ready` deltaP `-1.8801` edge `0.0569` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.338` n `211` status `ready` deltaP `-1.9884` edge `0.0129` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.6054` n `211` status `ready` deltaP `-1.7703` edge `-0.0225` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6011` n `211` status `ready` deltaP `-4.7686` edge `-0.1624` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.2077` n `211` status `ready` deltaP `2.746` edge `0.3942` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
