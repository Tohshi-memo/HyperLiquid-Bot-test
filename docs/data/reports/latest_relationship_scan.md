# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T03:07:28.386961+00:00`
- Price records: `672`
- Market context records: `5730`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.904` n `218` status `ready` deltaP `15.703` edge `0.5191` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1118` n `280` status `ready` deltaP `7.0775` edge `0.126` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2381` n `285` status `ready` deltaP `2.4866` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4214` n `285` status `ready` deltaP `2.0843` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6118` n `285` status `ready` deltaP `3.3617` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7997` n `285` status `ready` deltaP `3.2304` edge `0.0353` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.8002` n `285` status `ready` deltaP `-2.3369` edge `-0.0063` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.9383` n `285` status `ready` deltaP `1.4855` edge `0.0323` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1196` n `218` status `ready` deltaP `10.8611` edge `0.0424` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1441` n `280` status `ready` deltaP `1.703` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2458` n `280` status `ready` deltaP `2.8659` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_major_4h` score `-1.6575` n `280` status `ready` deltaP `7.6176` edge `0.1556` maxDD `-19.8939`
- `market_context_high->metal_4h` score `-2.61` n `280` status `ready` deltaP `-7.1777` edge `-0.0492` maxDD `-11.6719`
- `market_context_high->crypto_alt_4h` score `-2.923` n `280` status `ready` deltaP `5.6315` edge `0.1082` maxDD `-21.4794`
- `market_context_high->index_24h` score `-2.9566` n `218` status `ready` deltaP `1.0528` edge `0.0284` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8082` n `280` status `ready` deltaP `-3.149` edge `-0.0288` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3147` n `218` status `ready` deltaP `7.3697` edge `0.037` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.648` n `218` status `ready` deltaP `-7.4286` edge `-0.2425` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.5265` n `218` status `ready` deltaP `-10.748` edge `-0.0749` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
