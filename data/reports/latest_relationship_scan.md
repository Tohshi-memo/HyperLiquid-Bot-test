# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T22:07:27.940474+00:00`
- Price records: `672`
- Market context records: `6129`
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

- `news_risk_high->crypto_alt_24h` score `10.3998` n `30` status `ready` deltaP `38.8194` edge `0.6226` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8229` n `30` status `ready` deltaP `69.2708` edge `0.1901` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3579` n `32` status `ready` deltaP `45.503` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3799` n `32` status `ready` deltaP `28.5928` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2838` n `32` status `ready` deltaP `13.8286` edge `0.1191` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.686` n `32` status `ready` deltaP `8.9259` edge `0.0746` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.5253` n `195` status `ready` deltaP `4.6646` edge `0.1044` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0878` n `30` status `ready` deltaP `8.7152` edge `0.0178` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2832` n `195` status `ready` deltaP `1.2851` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5491` n `30` status `ready` deltaP `14.0973` edge `-0.1192` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6996` n `195` status `ready` deltaP `2.9323` edge `0.0095` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.772` n `195` status `ready` deltaP `-0.2595` edge `0.0143` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7769` n `32` status `ready` deltaP `-2.994` edge `-0.0299` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7871` n `195` status `ready` deltaP `-2.4382` edge `-0.0047` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.8296` n `195` status `ready` deltaP `2.3906` edge `-0.0052` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8899` n `195` status `ready` deltaP `3.9099` edge `0.0351` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9141` n `195` status `ready` deltaP `4.6139` edge `0.0288` maxDD `-9.807`
- `news_risk_high->crypto_major_24h` score `-0.9333` n `30` status `ready` deltaP `9.1666` edge `-0.1028` maxDD `-4.2368`
- `market_context_high->index_4h` score `-1.0107` n `195` status `ready` deltaP `0.0219` edge `0.0167` maxDD `-1.381`
- `market_context_high->metal_24h` score `-1.0693` n `195` status `ready` deltaP `14.6474` edge `0.0221` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
