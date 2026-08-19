# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T14:52:26.418289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11738`

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

- `market_context_high->equity_4h` score `2.2523` n `96` status `ready` deltaP `11.9156` edge `0.1971` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8968` n `96` status `ready` deltaP `15.3007` edge `0.0862` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.5223` n `96` status `ready` deltaP `4.6875` edge `0.2164` maxDD `-4.9964`
- `market_context_high->metal_4h` score `0.9739` n `96` status `ready` deltaP `16.565` edge `0.0283` maxDD `-1.273`
- `market_context_high->index_1h` score `0.963` n `96` status `ready` deltaP `16.2113` edge `0.0109` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.5859` n `96` status `ready` deltaP `9.2014` edge `0.1971` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.5466` n `96` status `ready` deltaP `9.1717` edge `0.0865` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.3588` n `96` status `ready` deltaP `18.2291` edge `-0.041` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.1341` n `96` status `ready` deltaP `9.1717` edge `0.0063` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1336` n `96` status `ready` deltaP `8.1046` edge `0.0226` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.1257` n `96` status `ready` deltaP `7.5599` edge `-0.0172` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.0349` n `96` status `ready` deltaP `5.0711` edge `0.0078` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.2919` n `96` status `ready` deltaP `7.1646` edge `0.0549` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4812` n `96` status `ready` deltaP `2.3827` edge `0.0069` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.532` n `96` status `ready` deltaP `1.0292` edge `0.0051` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6033` n `96` status `ready` deltaP `0.4319` edge `0.0048` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8721` n `96` status `ready` deltaP `-7.2917` edge `-0.0066` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.3919` n `96` status `ready` deltaP `-5.0347` edge `0.0577` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.7699` n `96` status `ready` deltaP `-21.0069` edge `-0.0158` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
