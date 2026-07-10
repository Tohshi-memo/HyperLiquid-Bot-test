# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T00:22:28.659211+00:00`
- Price records: `672`
- Market context records: `6231`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.6874` n `32` status `ready` deltaP `42.2194` edge `0.8739` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3113` n `32` status `ready` deltaP `54.0816` edge `0.1654` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1573` n `32` status `ready` deltaP `43.5213` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.8705` n `32` status `ready` deltaP `15.625` edge `0.3418` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.32` n `32` status `ready` deltaP `27.994` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2386` n `192` status `ready` deltaP `2.8599` edge `0.2683` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.6863` n `32` status `ready` deltaP `22.8104` edge `0.009` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.4586` n `192` status `ready` deltaP `-0.3176` edge `0.3769` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3937` n `32` status `ready` deltaP `14.4274` edge `0.1292` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7943` n `32` status `ready` deltaP `10.5726` edge `0.0775` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0533` n `192` status `ready` deltaP `19.8023` edge `0.118` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1949` n `32` status `ready` deltaP `8.801` edge `0.0035` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3089` n `192` status `ready` deltaP `0.9107` edge `-0.0011` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.582` n `192` status `ready` deltaP `4.1286` edge `0.0166` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.5943` n `192` status `ready` deltaP `-1.0479` edge `0.0021` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8041` n `32` status `ready` deltaP `-3.8922` edge `-0.0274` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8694` n `192` status `ready` deltaP `4.8434` edge `0.0315` maxDD `-9.3536`
- `market_context_high->equity_4h` score `-0.8868` n `192` status `ready` deltaP `2.0579` edge `0.0041` maxDD `-2.671`
- `market_context_high->metal_1h` score `-0.8964` n `192` status `ready` deltaP `1.3161` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9059` n `192` status `ready` deltaP `4.5316` edge `0.0304` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
