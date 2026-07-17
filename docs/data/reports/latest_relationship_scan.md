# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T08:37:28.502023+00:00`
- Price records: `672`
- Market context records: `7010`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11541`

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

- `market_context_high->unknown_24h` score `-0.2492` n `219` status `ready` deltaP `-5.4509` edge `0.4594` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.283` n `232` status `ready` deltaP `1.6828` edge `0.001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4736` n `232` status `ready` deltaP `2.0648` edge `0.0332` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6191` n `232` status `ready` deltaP `1.4918` edge `0.0018` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6553` n `232` status `ready` deltaP `-1.1899` edge `0.0007` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9293` n `232` status `ready` deltaP `4.1245` edge `0.0303` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9828` n `232` status `ready` deltaP `11.0965` edge `0.0064` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.1758` n `232` status `ready` deltaP `-1.7603` edge `-0.0141` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.334` n `232` status `ready` deltaP `-2.1242` edge `-0.0069` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6548` n `232` status `ready` deltaP `-4.0159` edge `-0.0364` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7514` n `232` status `ready` deltaP `8.2001` edge `-0.0093` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7657` n `232` status `ready` deltaP `4.491` edge `-0.0009` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8684` n `232` status `ready` deltaP `7.1068` edge `0.0114` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5114` n `232` status `ready` deltaP `-5.9293` edge `0.0668` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6737` n `232` status `ready` deltaP `2.0342` edge `0.0222` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.3428` n `219` status `ready` deltaP `-5.1132` edge `-0.0886` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3105` n `219` status `ready` deltaP `-6.4284` edge `-0.0163` maxDD `-5.3378`
- `market_context_high->crypto_major_4h` score `-4.808` n `232` status `ready` deltaP `2.008` edge `0.0144` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.2415` n `232` status `ready` deltaP `5.4931` edge `-0.0517` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3465` n `219` status `ready` deltaP `-8.9517` edge `-0.0556` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
