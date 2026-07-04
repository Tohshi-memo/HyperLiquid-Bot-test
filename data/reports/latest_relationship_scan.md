# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T15:19:38.519171+00:00`
- Price records: `672`
- Market context records: `5675`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `2.0328` n `199` status `ready` deltaP `16.2296` edge `0.5691` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9549` n `249` status `ready` deltaP `11.7213` edge `0.2242` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4962` n `249` status `ready` deltaP `8.7839` edge `0.1638` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.2454` n `249` status `ready` deltaP `5.9727` edge `0.1445` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2474` n `261` status `ready` deltaP `2.191` edge `0.0013` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4625` n `261` status `ready` deltaP `2.6275` edge `0.0401` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.4732` n `261` status `ready` deltaP `4.6144` edge `0.0305` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5738` n `261` status `ready` deltaP `1.2269` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6405` n `261` status `ready` deltaP `4.2564` edge `0.0428` maxDD `-6.9639`
- `market_context_high->fx_24h` score `-0.7379` n `199` status `ready` deltaP `15.263` edge `0.049` maxDD `-2.9798`
- `market_context_high->metal_1h` score `-0.7624` n `261` status `ready` deltaP `0.6585` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.9029` n `261` status `ready` deltaP `0.7066` edge `-0.0034` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1915` n `249` status `ready` deltaP `3.5661` edge `0.0069` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2635` n `249` status `ready` deltaP `-0.453` edge `0.0082` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5092` n `199` status `ready` deltaP `6.2352` edge `0.0364` maxDD `-16.9731`
- `market_context_high->metal_4h` score `-2.9038` n `249` status `ready` deltaP `-12.167` edge `-0.0536` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7399` n `249` status `ready` deltaP `-1.8158` edge `-0.032` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6747` n `199` status `ready` deltaP `4.1597` edge `0.0284` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3485` n `199` status `ready` deltaP `-12.924` edge `-0.2496` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.2617` n `199` status `ready` deltaP `-11.5072` edge `-0.0842` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
