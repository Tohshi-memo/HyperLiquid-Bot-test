# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T17:22:29.221519+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4074`

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

- `news_risk_high->equity_4h` score `2.5512` n `101` status `ready` deltaP `17.707` edge `0.2996` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0633` n `101` status `ready` deltaP `16.1827` edge `0.0285` maxDD `-0.4888`
- `news_risk_high->equity_24h` score `0.8208` n `101` status `ready` deltaP `30.3104` edge `1.0618` maxDD `-86.0244`
- `news_risk_high->index_1h` score `0.1645` n `101` status `ready` deltaP `9.5215` edge `0.005` maxDD `-0.4574`
- `news_risk_high->equity_1h` score `0.1467` n `101` status `ready` deltaP `3.8566` edge `0.0724` maxDD `-3.3438`
- `news_risk_high->index_24h` score `-0.1428` n `101` status `ready` deltaP `3.9724` edge `0.1451` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.359` n `101` status `ready` deltaP `-0.876` edge `-0.0002` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.4417` n `101` status `ready` deltaP `1.1064` edge `0.1046` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5841` n `101` status `ready` deltaP `2.0933` edge `0.1748` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.629` n `101` status `ready` deltaP `-1.0938` edge `-0.0075` maxDD `-0.6767`
- `news_risk_high->fx_4h` score `-0.7678` n `101` status `ready` deltaP `-2.1765` edge `-0.003` maxDD `-0.4745`
- `news_risk_high->crypto_alt_1h` score `-0.7778` n `101` status `ready` deltaP `0.7604` edge `0.018` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-0.8881` n `101` status `ready` deltaP `0.6429` edge `-0.0276` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.1408` n `101` status `ready` deltaP `-13.6075` edge `0.0072` maxDD `-0.3521`
- `news_risk_high->crypto_major_1h` score `-1.4906` n `101` status `ready` deltaP `-3.8907` edge `-0.0044` maxDD `-4.1772`
- `news_risk_high->metal_24h` score `-2.8758` n `101` status `ready` deltaP `3.6464` edge `-0.2034` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2648` n `101` status `ready` deltaP `-18.3168` edge `-0.0133` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.1629` n `101` status `ready` deltaP `-27.8344` edge `-0.0273` maxDD `-8.7238`
- `news_risk_high->crypto_major_24h` score `-6.0197` n `101` status `ready` deltaP `-15.1106` edge `0.1793` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.9635` n `101` status `ready` deltaP `-24.7851` edge `-0.0139` maxDD `-34.7593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
