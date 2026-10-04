# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T19:22:26.883981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5072`

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

- `market_context_high->unknown_1h` score `96.9032` n `97` status `ready` deltaP `-0.1605` edge `8.1178` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.5798` n `97` status `ready` deltaP `2.7564` edge `6.5611` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.4623` n `65` status `ready` deltaP `36.9723` edge `0.6457` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.0186` n `46` status `ready` deltaP `30.1026` edge `0.6161` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.6899` n `46` status `ready` deltaP `23.664` edge `0.6937` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.4315` n `65` status `ready` deltaP `24.3598` edge `0.5913` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.9741` n `65` status `ready` deltaP `21.1031` edge `0.4505` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.7958` n `97` status `ready` deltaP `20.9533` edge `0.3303` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8249` n `65` status `ready` deltaP `26.7361` edge `0.1405` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.7872` n `65` status `ready` deltaP `25.6074` edge `0.2059` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2781` n `65` status `ready` deltaP `35.8771` edge `0.0602` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8633` n `65` status `ready` deltaP `12.1119` edge `0.1934` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6502` n `65` status `ready` deltaP `23.1942` edge `0.1078` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1956` n `65` status `ready` deltaP `26.9645` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1248` n `97` status `ready` deltaP `15.0303` edge `0.1219` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6481` n `65` status `ready` deltaP `5.9166` edge `0.1498` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.5447` n `97` status `ready` deltaP `6.2155` edge `0.2662` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3813` n `97` status `ready` deltaP `24.8209` edge `0.0253` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3654` n `46` status `ready` deltaP `25.536` edge `0.1066` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9504` n `97` status `ready` deltaP `14.8666` edge `0.0065` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
