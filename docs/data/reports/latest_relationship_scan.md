# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T07:37:29.359962+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7486`

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

- `news_risk_high->unknown_24h` score `1010.2432` n `135` status `ready` deltaP `1.9097` edge `84.1742` maxDD `0.0`
- `market_context_high->unknown_1h` score `656.7704` n `36` status `ready` deltaP `9.7305` edge `54.666` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.1369` n `135` status `ready` deltaP `28.5532` edge `1.342` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `8.098` n `135` status `ready` deltaP `27.8588` edge `0.724` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.6641` n `135` status `ready` deltaP `23.9931` edge `0.7941` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.7955` n `135` status `ready` deltaP `34.0509` edge `0.1371` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.4349` n `135` status `ready` deltaP `26.2268` edge `0.2388` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.9266` n `135` status `ready` deltaP `29.476` edge `0.2075` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.8566` n `135` status `ready` deltaP `11.1122` edge `0.3466` maxDD `-15.9436`
- `market_context_high->crypto_major_1h` score `1.2213` n `36` status `ready` deltaP `6.8197` edge `0.1173` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `1.1741` n `36` status `ready` deltaP `7.8842` edge `0.1116` maxDD `-3.6387`
- `news_risk_high->crypto_alt_1h` score `1.1329` n `135` status `ready` deltaP `9.5509` edge `0.1218` maxDD `-4.2849`
- `market_context_high->fx_1h` score `1.0904` n `36` status `ready` deltaP `15.9015` edge `0.0071` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.9248` n `135` status `ready` deltaP `9.5509` edge `0.0757` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.8803` n `36` status `ready` deltaP `13.4398` edge `0.0658` maxDD `-2.4027`
- `market_context_high->metal_1h` score `0.744` n `36` status `ready` deltaP `8.9987` edge `0.0241` maxDD `-0.4338`
- `news_risk_high->index_1h` score `0.5053` n `135` status `ready` deltaP `8.9676` edge `0.0111` maxDD `-0.302`
- `market_context_high->index_1h` score `0.2608` n `36` status `ready` deltaP `6.0047` edge `0.0154` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.1442` n `135` status `ready` deltaP `6.7965` edge `0.028` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5467` n `135` status `ready` deltaP `2.19` edge `0.0681` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
