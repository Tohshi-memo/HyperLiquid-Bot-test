# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T11:07:40.705347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6886`

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

- `market_context_high->unknown_1h` score `324.4107` n `50` status `ready` deltaP `7.2814` edge `26.9906` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0536` n `50` status `ready` deltaP `6.8598` edge `23.3754` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.214` n `122` status `ready` deltaP `30.6524` edge `1.5011` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.6577` n `50` status `ready` deltaP `30.0903` edge `0.6625` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.8959` n `50` status `ready` deltaP `18.9146` edge `0.5189` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.8353` n `122` status `ready` deltaP `22.5552` edge `0.5708` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.5233` n `122` status `ready` deltaP `29.6432` edge `0.2282` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.1267` n `122` status `ready` deltaP `21.8608` edge `0.6987` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `4.0343` n `50` status `ready` deltaP `14.2073` edge `0.3708` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5365` n `50` status `ready` deltaP `16.7847` edge `0.5277` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.2233` n `122` status `ready` deltaP `13.0598` edge `0.3822` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.9582` n `50` status `ready` deltaP `33.4512` edge `0.037` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8619` n `50` status `ready` deltaP `14.4491` edge `0.1872` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.6063` n `50` status `ready` deltaP `12.5569` edge `0.1998` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5852` n `122` status `ready` deltaP `24.5019` edge `0.0999` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.3102` n `122` status `ready` deltaP `27.1773` edge `0.2424` maxDD `-2.192`
- `market_context_high->crypto_alt_24h` score `2.155` n `50` status `ready` deltaP `6.2917` edge `0.3086` maxDD `-11.6768`
- `market_context_high->fx_1h` score `1.4579` n `50` status `ready` deltaP `20.491` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8112` n `134` status `ready` deltaP `7.8984` edge `0.0686` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.7079` n `50` status `ready` deltaP `16.6875` edge `0.0813` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
