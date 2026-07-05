# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T23:07:30.316452+00:00`
- Price records: `672`
- Market context records: `5822`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.3757` n `281` status `ready` deltaP `6.5386` edge `0.1335` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.1651` n `248` status `ready` deltaP `15.3954` edge `0.3915` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.2162` n `281` status `ready` deltaP `2.9882` edge `0.0009` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5211` n `281` status `ready` deltaP `-0.7229` edge `-0.0011` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.595` n `281` status `ready` deltaP `0.7794` edge `0.0033` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6219` n `281` status `ready` deltaP `2.2594` edge `0.0002` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.7127` n `281` status `ready` deltaP `2.2647` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9635` n `281` status `ready` deltaP `2.8214` edge `0.033` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1094` n `281` status `ready` deltaP `1.3047` edge `0.0323` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1628` n `281` status `ready` deltaP `0.893` edge `0.0137` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4917` n `248` status `ready` deltaP `9.4422` edge `0.0276` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5063` n `281` status `ready` deltaP `-0.0754` edge `0.0023` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.1601` n `281` status `ready` deltaP `-4.1908` edge `-0.0431` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6713` n `281` status `ready` deltaP `-0.9456` edge `-0.0165` maxDD `-8.6511`
- `market_context_high->crypto_major_4h` score `-2.8265` n `281` status `ready` deltaP `7.6041` edge `0.151` maxDD `-25.6458`
- `market_context_high->index_24h` score `-4.3333` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.5557` n `281` status `ready` deltaP `5.0109` edge `0.0878` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7729` n `248` status `ready` deltaP `-12.4608` edge `-0.0611` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-7.3459` n `248` status `ready` deltaP `-2.4698` edge `-0.2264` maxDD `-16.5436`
- `market_context_high->crypto_alt_24h` score `-12.4552` n `248` status `ready` deltaP `-10.0246` edge `-0.4993` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
