# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T01:37:27.951964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9964`

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

- `market_context_high->unknown_4h` score `43.7194` n `49` status `ready` deltaP `7.3171` edge `3.5945` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `28.7006` n `49` status `ready` deltaP `18.789` edge `2.4517` maxDD `-13.153`
- `market_context_high->equity_24h` score `14.1601` n `49` status `ready` deltaP `12.0181` edge `1.1815` maxDD `-4.8626`
- `market_context_high->crypto_alt_24h` score `13.3531` n `49` status `ready` deltaP `17.3151` edge `1.1737` maxDD `-13.1098`
- `news_risk_high->crypto_major_24h` score `10.1632` n `101` status `ready` deltaP `-0.7099` edge `1.5375` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `5.6932` n `101` status `ready` deltaP `-0.3249` edge `0.9647` maxDD `-32.7147`
- `market_context_high->index_24h` score `4.7694` n `49` status `ready` deltaP `16.0112` edge `0.3181` maxDD `-0.5249`
- `news_risk_high->crypto_alt_4h` score `2.9328` n `101` status `ready` deltaP `14.3458` edge `0.2697` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.5953` n `101` status `ready` deltaP `31.8774` edge `0.2508` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3373` n `101` status `ready` deltaP `14.2853` edge `0.1461` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.126` n `101` status `ready` deltaP `16.3276` edge `0.1941` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6899` n `101` status `ready` deltaP `16.2314` edge `0.0849` maxDD `-2.8494`
- `market_context_high->index_4h` score `0.8516` n `49` status `ready` deltaP `18.4887` edge `0.0154` maxDD `-0.3583`
- `market_context_high->equity_1h` score `0.7163` n `49` status `ready` deltaP `5.5756` edge `0.0473` maxDD `-0.3155`
- `market_context_high->index_1h` score `0.6028` n `49` status `ready` deltaP `9.7122` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->fx_4h` score `0.5932` n `101` status `ready` deltaP `12.6041` edge `0.029` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4987` n `101` status `ready` deltaP `13.4004` edge `0.0124` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.1845` n `101` status `ready` deltaP `13.2878` edge `0.0322` maxDD `-2.0994`
- `market_context_high->equity_4h` score `0.1051` n `49` status `ready` deltaP `4.567` edge `0.0313` maxDD `-1.8613`
- `market_context_high->crypto_alt_4h` score `0.0852` n `49` status `ready` deltaP `5.5158` edge `0.0436` maxDD `-3.8616`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
