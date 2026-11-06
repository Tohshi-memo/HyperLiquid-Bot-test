# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T15:52:35.987353+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3932`

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

- `news_risk_high->equity_4h` score `2.0394` n `107` status `ready` deltaP `14.6584` edge `0.2543` maxDD `-4.2454`
- `news_risk_high->equity_24h` score `1.0217` n `107` status `ready` deltaP `29.8531` edge `1.0906` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.8112` n `107` status `ready` deltaP `13.7438` edge `0.024` maxDD `-0.5088`
- `news_risk_high->index_1h` score `-0.1964` n `107` status `ready` deltaP `6.7505` edge `0.0025` maxDD `-0.776`
- `news_risk_high->index_24h` score `-0.249` n `107` status `ready` deltaP `1.6444` edge `0.1406` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.5062` n `107` status `ready` deltaP `-0.4351` edge `0.0007` maxDD `-0.1984`
- `news_risk_high->fx_4h` score `-0.7629` n `107` status `ready` deltaP `-2.1569` edge `-0.0025` maxDD `-0.4745`
- `news_risk_high->crypto_alt_1h` score `-0.8046` n `107` status `ready` deltaP `0.9933` edge `0.013` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-0.8223` n `107` status `ready` deltaP `-1.1568` edge `0.0709` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.8229` n `107` status `ready` deltaP `1.1169` edge `0.1507` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.8255` n `107` status `ready` deltaP `-1.851` edge `-0.0085` maxDD `-0.8359`
- `news_risk_high->equity_1h` score `-1.0094` n `107` status `ready` deltaP `1.4019` edge `0.0456` maxDD `-6.7916`
- `news_risk_high->metal_4h` score `-1.0805` n `107` status `ready` deltaP `-2.2168` edge `-0.0332` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.1955` n `107` status `ready` deltaP `-13.8198` edge `0.0023` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.6634` n `107` status `ready` deltaP `-4.0153` edge `-0.0113` maxDD `-4.7103`
- `news_risk_high->commodity_1h` score `-2.9079` n `107` status `ready` deltaP `-14.6357` edge `-0.0081` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.016` n `107` status `ready` deltaP `1.2354` edge `-0.2053` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.4325` n `107` status `ready` deltaP `-28.1072` edge `-0.0299` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.1266` n `107` status `ready` deltaP `-16.8063` edge `0.1769` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2152` n `107` status `ready` deltaP `-24.4268` edge `-0.0107` maxDD `-36.8844`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
