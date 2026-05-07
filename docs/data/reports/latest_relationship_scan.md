# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T07:07:20.954913+00:00`
- Price records: `528`
- Market context records: `624`
- Flow alert records: `1765`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `5.2521` n `146` status `ready` deltaP `15.1604` edge `0.37` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.2193` n `146` status `ready` deltaP `7.417` edge `0.3903` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0881` n `146` status `ready` deltaP `9.0066` edge `0.0158` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3182` n `146` status `ready` deltaP `2.0416` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5593` n `146` status `ready` deltaP `1.7914` edge `0.0389` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7216` n `146` status `ready` deltaP `-0.5796` edge `-0.0033` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0666` n `146` status `ready` deltaP `-3.5475` edge `-0.0049` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2024` n `146` status `ready` deltaP `5.605` edge `-0.0061` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3308` n `146` status `ready` deltaP `-2.6949` edge `-0.0119` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.736` n `146` status `ready` deltaP `5.3905` edge `-0.0083` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.7465` n `146` status `ready` deltaP `4.7303` edge `0.0799` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.3096` n `146` status `ready` deltaP `14.1053` edge `0.0841` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.3391` n `146` status `ready` deltaP `-1.0732` edge `-0.0355` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.8616` n `146` status `ready` deltaP `-7.9887` edge `0.0143` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.3159` n `146` status `ready` deltaP `-3.6323` edge `-0.0369` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3763` n `146` status `ready` deltaP `-4.8939` edge `-0.0528` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6699` n `146` status `ready` deltaP `-6.3046` edge `0.0863` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2625` n `146` status `ready` deltaP `-2.3077` edge `-0.0139` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6526` n `146` status `ready` deltaP `2.3705` edge `-0.2157` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8405` n `146` status `ready` deltaP `-11.3397` edge `-0.0673` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
