# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T12:22:37.231284+00:00`
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

- `market_context_high->unknown_1h` score `342.5122` n `50` status `ready` deltaP `11.024` edge `28.4741` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `291.5371` n `50` status `ready` deltaP `10.8232` edge `24.2226` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5466` n `73` status `ready` deltaP `39.795` edge `1.0512` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.0712` n `73` status `ready` deltaP `34.8364` edge `0.6555` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.9312` n `50` status `ready` deltaP `34.0833` edge `0.742` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0429` n `50` status `ready` deltaP `16.5347` edge `0.8143` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.6995` n `50` status `ready` deltaP `16.4756` edge `0.5188` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7089` n `50` status `ready` deltaP `14.3598` edge `0.426` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3413` n `110` status `ready` deltaP `18.9053` edge `0.3701` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9913` n `50` status `ready` deltaP `14.2036` edge `0.2209` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9443` n `50` status `ready` deltaP `32.8415` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9376` n `50` status `ready` deltaP `14.1497` edge `0.1955` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.3728` n `50` status `ready` deltaP `11.0556` edge `0.4167` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.2884` n `110` status `ready` deltaP `22.0953` edge `0.113` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.1201` n `73` status `ready` deltaP `8.2477` edge `0.5322` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.5035` n `50` status `ready` deltaP `20.9401` edge `0.0121` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2538` n `73` status `ready` deltaP `12.1409` edge `0.2072` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9016` n `110` status `ready` deltaP `12.112` edge `0.2658` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8705` n `50` status `ready` deltaP `14.4444` edge `0.0724` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8322` n `116` status `ready` deltaP `5.1002` edge `0.0916` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
