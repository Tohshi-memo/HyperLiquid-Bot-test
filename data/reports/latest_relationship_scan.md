# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T14:07:27.869237+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.1794` n `125` status `ready` deltaP `10.5521` edge `0.0042` maxDD `-0.7906`
- `market_context_high->fx_4h` score `0.1643` n `113` status `ready` deltaP `9.1989` edge `0.01` maxDD `-0.3539`
- `market_context_high->equity_1h` score `0.1438` n `125` status `ready` deltaP `7.4599` edge `0.045` maxDD `-3.2868`
- `market_context_high->fx_1h` score `-0.1019` n `125` status `ready` deltaP `2.7485` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.2392` n `113` status `ready` deltaP `2.953` edge `0.113` maxDD `-8.4019`
- `market_context_high->unknown_1h` score `-0.3574` n `125` status `ready` deltaP `10.2204` edge `-0.0752` maxDD `-0.4843`
- `market_context_high->metal_4h` score `-0.3761` n `113` status `ready` deltaP `4.6298` edge `-0.0215` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.3764` n `113` status `ready` deltaP `4.6555` edge `0.014` maxDD `-1.7963`
- `market_context_high->metal_1h` score `-0.4521` n `125` status `ready` deltaP `0.9521` edge `-0.0044` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.4655` n `105` status `ready` deltaP `4.4147` edge `0.1151` maxDD `-4.666`
- `market_context_high->commodity_1h` score `-0.6712` n `125` status `ready` deltaP `-4.4934` edge `0.0005` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.6751` n `113` status `ready` deltaP `-1.743` edge `0.0101` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.9264` n `125` status `ready` deltaP `-0.3808` edge `0.0055` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.3526` n `125` status `ready` deltaP `-2.6874` edge `-0.053` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.494` n `113` status `ready` deltaP `0.4587` edge `-0.0839` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.9765` n `105` status `ready` deltaP `-12.128` edge `-0.0062` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1979` n `105` status `ready` deltaP `-5.7689` edge `-0.0495` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.3941` n `113` status `ready` deltaP `-1.4974` edge `-0.2541` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.5043` n `105` status `ready` deltaP `-16.7212` edge `-0.1352` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.2291` n `105` status `ready` deltaP `7.9465` edge `-0.4381` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
