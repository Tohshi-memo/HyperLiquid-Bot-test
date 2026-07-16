# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T08:52:27.028673+00:00`
- Price records: `672`
- Market context records: `6902`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11722`

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

- `market_context_high->unknown_24h` score `0.4122` n `187` status `ready` deltaP `-4.152` edge `0.4734` maxDD `-13.7629`
- `market_context_high->fx_1h` score `-0.195` n `224` status `ready` deltaP `3.1357` edge `0.0026` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3599` n `224` status `ready` deltaP `3.2587` edge `0.0247` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4387` n `224` status `ready` deltaP `4.745` edge `0.0222` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6151` n `224` status `ready` deltaP `-0.8982` edge `-0.0044` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7744` n `224` status `ready` deltaP `-0.8795` edge `-0.0023` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7765` n `224` status `ready` deltaP `14.6124` edge `0.0094` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8433` n `224` status `ready` deltaP `-3.8441` edge `-0.0057` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3365` n `224` status `ready` deltaP `-1.8838` edge `-0.0098` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5941` n `224` status `ready` deltaP `-3.2613` edge `-0.021` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7559` n `224` status `ready` deltaP `2.0851` edge `-0.021` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9322` n `224` status `ready` deltaP `4.7039` edge `-0.0211` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.1388` n `187` status `ready` deltaP `0.8832` edge `0.0027` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.197` n `224` status `ready` deltaP `2.3192` edge `0.0012` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.792` n `224` status `ready` deltaP `1.9055` edge `-0.0123` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.876` n `224` status `ready` deltaP `-0.2396` edge `-0.0344` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0351` n `224` status `ready` deltaP `-8.2753` edge `0.0388` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2034` n `187` status `ready` deltaP `-6.038` edge `-0.0064` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1985` n `224` status `ready` deltaP `2.1015` edge `-0.1424` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3834` n `187` status `ready` deltaP `-13.6683` edge `-0.1251` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
