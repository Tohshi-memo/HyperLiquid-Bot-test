# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T12:52:28.553637+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `358.3197` n `50` status `ready` deltaP `11.024` edge `29.7914` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `291.9127` n `50` status `ready` deltaP `10.8232` edge `24.2539` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5046` n `73` status `ready` deltaP `39.795` edge `1.0477` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `9.9438` n `73` status `ready` deltaP `34.4891` edge `0.6472` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.7582` n `50` status `ready` deltaP `33.7361` edge `0.7299` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0009` n `50` status `ready` deltaP `16.5347` edge `0.8108` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.6356` n `50` status `ready` deltaP `16.1707` edge `0.5155` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6677` n `50` status `ready` deltaP `14.0549` edge `0.4246` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3017` n `111` status `ready` deltaP `18.8297` edge `0.3673` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9431` n `50` status `ready` deltaP `32.8415` edge `0.0398` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.9313` n `50` status `ready` deltaP `13.9042` edge `0.2179` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8776` n `50` status `ready` deltaP `13.8503` edge `0.1925` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.29` n `50` status `ready` deltaP `10.7083` edge `0.4084` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.2739` n `111` status `ready` deltaP `22.0034` edge `0.1124` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.0076` n `73` status `ready` deltaP `7.9005` edge `0.5201` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4891` n `50` status `ready` deltaP `20.7904` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2401` n `73` status `ready` deltaP `11.9673` edge `0.2066` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.8786` n `111` status `ready` deltaP `12.1347` edge `0.2627` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8612` n `50` status `ready` deltaP `14.4444` edge `0.0712` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7723` n `116` status `ready` deltaP `4.8008` edge `0.0886` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
