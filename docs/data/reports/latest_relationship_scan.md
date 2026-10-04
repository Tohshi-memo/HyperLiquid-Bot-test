# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T05:22:33.794035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5068`

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

- `market_context_high->unknown_4h` score `309.028` n `51` status `ready` deltaP `8.2944` edge `25.7114` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `234.1489` n `63` status `ready` deltaP `0.5941` edge `19.5499` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `15.0668` n `46` status `ready` deltaP `33.2944` edge `1.1609` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.6438` n `46` status `ready` deltaP `39.737` edge `0.9373` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.6049` n `59` status `ready` deltaP `30.1354` edge `0.7762` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0484` n `65` status `ready` deltaP `40.1736` edge `0.6732` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5482` n `65` status `ready` deltaP `24.6646` edge `0.599` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.0854` n `51` status `ready` deltaP `16.4934` edge `0.4675` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.9224` n `59` status `ready` deltaP `33.7955` edge `0.1849` maxDD `0.0`
- `market_context_high->equity_24h` score `4.6308` n `46` status `ready` deltaP `10.8281` edge `0.4134` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9265` n `65` status `ready` deltaP `27.1318` edge `0.2076` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1538` n `65` status `ready` deltaP `34.3528` edge `0.06` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9903` n `65` status `ready` deltaP `13.3095` edge `0.196` maxDD `-1.5096`
- `market_context_high->crypto_alt_4h` score `2.9076` n `51` status `ready` deltaP `15.2528` edge `0.4` maxDD `-7.6465`
- `market_context_high->fx_4h` score `2.6266` n `51` status `ready` deltaP `30.9541` edge `0.0386` maxDD `-0.0864`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4494` n `63` status `ready` deltaP `13.8224` edge `0.157` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1082` n `65` status `ready` deltaP `25.9166` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `1.9843` n `63` status `ready` deltaP `9.7496` edge `0.175` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5055` n `65` status `ready` deltaP `4.719` edge `0.1459` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
