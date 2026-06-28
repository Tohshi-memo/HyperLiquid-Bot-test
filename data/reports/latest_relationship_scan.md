# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T00:37:32.921532+00:00`
- Price records: `672`
- Market context records: `4989`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `21.3019` n `90` status `ready` deltaP `4.358` edge `1.7962` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1872` n `87` status `ready` deltaP `18.0964` edge `0.5435` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `5.9124` n `74` status `ready` deltaP `28.5989` edge `0.3363` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.171` n `87` status `ready` deltaP `12.7366` edge `0.4854` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5039` n `87` status `ready` deltaP `20.737` edge `0.0893` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1097` n `87` status `ready` deltaP `11.0352` edge `0.1268` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.93` n `90` status `ready` deltaP `6.8629` edge `0.1235` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.9168` n `90` status `ready` deltaP `8.2269` edge `0.0789` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.6008` n `87` status `ready` deltaP `4.8553` edge `0.1828` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.384` n `90` status `ready` deltaP `6.4138` edge `0.0389` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.3588` n `87` status `ready` deltaP `5.3003` edge `0.0428` maxDD `-0.8587`
- `market_context_high->crypto_alt_1h` score `0.1518` n `90` status `ready` deltaP `4.5309` edge `0.0915` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2585` n `74` status `ready` deltaP `5.7386` edge `0.0048` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4152` n `90` status `ready` deltaP `0.4724` edge `0.0096` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4785` n `90` status `ready` deltaP `3.0339` edge `0.014` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8271` n `87` status `ready` deltaP `-1.1845` edge `-0.0011` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.269` n `87` status `ready` deltaP `3.5867` edge `-0.0044` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.6839` n `90` status `ready` deltaP `-11.151` edge `-0.0054` maxDD `-0.5135`
- `market_context_high->commodity_24h` score `-3.9402` n `74` status `ready` deltaP `7.8782` edge `-0.0468` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.3048` n `74` status `ready` deltaP `-1.5625` edge `0.004` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
