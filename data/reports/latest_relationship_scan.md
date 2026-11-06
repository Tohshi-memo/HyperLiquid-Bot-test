# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T08:52:30.919406+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.2168` n `135` status `ready` deltaP `6.4272` edge `0.193` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5007` n `135` status `ready` deltaP `2.6236` edge `0.0411` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6925` n `135` status `ready` deltaP `-2.4894` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7392` n `135` status `ready` deltaP `2.4817` edge `0.0008` maxDD `-1.3155`
- `news_risk_high->index_4h` score `-1.0832` n `135` status `ready` deltaP `3.986` edge `0.0102` maxDD `-3.385`
- `news_risk_high->metal_1h` score `-1.3488` n `135` status `ready` deltaP `-6.1388` edge `-0.0168` maxDD `-2.5487`
- `news_risk_high->fx_4h` score `-1.4314` n `135` status `ready` deltaP `-8.2543` edge `-0.0121` maxDD `-1.6437`
- `news_risk_high->index_24h` score `-1.5629` n `135` status `ready` deltaP `-9.0375` edge `0.0892` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-1.9782` n `135` status `ready` deltaP `-4.1772` edge `-0.006` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.2276` n `135` status `ready` deltaP `-22.1965` edge `-0.0221` maxDD `-1.5744`
- `news_risk_high->commodity_1h` score `-2.7147` n `135` status `ready` deltaP `-12.821` edge `-0.0041` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-3.0463` n `135` status `ready` deltaP `-5.9937` edge `0.0366` maxDD `-14.7064`
- `news_risk_high->equity_1h` score `-3.1544` n `135` status `ready` deltaP `-4.358` edge `0.0071` maxDD `-14.2732`
- `news_risk_high->equity_24h` score `-3.8802` n `135` status `ready` deltaP `14.4983` edge `0.7803` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5688` n `135` status `ready` deltaP `-20.1751` edge `-0.0108` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7546` n `135` status `ready` deltaP `-10.5217` edge `-0.0691` maxDD `-7.8909`
- `news_risk_high->equity_4h` score `-6.9809` n `135` status `ready` deltaP `4.4434` edge `0.0495` maxDD `-41.8693`
- `news_risk_high->metal_24h` score `-7.0606` n `135` status `ready` deltaP `-12.7348` edge `-0.2634` maxDD `-10.8737`
- `news_risk_high->commodity_24h` score `-10.8041` n `135` status `ready` deltaP `-21.2854` edge `0.0496` maxDD `-43.31`
- `news_risk_high->crypto_alt_24h` score `-12.3477` n `135` status `ready` deltaP `5.6581` edge `0.0787` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
