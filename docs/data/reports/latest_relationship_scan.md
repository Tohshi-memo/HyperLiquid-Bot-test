# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T13:52:32.022868+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4750`

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

- `market_context_high->unknown_1h` score `366.7413` n `50` status `ready` deltaP `11.1737` edge `30.4922` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `295.3356` n `50` status `ready` deltaP `12.1951` edge `24.53` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.1007` n `50` status `ready` deltaP `29.4593` edge `1.149` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.5859` n `50` status `ready` deltaP `37.1127` edge `0.8597` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.1395` n `62` status `ready` deltaP `39.167` edge `0.6875` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.461` n `62` status `ready` deltaP `28.7444` edge `0.7286` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7431` n `62` status `ready` deltaP `27.3555` edge `0.5973` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4809` n `50` status `ready` deltaP `18.4573` edge `0.5707` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.4109` n `50` status `ready` deltaP `18.3232` edge `0.541` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5842` n `62` status `ready` deltaP `33.4629` edge `0.1748` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0252` n `62` status `ready` deltaP `27.0752` edge `0.2162` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3033` n `50` status `ready` deltaP `14.9521` edge `0.2419` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1617` n `62` status `ready` deltaP `34.1365` edge `0.0621` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.1302` n `67` status `ready` deltaP `14.7734` edge `0.1979` maxDD `-1.5096`
- `market_context_high->fx_4h` score `3.0602` n `50` status `ready` deltaP `34.3659` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9438` n `50` status `ready` deltaP `13.1018` edge `0.203` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3915` n `62` status `ready` deltaP `19.3302` edge `0.112` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0234` n `67` status `ready` deltaP `24.9173` edge `0.0175` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5983` n `67` status `ready` deltaP `5.6685` edge `0.1473` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5957` n `50` status `ready` deltaP `22.1377` edge `0.0118` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
