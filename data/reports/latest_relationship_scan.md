# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T22:07:25.744202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9826`

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

- `market_context_high->unknown_1h` score `72.1831` n `47` status `ready` deltaP `10.116` edge `5.9549` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `34.2316` n `46` status `ready` deltaP `20.8258` edge `2.7294` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.781` n `46` status `ready` deltaP `18.2216` edge `1.537` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `17.6115` n `46` status `ready` deltaP `15.7986` edge `1.3623` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.5755` n `97` status `ready` deltaP `-2.6615` edge `1.4182` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.6667` n `46` status `ready` deltaP `27.2494` edge `0.3826` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.6394` n `103` status `ready` deltaP `13.6219` edge `0.3956` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5382` n `103` status `ready` deltaP `17.4328` edge `0.3197` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.7208` n `97` status `ready` deltaP `-4.82` edge `0.8303` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.6713` n `97` status `ready` deltaP `25.6049` edge `0.1698` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.4346` n `103` status `ready` deltaP `13.008` edge `0.1652` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4114` n `47` status `ready` deltaP `28.5385` edge `0.0261` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9437` n `103` status `ready` deltaP `15.4032` edge `0.1028` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4954` n `103` status `ready` deltaP `22.157` edge `0.0405` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.4174` n `46` status `ready` deltaP `21.2259` edge `0.0` maxDD `-0.2042`
- `market_context_high->equity_4h` score `1.2121` n `47` status `ready` deltaP `9.8274` edge `0.0773` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.0996` n `97` status `ready` deltaP `27.4485` edge `0.1211` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7235` n `47` status `ready` deltaP `12.0652` edge `0.0077` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.5833` n `97` status `ready` deltaP `17.3038` edge `0.0512` maxDD `-3.0086`
- `news_risk_high->metal_1h` score `0.5679` n `103` status `ready` deltaP `14.6038` edge `0.0093` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
