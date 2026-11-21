# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T19:07:29.501392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2652`

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

- `market_context_high->unknown_1h` score `9987.6173` n `126` status `ready` deltaP `1.1643` edge `832.3135` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6040.5843` n `126` status `ready` deltaP `-0.7719` edge `503.4177` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2856` n `126` status `ready` deltaP `2.6043` edge `0.0125` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3933` n `126` status `ready` deltaP `1.2118` edge `0.0027` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8579` n `126` status `ready` deltaP `7.0702` edge `0.0235` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4645` n `126` status `ready` deltaP `-9.7044` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1547` n `126` status `ready` deltaP `3.4431` edge `0.0034` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4093` n `126` status `ready` deltaP `-9.7187` edge `-0.0228` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.796` n `126` status `ready` deltaP `-7.605` edge `-0.019` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2523` n `126` status `ready` deltaP `0.0142` edge `-0.0393` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.9247` n `126` status `ready` deltaP `-6.4395` edge `-0.0564` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.2632` n `126` status `ready` deltaP `-5.6814` edge `-0.0722` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4553` n `126` status `ready` deltaP `-13.1697` edge `-0.0042` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1145` n `126` status `ready` deltaP `-21.2543` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.8643` n `126` status `ready` deltaP `6.6965` edge `0.1096` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.4175` n `126` status `ready` deltaP `-6.4436` edge `-0.1439` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.6252` n `126` status `ready` deltaP `14.5337` edge `0.3445` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8039` n `126` status `ready` deltaP `-26.1409` edge `-0.1156` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.8863` n `126` status `ready` deltaP `3.6458` edge `0.0572` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
