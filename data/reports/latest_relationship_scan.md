# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T06:52:29.506952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `39.0067` n `90` status `ready` deltaP `-2.7981` edge `3.3231` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.2174` n `62` status `ready` deltaP `39.4965` edge `0.6918` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3316` n `62` status `ready` deltaP `23.6969` edge `0.5874` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.0672` n `62` status `ready` deltaP `18.0734` edge `0.4784` maxDD `-0.1298`
- `news_risk_high->index_24h` score `5.1283` n `62` status `ready` deltaP `37.4784` edge `0.1775` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.929` n `90` status `ready` deltaP `12.5561` edge `0.8456` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.1485` n `62` status `ready` deltaP `34.1365` edge `0.061` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.7126` n `90` status `ready` deltaP `17.561` edge `0.2054` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.6181` n `62` status `ready` deltaP `19.3008` edge `0.1493` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.5918` n `62` status `ready` deltaP `10.7736` edge `0.1797` maxDD `-1.5096`
- `market_context_high->equity_24h` score `2.5626` n `90` status `ready` deltaP `15.6361` edge `0.1522` maxDD `-1.0977`
- `news_risk_high->index_1h` score `2.087` n `62` status `ready` deltaP `25.9224` edge `0.0161` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.7863` n `62` status `ready` deltaP `-5.7731` edge `0.3119` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4552` n `62` status `ready` deltaP `21.0956` edge `0.0875` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2761` n `62` status `ready` deltaP `3.9067` edge `0.1322` maxDD `-2.4854`
- `market_context_high->metal_24h` score `1.2525` n `90` status `ready` deltaP `21.5371` edge `0.1655` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0061` n `90` status `ready` deltaP `21.0637` edge `0.0181` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6627` n `90` status `ready` deltaP `11.3473` edge `0.0038` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.2786` n `90` status `ready` deltaP `7.7145` edge `0.5781` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.2196` n `90` status `ready` deltaP `10.7019` edge `0.0457` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
