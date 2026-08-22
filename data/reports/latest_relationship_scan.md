# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T10:52:24.561559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.0774` n `142` status `ready` deltaP `7.5757` edge `0.062` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.3381` n `133` status `ready` deltaP `19.1087` edge `-0.0553` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0789` n `133` status `ready` deltaP `7.6002` edge `0.0097` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0067` n `142` status `ready` deltaP `7.4028` edge `0.0046` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0484` n `142` status `ready` deltaP `3.732` edge `0.0048` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2385` n `142` status `ready` deltaP `2.3678` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2725` n `133` status `ready` deltaP `6.6236` edge `-0.0175` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3276` n `142` status `ready` deltaP `4.7082` edge `0.0336` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5777` n `133` status `ready` deltaP `2.7737` edge `0.011` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6585` n `133` status `ready` deltaP `-0.7038` edge `0.0053` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7756` n `142` status `ready` deltaP `-6.1715` edge `-0.0017` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5185` n `133` status `ready` deltaP `5.4225` edge `-0.0357` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.67` n `133` status `ready` deltaP `-0.4482` edge `0.0694` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.7824` n `116` status `ready` deltaP `-5.0108` edge `0.0682` maxDD `-4.666`
- `market_context_high->fx_24h` score `-2.0878` n `116` status `ready` deltaP `-2.8197` edge `0.0058` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.4516` n `142` status `ready` deltaP `-2.6882` edge `-0.0369` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4439` n `142` status `ready` deltaP `-4.7735` edge `-0.1093` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.359` n `116` status `ready` deltaP `-7.0762` edge `-0.0478` maxDD `-19.7767`
- `market_context_high->crypto_major_4h` score `-4.9825` n `133` status `ready` deltaP `-0.8871` edge `-0.3072` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.305` n `116` status `ready` deltaP `-22.9107` edge `-0.1966` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
