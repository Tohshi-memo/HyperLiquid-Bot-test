# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T14:07:27.549798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `110.7361` n `86` status `ready` deltaP `2.6056` edge `9.2418` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `95.5508` n `97` status `ready` deltaP `-0.6096` edge `8.0081` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `10.7864` n `46` status `ready` deltaP `27.3098` edge `0.8441` maxDD `-8.1838`
- `news_risk_high->crypto_major_4h` score `10.5385` n `65` status `ready` deltaP `37.4297` edge `0.649` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.4563` n `46` status `ready` deltaP `33.7485` edge `0.7116` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.7322` n `65` status `ready` deltaP `24.749` edge `0.5727` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2753` n `65` status `ready` deltaP `24.2073` edge `0.5793` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.5768` n `86` status `ready` deltaP `24.1918` edge `0.3738` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.0366` n `65` status `ready` deltaP `27.7778` edge `0.1512` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8116` n `65` status `ready` deltaP `25.9123` edge `0.2059` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0782` n `65` status `ready` deltaP `33.4381` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9112` n `65` status `ready` deltaP `12.561` edge `0.1944` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5634` n `65` status `ready` deltaP `21.9747` edge `0.1087` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.1909` n `46` status `ready` deltaP `4.8158` edge `0.2496` maxDD `-6.264`
- `market_context_high->crypto_major_1h` score `2.1728` n `97` status `ready` deltaP `15.4794` edge `0.1229` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0842` n `65` status `ready` deltaP `25.6172` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_4h` score `1.5888` n `86` status `ready` deltaP `4.6724` edge `0.276` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.5534` n `65` status `ready` deltaP `5.1681` edge `0.1469` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_4h` score `1.3249` n `86` status `ready` deltaP `23.862` edge `0.027` maxDD `-0.3868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
