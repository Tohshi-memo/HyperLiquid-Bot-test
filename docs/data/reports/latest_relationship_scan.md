# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T17:37:32.742650+00:00`
- Price records: `672`
- Market context records: `5795`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8128`

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

- `market_context_high->equity_24h` score `0.6161` n `248` status `ready` deltaP `15.3954` edge `0.4566` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0331` n `303` status `ready` deltaP `6.5554` edge `0.1174` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.264` n `303` status `ready` deltaP `2.0839` edge `0.0008` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6454` n `303` status `ready` deltaP `2.2099` edge `-0.001` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6455` n `303` status `ready` deltaP `3.0607` edge `0.0265` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7598` n `303` status `ready` deltaP `-1.788` edge `-0.005` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9706` n `303` status `ready` deltaP `2.9278` edge `0.0317` maxDD `-6.2348`
- `market_context_high->index_1h` score `-1.0032` n `303` status `ready` deltaP `-0.039` edge `0.0035` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.1173` n `248` status `ready` deltaP `13.3456` edge `0.038` maxDD `-4.6174`
- `market_context_high->crypto_alt_1h` score `-1.1403` n `303` status `ready` deltaP `1.3389` edge `0.0295` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1934` n `303` status `ready` deltaP `0.7702` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.491` n `303` status `ready` deltaP `0.1131` edge `0.003` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.3995` n `303` status `ready` deltaP `-3.3053` edge `-0.0256` maxDD `-13.4662`
- `market_context_high->metal_4h` score `-2.4869` n `303` status `ready` deltaP `-5.3228` edge `-0.0474` maxDD `-11.5426`
- `market_context_high->index_24h` score `-2.7948` n `248` status `ready` deltaP `3.7131` edge `0.0314` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0034` n `303` status `ready` deltaP `7.5234` edge `0.1368` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.595` n `303` status `ready` deltaP `5.3153` edge `0.0825` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.8918` n `248` status `ready` deltaP `-7.5213` edge `-0.2516` maxDD `-26.2125`
- `market_context_high->crypto_major_24h` score `-8.3266` n `248` status `ready` deltaP `0.532` edge `-0.1559` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.7526` n `248` status `ready` deltaP `-14.5274` edge `-0.0826` maxDD `-39.6616`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
