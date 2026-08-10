# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T21:22:29.441699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `0.9897` n `145` status `ready` deltaP `20.4064` edge `0.0272` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9029` n `177` status `ready` deltaP `12.2107` edge `0.0653` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6433` n `184` status `ready` deltaP `8.8356` edge `0.029` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0991` n `177` status `ready` deltaP `6.6772` edge `0.0072` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1242` n `184` status `ready` deltaP `4.3706` edge `0.0001` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.5031` n `145` status `ready` deltaP `0.1864` edge `0.0874` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6321` n `184` status `ready` deltaP `-4.491` edge `-0.0032` maxDD `-0.832`
- `market_context_high->metal_24h` score `-0.8898` n `145` status `ready` deltaP `2.5482` edge `0.0413` maxDD `-2.9283`
- `market_context_high->equity_24h` score `-0.8943` n `145` status `ready` deltaP `0.3418` edge `0.2702` maxDD `-22.6377`
- `market_context_high->index_4h` score `-0.8958` n `177` status `ready` deltaP `-3.6` edge `-0.0113` maxDD `-1.3634`
- `market_context_high->equity_1h` score `-1.0541` n `184` status `ready` deltaP `-3.5082` edge `-0.0081` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2251` n `184` status `ready` deltaP `-4.4682` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->crypto_alt_1h` score `-2.7431` n `184` status `ready` deltaP `-9.9974` edge `-0.0422` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0496` n `177` status `ready` deltaP `-6.4868` edge `-0.0345` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.0873` n `145` status `ready` deltaP `-2.9152` edge `-0.0787` maxDD `-17.8138`
- `market_context_high->equity_4h` score `-3.5849` n `177` status `ready` deltaP `-12.6843` edge `-0.1059` maxDD `-12.5315`
- `market_context_high->crypto_major_1h` score `-3.7265` n `184` status `ready` deltaP `-9.9486` edge `-0.0538` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-5.8433` n `145` status `ready` deltaP `-12.8226` edge `-0.1742` maxDD `-12.5138`
- `market_context_high->crypto_alt_4h` score `-6.287` n `177` status `ready` deltaP `-12.7291` edge `-0.1406` maxDD `-17.2101`
- `market_context_high->commodity_24h` score `-7.4277` n `145` status `ready` deltaP `-2.5506` edge `-0.1259` maxDD `-48.7496`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
