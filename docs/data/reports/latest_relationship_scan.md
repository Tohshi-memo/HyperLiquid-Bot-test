# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T06:22:29.884236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6722`

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

- `market_context_high->unknown_1h` score `324.6964` n `50` status `ready` deltaP `6.982` edge `27.0164` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0536` n `50` status `ready` deltaP `6.8598` edge `23.3754` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3082` n `127` status `ready` deltaP `29.1544` edge `1.4356` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `7.454` n `34` status `ready` deltaP `27.3285` edge `0.5806` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.7101` n `50` status `ready` deltaP `18.1524` edge `0.5085` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.403` n `127` status `ready` deltaP `22.7198` edge `0.6975` maxDD `-15.8971`
- `news_risk_high->equity_24h` score `5.9857` n `127` status `ready` deltaP `23.4142` edge `0.5776` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `3.9997` n `127` status `ready` deltaP `26.8593` edge `0.2035` maxDD `-1.2737`
- `market_context_high->crypto_alt_4h` score `3.5821` n `50` status `ready` deltaP `13.4451` edge `0.3382` maxDD `-7.6792`
- `market_context_high->crypto_alt_24h` score `3.1962` n `34` status `ready` deltaP `10.141` edge `0.3697` maxDD `-11.6768`
- `market_context_high->crypto_major_1h` score `2.9111` n `50` status `ready` deltaP `14.5988` edge `0.1903` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8949` n `50` status `ready` deltaP `32.689` edge `0.0368` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.613` n `127` status `ready` deltaP `24.8647` edge `0.0998` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.5967` n `50` status `ready` deltaP `12.5569` edge `0.199` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `2.3754` n `127` status `ready` deltaP `11.1616` edge `0.3242` maxDD `-10.7193`
- `news_risk_high->metal_24h` score `2.0547` n `127` status `ready` deltaP `24.1839` edge `0.2296` maxDD `-2.192`
- `market_context_high->equity_24h` score `1.6712` n `34` status `ready` deltaP `4.4935` edge `0.3705` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.4436` n `50` status `ready` deltaP `20.3413` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.842` n `127` status `ready` deltaP `8.0131` edge `0.0704` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.6876` n `127` status `ready` deltaP `7.9742` edge `0.0952` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
