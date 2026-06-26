# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T05:22:25.576886+00:00`
- Price records: `672`
- Market context records: `4796`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7871` n `122` status `ready` deltaP `19.3298` edge `0.6411` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `2.7133` n `122` status `ready` deltaP `12.2804` edge `0.186` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.3074` n `113` status `ready` deltaP `13.1576` edge `0.1969` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.0937` n `122` status `ready` deltaP `5.5315` edge `0.0297` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0511` n `122` status `ready` deltaP `11.8153` edge `0.045` maxDD `-4.377`
- `market_context_high->equity_4h` score `0.0021` n `122` status `ready` deltaP `8.844` edge `0.1099` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3088` n `122` status `ready` deltaP `7.6045` edge `0.0166` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4155` n `122` status `ready` deltaP `3.2787` edge `0.0025` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6767` n `122` status `ready` deltaP `1.8676` edge `0.0079` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8849` n `122` status `ready` deltaP `-0.8835` edge `-0.0029` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3488` n `122` status `ready` deltaP `-1.0479` edge `-0.005` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1264` n `113` status `ready` deltaP `19.8992` edge `0.1056` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.219` n `122` status `ready` deltaP `-0.4982` edge `-0.0636` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.08` n `122` status `ready` deltaP `1.3473` edge `-0.0417` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.1978` n `113` status `ready` deltaP `-13.683` edge `-0.0203` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4204` n `122` status `ready` deltaP `1.1338` edge `-0.0669` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.6786` n `122` status `ready` deltaP `5.5078` edge `0.0059` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.7174` n `113` status `ready` deltaP `-8.0307` edge `-0.125` maxDD `-22.4996`
- `market_context_high->crypto_major_4h` score `-7.9735` n `122` status `ready` deltaP `4.2683` edge `-0.1276` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.249` n `122` status `ready` deltaP `6.9922` edge `-0.2801` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
