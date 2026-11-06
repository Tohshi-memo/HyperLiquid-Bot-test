# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T15:37:26.516509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3928`

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

- `news_risk_high->equity_4h` score `1.6611` n `108` status `ready` deltaP `14.0526` edge `0.2343` maxDD `-6.2017`
- `news_risk_high->equity_24h` score `1.0324` n `108` status `ready` deltaP `29.3253` edge `1.0955` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.7063` n `108` status `ready` deltaP `13.2904` edge `0.0218` maxDD `-0.7903`
- `news_risk_high->index_24h` score `-0.2722` n `108` status `ready` deltaP `1.3329` edge `0.1397` maxDD `-6.6786`
- `news_risk_high->index_1h` score `-0.3051` n `108` status `ready` deltaP `6.2486` edge `0.0019` maxDD `-0.8518`
- `news_risk_high->fx_1h` score `-0.5463` n `108` status `ready` deltaP `-0.937` edge `0.0007` maxDD `-0.1984`
- `news_risk_high->fx_4h` score `-0.7481` n `108` status `ready` deltaP `-1.9026` edge `-0.0023` maxDD `-0.4745`
- `news_risk_high->crypto_alt_1h` score `-0.7861` n `108` status `ready` deltaP `1.3196` edge `0.0132` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-0.8858` n `108` status `ready` deltaP `-2.1513` edge `-0.0096` maxDD `-0.9899`
- `news_risk_high->crypto_alt_4h` score `-0.8987` n `108` status `ready` deltaP `0.7848` edge `0.1432` maxDD `-14.0916`
- `news_risk_high->crypto_major_4h` score `-0.9455` n `108` status `ready` deltaP `-1.5808` edge `0.0621` maxDD `-9.1553`
- `news_risk_high->fx_24h` score `-1.1911` n `108` status `ready` deltaP `-13.6294` edge `0.0016` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.2679` n `108` status `ready` deltaP `0.9259` edge `0.0396` maxDD `-7.4481`
- `news_risk_high->crypto_major_1h` score `-1.6007` n `108` status `ready` deltaP `-3.4875` edge `-0.0096` maxDD `-4.7103`
- `news_risk_high->metal_4h` score `-1.733` n `108` status `ready` deltaP `-2.71` edge `-0.0358` maxDD `-1.5773`
- `news_risk_high->commodity_1h` score `-2.8697` n `108` status `ready` deltaP `-14.1883` edge `-0.0079` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.0576` n `108` status `ready` deltaP `0.5863` edge `-0.2063` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.3749` n `108` status `ready` deltaP `-27.5068` edge `-0.0291` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.1188` n `108` status `ready` deltaP `-16.9102` edge `0.1786` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2601` n `108` status `ready` deltaP `-24.4874` edge `-0.01` maxDD `-37.2072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
