# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T06:07:25.883893+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `281.7214` n `54` status `ready` deltaP `6.9219` edge `23.445` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `216.2342` n `66` status `ready` deltaP `1.1659` edge `18.0532` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.7684` n `46` status `ready` deltaP `32.7745` edge `1.1395` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.4222` n `46` status `ready` deltaP `39.2171` edge `0.9223` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.4457` n `59` status `ready` deltaP `29.6154` edge `0.7664` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0808` n `65` status `ready` deltaP `40.1736` edge `0.6759` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.559` n `65` status `ready` deltaP `24.6646` edge `0.5999` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1132` n `54` status `ready` deltaP `18.2363` edge `0.4582` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.8688` n `59` status `ready` deltaP `33.2756` edge `0.1839` maxDD `0.0`
- `market_context_high->equity_24h` score `4.4716` n `46` status `ready` deltaP `10.3081` edge `0.4036` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9313` n `65` status `ready` deltaP `27.1318` edge `0.208` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.155` n `65` status `ready` deltaP `34.3528` edge `0.0601` maxDD `-0.4296`
- `market_context_high->crypto_alt_4h` score `3.1384` n `54` status `ready` deltaP `16.8868` edge `0.4187` maxDD `-7.6465`
- `news_risk_high->crypto_major_1h` score `2.9975` n `65` status `ready` deltaP `13.3095` edge `0.1966` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.5442` n `66` status `ready` deltaP `15.3375` edge `0.1548` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.2718` n `54` status `ready` deltaP `27.0326` edge `0.0359` maxDD `-0.1439`
- `market_context_high->crypto_alt_1h` score `2.1231` n `66` status `ready` deltaP `11.409` edge `0.1755` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5115` n `65` status `ready` deltaP `4.719` edge `0.1464` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
