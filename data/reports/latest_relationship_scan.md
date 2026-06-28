# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T16:37:28.242581+00:00`
- Price records: `672`
- Market context records: `5058`
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

- `market_context_high->unknown_1h` score `12.4413` n `99` status `ready` deltaP `3.6095` edge `1.0628` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9531` n `99` status `ready` deltaP `21.2414` edge `0.7067` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.6408` n `99` status `ready` deltaP `17.2949` edge `0.4908` maxDD `-7.5491`
- `market_context_high->crypto_major_4h` score `5.1677` n `99` status `ready` deltaP `15.7321` edge `0.4842` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `0.8738` n `99` status `ready` deltaP `7.3157` edge `0.1128` maxDD `-4.4335`
- `market_context_high->metal_4h` score `0.8509` n `99` status `ready` deltaP `9.4805` edge `0.1156` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.5486` n `99` status `ready` deltaP `5.2122` edge `0.1654` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.4985` n `99` status `ready` deltaP `7.6136` edge `0.0705` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.4406` n `99` status `ready` deltaP `7.4654` edge `0.0366` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2099` n `99` status `ready` deltaP `5.3318` edge `0.0919` maxDD `-5.3758`
- `market_context_high->fx_24h` score `-0.0282` n `75` status `ready` deltaP `9.5972` edge `0.0086` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0707` n `99` status `ready` deltaP `4.7734` edge `0.0384` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3274` n `99` status `ready` deltaP `1.441` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.3986` n `99` status `ready` deltaP `0.9542` edge `0.0123` maxDD `-0.5808`
- `market_context_high->commodity_4h` score `-0.8149` n `99` status `ready` deltaP `7.4787` edge `0.0075` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9971` n `99` status `ready` deltaP `-4.0497` edge `-0.0019` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4668` n `99` status `ready` deltaP `-8.5103` edge `-0.0045` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.5881` n `75` status `ready` deltaP `6.0417` edge `0.0452` maxDD `-32.9721`
- `market_context_high->unknown_24h` score `-4.1766` n `75` status `ready` deltaP `27.1805` edge `-0.495` maxDD `-1.4072`
- `market_context_high->commodity_24h` score `-4.4017` n `75` status `ready` deltaP `0.4723` edge `-0.0851` maxDD `-25.9231`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
