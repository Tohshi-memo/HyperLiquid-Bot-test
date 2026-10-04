# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T05:45:24.809679+00:00`
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

- `market_context_high->unknown_4h` score `290.4678` n `53` status `ready` deltaP `6.7821` edge `24.1748` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `221.946` n `65` status `ready` deltaP `-0.3063` edge `18.539` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.8675` n `46` status `ready` deltaP `32.9478` edge `1.1466` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.4972` n `46` status `ready` deltaP `39.3904` edge `0.9274` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.4992` n `59` status `ready` deltaP `29.7888` edge `0.7697` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.0664` n `65` status `ready` deltaP `40.1736` edge `0.6747` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5542` n `65` status `ready` deltaP `24.6646` edge `0.5995` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1213` n `53` status `ready` deltaP `17.6772` edge `0.4626` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.8875` n `59` status `ready` deltaP `33.4489` edge `0.1843` maxDD `0.0`
- `market_context_high->equity_24h` score `4.5251` n `46` status `ready` deltaP `10.4815` edge `0.4069` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9289` n `65` status `ready` deltaP `27.1318` edge `0.2078` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.155` n `65` status `ready` deltaP `34.3528` edge `0.0601` maxDD `-0.4296`
- `market_context_high->crypto_alt_4h` score `3.073` n `53` status `ready` deltaP `16.3627` edge `0.4138` maxDD `-7.6465`
- `news_risk_high->crypto_major_1h` score `2.9951` n `65` status `ready` deltaP `13.3095` edge `0.1964` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.5291` n `65` status `ready` deltaP `14.848` edge `0.1568` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.3853` n `53` status `ready` deltaP `28.2904` edge `0.0367` maxDD `-0.1225`
- `market_context_high->crypto_alt_1h` score `2.097` n `65` status `ready` deltaP `10.8729` edge `0.1769` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5103` n `65` status `ready` deltaP `4.719` edge `0.1463` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
