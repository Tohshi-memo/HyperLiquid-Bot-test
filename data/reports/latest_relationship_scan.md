# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T15:22:29.304662+00:00`
- Price records: `672`
- Market context records: `5053`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10292`

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

- `market_context_high->unknown_1h` score `11.6057` n `101` status `ready` deltaP `3.3497` edge `0.9949` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.5696` n `98` status `ready` deltaP `20.5731` edge `0.6792` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4225` n `98` status `ready` deltaP `17.7918` edge `0.4917` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3915` n `98` status `ready` deltaP `15.4928` edge `0.4854` maxDD `-7.8181`
- `market_context_high->metal_4h` score `0.9066` n `98` status `ready` deltaP `10.0267` edge `0.1166` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7511` n `101` status `ready` deltaP `6.9662` edge `0.1079` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.7074` n `101` status `ready` deltaP `7.1841` edge `0.0684` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.3845` n `98` status `ready` deltaP `3.307` edge `0.1654` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.337` n `101` status `ready` deltaP `6.2755` edge `0.0359` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1532` n `101` status `ready` deltaP `5.112` edge `0.0878` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.1059` n `77` status `ready` deltaP `8.1778` edge `0.0081` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1367` n `98` status `ready` deltaP `3.9634` edge `0.0383` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3237` n `101` status `ready` deltaP `1.4511` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4602` n `101` status `ready` deltaP `0.495` edge `0.0118` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.5507` n `98` status `ready` deltaP `6.9531` edge `0.0083` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0264` n `98` status `ready` deltaP `-4.4332` edge `-0.0031` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4959` n `101` status `ready` deltaP `-8.8412` edge `-0.0047` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-2.6797` n `77` status `ready` deltaP `27.4576` edge `-0.3721` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.4769` n `77` status `ready` deltaP `6.5588` edge `0.056` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6655` n `77` status `ready` deltaP `0.3359` edge `-0.0895` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
