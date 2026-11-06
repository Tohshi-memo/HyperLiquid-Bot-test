# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T13:07:27.035048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3915`

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

- `news_risk_high->equity_24h` score `0.1618` n `118` status `ready` deltaP `23.1424` edge `1.0251` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.1386` n `118` status `ready` deltaP `8.8647` edge `0.0122` maxDD `-2.1257`
- `news_risk_high->index_1h` score `-0.2078` n `118` status `ready` deltaP `6.7822` edge `0.0023` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.4437` n `118` status `ready` deltaP `-2.0983` edge `-0.0015` maxDD `-0.3119`
- `news_risk_high->crypto_alt_4h` score `-0.5472` n `118` status `ready` deltaP `4.4078` edge `0.1641` maxDD `-14.0916`
- `news_risk_high->index_24h` score `-0.6208` n `118` status `ready` deltaP `-3.0614` edge `0.1243` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.7224` n `118` status `ready` deltaP `0.7003` edge `0.0255` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-1.0521` n `118` status `ready` deltaP `-3.3898` edge `-0.0116` maxDD `-1.2782`
- `news_risk_high->crypto_major_4h` score `-1.1659` n `118` status `ready` deltaP `-3.7309` edge `0.0565` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.197` n `118` status `ready` deltaP `-2.5373` edge `-0.0019` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.3559` n `118` status `ready` deltaP `-15.7645` edge `-0.0053` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.3956` n `118` status `ready` deltaP `-0.9972` edge `0.018` maxDD `-10.2217`
- `news_risk_high->crypto_major_1h` score `-1.5946` n `118` status `ready` deltaP `-3.7857` edge `-0.0071` maxDD `-4.7103`
- `news_risk_high->equity_4h` score `-2.5265` n `118` status `ready` deltaP `9.322` edge `0.0992` maxDD `-24.4178`
- `news_risk_high->metal_4h` score `-2.5919` n `118` status `ready` deltaP `-6.7254` edge `-0.0468` maxDD `-2.9483`
- `news_risk_high->commodity_1h` score `-2.7635` n `118` status `ready` deltaP `-13.3107` edge `-0.0049` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.4299` n `118` status `ready` deltaP `-4.6243` edge `-0.2193` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.7521` n `118` status `ready` deltaP `-22.1373` edge `-0.013` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.4156` n `118` status `ready` deltaP `-17.3978` edge `0.1438` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2582` n `118` status `ready` deltaP `-23.4796` edge `0.0102` maxDD `-39.3485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
