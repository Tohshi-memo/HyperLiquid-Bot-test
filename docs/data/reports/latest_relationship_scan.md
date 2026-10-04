# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T05:07:27.484383+00:00`
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

- `market_context_high->unknown_4h` score `318.903` n `50` status `ready` deltaP `8.1768` edge `26.5351` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `240.5784` n `62` status `ready` deltaP `0.3381` edge `20.0874` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `15.1406` n `46` status `ready` deltaP `33.4677` edge `1.1659` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.6996` n `46` status `ready` deltaP `39.9103` edge `0.9408` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.6536` n `59` status `ready` deltaP `30.3087` edge `0.7791` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0364` n `65` status `ready` deltaP `40.1736` edge `0.6722` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5398` n `65` status `ready` deltaP `24.6646` edge `0.5983` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.0772` n `50` status `ready` deltaP `15.8659` edge `0.471` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.9387` n `59` status `ready` deltaP `33.9688` edge `0.1851` maxDD `0.0`
- `market_context_high->equity_24h` score `4.6795` n `46` status `ready` deltaP `11.0014` edge `0.4163` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9253` n `65` status `ready` deltaP `27.1318` edge `0.2075` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1538` n `65` status `ready` deltaP `34.3528` edge `0.06` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9843` n `65` status `ready` deltaP `13.3095` edge `0.1955` maxDD `-1.5096`
- `market_context_high->crypto_alt_4h` score `2.8552` n `50` status `ready` deltaP `14.6646` edge `0.3972` maxDD `-7.6465`
- `market_context_high->fx_4h` score `2.7479` n `50` status `ready` deltaP `32.3659` edge `0.0393` maxDD `-0.0864`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4172` n `62` status `ready` deltaP `13.2847` edge `0.1579` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1201` n `65` status `ready` deltaP `26.0663` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `1.9564` n `62` status `ready` deltaP `9.1607` edge `0.1766` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5007` n `65` status `ready` deltaP `4.719` edge `0.1455` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
