# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T13:07:30.714338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4834`

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

- `market_context_high->unknown_1h` score `366.6105` n `50` status `ready` deltaP `11.1737` edge `30.4813` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.499` n `50` status `ready` deltaP `12.0427` edge `24.4613` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.8767` n `50` status `ready` deltaP `28.9393` edge `1.1338` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.3523` n `50` status `ready` deltaP `36.5927` edge `0.8437` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `11.1541` n `62` status `ready` deltaP `39.3195` edge `0.6877` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.375` n `62` status `ready` deltaP `28.2244` edge `0.7249` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.7263` n `62` status `ready` deltaP `27.3555` edge `0.5959` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4955` n `50` status `ready` deltaP `18.6098` edge `0.5709` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3941` n `50` status `ready` deltaP `18.3232` edge `0.5396` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5366` n `62` status `ready` deltaP `32.9429` edge `0.1743` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0216` n `62` status `ready` deltaP `27.0752` edge `0.2159` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3033` n `50` status `ready` deltaP `14.9521` edge `0.2419` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.2189` n `64` status `ready` deltaP `14.7268` edge `0.2056` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.1239` n `62` status `ready` deltaP `33.6792` edge `0.062` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0602` n `50` status `ready` deltaP `34.3659` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9414` n `50` status `ready` deltaP `13.1018` edge `0.2028` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3659` n `62` status `ready` deltaP `19.0253` edge `0.1119` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9455` n `64` status `ready` deltaP `23.8679` edge `0.018` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5705` n `50` status `ready` deltaP `21.8383` edge `0.0117` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.5106` n `64` status `ready` deltaP `5.2021` edge `0.1431` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
