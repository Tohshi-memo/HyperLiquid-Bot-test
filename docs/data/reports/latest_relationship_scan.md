# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T12:52:30.034713+00:00`
- Price records: `672`
- Market context records: `7141`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.672` n `143` status `ready` deltaP `16.6948` edge `0.0147` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1136` n `155` status `ready` deltaP `4.942` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4463` n `155` status `ready` deltaP `-1.695` edge `0.0383` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6248` n `155` status `ready` deltaP `-0.3689` edge `0.0254` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6349` n `155` status `ready` deltaP `3.6981` edge `0.035` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7144` n `155` status `ready` deltaP `-1.9799` edge `-0.0163` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7702` n `155` status `ready` deltaP `1.0923` edge `-0.005` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4191` n `155` status `ready` deltaP `-5.5554` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->commodity_4h` score `-2.0775` n `143` status `ready` deltaP `-4.7533` edge `-0.0379` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2862` n `143` status `ready` deltaP `-5.5475` edge `0.0181` maxDD `-5.397`
- `market_context_high->metal_4h` score `-2.8364` n `143` status `ready` deltaP `-8.4876` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5638` n `155` status `ready` deltaP `-0.6829` edge `-0.0444` maxDD `-15.1758`
- `market_context_high->index_4h` score `-3.9205` n `143` status `ready` deltaP `-1.2451` edge `-0.0485` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9875` n `133` status `ready` deltaP `-16.0518` edge `-0.0259` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.2259` n `143` status `ready` deltaP `0.4221` edge `-0.0051` maxDD `-24.9898`
- `market_context_high->crypto_alt_4h` score `-5.5902` n `143` status `ready` deltaP `-3.9165` edge `-0.0425` maxDD `-23.7793`
- `market_context_high->unknown_24h` score `-10.1215` n `133` status `ready` deltaP `-32.8765` edge `-0.1096` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.1466` n `143` status `ready` deltaP `-2.697` edge `-0.2486` maxDD `-64.9841`
- `market_context_high->metal_24h` score `-14.5055` n `133` status `ready` deltaP `-30.0399` edge `-0.1904` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
