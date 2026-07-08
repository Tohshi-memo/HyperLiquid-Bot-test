# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T18:37:26.303798+00:00`
- Price records: `672`
- Market context records: `6113`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `9.0209` n `30` status `ready` deltaP `36.3889` edge `0.5239` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.9803` n `30` status `ready` deltaP `70.8333` edge `0.1928` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1861` n `32` status `ready` deltaP `43.5213` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3164` n `32` status `ready` deltaP `27.8443` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2651` n `32` status `ready` deltaP `13.6789` edge `0.1177` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.9719` n `195` status `ready` deltaP `6.6463` edge `0.1284` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6494` n `32` status `ready` deltaP `8.9259` edge `0.0699` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.029` n `30` status `ready` deltaP `9.2361` edge `0.0293` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3245` n `195` status `ready` deltaP `0.5366` edge `-0.0006` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4356` n `30` status `ready` deltaP `14.2709` edge `-0.1109` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6375` n `195` status `ready` deltaP `3.5421` edge `0.0134` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6685` n `195` status `ready` deltaP `-1.2406` edge `-0.0028` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.6965` n `195` status `ready` deltaP `0.489` edge `0.019` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7621` n `32` status `ready` deltaP `-2.8443` edge `-0.029` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8068` n `195` status `ready` deltaP `2.5403` edge `-0.0043` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.8972` n `195` status `ready` deltaP `1.5463` edge `0.0211` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.9265` n `195` status `ready` deltaP `3.9099` edge `0.0304` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9328` n `195` status `ready` deltaP `4.4642` edge `0.0274` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.1256` n `32` status `ready` deltaP `-10.1235` edge `-0.0205` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2587` n `195` status `ready` deltaP `-3.0562` edge `0.0024` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
