# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T13:46:36.459941+00:00`
- Price records: `672`
- Market context records: `6288`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.213` n `32` status `ready` deltaP `43.2292` edge `0.9943` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9617` n `32` status `ready` deltaP `50.5208` edge `0.16` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1865` n `32` status `ready` deltaP `43.8262` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1196` n `32` status `ready` deltaP `16.6667` edge `0.495` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.8145` n `32` status `ready` deltaP `26.5625` edge `0.078` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3979` n `32` status `ready` deltaP `28.8922` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.407` n `32` status `ready` deltaP `14.2777` edge `0.1319` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3542` n `206` status `ready` deltaP `-0.4258` edge `0.2165` maxDD `-3.7317`
- `news_risk_high->crypto_alt_1h` score `0.8776` n `32` status `ready` deltaP `11.4708` edge `0.0822` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3749` n `194` status `ready` deltaP `7.2243` edge `0.0748` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.2914` n `194` status `ready` deltaP `-3.4479` edge `0.3005` maxDD `-11.925`
- `market_context_high->metal_4h` score `-0.2173` n `194` status `ready` deltaP `6.767` edge `0.0331` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.2195` n `180` status `ready` deltaP `19.4097` edge `0.0993` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.3081` n `32` status `ready` deltaP `7.1181` edge `0.0002` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4461` n `206` status `ready` deltaP `3.1306` edge `-0.0003` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5825` n `206` status `ready` deltaP `0.0727` edge `0.0016` maxDD `-1.0499`
- `market_context_high->fx_1h` score `-0.6403` n `206` status `ready` deltaP `-0.9622` edge `-0.0016` maxDD `-0.6273`
- `news_risk_high->metal_1h` score `-0.7138` n `32` status `ready` deltaP `-2.6946` edge `-0.0238` maxDD `-1.6464`
- `market_context_high->commodity_4h` score `-0.8116` n `194` status `ready` deltaP `-3.2232` edge `0.0075` maxDD `-1.2054`
- `market_context_high->crypto_alt_1h` score `-0.8723` n `206` status `ready` deltaP `5.4939` edge `0.0268` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
