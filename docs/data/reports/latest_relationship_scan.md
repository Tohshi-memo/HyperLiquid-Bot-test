# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T15:52:26.480213+00:00`
- Price records: `672`
- Market context records: `7044`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `0.0622` n `203` status `ready` deltaP `13.8855` edge `0.0104` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2131` n `203` status `ready` deltaP `2.4291` edge `0.0016` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.29` n `203` status `ready` deltaP `2.0479` edge `0.0356` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5495` n `203` status `ready` deltaP `4.2742` edge `0.0363` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.7305` n `203` status `ready` deltaP `-0.1261` edge `-0.0017` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.7358` n `203` status `ready` deltaP `-2.8347` edge `-0.0138` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-0.7769` n `203` status `ready` deltaP `-3.2123` edge `-0.0014` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.9796` n `203` status `ready` deltaP `-2.4778` edge `0.0113` maxDD `-2.4468`
- `market_context_high->unknown_4h` score `-1.6304` n `203` status `ready` deltaP `-6.2072` edge `0.0953` maxDD `-6.8495`
- `market_context_high->equity_1h` score `-1.7697` n `203` status `ready` deltaP `4.5441` edge `-0.0149` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.0582` n `203` status `ready` deltaP `4.221` edge `-0.0221` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0659` n `203` status `ready` deltaP `3.9837` edge `0.0069` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.1124` n `203` status `ready` deltaP `-4.0798` edge `-0.0328` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.2249` n `200` status `ready` deltaP `-0.2292` edge `-0.053` maxDD `-4.4704`
- `market_context_high->unknown_24h` score `-2.5273` n `200` status `ready` deltaP `-10.8819` edge `0.252` maxDD `-22.6109`
- `market_context_high->crypto_alt_4h` score `-2.5343` n `203` status `ready` deltaP `2.9902` edge `0.0337` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7616` n `203` status `ready` deltaP `4.574` edge `0.0439` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6254` n `200` status `ready` deltaP `-1.3056` edge `-0.0107` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.4014` n `203` status `ready` deltaP `4.4906` edge `-0.0918` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.7839` n `200` status `ready` deltaP `-15.7708` edge `-0.0745` maxDD `-43.8547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
