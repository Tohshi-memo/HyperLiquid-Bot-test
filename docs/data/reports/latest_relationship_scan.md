# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T12:37:29.542485+00:00`
- Price records: `672`
- Market context records: `5879`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7752` n `30` status `ready` deltaP `39.3902` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5787` n `231` status `ready` deltaP `9.252` edge `0.1799` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9579` n `30` status `ready` deltaP `11.8363` edge `0.0906` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3198` n `30` status `ready` deltaP `5.6188` edge `0.0497` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.3595` n `237` status `ready` deltaP `4.69` edge `0.0333` maxDD `-4.5619`
- `news_risk_high->metal_1h` score `-0.4087` n `30` status `ready` deltaP `1.8363` edge `-0.028` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.4521` n `237` status `ready` deltaP `-1.2456` edge `-0.0008` maxDD `-0.5751`
- `market_context_high->commodity_1h` score `-0.4961` n `237` status `ready` deltaP `-0.7965` edge `-0.0012` maxDD `-1.9006`
- `market_context_high->metal_1h` score `-0.5344` n `237` status `ready` deltaP `2.9334` edge `0.003` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.5837` n `237` status `ready` deltaP `0.8919` edge `0.004` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.5876` n `237` status `ready` deltaP `3.3553` edge `0.0344` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9747` n `237` status `ready` deltaP `2.5386` edge `0.0353` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1754` n `231` status `ready` deltaP `0.4112` edge `0.0153` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2494` n `30` status `ready` deltaP `-12.6946` edge `-0.0241` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.822` n `30` status `ready` deltaP `-13.8821` edge `-0.0535` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.982` n `231` status `ready` deltaP `10.1059` edge `0.2047` maxDD `-25.6458`
- `market_context_high->fx_4h` score `-1.9904` n `231` status `ready` deltaP `-8.1856` edge `-0.0057` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.2785` n `231` status `ready` deltaP `-0.722` edge `-0.0137` maxDD `-6.3754`
- `news_risk_high->index_4h` score `-2.3221` n `30` status `ready` deltaP `-17.1646` edge `-0.0799` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
